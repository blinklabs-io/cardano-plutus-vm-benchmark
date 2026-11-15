// Command mainnet-corpus turns plutigo's recent mainnet replay corpus into
// closed .flat programs for the benchmark.
//
// Each replay case holds a validator and the ledger arguments it was run
// with (datum, redeemer and script context, or fewer). The benchmark VMs
// take one closed program per file, so each validator is applied to its
// arguments as Data constants and FLAT-encoded, the same shape as the
// plutus_use_cases programs. Only cases that succeeded on mainnet are kept,
// and every written program is checked to evaluate successfully.
package main

import (
	"compress/gzip"
	"encoding/hex"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"
	"sort"
	"strings"

	"github.com/blinklabs-io/plutigo/cek"
	"github.com/blinklabs-io/plutigo/data"
	"github.com/blinklabs-io/plutigo/syn"
)

type corpus struct {
	Cases []replayCase `json:"cases"`
}

type replayCase struct {
	ID               string   `json:"id"`
	FlatProgramHex   string   `json:"flat_program_hex"`
	ArgumentsCBORHex []string `json:"arguments_cbor_hex"`
	Expected         struct {
		Success bool `json:"success"`
	} `json:"expected"`
}

func main() {
	out := flag.String("out", "", "directory to write the .flat programs to")
	flag.Parse()
	if *out == "" || flag.NArg() == 0 {
		log.Fatal("usage: mainnet-corpus -out DIR CORPUS.json[.gz]...")
	}
	if err := os.MkdirAll(*out, 0o755); err != nil {
		log.Fatal(err)
	}

	var cases []replayCase
	for _, path := range flag.Args() {
		c, err := load(path)
		if err != nil {
			log.Fatalf("%s: %v", path, err)
		}
		cases = append(cases, c.Cases...)
	}
	sort.Slice(cases, func(i, j int) bool { return cases[i].ID < cases[j].ID })

	written, skipped := 0, 0
	names := map[string]string{}
	for _, c := range cases {
		if !c.Expected.Success {
			skipped++
			continue
		}
		name := fileName(c.ID)
		if prev, ok := names[name]; ok {
			log.Fatalf("cases %s and %s map to the same file %s", prev, c.ID, name)
		}
		names[name] = c.ID
		program, err := build(c)
		if err != nil {
			log.Fatalf("%s: %v", c.ID, err)
		}
		if err := check(program); err != nil {
			log.Fatalf("%s: %v", c.ID, err)
		}
		if err := os.WriteFile(filepath.Join(*out, name), program, 0o644); err != nil {
			log.Fatal(err)
		}
		written++
	}
	fmt.Printf("wrote %d programs, skipped %d cases that failed on mainnet\n", written, skipped)
}

func load(path string) (*corpus, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	var r io.Reader = f
	if strings.HasSuffix(path, ".gz") {
		gz, err := gzip.NewReader(f)
		if err != nil {
			return nil, err
		}
		defer gz.Close()
		r = gz
	}
	var c corpus
	if err := json.NewDecoder(r).Decode(&c); err != nil {
		return nil, err
	}
	return &c, nil
}

// fileName maps "<txid>#<purpose>:<index>" to "<txid>-<purpose>-<index>.flat".
func fileName(id string) string {
	tx, redeemer, ok := strings.Cut(id, "#")
	if !ok {
		log.Fatalf("unexpected case id %q", id)
	}
	return tx + "-" + strings.ReplaceAll(redeemer, ":", "-") + ".flat"
}

// build applies the validator to its arguments and FLAT-encodes the result.
func build(c replayCase) ([]byte, error) {
	flat, err := hex.DecodeString(c.FlatProgramHex)
	if err != nil {
		return nil, fmt.Errorf("program hex: %w", err)
	}
	program, err := syn.Decode[syn.DeBruijn](flat)
	if err != nil {
		return nil, fmt.Errorf("decode program: %w", err)
	}
	term := program.Term
	for i, argHex := range c.ArgumentsCBORHex {
		argCBOR, err := hex.DecodeString(argHex)
		if err != nil {
			return nil, fmt.Errorf("argument %d hex: %w", i, err)
		}
		arg, err := data.Decode(argCBOR)
		if err != nil {
			return nil, fmt.Errorf("argument %d: %w", i, err)
		}
		term = &syn.Apply[syn.DeBruijn]{
			Function: term,
			Argument: &syn.Constant{Con: &syn.Data{Inner: arg}},
		}
	}
	program.Term = term
	return syn.Encode(program)
}

// check evaluates the program the way the plutigo benchmark does.
func check(flat []byte) error {
	program, err := syn.Decode[syn.DeBruijn](flat)
	if err != nil {
		return fmt.Errorf("decode applied program: %w", err)
	}
	ctx := cek.NewDefaultEvalContext(program.Version, cek.ProtoVersion{Major: 200})
	machine := cek.NewMachine[syn.DeBruijn](program.Version, 0, ctx)
	if _, err := machine.Run(program.Term); err != nil {
		return fmt.Errorf("evaluate applied program: %w", err)
	}
	return nil
}
