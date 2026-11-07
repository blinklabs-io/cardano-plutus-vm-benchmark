# Cardano Plutus VM Benchmark

Reproducible, cross-language benchmark suite for Plutus (UPLC) virtual machine implementations.

Builds 12 VMs from source or released packages inside Docker, runs each VM's benchmark framework, and generates a unified comparison report. [View full results](https://blinklabs-io.github.io/cardano-plutus-vm-benchmark/)

## Latest Results (2026-11-07)

> System: Intel Core i7-6700 @ 3.40 GHz, 8 logical cores, 15 GiB RAM, Linux kernel 6.8.0-147-generic

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 169.64 us | 1.00x |
| **uplc-turbo Bytecode VM (Rust)** | Rust | 313.49 us | 1.85x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 342.91 us | 2.02x |
| **Plutigo CEK (Go)** | Go | 368.03 us | 2.17x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 387.76 us | 2.29x |
| **Amaru UPLC CEK (Rust)** | Rust | 388.78 us | 2.29x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 480.91 us | 2.83x |
| **Plutuz CEK (Zig)** | Zig | 682.81 us | 4.03x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 766.45 us | 4.52x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 792.41 us | 4.67x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 888.63 us | 5.24x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.46 ms | 14.50x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.47 ms | 14.57x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 20.50 ms | 120.83x |
| **opshin CEK (Python / CPython)** | Python / CPython | 119.62 ms | 705.11x |

*All 15 benchmark configurations were measured on Nov 7 across 89 `plutus_use_cases` scripts. Julc had 11 evaluation failures and OpShin had 30; failures are shown in the report and use the slowest successful time for that script in the geometric mean. Lower is better. See [`results/2026-11-07/report.md`](results/2026-11-07/report.md) for versions, results, and coverage.*

## VMs Benchmarked

| VM | Language | Benchmark Framework | Repository |
|---|---|---|---|
| **plutus-core** | Haskell / GHC | Criterion | [IntersectMBO/plutus](https://github.com/IntersectMBO/plutus) (`plutus-benchmark`) |
| **Amaru UPLC** | Rust | Repository Criterion.rs adapter | [`amaru-uplc` v0.6.0](https://crates.io/crates/amaru-uplc/0.6.0) |
| **Harmonic Labs plutus-machine** | TypeScript / Node.js | Repository Node.js adapter | [`plutus-machine` v3.0.5](https://www.npmjs.com/package/@harmoniclabs/plutus-machine/v/3.0.5), the evaluator used by Pebble v0.5.0 |
| **uplc-turbo (bytecode)** | Rust | Criterion.rs | [pragma-org/uplc PR #47](https://github.com/pragma-org/uplc/pull/47) branch `pi/bytecode` (unmerged) |
| **Plutuz** | Zig | Custom (JSON) | [utxo-company/plutuz](https://github.com/utxo-company/plutuz) |
| **Chrysalis** | C# / .NET | BenchmarkDotNet (JIT + AOT) | [SAIB-Inc/Chrysalis](https://github.com/SAIB-Inc/Chrysalis) |
| **Plutigo v0.11.4** | Go | testing.B | [blinklabs-io/plutigo](https://github.com/blinklabs-io/plutigo) |
| **blaze-plutus** | TypeScript | Vitest bench (V8 + JSC) | [butaneprotocol/blaze-cardano](https://github.com/butaneprotocol/blaze-cardano) |
| **opshin-uplc** | Python | Custom | [OpShin/uplc](https://github.com/OpShin/uplc) |
| **Scalus** | Scala / JVM | JMH | [scalus3/scalus](https://github.com/scalus3/scalus) |
| **Julc** | Java | JMH (CEK) | [bloxbean/julc](https://github.com/bloxbean/julc) |
| **llvm-uplc** | C++ / LLVM | Custom (`uplcbench`, JSON) | [SeungheonOh/llvm-uplc](https://github.com/SeungheonOh/llvm-uplc) |

## What's Measured

Each VM: **flat-decode + CEK evaluate** on 89 real-world Plutus smart contract scripts (auction, escrow, uniswap, stablecoin, etc.).

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

Edit `.env` to change pinned git SHAs, then rebuild:

```bash
# Edit .env with new SHAs
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
scripts/                  # Per-VM runner scripts + orchestrator
parsers/                  # Output normalizers (one per framework)
report/                   # Unified CSV -> markdown report generator
harness/                  # Release-package adapters for Amaru and plutus-machine
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
