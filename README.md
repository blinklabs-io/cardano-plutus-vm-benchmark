# Cardano Plutus VM Benchmark

Reproducible, cross-language benchmark suite for Plutus (UPLC) virtual machine implementations.

Builds 10 VMs from source inside Docker, runs each VM's **native benchmark framework**, and generates a unified comparison report. [View full results](https://blinklabs-io.github.io/cardano-plutus-vm-benchmark/)

## Latest Results (2026-05-09)

> AMD Ryzen 9 9900X3D, 24 cores, 47 GB RAM, Ubuntu 24.04 (WSL2)

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc (JIT)** | C++ / LLVM | 95.09 us | 1.00x |
| **Scalus (JIT)** | Scala / JVM | 169.09 us | 1.78x |
| **plutus-core** | Haskell | 176.05 us | 1.85x |
| **uplc-turbo (bytecode)** | Rust | 205.45 us | 2.16x |
| **Julc** | Java / GraalVM | 247.62 us | 2.60x |
| **uplc-turbo (AST)** | Rust | 267.72 us | 2.82x |
| **Scalus (CEK)** | Scala / JVM | 282.70 us | 2.97x |
| **Plutuz** | Zig | 365.69 us | 3.85x |
| **Chrysalis (JIT)** | C# / .NET | 386.98 us | 4.07x |
| **Chrysalis (AOT)** | C# / .NET | 388.27 us | 4.08x |
| **Plutigo** | Go | 551.81 us | 5.80x |
| **blaze-plutus (JSC)** | TypeScript | 1.20 ms | 12.66x |
| **blaze-plutus (V8)** | TypeScript | 1.21 ms | 12.72x |
| **opshin** | Python | 49.69 ms | 522.52x |

*Geometric mean of 89 plutus_use_cases scripts. Lower is better. Copied from [`results/2026-05-09/report.md`](results/2026-05-09/report.md); refresh this table whenever a new results directory is committed.*

## VMs Benchmarked

| VM | Language | Benchmark Framework | Repository |
|---|---|---|---|
| **uplc-turbo** | Rust | Criterion.rs | [pragma-org/uplc](https://github.com/pragma-org/uplc) |
| **uplc-turbo (bytecode)** | Rust | Criterion.rs | [pragma-org/uplc PR #47](https://github.com/pragma-org/uplc/pull/47) branch `pi/bytecode` (unmerged) |
| **Plutuz** | Zig | Custom (JSON) | [utxo-company/plutuz](https://github.com/utxo-company/plutuz) |
| **Chrysalis** | C# / .NET | BenchmarkDotNet (JIT + AOT) | [SAIB-Inc/Chrysalis](https://github.com/SAIB-Inc/Chrysalis) |
| **Plutigo** | Go | testing.B | [blinklabs-io/plutigo](https://github.com/blinklabs-io/plutigo) |
| **blaze-plutus** | TypeScript | Vitest bench (V8 + JSC) | [butaneprotocol/blaze-cardano](https://github.com/butaneprotocol/blaze-cardano) |
| **opshin-uplc** | Python | Custom | [OpShin/uplc](https://github.com/OpShin/uplc) |
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
docker compose run --rm -e BENCH_VMS=chrysalis,uplc-turbo benchmark

# Record the host CPU when the container cannot see it (e.g. Docker on macOS)
HOST_CPU="Apple M4 Pro" docker compose run --rm benchmark
```

Results are written to `./results/<date>/`:
- `unified.csv` — all VMs, all scripts, nanosecond precision
- `report.md` — markdown comparison table with geometric means
- Per-VM raw output logs

## Updating VM Versions

Edit `.env` to change pinned git SHAs, then rebuild:

```bash
# Edit .env with new SHAs
docker compose build --no-cache
docker compose run --rm benchmark
```

## Project Structure

```
data/plutus_use_cases/    # 89 canonical .flat benchmark scripts
Dockerfile                # Multi-stage: build all VMs, single ubuntu:24.04 runtime
docker-compose.yml        # One-command orchestration
.env              # Pinned git SHAs and toolchain versions
scripts/                  # Per-VM runner scripts + orchestrator
parsers/                  # Output normalizers (one per framework)
report/                   # Unified CSV -> markdown report generator
results/                  # Git-tracked historical results
```

## Methodology

See [METHODOLOGY.md](METHODOLOGY.md) for details on fairness, statistical methodology, and limitations.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## TODO

- [ ] Add Aiken UPLC (Rust, [aiken-lang/aiken](https://github.com/aiken-lang/aiken) `crates/uplc`) — needs custom bench harness, no native benchmarks exist
- [ ] Add Haskell plutus-core (IOG reference implementation) — requires GHC + cabal Docker setup

## License

[MIT](LICENSE)
