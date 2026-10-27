# Cardano Plutus VM Benchmark

Reproducible, cross-language benchmark suite for Plutus (UPLC) virtual machine implementations.

Builds 11 VMs from source inside Docker, runs each VM's **native benchmark framework**, and generates a unified comparison report. [View full results](https://blinklabs-io.github.io/cardano-plutus-vm-benchmark/)

## Latest Results (2026-10-27-0)

> System: Intel Core i7-6700 @ 3.40 GHz, 8 logical cores, 15 GiB RAM, Ubuntu 24.04.5 LTS

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc UPLC→native JIT (C++ / LLVM)** | C++ / LLVM | 165.41 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 174.92 us | 1.06x |
| **uplc-turbo Bytecode VM (Rust)** | Rust | 297.38 us | 1.80x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 354.88 us | 2.15x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 458.16 us | 2.77x |
| **Plutigo CEK (Go)** | Go | 461.28 us | 2.79x |
| **Amaru UPLC CEK (Rust)** | Rust | 507.39 us | 3.07x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 639.38 us | 3.87x |
| **Plutuz CEK (Zig)** | Zig | 659.34 us | 3.99x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 722.85 us | 4.37x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 753.88 us | 4.56x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.26 ms | 13.66x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.30 ms | 13.92x |
| **opshin CEK (Python / CPython)** | Python / CPython | 53.33 ms | 322.43x |

*Plutigo v0.10.0 and Amaru UPLC v0.4.0 from the Amaru monorepo; geometric means across 89 `plutus_use_cases` scripts. Plutigo was measured twice on Oct 27 and aggregated; Amaru was measured from the monorepo pin on Oct 27. Remaining VM measurements are carried forward from Oct 26. Plutigo measured 461.28 us, 3.58% slower than v0.9.11's 445.34 us. Lower is better. See [`results/2026-10-27-0/report.md`](results/2026-10-27-0/report.md) for versions, results, and coverage.*

## VMs Benchmarked

| VM | Language | Benchmark Framework | Repository |
|---|---|---|---|
| **plutus-core** | Haskell / GHC | Criterion | [IntersectMBO/plutus](https://github.com/IntersectMBO/plutus) (`plutus-benchmark`) |
| **Amaru UPLC** | Rust | Criterion.rs | [`amaru-uplc` v0.4.0](https://github.com/pragma-org/amaru/tree/main/crates/amaru-uplc) |
| **uplc-turbo (bytecode)** | Rust | Criterion.rs | [pragma-org/uplc PR #47](https://github.com/pragma-org/uplc/pull/47) branch `pi/bytecode` (unmerged) |
| **Plutuz** | Zig | Custom (JSON) | [utxo-company/plutuz](https://github.com/utxo-company/plutuz) |
| **Chrysalis** | C# / .NET | BenchmarkDotNet (JIT + AOT) | [SAIB-Inc/Chrysalis](https://github.com/SAIB-Inc/Chrysalis) |
| **Plutigo v0.10.0** | Go | testing.B | [blinklabs-io/plutigo](https://github.com/blinklabs-io/plutigo) |
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
