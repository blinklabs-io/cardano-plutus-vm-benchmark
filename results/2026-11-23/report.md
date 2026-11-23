# Cardano Plutus VM Benchmark Results

**Date:** 2026-11-23

**Corpus:** Plutus use cases (`plutus_use_cases`): all 89 programs. The per-script tables list every program measured.

## Environment
```
date: 2026-11-23T04:26:01+00:00
kernel: 6.8.0-147-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
corpus: plutus_use_cases (89 of 89 programs, sample all, seed 1; list in corpus.txt)
```

## VM Versions

| VM | Source revision | Toolchain |
|---|---|---|
| plutus-core CEK (Haskell / GHC) | master@ef2eb74 ([ef2eb74](https://github.com/IntersectMBO/plutus/commit/ef2eb74d836259d11b7f4cc4261851e707cfedb3)) | GHC 9.6.4 |
| Scalus UPLC→JVM JIT (Scala / JVM) | master@a3e3487 ([a3e3487](https://github.com/scalus3/scalus/commit/a3e348790452d614cf242f980380fc1246fc01f8)) | JDK 21 / Scala 3 |
| Scalus CEK (Scala / JVM) | master@a3e3487 ([a3e3487](https://github.com/scalus3/scalus/commit/a3e348790452d614cf242f980380fc1246fc01f8)) | JDK 21 / Scala 3 |
| Julc CEK (Java / GraalVM) | v0.1.0-pre22 ([b782bf4](https://github.com/bloxbean/julc/commit/b782bf4c1858a779c4d2e60ae5273c8c888edfc9)) | GraalVM 25.0.2-graal |
| llvm-uplc post-JIT execution (C++ / LLVM) | master@6bcef67 ([6bcef67](https://github.com/SeungheonOh/llvm-uplc/commit/6bcef67ce1995d232327f13d9080fe2f0261a55c)) | LLVM 22.1.0 |
| Amaru UPLC CEK (Rust) | [0.6.0](https://crates.io/crates/amaru-uplc/0.6.0) | rustc nightly-2026-09-04 |
| Aiken UPLC CEK (Rust) | main@b298f3f ([b298f3f](https://github.com/aiken-lang/aiken/commit/b298f3fe77a8f4704c79167294ab289f29c191fc)) | rustc 1.97 |
| Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | [3.1.0](https://www.npmjs.com/package/@harmoniclabs/plutus-machine/v/3.1.0) | Bun 1.3.14 |
| Plutuz CEK (Zig) | main@33b812d ([33b812d](https://github.com/utxo-company/plutuz/commit/33b812dbcf88f6851286e54cb93a4a443353f94c)) | Zig 0.15.2 |
| Chrysalis CEK (C# / .NET) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Chrysalis CEK (C# / .NET AOT) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Plutigo CEK (Go) | main@af1f997 ([af1f997](https://github.com/blinklabs-io/plutigo/commit/af1f9974d47624ad04241dda957670ad7421a6c1)) | Go 1.27.3 |
| blaze-plutus CEK (TypeScript / Bun JSC) | main@9936de1 ([9936de1](https://github.com/butaneprotocol/blaze-cardano/commit/9936de18a1c2a6999ae8a341703b1b0e32c5865d)) | Bun 1.3.14 |
| blaze-plutus CEK (TypeScript / Node V8) | main@9936de1 ([9936de1](https://github.com/butaneprotocol/blaze-cardano/commit/9936de18a1c2a6999ae8a341703b1b0e32c5865d)) | Node.js 22 |
| opshin CEK (Python / CPython) | 1.3.3 ([eda2fba](https://github.com/OpShin/uplc/commit/eda2fbaa89c1a2db4ec6c6c1fa5eea2a8b2671d4)) | Python 3.14 |

*Measurement caveats: llvm-uplc and Scalus JIT report execution after JIT compilation; llvm-uplc's per-script compilation time is retained only in the raw JSON. Scalus JIT, Scalus CEK, Julc and Chrysalis use three measurement samples, and their raw framework output should be consulted for uncertainty.*

## Full tier: decode and evaluate

Each iteration decodes the whole .flat file, including its Data arguments, and evaluates it.

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Plutigo CEK (Go)** | Go | 336.05 us | 1.00x |
| **Amaru UPLC CEK (Rust)** | Rust | 362.83 us | 1.08x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 441.56 us | 1.31x |
| **Plutuz CEK (Zig)** | Zig | 658.56 us | 1.96x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 702.65 us | 2.09x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 738.32 us | 2.20x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 973.39 us | 2.90x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.29 ms | 6.81x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.30 ms | 6.85x |
| **Aiken UPLC CEK (Rust)** | Rust | 2.95 ms | 8.77x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 8.11 ms | 24.13x |
| **opshin CEK (Python / CPython)** | Python / CPython | 74.66 ms | 222.16x |

#### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
| Amaru UPLC CEK (Rust) | 89 | 0 | 0 | 89 |
| Scalus CEK (Scala / JVM) | 89 | 0 | 0 | 89 |
| Plutuz CEK (Zig) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET AOT) | 89 | 0 | 0 | 89 |
| plutus-core CEK (Haskell / GHC) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| Aiken UPLC CEK (Rust) | 89 | 0 | 0 | 89 |
| Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus CEK (Scala / JVM) | Amaru UPLC CEK (Rust) | Aiken UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 497.96 us | 213.34 us | 181.38 us | 1.70 ms | 4.82 ms | 334.53 us | 325.90 us | 338.53 us | **159.77 us** | 937.60 us | 1.07 ms | 113.10 ms |
| auction_1-2 | 1.59 ms | 695.82 us | 596.54 us | 4.67 ms | 9.22 ms | 1.04 ms | 1.14 ms | 1.25 ms | **555.99 us** | 3.00 ms | 3.17 ms | 400.18 ms |
| auction_1-3 | 1.59 ms | 690.97 us | 592.29 us | 4.59 ms | 9.71 ms | 1.01 ms | 1.15 ms | 1.23 ms | **541.98 us** | 3.05 ms | 3.20 ms | 399.40 ms |
| auction_1-4 | 552.82 us | 250.29 us | 212.17 us | 1.90 ms | 6.65 ms | 395.85 us | 399.82 us | 430.94 us | **186.92 us** | 1.21 ms | 1.28 ms | 134.05 ms |
| auction_2-1 | 500.95 us | 212.77 us | 181.51 us | 1.71 ms | 5.05 ms | 334.29 us | 329.78 us | 337.00 us | **159.58 us** | 1.00 ms | 1.02 ms | 112.97 ms |
| auction_2-2 | 1.60 ms | 692.77 us | 590.95 us | 4.60 ms | 9.20 ms | 1.06 ms | 1.17 ms | 1.26 ms | **553.28 us** | 3.01 ms | 3.19 ms | 396.30 ms |
| auction_2-3 | 1.81 ms | 842.45 us | 715.37 us | 5.03 ms | 11.15 ms | 1.28 ms | 1.48 ms | 1.58 ms | **668.99 us** | 3.75 ms | 3.98 ms | 498.61 ms |
| auction_2-4 | 1.61 ms | 691.51 us | 584.65 us | 4.57 ms | 9.56 ms | 1.02 ms | 1.19 ms | 1.23 ms | **553.93 us** | 3.15 ms | 3.19 ms | 400.07 ms |
| auction_2-5 | 557.72 us | 247.65 us | 213.16 us | 1.83 ms | 6.68 ms | 396.05 us | 387.73 us | 412.60 us | **191.58 us** | 1.20 ms | 1.28 ms | 135.26 ms |
| coop-1 | 434.80 us | 243.01 us | **168.47 us** | 1.32 ms | 7.38 ms | 367.10 us | 346.70 us | 369.17 us | 177.76 us | 1.74 ms | 1.61 ms | FAIL |
| coop-2 | 1.30 ms | 766.51 us | **492.50 us** | 3.22 ms | 25.97 ms | 965.18 us | 1.15 ms | 1.19 ms | 556.31 us | 5.14 ms | 4.43 ms | FAIL |
| coop-3 | 2.68 ms | 2.08 ms | **1.29 ms** | 6.57 ms | 31.03 ms | 2.53 ms | 3.73 ms | 3.68 ms | 1.57 ms | 16.47 ms | 10.97 ms | FAIL |
| coop-4 | 1.60 ms | 926.23 us | **629.92 us** | 3.78 ms | 22.27 ms | 1.16 ms | 1.39 ms | 1.48 ms | 682.39 us | 6.15 ms | 5.31 ms | FAIL |
| coop-5 | 959.88 us | 461.27 us | **328.50 us** | 2.63 ms | 11.43 ms | 613.77 us | 681.89 us | 711.15 us | 340.65 us | 3.71 ms | 2.62 ms | FAIL |
| coop-6 | 981.09 us | 660.64 us | **417.03 us** | 2.55 ms | 24.67 ms | 917.35 us | 978.19 us | 1.00 ms | 483.59 us | 4.53 ms | 3.97 ms | FAIL |
| coop-7 | 577.22 us | 335.87 us | **226.68 us** | 1.65 ms | 11.57 ms | 494.22 us | 482.65 us | 497.46 us | 241.50 us | 2.27 ms | 2.05 ms | FAIL |
| crowdfunding-success-1 | 614.19 us | 254.17 us | 206.22 us | 2.06 ms | 6.13 ms | 384.15 us | 379.75 us | 393.25 us | **189.36 us** | 1.46 ms | 1.23 ms | 133.32 ms |
| crowdfunding-success-2 | 612.15 us | 254.12 us | 204.76 us | 2.06 ms | 5.92 ms | 383.69 us | 376.77 us | 394.75 us | **189.12 us** | 1.30 ms | 1.23 ms | 132.76 ms |
| crowdfunding-success-3 | 612.04 us | 256.55 us | 205.83 us | 2.06 ms | 5.92 ms | 384.22 us | 375.39 us | 396.97 us | **194.23 us** | 1.27 ms | 1.23 ms | 134.07 ms |
| currency-1 | 629.11 us | 293.08 us | 237.97 us | 2.11 ms | 4.57 ms | 442.12 us | 477.37 us | 508.41 us | **225.10 us** | 1.54 ms | 1.35 ms | 165.92 ms |
| escrow-redeem_1-1 | 877.88 us | 401.63 us | 319.76 us | 2.88 ms | 7.09 ms | 580.64 us | 635.48 us | 682.41 us | **305.57 us** | 2.08 ms | 1.88 ms | 220.34 ms |
| escrow-redeem_1-2 | 873.71 us | 402.53 us | 326.05 us | 2.81 ms | 7.29 ms | 580.52 us | 630.43 us | 707.82 us | **305.48 us** | 2.09 ms | 1.88 ms | 219.02 ms |
| escrow-redeem_2-1 | 948.00 us | 439.45 us | 356.22 us | 2.96 ms | 8.13 ms | 642.69 us | 712.62 us | 774.29 us | **338.43 us** | 2.42 ms | 2.13 ms | 248.46 ms |
| escrow-redeem_2-2 | 942.45 us | 441.03 us | 353.83 us | 2.94 ms | 8.19 ms | 642.45 us | 728.34 us | 794.43 us | **340.43 us** | 2.43 ms | 2.13 ms | 245.44 ms |
| escrow-redeem_2-3 | 942.05 us | 441.23 us | 354.32 us | 2.96 ms | 8.06 ms | 642.59 us | 725.33 us | 774.78 us | **341.26 us** | 2.41 ms | 2.14 ms | 248.78 ms |
| escrow-refund-1 | 688.53 us | 254.84 us | 197.13 us | 2.40 ms | 4.49 ms | 367.47 us | 337.43 us | 354.44 us | **177.53 us** | 1.03 ms | 1.05 ms | 123.00 ms |
| future-increase-margin-1 | 623.94 us | 290.33 us | 240.32 us | 2.12 ms | 4.57 ms | 429.11 us | 485.20 us | 513.27 us | **224.69 us** | 1.37 ms | 1.36 ms | 163.14 ms |
| future-increase-margin-2 | 1.07 ms | 534.85 us | 437.69 us | 3.29 ms | 9.91 ms | 786.23 us | 959.61 us | 991.50 us | **422.01 us** | 2.68 ms | 2.88 ms | 317.47 ms |
| future-increase-margin-3 | 1.08 ms | 529.43 us | 432.56 us | 3.29 ms | 10.12 ms | 786.53 us | 928.01 us | 1.00 ms | **432.10 us** | 2.78 ms | 2.92 ms | 321.03 ms |
| future-increase-margin-4 | 1.68 ms | 648.07 us | 538.42 us | 4.96 ms | 8.41 ms | 964.03 us | 1.02 ms | 1.08 ms | **495.35 us** | 2.66 ms | 3.02 ms | FAIL |
| future-increase-margin-5 | 2.05 ms | 898.87 us | 785.62 us | 5.57 ms | 12.39 ms | 1.49 ms | 1.66 ms | 1.66 ms | **662.44 us** | 5.09 ms | 6.59 ms | FAIL |
| future-pay-out-1 | 639.37 us | 290.66 us | 238.57 us | 2.10 ms | 4.69 ms | 438.47 us | 481.24 us | 506.16 us | **225.82 us** | 1.37 ms | 1.36 ms | 162.18 ms |
| future-pay-out-2 | 1.08 ms | 538.70 us | 435.41 us | 3.30 ms | 10.10 ms | 786.13 us | 967.94 us | 998.37 us | **422.62 us** | 2.73 ms | 2.70 ms | 326.56 ms |
| future-pay-out-3 | 1.08 ms | 533.75 us | 437.54 us | 3.32 ms | 10.26 ms | 787.95 us | 945.51 us | 1.00 ms | **424.29 us** | 2.60 ms | 2.71 ms | 320.25 ms |
| future-pay-out-4 | 2.12 ms | 893.80 us | 784.87 us | 5.53 ms | 12.26 ms | 1.50 ms | 1.57 ms | 1.68 ms | **662.18 us** | 4.96 ms | 6.44 ms | FAIL |
| future-settle-early-1 | 625.95 us | 292.56 us | 243.18 us | 2.10 ms | 4.76 ms | 426.90 us | 474.17 us | 545.93 us | **225.14 us** | 1.36 ms | 1.35 ms | 164.45 ms |
| future-settle-early-2 | 1.08 ms | 531.84 us | 437.54 us | 3.26 ms | 9.96 ms | 785.41 us | 945.42 us | 1.00 ms | **424.08 us** | 2.63 ms | 2.72 ms | 318.24 ms |
| future-settle-early-3 | 1.08 ms | 526.16 us | 438.68 us | 3.27 ms | 10.02 ms | 784.24 us | 1.00 ms | 1.01 ms | **424.32 us** | 2.61 ms | 2.72 ms | 320.29 ms |
| future-settle-early-4 | 1.84 ms | 769.35 us | 630.92 us | 5.12 ms | 10.28 ms | 1.19 ms | 1.20 ms | 1.27 ms | **546.55 us** | 4.14 ms | 5.50 ms | FAIL |
| game-sm-success_1-1 | 1.32 ms | 514.80 us | 415.47 us | 4.01 ms | 7.80 ms | 754.32 us | 802.96 us | 810.77 us | **389.27 us** | 2.12 ms | 2.29 ms | 262.26 ms |
| game-sm-success_1-2 | 474.17 us | 208.98 us | 183.52 us | 1.61 ms | 5.70 ms | 339.26 us | 335.75 us | 340.85 us | **161.44 us** | 1.08 ms | 1.13 ms | 118.98 ms |
| game-sm-success_1-3 | 1.58 ms | 686.82 us | 581.82 us | 4.49 ms | 10.37 ms | 1.03 ms | 1.14 ms | 1.22 ms | **545.32 us** | 3.30 ms | 3.45 ms | 392.94 ms |
| game-sm-success_1-4 | 509.55 us | 232.18 us | 204.05 us | 1.66 ms | 6.77 ms | 376.99 us | 373.77 us | 385.86 us | **181.52 us** | 1.29 ms | 1.30 ms | 132.00 ms |
| game-sm-success_2-1 | 1.32 ms | 511.39 us | 416.99 us | 3.96 ms | 7.91 ms | 754.86 us | 745.15 us | 798.26 us | **388.58 us** | 2.13 ms | 2.31 ms | 268.60 ms |
| game-sm-success_2-2 | 473.56 us | 213.09 us | 183.26 us | 1.61 ms | 5.86 ms | 351.84 us | 336.42 us | 337.92 us | **161.47 us** | 1.09 ms | 1.14 ms | 118.92 ms |
| game-sm-success_2-3 | 1.58 ms | 680.15 us | 579.54 us | 4.55 ms | 10.38 ms | 1.03 ms | 1.16 ms | 1.26 ms | **544.34 us** | 3.25 ms | 3.43 ms | 391.99 ms |
| game-sm-success_2-4 | 509.38 us | 230.56 us | 202.22 us | 1.67 ms | 6.79 ms | 377.29 us | 369.75 us | 386.58 us | **180.73 us** | 1.28 ms | 1.30 ms | 132.02 ms |
| game-sm-success_2-5 | 1.58 ms | 687.66 us | 606.72 us | 4.47 ms | 10.45 ms | 1.03 ms | 1.14 ms | 1.22 ms | **543.75 us** | 3.27 ms | 3.41 ms | 393.11 ms |
| game-sm-success_2-6 | 510.16 us | 235.68 us | 203.75 us | 1.88 ms | 6.80 ms | 377.30 us | 366.65 us | 401.19 us | **184.98 us** | 1.30 ms | 1.31 ms | 131.77 ms |
| guardrail-sorted-large | 716.08 us | 481.26 us | **348.52 us** | 2.12 ms | 11.54 ms | 562.29 us | 699.94 us | 763.49 us | 380.90 us | 3.67 ms | 2.71 ms | FAIL |
| guardrail-sorted-small | 255.28 us | 122.72 us | 95.06 us | 793.66 us | 1.22 ms | 158.25 us | 162.16 us | 171.83 us | **90.43 us** | 722.20 us | 621.90 us | FAIL |
| guardrail-unsorted-large | 872.88 us | 633.14 us | **433.16 us** | 2.41 ms | 12.87 ms | 724.23 us | 932.67 us | 1.02 ms | 505.69 us | 5.62 ms | 3.51 ms | FAIL |
| guardrail-unsorted-small | 252.85 us | 118.39 us | 93.33 us | 787.56 us | 1.18 ms | 155.15 us | 168.20 us | 166.81 us | **88.58 us** | 750.50 us | 619.90 us | FAIL |
| multisig-sm-01 | 1.41 ms | 551.89 us | 457.49 us | 4.28 ms | 7.56 ms | 804.49 us | 805.95 us | 860.31 us | **413.91 us** | 2.74 ms | 2.40 ms | FAIL |
| multisig-sm-02 | 1.41 ms | 531.56 us | 442.48 us | 4.25 ms | 7.67 ms | 794.72 us | 784.78 us | 822.19 us | **409.90 us** | 2.68 ms | 2.34 ms | FAIL |
| multisig-sm-03 | 1.40 ms | 548.15 us | 447.22 us | 4.25 ms | 7.60 ms | 791.52 us | 783.17 us | 822.03 us | **412.26 us** | 2.80 ms | 2.35 ms | FAIL |
| multisig-sm-04 | 1.41 ms | 549.72 us | 448.29 us | 4.33 ms | 7.74 ms | 801.83 us | 812.40 us | 841.89 us | **415.61 us** | 2.31 ms | 2.37 ms | FAIL |
| multisig-sm-05 | 1.60 ms | 656.98 us | 562.43 us | 4.61 ms | 8.90 ms | 984.50 us | 1.10 ms | 1.15 ms | **512.97 us** | 3.07 ms | 3.10 ms | FAIL |
| multisig-sm-06 | 1.41 ms | 543.09 us | 451.04 us | 4.25 ms | 7.62 ms | 823.94 us | 813.99 us | 858.89 us | **414.89 us** | 2.44 ms | 2.38 ms | FAIL |
| multisig-sm-07 | 1.40 ms | 543.12 us | 445.21 us | 4.21 ms | 7.54 ms | 793.97 us | 789.22 us | 829.20 us | **416.50 us** | 2.30 ms | 2.34 ms | FAIL |
| multisig-sm-08 | 1.41 ms | 541.02 us | 446.19 us | 4.25 ms | 7.57 ms | 794.02 us | 800.30 us | 827.09 us | **411.34 us** | 2.34 ms | 2.35 ms | FAIL |
| multisig-sm-09 | 1.42 ms | 547.56 us | 447.93 us | 4.27 ms | 7.71 ms | 802.84 us | 812.59 us | 841.84 us | **415.18 us** | 2.33 ms | 2.37 ms | FAIL |
| multisig-sm-10 | 1.59 ms | 656.37 us | 563.24 us | 4.70 ms | 8.79 ms | 983.77 us | 1.06 ms | 1.16 ms | **513.58 us** | 3.20 ms | 3.09 ms | FAIL |
| ping-pong-1 | 1.18 ms | 461.52 us | 370.67 us | 3.64 ms | 6.42 ms | 671.82 us | 672.03 us | 702.28 us | **341.11 us** | 1.92 ms | 1.97 ms | 232.86 ms |
| ping-pong-2 | 1.18 ms | 463.71 us | 373.29 us | 3.62 ms | 6.38 ms | 672.01 us | 676.57 us | 712.14 us | **341.70 us** | 2.01 ms | 1.97 ms | 232.14 ms |
| ping-pong_2-1 | 1.03 ms | 370.25 us | 283.05 us | 3.43 ms | 5.09 ms | 507.92 us | 470.75 us | 503.21 us | **251.89 us** | 1.45 ms | 1.40 ms | 170.59 ms |
| prism-1 | 436.26 us | 182.92 us | 160.44 us | 1.51 ms | 4.76 ms | 297.06 us | 292.29 us | 295.61 us | **140.79 us** | 963.90 us | 976.70 us | 102.96 ms |
| prism-2 | 1.32 ms | 534.52 us | 431.92 us | 3.98 ms | 8.30 ms | 786.44 us | 811.44 us | 838.72 us | **402.14 us** | 2.42 ms | 2.34 ms | 275.10 ms |
| prism-3 | 757.32 us | 381.96 us | 328.79 us | 2.40 ms | 7.68 ms | 575.70 us | 660.20 us | 693.58 us | **296.86 us** | 2.00 ms | 1.96 ms | 216.95 ms |
| pubkey-1 | 419.36 us | 175.43 us | 145.17 us | 1.50 ms | 4.24 ms | 269.69 us | 249.78 us | 254.84 us | **130.88 us** | 859.90 us | 846.70 us | 97.58 ms |
| stablecoin_1-1 | 2.64 ms | 1.14 ms | 984.87 us | 6.35 ms | 14.51 ms | 1.74 ms | 1.87 ms | 1.90 ms | **747.92 us** | 6.68 ms | 9.61 ms | FAIL |
| stablecoin_1-2 | 470.71 us | 208.14 us | 181.56 us | 1.57 ms | 5.89 ms | 347.78 us | 327.23 us | 333.68 us | **160.29 us** | 1.23 ms | 1.12 ms | 115.83 ms |
| stablecoin_1-3 | 2.90 ms | 1.21 ms | 1.10 ms | 6.58 ms | 16.07 ms | 1.94 ms | 2.03 ms | 2.14 ms | **831.42 us** | 7.23 ms | 10.40 ms | FAIL |
| stablecoin_1-4 | 482.69 us | 218.40 us | 189.61 us | 1.66 ms | 6.34 ms | 351.25 us | 339.98 us | 365.38 us | **167.13 us** | 1.20 ms | 1.18 ms | 122.43 ms |
| stablecoin_1-5 | 3.18 ms | 1.40 ms | 1.36 ms | 7.14 ms | 19.39 ms | 2.40 ms | 2.55 ms | 2.67 ms | **1.00 ms** | 9.11 ms | 12.28 ms | FAIL |
| stablecoin_1-6 | 543.43 us | 250.44 us | 218.84 us | 1.80 ms | 7.84 ms | 406.49 us | 409.55 us | 425.54 us | **195.18 us** | 1.46 ms | 1.41 ms | 143.33 ms |
| stablecoin_2-1 | 2.64 ms | 1.13 ms | 976.32 us | 6.32 ms | 14.62 ms | 1.74 ms | 1.81 ms | 1.89 ms | **745.60 us** | 6.74 ms | 9.58 ms | FAIL |
| stablecoin_2-2 | 471.50 us | 208.26 us | 181.66 us | 1.62 ms | 6.05 ms | 336.06 us | 325.09 us | 332.11 us | **160.00 us** | 1.20 ms | 1.12 ms | 115.55 ms |
| stablecoin_2-3 | 2.81 ms | 1.21 ms | 1.10 ms | 6.61 ms | 16.16 ms | 1.94 ms | 2.21 ms | 2.14 ms | **831.02 us** | 7.31 ms | 10.37 ms | FAIL |
| stablecoin_2-4 | 482.57 us | 218.06 us | 188.38 us | 1.61 ms | 6.40 ms | 351.49 us | 349.07 us | 365.99 us | **171.01 us** | 1.22 ms | 1.18 ms | 122.52 ms |
| token-account-1 | 568.74 us | 246.50 us | 210.43 us | 1.98 ms | 4.26 ms | 364.20 us | 370.85 us | 399.43 us | **185.99 us** | 1.10 ms | 1.10 ms | 129.21 ms |
| token-account-2 | 685.15 us | 340.64 us | 288.78 us | 2.22 ms | 6.69 ms | 512.64 us | 598.98 us | 617.71 us | **271.71 us** | 1.84 ms | 1.71 ms | 205.18 ms |
| uniswap-1 | 762.89 us | 401.66 us | 343.41 us | 2.48 ms | 6.04 ms | 605.10 us | 737.38 us | 798.39 us | **327.15 us** | 2.25 ms | 2.05 ms | 257.87 ms |
| uniswap-2 | 608.65 us | 275.51 us | 233.71 us | 2.04 ms | 5.40 ms | 407.49 us | 426.25 us | 453.26 us | **206.59 us** | 1.23 ms | 1.28 ms | 144.70 ms |
| uniswap-3 | 3.25 ms | 1.53 ms | 1.35 ms | 7.35 ms | 22.49 ms | 2.49 ms | 2.92 ms | 3.02 ms | **1.30 ms** | 9.50 ms | 9.09 ms | 892.69 ms |
| uniswap-4 | 637.85 us | 316.75 us | 282.84 us | 1.98 ms | 10.34 ms | 522.07 us | 536.12 us | 557.03 us | **247.41 us** | 1.79 ms | 1.82 ms | 189.02 ms |
| uniswap-5 | 2.52 ms | 1.14 ms | 956.97 us | 6.40 ms | 18.63 ms | 1.65 ms | 1.92 ms | 2.03 ms | **908.72 us** | 5.89 ms | 6.22 ms | 612.88 ms |
| uniswap-6 | 621.35 us | 315.08 us | 284.94 us | 1.93 ms | 9.94 ms | 492.04 us | 516.69 us | 534.69 us | **240.23 us** | 1.79 ms | 1.75 ms | 176.47 ms |
| vesting-1 | 885.94 us | 408.70 us | 335.67 us | 2.86 ms | 6.22 ms | 577.09 us | 643.22 us | 687.02 us | **317.69 us** | 1.78 ms | 1.84 ms | 222.59 ms |

## Eval tier: evaluate a decoded program

The program is decoded before timing; each iteration evaluates it. JIT VMs compile before timing too.

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 161.47 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 173.75 us | 1.08x |
| **Plutigo CEK (Go)** | Go | 233.70 us | 1.45x |
| **Amaru UPLC CEK (Rust)** | Rust | 246.79 us | 1.53x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 274.76 us | 1.70x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 325.05 us | 2.01x |
| **Plutuz CEK (Zig)** | Zig | 450.70 us | 2.79x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 498.08 us | 3.08x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 534.13 us | 3.31x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 688.21 us | 4.26x |
| **Aiken UPLC CEK (Rust)** | Rust | 789.73 us | 4.89x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.81 ms | 11.22x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.83 ms | 11.35x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 7.11 ms | 44.03x |
| **opshin CEK (Python / CPython)** | Python / CPython | 62.33 ms | 386.03x |

#### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| llvm-uplc post-JIT execution (C++ / LLVM) | 89 | 0 | 0 | 89 |
| Scalus UPLC→JVM JIT (Scala / JVM) | 89 | 0 | 0 | 89 |
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
| Amaru UPLC CEK (Rust) | 89 | 0 | 0 | 89 |
| Scalus CEK (Scala / JVM) | 89 | 0 | 0 | 89 |
| plutus-core CEK (Haskell / GHC) | 89 | 0 | 0 | 89 |
| Plutuz CEK (Zig) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET AOT) | 89 | 0 | 0 | 89 |
| Julc CEK (Java / GraalVM) | 78 | 11 | 0 | 89 |
| Aiken UPLC CEK (Rust) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc post-JIT execution (C++ / LLVM) | Amaru UPLC CEK (Rust) | Aiken UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 155.57 us | **40.47 us** | 117.78 us | 232.46 us | 67.48 us | 118.36 us | 364.31 us | 3.93 ms | 213.15 us | 218.26 us | 229.84 us | 103.09 us | 758.30 us | 838.00 us | 92.52 ms |
| auction_1-2 | 519.28 us | 891.25 us | 441.44 us | 774.94 us | **265.87 us** | 436.91 us | 1.36 ms | 6.96 ms | 733.42 us | 890.97 us | 976.45 us | 412.62 us | 2.57 ms | 2.63 ms | 338.88 ms |
| auction_1-3 | 512.77 us | 596.85 us | 437.77 us | 801.80 us | **273.59 us** | 433.66 us | 1.38 ms | 7.44 ms | 709.41 us | 874.90 us | 955.85 us | 400.41 us | 2.61 ms | 2.60 ms | 341.65 ms |
| auction_1-4 | 197.92 us | **48.83 us** | 151.60 us | 286.38 us | 86.76 us | 148.35 us | 448.61 us | 5.74 ms | 273.80 us | 278.41 us | 289.21 us | 127.33 us | 1.02 ms | 1.14 ms | 114.40 ms |
| auction_2-1 | 154.94 us | **38.29 us** | 117.02 us | 235.45 us | 70.89 us | 122.01 us | 363.22 us | 4.08 ms | 212.78 us | 218.72 us | 230.05 us | 101.12 us | 776.80 us | 835.30 us | 91.34 ms |
| auction_2-2 | 517.59 us | 863.93 us | 443.09 us | 787.08 us | **264.96 us** | 435.05 us | 1.38 ms | 7.01 ms | 736.90 us | 863.79 us | 959.74 us | 409.80 us | 2.62 ms | 2.59 ms | 345.68 ms |
| auction_2-3 | 665.11 us | 906.68 us | 591.67 us | 998.89 us | **345.30 us** | 561.67 us | 1.78 ms | 9.02 ms | 949.25 us | 1.18 ms | 1.28 ms | 520.06 us | 3.45 ms | 3.38 ms | 437.26 ms |
| auction_2-4 | 513.51 us | 566.00 us | 436.33 us | 781.29 us | **256.35 us** | 434.82 us | 1.39 ms | 7.69 ms | 721.50 us | 862.24 us | 1.02 ms | 399.56 us | 2.65 ms | 2.62 ms | 340.28 ms |
| auction_2-5 | 195.53 us | **47.95 us** | 150.01 us | 286.80 us | 82.41 us | 148.17 us | 452.18 us | 5.72 ms | 273.77 us | 277.45 us | 284.18 us | 126.93 us | 1.02 ms | 1.09 ms | 111.65 ms |
| coop-1 | 204.41 us | **40.91 us** | 191.46 us | FAIL | 87.17 us | 123.39 us | 406.49 us | 6.21 ms | 289.03 us | 253.09 us | 286.93 us | 134.71 us | 1.42 ms | 1.34 ms | FAIL |
| coop-2 | 654.07 us | **155.77 us** | 610.17 us | FAIL | 285.96 us | 386.42 us | 1.27 ms | 22.64 ms | 794.06 us | 848.55 us | 900.49 us | 446.38 us | 4.09 ms | 4.18 ms | FAIL |
| coop-3 | 1.81 ms | **644.25 us** | 1.94 ms | FAIL | 946.40 us | 1.22 ms | 4.57 ms | 29.59 ms | 2.36 ms | 2.91 ms | 3.13 ms | 1.46 ms | 13.39 ms | 11.68 ms | FAIL |
| coop-4 | 840.36 us | **244.23 us** | 765.20 us | FAIL | 385.31 us | 495.70 us | 1.74 ms | 20.92 ms | 960.35 us | 1.09 ms | 1.14 ms | 558.98 us | 6.89 ms | 4.67 ms | FAIL |
| coop-5 | 360.05 us | **84.56 us** | 327.29 us | FAIL | 166.67 us | 219.08 us | 769.56 us | 10.86 ms | 431.53 us | 471.18 us | 483.33 us | 233.73 us | 2.24 ms | 2.07 ms | FAIL |
| coop-6 | 600.06 us | **141.47 us** | 568.46 us | FAIL | 259.45 us | 350.27 us | 1.16 ms | 21.36 ms | 820.55 us | 768.28 us | 804.49 us | 406.84 us | 3.97 ms | 3.68 ms | FAIL |
| coop-7 | 297.38 us | **53.16 us** | 264.98 us | FAIL | 125.20 us | 170.62 us | 572.59 us | 10.39 ms | 405.73 us | 364.14 us | 374.76 us | 187.71 us | 1.86 ms | 1.87 ms | FAIL |
| crowdfunding-success-1 | 182.71 us | **39.63 us** | 136.80 us | 261.68 us | 83.32 us | 130.14 us | 428.57 us | 5.76 ms | 238.27 us | 248.05 us | 269.03 us | 119.30 us | 1.02 ms | 959.90 us | 107.49 ms |
| crowdfunding-success-2 | 181.13 us | **43.64 us** | 136.32 us | 262.96 us | 83.69 us | 129.05 us | 427.26 us | 5.71 ms | 237.45 us | 245.74 us | 254.72 us | 119.52 us | 998.80 us | 962.50 us | 106.16 ms |
| crowdfunding-success-3 | 186.76 us | **43.70 us** | 138.07 us | 262.23 us | 84.26 us | 128.20 us | 428.64 us | 5.81 ms | 238.33 us | 246.53 us | 255.77 us | 119.02 us | 1.04 ms | 962.70 us | 106.12 ms |
| currency-1 | 202.53 us | **60.81 us** | 176.91 us | 314.24 us | 104.72 us | 160.71 us | 540.50 us | 4.36 ms | 294.53 us | 341.61 us | 380.12 us | 155.42 us | 1.23 ms | 1.08 ms | 136.27 ms |
| escrow-redeem_1-1 | 294.80 us | **80.72 us** | 242.98 us | 425.82 us | 146.03 us | 214.16 us | 741.31 us | 6.98 ms | 386.29 us | 447.62 us | 477.55 us | 217.70 us | 1.74 ms | 1.49 ms | 180.65 ms |
| escrow-redeem_1-2 | 293.95 us | **83.82 us** | 247.07 us | 419.63 us | 146.22 us | 214.75 us | 736.48 us | 7.03 ms | 386.28 us | 445.61 us | 498.95 us | 214.94 us | 1.81 ms | 1.49 ms | 182.82 ms |
| escrow-redeem_2-1 | 342.25 us | **100.71 us** | 280.15 us | 476.02 us | 172.22 us | 254.10 us | 855.29 us | 7.41 ms | 448.55 us | 544.39 us | 561.35 us | 247.88 us | 1.82 ms | 1.73 ms | 211.04 ms |
| escrow-redeem_2-2 | 340.34 us | **103.04 us** | 279.47 us | 490.59 us | 168.70 us | 248.53 us | 861.83 us | 7.32 ms | 447.48 us | 523.63 us | 566.15 us | 249.40 us | 1.74 ms | 1.73 ms | 210.53 ms |
| escrow-redeem_2-3 | 338.63 us | **96.67 us** | 281.12 us | 476.60 us | 167.80 us | 249.65 us | 865.97 us | 7.40 ms | 448.46 us | 534.17 us | 562.35 us | 248.63 us | 1.80 ms | 1.73 ms | 209.60 ms |
| escrow-refund-1 | 134.94 us | **31.79 us** | 100.18 us | 220.46 us | 66.37 us | 97.29 us | 331.47 us | 3.74 ms | 177.71 us | 184.57 us | 194.38 us | 89.58 us | 646.30 us | 707.80 us | 93.46 ms |
| future-increase-margin-1 | 204.94 us | **64.88 us** | 175.81 us | 316.05 us | 105.64 us | 159.34 us | 541.83 us | 4.09 ms | 284.13 us | 344.49 us | 369.83 us | 156.31 us | 1.04 ms | 1.09 ms | 137.54 ms |
| future-increase-margin-2 | 440.57 us | **145.59 us** | 364.79 us | 612.56 us | 219.21 us | 325.14 us | 1.14 ms | 9.53 ms | 589.08 us | 698.11 us | 774.62 us | 328.90 us | 2.19 ms | 2.24 ms | 277.49 ms |
| future-increase-margin-3 | 440.58 us | **146.33 us** | 368.39 us | 616.64 us | 218.40 us | 324.88 us | 1.15 ms | 9.45 ms | 587.55 us | 719.86 us | 767.61 us | 328.38 us | 2.21 ms | 2.25 ms | 279.28 ms |
| future-increase-margin-4 | 406.41 us | 515.57 us | 336.18 us | 651.30 us | **210.48 us** | 340.70 us | 1.07 ms | 6.95 ms | 595.03 us | 673.22 us | 725.52 us | 317.44 us | 1.98 ms | 2.07 ms | FAIL |
| future-increase-margin-5 | 669.06 us | 1.43 ms | 586.87 us | 1.09 ms | **378.02 us** | 579.91 us | 1.70 ms | 10.68 ms | 1.13 ms | 1.16 ms | 1.28 ms | 495.77 us | 4.14 ms | 5.43 ms | FAIL |
| future-pay-out-1 | 203.33 us | **62.98 us** | 174.31 us | 316.07 us | 105.11 us | 158.59 us | 542.67 us | 4.22 ms | 284.44 us | 342.74 us | 371.47 us | 155.83 us | 1.06 ms | 1.13 ms | 135.37 ms |
| future-pay-out-2 | 441.67 us | **150.97 us** | 370.79 us | 619.04 us | 218.82 us | 326.50 us | 1.14 ms | 9.56 ms | 588.54 us | 706.77 us | 767.06 us | 327.03 us | 2.25 ms | 2.52 ms | 278.29 ms |
| future-pay-out-3 | 441.35 us | **153.84 us** | 370.85 us | 619.40 us | 219.29 us | 330.88 us | 1.13 ms | 9.56 ms | 587.46 us | 704.05 us | 768.92 us | 328.65 us | 2.22 ms | 2.42 ms | 277.58 ms |
| future-pay-out-4 | 673.68 us | 1.49 ms | 583.11 us | 1.09 ms | **379.10 us** | 580.37 us | 1.70 ms | 10.31 ms | 1.12 ms | 1.19 ms | 1.28 ms | 485.53 us | 4.19 ms | 5.39 ms | FAIL |
| future-settle-early-1 | 204.50 us | **60.89 us** | 176.10 us | 319.10 us | 105.78 us | 160.38 us | 549.60 us | 4.29 ms | 286.40 us | 341.35 us | 386.72 us | 155.43 us | 1.06 ms | 1.08 ms | 138.31 ms |
| future-settle-early-2 | 440.68 us | **151.99 us** | 367.76 us | 612.07 us | 220.52 us | 327.18 us | 1.14 ms | 9.58 ms | 589.10 us | 702.92 us | 775.61 us | 327.18 us | 2.28 ms | 2.25 ms | 280.53 ms |
| future-settle-early-3 | 441.06 us | **141.70 us** | 363.50 us | 612.39 us | 224.92 us | 328.32 us | 1.14 ms | 9.68 ms | 590.77 us | 752.48 us | 767.52 us | 326.90 us | 2.13 ms | 2.25 ms | 278.78 ms |
| future-settle-early-4 | 515.67 us | 1.29 ms | 452.78 us | 849.40 us | **299.47 us** | 428.33 us | 1.26 ms | 8.60 ms | 809.34 us | 874.66 us | 934.45 us | 359.60 us | 3.04 ms | 4.55 ms | FAIL |
| game-sm-success_1-1 | 332.51 us | 341.97 us | 277.34 us | 508.32 us | **169.35 us** | 253.40 us | 818.79 us | 6.73 ms | 464.45 us | 511.76 us | 537.04 us | 246.85 us | 1.48 ms | 1.66 ms | 208.91 ms |
| game-sm-success_1-2 | 169.38 us | **38.19 us** | 130.24 us | 247.95 us | 76.43 us | 124.59 us | 394.57 us | 5.31 ms | 236.60 us | 237.45 us | 250.82 us | 112.58 us | 813.60 us | 939.10 us | 99.19 ms |
| game-sm-success_1-3 | 524.68 us | 571.00 us | 443.86 us | 788.33 us | **272.55 us** | 413.98 us | 1.36 ms | 9.40 ms | 729.90 us | 858.59 us | 938.17 us | 402.76 us | 2.49 ms | 2.64 ms | 334.61 ms |
| game-sm-success_1-4 | 196.90 us | **44.15 us** | 150.50 us | 280.04 us | 88.13 us | 141.79 us | 451.52 us | 6.30 ms | 274.18 us | 281.30 us | 287.10 us | 128.50 us | 983.70 us | 1.09 ms | 113.67 ms |
| game-sm-success_2-1 | 332.43 us | 321.91 us | 274.50 us | 503.06 us | **169.56 us** | 258.01 us | 820.30 us | 6.43 ms | 456.13 us | 549.31 us | 556.88 us | 247.88 us | 1.56 ms | 1.64 ms | 208.57 ms |
| game-sm-success_2-2 | 171.12 us | **36.93 us** | 129.93 us | 247.13 us | 76.33 us | 124.00 us | 391.68 us | 5.20 ms | 236.47 us | 242.49 us | 250.67 us | 110.51 us | 860.50 us | 943.80 us | 97.78 ms |
| game-sm-success_2-3 | 517.75 us | 599.55 us | 441.05 us | 783.32 us | **270.95 us** | 425.17 us | 1.35 ms | 8.99 ms | 734.18 us | 848.59 us | 935.42 us | 401.20 us | 2.50 ms | 2.62 ms | 335.02 ms |
| game-sm-success_2-4 | 194.78 us | **42.25 us** | 149.38 us | 283.23 us | 87.92 us | 142.88 us | 453.45 us | 6.63 ms | 274.31 us | 268.49 us | 286.68 us | 127.42 us | 988.70 us | 1.10 ms | 113.80 ms |
| game-sm-success_2-5 | 520.50 us | 599.52 us | 443.12 us | 776.93 us | **271.95 us** | 415.31 us | 1.35 ms | 9.70 ms | 736.08 us | 842.81 us | 974.35 us | 401.45 us | 2.58 ms | 2.62 ms | 335.97 ms |
| game-sm-success_2-6 | 195.96 us | **44.89 us** | 150.35 us | 278.82 us | 87.72 us | 143.45 us | 452.90 us | 6.10 ms | 273.11 us | 278.79 us | 288.07 us | 127.74 us | 1.01 ms | 1.09 ms | 111.80 ms |
| guardrail-sorted-large | 374.71 us | **225.29 us** | 379.71 us | FAIL | 309.62 us | 233.74 us | 847.74 us | 8.85 ms | 445.32 us | 556.05 us | 610.46 us | 269.38 us | 2.52 ms | 2.51 ms | FAIL |
| guardrail-sorted-small | 64.48 us | 84.63 us | 77.99 us | FAIL | **26.30 us** | 44.95 us | 163.25 us | 721.53 us | 83.28 us | 85.26 us | 94.04 us | 47.31 us | 585.60 us | 427.80 us | FAIL |
| guardrail-unsorted-large | 519.00 us | **297.57 us** | 535.55 us | FAIL | 366.23 us | 317.89 us | 1.15 ms | 10.35 ms | 612.42 us | 800.65 us | 868.50 us | 388.11 us | 5.06 ms | 3.18 ms | FAIL |
| guardrail-unsorted-small | 61.15 us | 84.89 us | 74.66 us | FAIL | **25.24 us** | 43.70 us | 161.39 us | 672.96 us | 76.88 us | 80.26 us | 92.69 us | 45.22 us | 499.10 us | 419.40 us | FAIL |
| multisig-sm-01 | 343.11 us | 361.31 us | 285.26 us | 541.71 us | **176.00 us** | 271.44 us | 873.52 us | 6.43 ms | 475.31 us | 546.11 us | 596.10 us | 262.35 us | 2.04 ms | 1.68 ms | FAIL |
| multisig-sm-02 | 330.66 us | 471.76 us | 268.74 us | 522.20 us | **175.43 us** | 265.90 us | 845.98 us | 6.51 ms | 461.85 us | 493.22 us | 563.26 us | 256.48 us | 2.04 ms | 1.64 ms | FAIL |
| multisig-sm-03 | 335.84 us | 508.36 us | 278.25 us | 527.51 us | **177.07 us** | 267.58 us | 854.21 us | 6.51 ms | 465.44 us | 521.32 us | 565.78 us | 258.59 us | 2.06 ms | 1.67 ms | FAIL |
| multisig-sm-04 | 337.39 us | 475.98 us | 282.65 us | 533.04 us | **176.78 us** | 268.21 us | 867.87 us | 6.33 ms | 470.73 us | 534.19 us | 572.92 us | 261.51 us | 2.07 ms | 1.66 ms | FAIL |
| multisig-sm-05 | 461.58 us | 827.73 us | 390.86 us | 731.40 us | **246.11 us** | 382.59 us | 1.24 ms | 7.47 ms | 659.34 us | 770.80 us | 845.33 us | 359.68 us | 2.96 ms | 2.30 ms | FAIL |
| multisig-sm-06 | 335.18 us | 380.92 us | 283.41 us | 548.47 us | **177.16 us** | 275.70 us | 873.07 us | 6.43 ms | 476.03 us | 536.10 us | 577.73 us | 261.99 us | 1.87 ms | 1.67 ms | FAIL |
| multisig-sm-07 | 331.93 us | 524.35 us | 270.78 us | 529.38 us | **178.89 us** | 266.58 us | 846.42 us | 6.39 ms | 468.92 us | 504.33 us | 560.73 us | 257.34 us | 1.82 ms | 1.64 ms | FAIL |
| multisig-sm-08 | 333.99 us | 521.39 us | 277.13 us | 536.33 us | **176.96 us** | 267.62 us | 857.44 us | 6.20 ms | 466.54 us | 517.90 us | 585.73 us | 264.25 us | 1.85 ms | 1.65 ms | FAIL |
| multisig-sm-09 | 336.54 us | 477.70 us | 281.82 us | 545.25 us | **177.46 us** | 268.95 us | 871.39 us | 6.41 ms | 470.97 us | 530.86 us | 566.87 us | 261.26 us | 1.89 ms | 1.67 ms | FAIL |
| multisig-sm-10 | 459.53 us | 873.86 us | 391.04 us | 726.69 us | **246.00 us** | 385.46 us | 1.23 ms | 7.71 ms | 655.36 us | 752.74 us | 841.39 us | 359.97 us | 2.77 ms | 2.31 ms | FAIL |
| ping-pong-1 | 273.70 us | 202.50 us | 237.10 us | 439.60 us | **147.73 us** | 222.79 us | 718.71 us | 5.52 ms | 391.90 us | 419.69 us | 464.54 us | 212.53 us | 1.59 ms | 1.39 ms | 181.97 ms |
| ping-pong-2 | 276.63 us | 186.13 us | 237.66 us | 449.13 us | **147.07 us** | 218.37 us | 718.42 us | 5.16 ms | 391.49 us | 444.93 us | 462.62 us | 212.24 us | 1.57 ms | 1.39 ms | 181.06 ms |
| ping-pong_2-1 | 173.85 us | **83.11 us** | 142.38 us | 302.20 us | 92.33 us | 131.65 us | 445.28 us | 3.99 ms | 232.91 us | 255.30 us | 268.07 us | 124.85 us | 973.70 us | 884.30 us | 121.55 ms |
| prism-1 | 141.45 us | **30.36 us** | 117.50 us | 208.82 us | 64.48 us | 104.14 us | 328.76 us | 4.42 ms | 198.75 us | 202.64 us | 208.88 us | 92.66 us | 822.40 us | 787.20 us | 83.63 ms |
| prism-2 | 353.97 us | 269.95 us | 294.22 us | 538.32 us | **179.63 us** | 271.09 us | 859.25 us | 7.57 ms | 489.71 us | 547.68 us | 580.50 us | 260.20 us | 1.74 ms | 1.77 ms | 226.96 ms |
| prism-3 | 304.65 us | **99.35 us** | 257.41 us | 451.09 us | 153.92 us | 242.88 us | 761.26 us | 7.36 ms | 442.29 us | 489.37 us | 529.31 us | 223.19 us | 1.64 ms | 1.63 ms | 188.40 ms |
| pubkey-1 | 123.89 us | **25.60 us** | 99.92 us | 181.79 us | 58.08 us | 90.92 us | 285.20 us | 3.88 ms | 167.57 us | 166.23 us | 174.19 us | 79.22 us | 626.40 us | 665.70 us | 71.64 ms |
| stablecoin_1-1 | 808.15 us | 2.44 ms | 738.86 us | 1.37 ms | **434.50 us** | 720.74 us | 1.70 ms | 12.37 ms | 1.26 ms | 1.35 ms | 1.40 ms | 545.98 us | 5.28 ms | 8.22 ms | FAIL |
| stablecoin_1-2 | 162.62 us | **39.32 us** | 127.47 us | 242.08 us | 77.02 us | 121.81 us | 385.98 us | 5.62 ms | 230.47 us | 229.49 us | 242.59 us | 108.34 us | 890.90 us | 914.90 us | 96.51 ms |
| stablecoin_1-3 | 913.30 us | 2.51 ms | 821.33 us | 1.57 ms | **474.50 us** | 861.01 us | 1.94 ms | 13.98 ms | 1.47 ms | 1.53 ms | 1.65 ms | 620.68 us | 6.04 ms | 8.99 ms | FAIL |
| stablecoin_1-4 | 175.91 us | **39.02 us** | 137.08 us | 256.24 us | 81.58 us | 131.46 us | 404.12 us | 6.13 ms | 244.53 us | 244.28 us | 258.00 us | 114.62 us | 959.80 us | 971.30 us | 102.97 ms |
| stablecoin_1-5 | 1.14 ms | 2.64 ms | 999.96 us | 2.02 ms | **551.17 us** | 1.10 ms | 2.43 ms | 16.90 ms | 1.92 ms | 2.09 ms | 2.13 ms | 790.45 us | 7.26 ms | 10.43 ms | FAIL |
| stablecoin_1-6 | 214.96 us | **46.79 us** | 165.20 us | 303.93 us | 101.97 us | 155.80 us | 491.14 us | 7.54 ms | 299.87 us | 301.63 us | 313.23 us | 139.94 us | 1.03 ms | 1.21 ms | 122.80 ms |
| stablecoin_2-1 | 810.10 us | 2.44 ms | 734.64 us | 1.36 ms | **431.43 us** | 718.34 us | 1.70 ms | 13.04 ms | 1.26 ms | 1.36 ms | 1.41 ms | 535.04 us | 4.88 ms | 8.18 ms | FAIL |
| stablecoin_2-2 | 162.31 us | **37.88 us** | 125.34 us | 239.69 us | 77.14 us | 123.47 us | 385.57 us | 5.80 ms | 230.87 us | 231.15 us | 240.72 us | 108.28 us | 805.50 us | 915.90 us | 96.59 ms |
| stablecoin_2-3 | 914.42 us | 2.65 ms | 812.11 us | 1.57 ms | **472.49 us** | 846.91 us | 1.94 ms | 13.52 ms | 1.47 ms | 1.56 ms | 1.63 ms | 620.07 us | 5.73 ms | 9.01 ms | FAIL |
| stablecoin_2-4 | 176.63 us | **38.36 us** | 135.75 us | 255.07 us | 80.73 us | 132.20 us | 408.14 us | 5.97 ms | 244.97 us | 251.60 us | 258.32 us | 113.88 us | 904.40 us | 975.30 us | 103.32 ms |
| token-account-1 | 159.31 us | **56.06 us** | 130.23 us | 255.02 us | 82.28 us | 129.27 us | 405.04 us | 3.63 ms | 221.74 us | 255.88 us | 270.21 us | 118.68 us | 792.60 us | 840.30 us | 104.16 ms |
| token-account-2 | 274.03 us | **71.23 us** | 228.72 us | 389.25 us | 139.51 us | 204.29 us | 705.93 us | 6.26 ms | 384.50 us | 445.84 us | 486.23 us | 204.66 us | 1.42 ms | 1.44 ms | 176.73 ms |
| uniswap-1 | 316.36 us | **104.09 us** | 285.00 us | 474.09 us | 167.02 us | 247.56 us | 917.81 us | 5.90 ms | 458.99 us | 578.39 us | 647.19 us | 255.77 us | 1.71 ms | 1.74 ms | 227.15 ms |
| uniswap-2 | 186.94 us | **54.85 us** | 158.12 us | 293.88 us | 95.43 us | 147.34 us | 461.20 us | 4.59 ms | 265.99 us | 296.68 us | 316.30 us | 135.24 us | 970.30 us | 1.01 ms | 120.37 ms |
| uniswap-3 | 1.40 ms | 906.15 us | 1.20 ms | 1.97 ms | **608.78 us** | 1.08 ms | 3.32 ms | 19.82 ms | 2.08 ms | 2.31 ms | 2.56 ms | 1.10 ms | 7.47 ms | 7.47 ms | 810.69 ms |
| uniswap-4 | 283.42 us | **60.59 us** | 218.98 us | 391.42 us | 127.29 us | 206.71 us | 630.28 us | 9.89 ms | 393.23 us | 404.76 us | 438.45 us | 186.02 us | 1.46 ms | 1.58 ms | 158.92 ms |
| uniswap-5 | 948.25 us | 686.80 us | 785.72 us | 1.33 ms | **430.51 us** | 720.50 us | 2.13 ms | 17.71 ms | 1.26 ms | 1.46 ms | 1.59 ms | 714.23 us | 4.93 ms | 5.02 ms | 536.83 ms |
| uniswap-6 | 266.91 us | **58.76 us** | 219.21 us | 377.58 us | 122.90 us | 198.63 us | 595.88 us | 9.88 ms | 377.19 us | 405.27 us | 400.05 us | 177.87 us | 1.44 ms | 1.51 ms | 152.34 ms |
| vesting-1 | 296.36 us | 161.34 us | 248.14 us | 424.76 us | **155.96 us** | 218.58 us | 760.60 us | 5.34 ms | 382.41 us | 471.59 us | 499.69 us | 223.93 us | 1.48 ms | 1.44 ms | 187.04 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*