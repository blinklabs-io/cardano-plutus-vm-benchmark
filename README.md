# Cardano Plutus VM Benchmark

Reproducible, cross-language benchmark suite for Plutus (UPLC) virtual machine implementations.

Builds 11 VMs from source or released packages inside Docker, runs each VM's benchmark framework, and generates a unified comparison report. [View full results](https://blinklabs-io.github.io/cardano-plutus-vm-benchmark/)

This version is maintained by [Blink Labs](https://blinklabs.io). It continues the [original benchmark by SAIB Inc.](https://github.com/SAIB-Inc/cardano-plutus-vm-benchmark) and tracks the newest code of each VM rather than only its latest stable release (see [Updating VM Versions](#updating-vm-versions)).

## Latest Results (2026-11-17)

> System: Intel Core i7-6700 @ 3.40 GHz, 8 logical cores, 15 GiB RAM, Linux kernel 6.8.0-147-generic

Each VM was built from the newest code on its default branch, or its newest published package (see [`versions.csv`](results/2026-11-17/versions.csv)). Each corpus and each tier is ranked separately; lower is better. The [page](https://blinklabs-io.github.io/cardano-plutus-vm-benchmark/) switches between them and lists every program measured.

### Plutus use cases: all 89 programs

#### Full tier: decode and evaluate

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Plutigo CEK (Go)** | Go | 352.36 us | 1.00x |
| **Amaru UPLC CEK (Rust)** | Rust | 377.15 us | 1.07x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 459.30 us | 1.30x |
| **Plutuz CEK (Zig)** | Zig | 688.36 us | 1.95x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 731.66 us | 2.08x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 769.35 us | 2.18x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 1.03 ms | 2.92x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.37 ms | 6.72x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.41 ms | 6.85x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 15.00 ms | 42.56x |
| **opshin CEK (Python / CPython)** | Python / CPython | 109.11 ms | 309.66x |

#### Eval tier: evaluate a decoded program

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 168.41 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 186.75 us | 1.11x |
| **Plutigo CEK (Go)** | Go | 245.50 us | 1.46x |
| **Amaru UPLC CEK (Rust)** | Rust | 255.17 us | 1.52x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 285.65 us | 1.70x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 340.80 us | 2.02x |
| **Plutuz CEK (Zig)** | Zig | 470.71 us | 2.80x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 523.13 us | 3.11x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 556.45 us | 3.30x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 762.69 us | 4.53x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.86 ms | 11.04x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.88 ms | 11.19x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 13.20 ms | 78.39x |
| **opshin CEK (Python / CPython)** | Python / CPython | 94.50 ms | 561.16x |

*Julc fails 11 scripts and OpShin 30; failures use the slowest successful time for that script in the geometric mean. Scalus JIT was rerun after an sbt packaging error. See [`results/2026-11-17/report.md`](results/2026-11-17/report.md).*

### Mainnet validators: every script of 40 of 522 transactions, seed 1

Ranked per transaction: a VM's time for a transaction is the sum of its times for every script the transaction runs (102 scripts in all). A VM that fails any script fails the transaction.

#### Full tier: decode and evaluate

| VM | Language | Geo Mean | vs Fastest | Failed transactions |
|---|---|---|---|---|
| **Amaru UPLC CEK (Rust)** | Rust | 350.87 us | 1.00x | 0 |
| **Plutigo CEK (Go)** | Go | 388.74 us | 1.11x | 0 |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 436.27 us | 1.24x | 0 |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 547.33 us | 1.56x | 0 |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 565.61 us | 1.61x | 0 |
| **Plutuz CEK (Zig)** | Zig | 872.44 us | 2.49x | 0 |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 1.26 ms | 3.58x | 0 |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.80 ms | 5.14x | 0 |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.86 ms | 5.29x | 0 |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 14.35 ms | 40.89x | 0 |
| **opshin CEK (Python / CPython)** | Python / CPython | 33.51 ms | 95.51x | 24 |

#### Eval tier: evaluate a decoded program

| VM | Language | Geo Mean | vs Fastest | Failed transactions |
|---|---|---|---|---|
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 96.68 us | 1.00x | 0 |
| **Plutigo CEK (Go)** | Go | 152.87 us | 1.58x | 0 |
| **Amaru UPLC CEK (Rust)** | Rust | 155.24 us | 1.61x | 0 |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 160.48 us | 1.66x | 0 |
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 166.40 us | 1.72x | 0 |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 173.03 us | 1.79x | 0 |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 262.25 us | 2.71x | 0 |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 269.48 us | 2.79x | 0 |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 390.18 us | 4.04x | 0 |
| **Plutuz CEK (Zig)** | Zig | 540.39 us | 5.59x | 0 |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.03 ms | 10.68x | 0 |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.08 ms | 11.12x | 0 |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 11.24 ms | 116.23x | 0 |
| **opshin CEK (Python / CPython)** | Python / CPython | 24.45 ms | 252.91x | 24 |

*OpShin fails 24 of the 102 scripts, each of which succeeded on mainnet; a failed transaction uses the slowest successful total for it in the geometric mean. [`results/2026-11-16-mainnet_recent/report.md`](results/2026-11-16-mainnet_recent/report.md) also ranks per script run, and [`corpus.txt`](results/2026-11-16-mainnet_recent/corpus.txt) lists the programs.*

*Full tier: each iteration decodes the whole `.flat` file, including its Data arguments, and evaluates it. Eval tier: the program is decoded before timing; JIT VMs (Scalus JIT, llvm-uplc) and Julc appear here only (see [METHODOLOGY.md](METHODOLOGY.md#what-is-measured)). Scalus JIT's three-sample JMH intervals are wide, so its results are low confidence.*

## VMs Benchmarked

| VM | Language | Benchmark Framework | Repository |
|---|---|---|---|
| **plutus-core** | Haskell / GHC | Criterion | [IntersectMBO/plutus](https://github.com/IntersectMBO/plutus) (`plutus-benchmark`) |
| **Amaru UPLC** | Rust | Repository Criterion.rs adapter | [`amaru-uplc`](https://crates.io/crates/amaru-uplc) |
| **Aiken UPLC** | Rust | Repository Criterion.rs adapter | [aiken-lang/aiken](https://github.com/aiken-lang/aiken) (`crates/uplc`) |
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

A second corpus, `data/mainnet_recent/`, holds 1360 validator evaluations from recent mainnet transactions. Select it with `BENCH_CORPUS=mainnet_recent`. They come from 522 transactions, and a run samples whole transactions: by default every script of 40 transactions (about 100 programs), selected by `BENCH_SEED` (default `1`). The same seed always selects the same transactions. `BENCH_SAMPLE` sets the number of transactions, and `BENCH_SAMPLE=all` runs every program. Mainnet results are ranked per transaction only when every corpus script for that transaction is present in the run, summing each VM's times across those scripts. Reports also rank per script run (see [METHODOLOGY.md](METHODOLOGY.md#mainnet-corpus)).

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

The page shows the newest run of each corpus (`python report/generate_report.py --latest results`), with switches for the corpus, the tier and, when complete transaction groups are available, ranking per transaction or per script run. Each corpus view lists the programs it measured and, for a sample, the seed that selected them.
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
harness/                  # Adapters for Amaru, Aiken and plutus-machine; eval-tier patches and harnesses
results/                  # Git-tracked results, including per-run versions.csv
```

## Methodology

See [METHODOLOGY.md](METHODOLOGY.md) for details on fairness, statistical methodology, and limitations.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## TODO


## License

[MIT](LICENSE)
