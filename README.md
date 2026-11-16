# Cardano Plutus VM Benchmark

Reproducible, cross-language benchmark suite for Plutus (UPLC) virtual machine implementations.

Builds 11 VMs from source or released packages inside Docker, runs each VM's benchmark framework, and generates a unified comparison report. [View full results](https://blinklabs-io.github.io/cardano-plutus-vm-benchmark/)

This version is maintained by [Blink Labs](https://blinklabs.io). It continues the [original benchmark by SAIB Inc.](https://github.com/SAIB-Inc/cardano-plutus-vm-benchmark) and tracks the newest code of each VM rather than only its latest stable release (see [Updating VM Versions](#updating-vm-versions)).

## Latest Results (2026-11-16)

> System: Intel Core i7-6700 @ 3.40 GHz, 8 logical cores, 15 GiB RAM, Linux kernel 6.8.0-147-generic

Each VM was built from the newest code on its default branch, or its newest published package (see [`versions.csv`](results/2026-11-16/versions.csv)). Each corpus and each tier is ranked separately; lower is better. The [page](https://blinklabs-io.github.io/cardano-plutus-vm-benchmark/) switches between them and lists every program measured.

### Plutus use cases: all 89 programs

#### Full tier: decode and evaluate

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Plutigo CEK (Go)** | Go | 354.85 us | 1.00x |
| **Amaru UPLC CEK (Rust)** | Rust | 378.53 us | 1.07x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 464.73 us | 1.31x |
| **Plutuz CEK (Zig)** | Zig | 690.09 us | 1.94x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 733.87 us | 2.07x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 770.52 us | 2.17x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 1.07 ms | 3.01x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.32 ms | 6.55x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.36 ms | 6.64x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 15.14 ms | 42.68x |
| **opshin CEK (Python / CPython)** | Python / CPython | 109.15 ms | 307.61x |

#### Eval tier: evaluate a decoded program

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 171.23 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 192.79 us | 1.13x |
| **Plutigo CEK (Go)** | Go | 247.20 us | 1.44x |
| **Amaru UPLC CEK (Rust)** | Rust | 258.02 us | 1.51x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 286.69 us | 1.67x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 368.79 us | 2.15x |
| **Plutuz CEK (Zig)** | Zig | 474.98 us | 2.77x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 520.75 us | 3.04x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 556.08 us | 3.25x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 833.53 us | 4.87x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.89 ms | 11.06x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.91 ms | 11.13x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 13.35 ms | 77.99x |
| **opshin CEK (Python / CPython)** | Python / CPython | 94.05 ms | 549.27x |

*Julc fails 11 scripts and OpShin 30; failures use the slowest successful time for that script in the geometric mean. See [`results/2026-11-16/report.md`](results/2026-11-16/report.md).*

### Mainnet validators: 100 of 1360 programs, seed 1

#### Full tier: decode and evaluate

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Amaru UPLC CEK (Rust)** | Rust | 164.66 us | 1.00x |
| **Plutigo CEK (Go)** | Go | 173.21 us | 1.05x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 207.31 us | 1.26x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 252.38 us | 1.53x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 256.26 us | 1.56x |
| **Plutuz CEK (Zig)** | Zig | 348.65 us | 2.12x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 591.95 us | 3.59x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 781.21 us | 4.74x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 873.05 us | 5.30x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 7.19 ms | 43.66x |
| **opshin CEK (Python / CPython)** | Python / CPython | 45.36 ms | 275.46x |

#### Eval tier: evaluate a decoded program

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 16.39 us | 1.00x |
| **Plutigo CEK (Go)** | Go | 39.02 us | 2.38x |
| **Amaru UPLC CEK (Rust)** | Rust | 39.27 us | 2.40x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 41.45 us | 2.53x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 47.66 us | 2.91x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 71.09 us | 4.34x |
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 71.33 us | 4.35x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 73.49 us | 4.48x |
| **Plutuz CEK (Zig)** | Zig | 133.50 us | 8.14x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 154.59 us | 9.43x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 248.14 us | 15.14x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 288.07 us | 17.57x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 4.76 ms | 290.33x |
| **opshin CEK (Python / CPython)** | Python / CPython | 27.71 ms | 1690.58x |

*OpShin fails 19 programs and plutus-machine 1, each of which succeeded on mainnet; failures use the slowest successful time for that program in the geometric mean. Scalus JIT was rerun on the same 100 programs after an sbt packaging error. See [`results/2026-11-15-mainnet_recent/report.md`](results/2026-11-15-mainnet_recent/report.md) and its [`corpus.txt`](results/2026-11-15-mainnet_recent/corpus.txt).*

*Full tier: each iteration decodes the whole `.flat` file, including its Data arguments, and evaluates it. Eval tier: the program is decoded before timing; JIT VMs (Scalus JIT, llvm-uplc) and Julc appear here only (see [METHODOLOGY.md](METHODOLOGY.md#what-is-measured)). Scalus JIT's three-sample JMH intervals are wide, so its results are low confidence.*

## VMs Benchmarked

| VM | Language | Benchmark Framework | Repository |
|---|---|---|---|
| **plutus-core** | Haskell / GHC | Criterion | [IntersectMBO/plutus](https://github.com/IntersectMBO/plutus) (`plutus-benchmark`) |
| **Amaru UPLC** | Rust | Repository Criterion.rs adapter | [`amaru-uplc`](https://crates.io/crates/amaru-uplc) |
| **Harmonic Labs plutus-machine** | TypeScript / Node.js | Repository Node.js adapter | [`@harmoniclabs/plutus-machine`](https://www.npmjs.com/package/@harmoniclabs/plutus-machine), the evaluator used by Pebble |
| **Plutuz** | Zig | Custom (JSON) | [utxo-company/plutuz](https://github.com/utxo-company/plutuz) |
| **Chrysalis** | C# / .NET | BenchmarkDotNet (JIT + AOT) | [SAIB-Inc/Chrysalis](https://github.com/SAIB-Inc/Chrysalis) |
| **Plutigo** | Go | testing.B | [blinklabs-io/plutigo](https://github.com/blinklabs-io/plutigo) |
| **blaze-plutus** | TypeScript | Vitest bench (Node / V8 and Bun / JavaScriptCore) | [butaneprotocol/blaze-cardano](https://github.com/butaneprotocol/blaze-cardano) |
| **opshin-uplc** | Python | Custom | [OpShin/uplc](https://github.com/OpShin/uplc) |
| **Scalus** | Scala / JVM | JMH | [scalus3/scalus](https://github.com/scalus3/scalus) |
| **Julc** | Java | JMH (CEK) | [bloxbean/julc](https://github.com/bloxbean/julc) |
| **llvm-uplc** | C++ / LLVM | Custom (`uplcbench`, JSON) | [SeungheonOh/llvm-uplc](https://github.com/SeungheonOh/llvm-uplc) |

## What's Measured

Each VM runs 89 real-world Plutus smart contract scripts (auction, escrow, uniswap, stablecoin, etc.) in two tiers: the **full tier** times flat-decode + evaluate, and the **eval tier** times evaluation of a program decoded before timing. See [METHODOLOGY.md](METHODOLOGY.md#what-is-measured) for what each VM times in each tier.

All VMs use the same canonical `.flat` test data committed in `data/plutus_use_cases/`.

A second corpus, `data/mainnet_recent/`, holds 1360 validator evaluations from recent mainnet transactions. Select it with `BENCH_CORPUS=mainnet_recent`. They come from 522 transactions, and a run samples whole transactions: by default every script of 40 transactions (about 100 programs), selected by `BENCH_SEED` (default `1`). The same seed always selects the same transactions. `BENCH_SAMPLE` sets the number of transactions, and `BENCH_SAMPLE=all` runs every program. Mainnet results are ranked per transaction, summing each VM's times over every script a transaction runs, as well as per script run (see [METHODOLOGY.md](METHODOLOGY.md#mainnet-corpus)).

## Quick Start

```bash
# Build and run all benchmarks
docker compose up

# Or step by step
docker compose build
docker compose run --rm benchmark

# Run specific VMs only
docker compose run --rm -e BENCH_VMS=chrysalis,amaru-uplc benchmark

# Run on the mainnet corpus instead of plutus_use_cases (40 transactions, seed 1)
docker compose run --rm -e BENCH_CORPUS=mainnet_recent benchmark

# Another seed, a larger sample, or the whole mainnet corpus
docker compose run --rm -e BENCH_CORPUS=mainnet_recent -e BENCH_SEED=7 -e BENCH_SAMPLE=100 benchmark
docker compose run --rm -e BENCH_CORPUS=mainnet_recent -e BENCH_SAMPLE=all benchmark

# Record the host CPU when the container cannot see it (e.g. Docker on macOS)
HOST_CPU="Apple M4 Pro" docker compose run --rm benchmark
```

Results are written to `./results/<date>/`:
- `unified.csv` — all VMs, all scripts, nanosecond precision
- `report.md` — markdown comparison table with geometric means
- `versions.csv` — VM release labels, source commits, and toolchains
- `corpus.txt` — the programs the run measured

The page shows the newest run of each corpus (`python report/generate_report.py --latest results`), with switches for the corpus, the tier and, for mainnet, ranking per transaction or per script run. Each corpus view lists the programs it measured and, for a sample, the seed that selected them.
- Per-VM raw output logs

## Updating VM Versions

The benchmark tracks the newest code of each VM, not only its latest stable
release. `scripts/update-pins.sh` moves every pin in `.env` forward:

- a VM built from git is pinned to the newest commit on its default branch,
  labelled with its tag when that commit is tagged, otherwise `<branch>@<commit>`;
- a VM used through a package registry (Amaru UPLC on crates.io,
  plutus-machine on npm) is pinned to its newest published version,
  pre-releases included, and its adapter lockfile is regenerated.

Pins stay exact (full commit SHAs and exact package versions), so every run
can be rebuilt from the `.env` committed with it.

```bash
scripts/update-pins.sh
docker compose build --no-cache
docker compose run --rm benchmark
```

Each run records the VM release labels, source commit SHAs, and toolchain
versions in `versions.csv`. The generated page shows this provenance under
**VM Versions & Toolchain**; source revisions link to their exact commits.

## Project Structure

```
data/plutus_use_cases/    # 89 canonical .flat benchmark scripts
data/mainnet_recent/      # 1360 applied mainnet validators (BENCH_CORPUS=mainnet_recent)
tools/mainnet-corpus/     # Generator for data/mainnet_recent
Dockerfile                # Multi-stage: build all VMs, single ubuntu:24.04 runtime
docker-compose.yml        # One-command orchestration
.env              # Pinned git SHAs and toolchain versions
scripts/                  # Per-VM runner scripts, orchestrator, update-pins.sh
parsers/                  # Output normalizers (one per framework)
report/                   # Unified CSV -> markdown report generator
harness/                  # Adapters for Amaru and plutus-machine; eval-tier patches and harnesses
results/                  # Git-tracked results, including per-run versions.csv
```

## Methodology

See [METHODOLOGY.md](METHODOLOGY.md) for details on fairness, statistical methodology, and limitations.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## TODO

- [ ] Add Aiken UPLC (Rust, [aiken-lang/aiken](https://github.com/aiken-lang/aiken) `crates/uplc`) — needs custom bench harness, no native benchmarks exist

## License

[MIT](LICENSE)
