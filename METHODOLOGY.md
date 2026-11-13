# Methodology

This benchmark is maintained by [Blink Labs](https://blinklabs.io) and continues the [original benchmark by SAIB Inc.](https://github.com/SAIB-Inc/cardano-plutus-vm-benchmark)

## What is Measured

Results come in two tiers, which are ranked separately:

- **Full tier**: each iteration decodes the whole `.flat` file (the script and its Data arguments) into the VM's term representation and evaluates it. This is the end-to-end cost of evaluating a program from its serialized form.
- **Eval tier**: the program is decoded before timing, and each iteration evaluates it. This is the cost of the evaluator alone.

Both tiers include whatever per-run setup a VM performs for each evaluation (for example, creating a machine). Each VM writes `<vm>.csv` for the full tier and `<vm>-eval.csv` for the eval tier, and `unified.csv` records the tier of every row.

| VM | Full tier | Eval tier |
|---|---|---|
| plutus-core | `validation-flat` (our `harness/haskell/BenchFlat.hs`): decodes and fully forces the program, then evaluates it | upstream `validation` (`BenchCek.hs`) |
| Plutigo | `BenchmarkFlatFiles` (`cek.RunFlat`) | `BenchmarkFlatFilesPrepared`: `cek.PrepareProgram` decodes the program and checks its structure and scopes once before timing, as a node does for a cached script, and each iteration runs `cek.RunPreparedScriptContext` |
| Scalus CEK | `CekJVMBenchmark.bench` | `CekJVMBenchmark.benchEval` |
| Scalus JIT | — | `JITBenchmark.benchJIT`; decoding and JIT compilation are in `@Setup` |
| llvm-uplc | — | `uplcbench --mode compiled`; decoding and JIT compilation are before timing |
| Julc | — | `CekJavaBenchmark.bench`; decoding is in `@Setup`, and each call prepares the program (builtin availability walk and cost model construction) |
| Amaru UPLC | our harness | our harness, `PVB_TIER=eval` |
| Harmonic Labs plutus-machine | our harness | our harness, `PVB_TIER=eval` |
| opshin | our script | our script, `PVB_TIER=eval` |
| Chrysalis (JIT and AOT) | upstream `DecodeAndEval` | `Eval`, added by `harness/chrysalis/eval-tier.patch` |
| blaze-plutus (Node / V8 and Bun / JavaScriptCore) | upstream bench | `PVB_TIER=eval`, added by `harness/blaze/pvb.patch` |
| Plutuz | upstream bench | `PVB_TIER=eval`, added by `harness/plutuz/eval-tier.patch`; each iteration decodes a fresh program before its timer starts |

Plutigo and plutus-core evaluate every script as a Plutus V3 program, as plutus-core's own `validation` benchmark does.

Where the eval tier reuses one decoded program across iterations and the term representation is mutable (plutus-machine, opshin, blaze-plutus), the harness first checks that evaluation leaves the decoded program unchanged, and records the script as failed if it does not.

## VM Versions

The benchmark tracks the newest code of each VM, not only its latest stable release. `scripts/update-pins.sh` pins:

- each VM built from git to the newest commit on its default branch, by full commit SHA. The label is the commit's tag when it is tagged, otherwise `<branch>@<commit>`;
- each VM used through a package registry (Amaru UPLC on crates.io, plutus-machine on npm) to its newest published version, pre-releases included, with its adapter lockfile regenerated.

Each run records the label, commit and toolchain of every VM in `versions.csv`, and the page lists them under **VM Versions & Toolchain**. Toolchain versions (compilers and runtimes) are updated separately.

## Runtimes

blaze-plutus runs twice, on Node (V8) and on Bun (JavaScriptCore). The Bun row runs `bun --bun run vitest`: vitest's command starts with `#!/usr/bin/env node`, and without `--bun` Bun hands it to Node. `harness/blaze/pvb.patch` makes the benchmark print the runtime that runs it, and each blaze runner fails if it is not the expected one.

## Test Data

89 flat-encoded Plutus smart contract scripts from the `plutus-use-cases` test suite. These are real-world contracts covering:

- Auction, Crowdfunding, Currency, Escrow
- Futures (settle, pay-out, increase-margin)
- Game state machines, Multisig state machines
- Ping-pong, Prism, Pubkey
- Stablecoin, Token account, Uniswap, Vesting

Script sizes range from 3 KB to 13 KB. All VMs use the same canonical copies from `data/plutus_use_cases/`.

## Why Native Benchmarks

Each VM uses its own benchmark framework rather than a uniform harness:

| VM | Framework | Warmup | Min Iterations | Time Budget |
|---|---|---|---|---|
| plutus-core | Criterion (Haskell) | Automatic | Automatic | Automatic |
| Chrysalis | BenchmarkDotNet (`--job short`) | 3 iterations | 3 | Auto |
| Amaru UPLC | Repository Criterion.rs adapter | Automatic (warmup phase) | Auto | Auto |
| Harmonic Labs plutus-machine | Repository Node.js adapter | 5 iterations | 50 | 5s |
| Plutigo | Go testing.B | Automatic (b.N scaling) | Auto | 5s |
| blaze-plutus | Vitest bench | Automatic | Auto | Auto |
| Plutuz | Custom | 5 iterations | 50 | 5s |
| opshin-uplc | Custom | 5 iterations | 50 | 5s |
| llvm-uplc | Custom (`uplcbench`) | 5 iterations | 50 | 5s |
| Scalus, Julc | JMH (`-wi 1 -i 3 -f 1`) | 1 iteration | 3 | 5s |

Each framework handles warmup, iteration count, and outlier detection using its own proven methodology. Reimplementing this in a uniform harness would be less accurate and harder to maintain.

## Fairness Constraints

- **Same data**: all VMs decode the same 89 `.flat` files
- **Same machine**: all VMs run inside a single Docker container (`ubuntu:24.04`, glibc)
- **Sequential execution**: VMs run one at a time to avoid CPU contention
- **Pinned versions**: every VM is pinned to an exact source revision or package version in `.env`, moved to the newest by `scripts/update-pins.sh` (see [VM Versions](#vm-versions))
- **Implementation-owned benchmark paths**: each VM uses its native benchmark when one is published. The Amaru adapter exercises the released crate through the same Criterion loop as its source benchmark. The plutus-machine adapter exercises the exact npm package used by Pebble, but replaces `process.env` with a plain object before loading it (see Limitations).
- **Amaru release profile**: its adapter is compiled with fat LTO and one codegen unit. Its default V3/PV11 cost model is constructed once per process and cloned for each `Program::eval`, matching the upstream adapter.

## Unified Output

All results are normalized to a common CSV schema:

```csv
vm,script,mean_ns,median_ns,min_ns,max_ns,stddev_ns,iterations
```

Times are in **nanoseconds**. The summary uses **geometric mean** across all 89 scripts, which is standard for cross-benchmark comparison (it handles the wide range of script complexities without being dominated by outliers).

## Limitations

- **Different statistical methodologies**: each framework computes mean/median/stddev differently. BenchmarkDotNet and Criterion are the most sophisticated; Go bench and the custom frameworks are simpler.
- **Go bench lacks stddev/min/max**: only reports mean ns/op in default output.
- **Unavailable statistics**: `-1` marks a statistic the framework does not provide. Vitest's text output has no median or standard deviation; its RME is retained in the raw log and is not a standard deviation. JMH CSV provides a confidence interval, not median, minimum, maximum, or standard deviation; the raw JMH CSV retains that confidence interval. Rankings use `mean_ns` only.
- **Short BenchmarkDotNet job**: `--job short` takes 3 measurement iterations, so on noisy scripts the Chrysalis 99.9% confidence error can exceed the mean.
- **Short JMH job**: Scalus JIT, Scalus CEK and Julc use three measurement samples. Scalus JIT's raw 99.9% confidence intervals are wider than the mean for most scripts in the published runs, so its aggregate should be treated as low confidence.
- **JIT compilation**: llvm-uplc and Scalus JIT compile each script before timing, so they appear only in the eval tier. llvm-uplc retains its compilation time as `compile_ns` in the raw JSON.
- **Results before tiers**: runs recorded before tiers were introduced have no `tier` column and are read as the full tier, but their plutus-core, Julc, Scalus JIT and llvm-uplc rows measured evaluation without decoding.
- **blaze-plutus on Bun before the runtime check**: runs recorded before the runtime check ran their "Bun JSC" row with `bun run vitest`, which runs on Node. Those rows measured Node (V8), not JavaScriptCore.
- **Unreleased code**: following each VM's default branch measures code that may change before its next release, including regressions that a release would fix. The label in `versions.csv` says whether a pin is a tagged release.
- **plutus-machine `process.env` replacement**: the package reads `PEBBLE_PROFILE` on every CEK step. The adapter swaps `process.env` for a plain object so that native lookup is not measured, which also removes a per-step cost Pebble users pay. Its numbers are therefore not end-to-end and are not directly comparable to the other VMs.
- **JIT warmup variance**: .NET and Node.js/Bun have JIT compilation, meaning early iterations are slower. Their frameworks account for this, but it's a fundamentally different execution model than ahead-of-time compiled VMs.
- **Memory comparison**: each VM uses different allocators and GC strategies. Memory numbers are not directly comparable across languages.
- **Docker overhead**: container execution adds minimal but non-zero overhead vs bare metal. This affects all VMs equally.

## Reproducing

Anyone with Docker can reproduce results:

```bash
git clone https://github.com/blinklabs-io/cardano-plutus-vm-benchmark.git
cd cardano-plutus-vm-benchmark
docker compose up
```

For the most consistent results, run on a dedicated machine with no other workloads.
