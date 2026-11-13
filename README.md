# Cardano Plutus VM Benchmark

Reproducible, cross-language benchmark suite for Plutus (UPLC) virtual machine implementations.

Builds 11 VMs from source or released packages inside Docker, runs each VM's benchmark framework, and generates a unified comparison report. [View full results](https://blinklabs-io.github.io/cardano-plutus-vm-benchmark/)

This version is maintained by [Blink Labs](https://blinklabs.io). It continues the [original benchmark by SAIB Inc.](https://github.com/SAIB-Inc/cardano-plutus-vm-benchmark) and tracks the newest code of each VM rather than only its latest stable release (see [Updating VM Versions](#updating-vm-versions)).

## Latest Results (2026-11-11)

> System: Intel Core i7-6700 @ 3.40 GHz, 8 logical cores, 15 GiB RAM, Linux kernel 6.8.0-147-generic

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 162.69 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 174.84 us | 1.07x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 351.02 us | 2.16x |
| **Plutigo CEK (Go)** | Go | 352.55 us | 2.17x |
| **Amaru UPLC CEK (Rust)** | Rust | 370.44 us | 2.28x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 444.33 us | 2.73x |
| **Plutuz CEK (Zig)** | Zig | 655.00 us | 4.03x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 706.66 us | 4.34x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 748.33 us | 4.60x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 804.04 us | 4.94x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.29 ms | 14.05x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.30 ms | 14.13x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 14.45 ms | 88.82x |
| **opshin CEK (Python / CPython)** | Python / CPython | 104.09 ms | 639.84x |

*All 14 benchmark configurations were measured on Nov 11 across 89 `plutus_use_cases` scripts. Julc had 11 evaluation failures and OpShin had 30; failures are shown in the report and use the slowest successful time for that script in the geometric mean. Lower is better. Scalus JIT's three-sample JMH intervals are wider than its means for most scripts, so its result is low confidence. See [`results/2026-11-11/report.md`](results/2026-11-11/report.md) for versions, results, and coverage.*

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

## Quick Start

```bash
# Build and run all benchmarks
docker compose up

# Or step by step
docker compose build
docker compose run --rm benchmark

# Run specific VMs only
docker compose run --rm -e BENCH_VMS=chrysalis,amaru-uplc benchmark

# Record the host CPU when the container cannot see it (e.g. Docker on macOS)
HOST_CPU="Apple M4 Pro" docker compose run --rm benchmark
```

Results are written to `./results/<date>/`:
- `unified.csv` — all VMs, all scripts, nanosecond precision
- `report.md` — markdown comparison table with geometric means
- `versions.csv` — VM release labels, source commits, and toolchains
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
