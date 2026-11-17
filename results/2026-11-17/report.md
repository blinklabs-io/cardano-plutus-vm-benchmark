# Cardano Plutus VM Benchmark Results

**Date:** 2026-11-17

**Corpus:** Plutus use cases (`plutus_use_cases`): all 89 programs. The per-script tables list every program measured.

## Environment
```
date: 2026-11-17T08:09:15+00:00
kernel: 6.8.0-147-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
corpus: plutus_use_cases (89 of 89 programs, sample all, seed 1; list in corpus.txt)
```

## VM Versions

| VM | Source revision | Toolchain |
|---|---|---|
| plutus-core CEK (Haskell / GHC) | master@12ddaca ([12ddaca](https://github.com/IntersectMBO/plutus/commit/12ddacadae1ac78709c8fc7aa2eec252df60a41d)) | GHC 9.6.4 |
| Scalus UPLC→JVM JIT (Scala / JVM) | master@a3e3487 ([a3e3487](https://github.com/scalus3/scalus/commit/a3e348790452d614cf242f980380fc1246fc01f8)) | JDK 21 / Scala 3 |
| Scalus CEK (Scala / JVM) | master@a3e3487 ([a3e3487](https://github.com/scalus3/scalus/commit/a3e348790452d614cf242f980380fc1246fc01f8)) | JDK 21 / Scala 3 |
| Julc CEK (Java / GraalVM) | main@8724e2c ([8724e2c](https://github.com/bloxbean/julc/commit/8724e2ce2008db78a3f9679fc0160fc10bead83a)) | GraalVM 25.0.2-graal |
| llvm-uplc post-JIT execution (C++ / LLVM) | master@6bcef67 ([6bcef67](https://github.com/SeungheonOh/llvm-uplc/commit/6bcef67ce1995d232327f13d9080fe2f0261a55c)) | LLVM 22.1.0 |
| Amaru UPLC CEK (Rust) | [0.6.0](https://crates.io/crates/amaru-uplc/0.6.0) | rustc nightly-2026-09-04 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | [3.0.5](https://www.npmjs.com/package/@harmoniclabs/plutus-machine/v/3.0.5) | Node.js 22 |
| Plutuz CEK (Zig) | main@33b812d ([33b812d](https://github.com/utxo-company/plutuz/commit/33b812dbcf88f6851286e54cb93a4a443353f94c)) | Zig 0.15.2 |
| Chrysalis CEK (C# / .NET) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Chrysalis CEK (C# / .NET AOT) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Plutigo CEK (Go) | main@ba8c219 ([ba8c219](https://github.com/blinklabs-io/plutigo/commit/ba8c21970a6e23356df46390371e456fec2ff9db)) | Go 1.27.3 |
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
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus CEK (Scala / JVM) | Amaru UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 511.41 us | 221.27 us | 205.90 us | 7.65 ms | 333.51 us | 323.37 us | 338.24 us | **164.50 us** | 1.02 ms | 1.29 ms | 120.73 ms |
| auction_1-2 | 1.74 ms | 740.53 us | 609.21 us | 12.80 ms | 1.17 ms | 1.26 ms | 1.42 ms | **579.99 us** | 3.43 ms | 3.39 ms | 401.36 ms |
| auction_1-3 | 1.64 ms | 706.73 us | 594.42 us | 13.27 ms | 1.08 ms | 1.32 ms | 1.25 ms | **549.71 us** | 3.10 ms | 3.58 ms | 394.75 ms |
| auction_1-4 | 618.16 us | 261.18 us | 220.34 us | 9.93 ms | 403.73 us | 415.76 us | 423.06 us | **209.07 us** | 1.30 ms | 1.42 ms | 137.27 ms |
| auction_2-1 | 529.43 us | 215.06 us | 191.68 us | 7.18 ms | 333.38 us | 336.08 us | 380.43 us | **171.08 us** | 1.08 ms | 1.10 ms | 113.25 ms |
| auction_2-2 | 1.62 ms | 724.64 us | 598.35 us | 13.49 ms | 1.06 ms | 1.20 ms | 1.32 ms | **566.39 us** | 3.17 ms | 3.71 ms | 425.84 ms |
| auction_2-3 | 1.92 ms | 882.98 us | 741.03 us | 17.55 ms | 1.33 ms | 1.64 ms | 1.65 ms | **685.43 us** | 3.96 ms | 4.29 ms | 492.92 ms |
| auction_2-4 | 1.63 ms | 726.73 us | 673.17 us | 14.26 ms | 1.06 ms | 1.31 ms | 1.26 ms | **554.96 us** | 3.34 ms | 3.56 ms | 426.81 ms |
| auction_2-5 | 576.20 us | 261.26 us | 216.71 us | 9.57 ms | 431.06 us | 408.03 us | 414.94 us | **191.29 us** | 1.21 ms | 1.53 ms | 138.60 ms |
| coop-1 | 439.09 us | 245.88 us | **173.10 us** | 10.40 ms | 376.62 us | 337.39 us | 368.67 us | 193.60 us | 1.79 ms | 1.75 ms | FAIL |
| coop-2 | 1.47 ms | 804.83 us | **506.18 us** | 31.98 ms | 1.11 ms | 1.20 ms | 1.18 ms | 654.85 us | 5.50 ms | 5.29 ms | FAIL |
| coop-3 | 2.75 ms | 2.18 ms | **1.31 ms** | 36.34 ms | 2.64 ms | 4.18 ms | 4.21 ms | 1.65 ms | 16.53 ms | 11.87 ms | FAIL |
| coop-4 | 1.76 ms | 993.20 us | **646.49 us** | 28.74 ms | 1.20 ms | 1.54 ms | 1.52 ms | 719.83 us | 5.76 ms | 5.32 ms | FAIL |
| coop-5 | 969.97 us | 465.90 us | **341.39 us** | 17.78 ms | 627.55 us | 677.44 us | 711.31 us | 348.31 us | 3.93 ms | 2.51 ms | FAIL |
| coop-6 | 1.10 ms | 708.21 us | **465.76 us** | 33.18 ms | 923.97 us | 959.92 us | 1.09 ms | 499.57 us | 4.77 ms | 3.87 ms | FAIL |
| coop-7 | 585.84 us | 334.58 us | **233.62 us** | 16.41 ms | 501.19 us | 509.53 us | 528.16 us | 258.64 us | 2.11 ms | 1.95 ms | FAIL |
| crowdfunding-success-1 | 668.54 us | 264.95 us | **209.35 us** | 9.18 ms | 394.87 us | 423.42 us | 411.25 us | 210.80 us | 1.32 ms | 1.23 ms | 137.57 ms |
| crowdfunding-success-2 | 662.08 us | 267.26 us | 212.59 us | 9.03 ms | 395.63 us | 375.45 us | 420.78 us | **208.34 us** | 1.30 ms | 1.23 ms | 134.73 ms |
| crowdfunding-success-3 | 630.38 us | 267.49 us | 221.01 us | 9.01 ms | 431.97 us | 379.50 us | 395.50 us | **192.64 us** | 1.29 ms | 1.30 ms | 155.99 ms |
| currency-1 | 644.33 us | 301.13 us | 243.10 us | 6.79 ms | 466.08 us | 471.65 us | 509.58 us | **231.47 us** | 1.53 ms | 1.41 ms | 173.59 ms |
| escrow-redeem_1-1 | 902.29 us | 405.53 us | 322.68 us | 10.63 ms | 578.36 us | 690.36 us | 694.67 us | **313.26 us** | 2.10 ms | 1.90 ms | 215.28 ms |
| escrow-redeem_1-2 | 939.80 us | 432.89 us | 372.40 us | 11.49 ms | 593.07 us | 645.67 us | 695.89 us | **313.82 us** | 2.10 ms | 1.88 ms | 222.73 ms |
| escrow-redeem_2-1 | 972.28 us | 449.00 us | **359.63 us** | 11.86 ms | 680.23 us | 764.19 us | 825.39 us | 367.33 us | 2.41 ms | 2.33 ms | 244.47 ms |
| escrow-redeem_2-2 | 1.02 ms | 468.58 us | **357.16 us** | 11.55 ms | 673.22 us | 822.99 us | 799.11 us | 390.88 us | 2.50 ms | 2.23 ms | 241.15 ms |
| escrow-redeem_2-3 | 1.00 ms | 451.34 us | 378.32 us | 11.63 ms | 677.86 us | 736.89 us | 804.50 us | **356.13 us** | 2.49 ms | 2.13 ms | 251.31 ms |
| escrow-refund-1 | 770.15 us | 277.25 us | 225.62 us | 6.56 ms | 390.30 us | 339.44 us | 393.34 us | **180.40 us** | 1.09 ms | 1.06 ms | 131.57 ms |
| future-increase-margin-1 | 640.10 us | 295.79 us | 239.99 us | 6.57 ms | 476.05 us | 507.92 us | 506.25 us | **231.42 us** | 1.39 ms | 1.35 ms | 175.98 ms |
| future-increase-margin-2 | 1.17 ms | 559.14 us | 439.47 us | 14.75 ms | 811.65 us | 994.89 us | 1.03 ms | **428.33 us** | 2.62 ms | 2.70 ms | 324.88 ms |
| future-increase-margin-3 | 1.18 ms | 552.13 us | 455.83 us | 16.46 ms | 800.46 us | 1.01 ms | 1.12 ms | **434.86 us** | 2.66 ms | 2.71 ms | 330.80 ms |
| future-increase-margin-4 | 1.76 ms | 668.23 us | 595.04 us | 13.68 ms | 975.34 us | 1.11 ms | 1.09 ms | **544.44 us** | 2.61 ms | 2.73 ms | FAIL |
| future-increase-margin-5 | 2.12 ms | 940.82 us | 797.12 us | 150.23 ms | 1.51 ms | 1.58 ms | 1.68 ms | **696.09 us** | 5.07 ms | 6.55 ms | FAIL |
| future-pay-out-1 | 645.53 us | 293.96 us | 239.06 us | 7.00 ms | 428.52 us | 489.17 us | 571.12 us | **233.92 us** | 1.42 ms | 1.37 ms | 173.15 ms |
| future-pay-out-2 | 1.13 ms | 579.97 us | 464.33 us | 14.00 ms | 813.60 us | 957.47 us | 1.00 ms | **424.65 us** | 2.57 ms | 2.72 ms | 335.18 ms |
| future-pay-out-3 | 1.09 ms | 530.64 us | **439.40 us** | 14.01 ms | 825.06 us | 1.04 ms | 1.00 ms | 440.21 us | 2.62 ms | 2.73 ms | 336.85 ms |
| future-pay-out-4 | 2.24 ms | 951.28 us | 795.05 us | 155.84 ms | 1.70 ms | 1.60 ms | 1.99 ms | **671.19 us** | 5.00 ms | 6.40 ms | FAIL |
| future-settle-early-1 | 666.36 us | 298.78 us | 254.72 us | 7.25 ms | 446.13 us | 472.96 us | 508.56 us | **245.26 us** | 1.38 ms | 1.43 ms | 179.62 ms |
| future-settle-early-2 | 1.18 ms | 575.08 us | **484.83 us** | 13.90 ms | 791.42 us | 933.84 us | 996.70 us | 487.22 us | 2.70 ms | 2.97 ms | 312.41 ms |
| future-settle-early-3 | 1.09 ms | 534.02 us | 444.47 us | 14.30 ms | 819.78 us | 969.57 us | 1.13 ms | **429.31 us** | 2.58 ms | 2.73 ms | 317.77 ms |
| future-settle-early-4 | 2.06 ms | 808.22 us | 650.17 us | 149.74 ms | 1.30 ms | 1.29 ms | 1.30 ms | **556.93 us** | 4.25 ms | 5.53 ms | FAIL |
| game-sm-success_1-1 | 1.38 ms | 535.83 us | 435.85 us | 10.93 ms | 804.40 us | 803.02 us | 852.76 us | **392.85 us** | 2.35 ms | 2.30 ms | 260.82 ms |
| game-sm-success_1-2 | 522.03 us | 217.03 us | 188.52 us | 8.64 ms | 341.17 us | 363.50 us | 370.01 us | **169.52 us** | 1.13 ms | 1.15 ms | 121.83 ms |
| game-sm-success_1-3 | 1.63 ms | 697.48 us | 608.34 us | 15.59 ms | 1.10 ms | 1.15 ms | 1.21 ms | **566.69 us** | 3.28 ms | 3.44 ms | 416.56 ms |
| game-sm-success_1-4 | 551.71 us | 242.65 us | 216.59 us | 10.59 ms | 430.67 us | 384.06 us | 387.13 us | **200.74 us** | 1.20 ms | 1.31 ms | 148.37 ms |
| game-sm-success_2-1 | 1.38 ms | 533.28 us | 447.14 us | 10.54 ms | 787.01 us | 851.78 us | 879.72 us | **409.24 us** | 2.09 ms | 2.31 ms | 258.17 ms |
| game-sm-success_2-2 | 479.13 us | 211.41 us | 182.97 us | 8.16 ms | 340.82 us | 350.29 us | 345.03 us | **170.64 us** | 1.05 ms | 1.14 ms | 123.07 ms |
| game-sm-success_2-3 | 1.65 ms | 717.39 us | 598.59 us | 13.80 ms | 1.06 ms | 1.16 ms | 1.29 ms | **545.94 us** | 3.18 ms | 3.40 ms | 411.48 ms |
| game-sm-success_2-4 | 548.79 us | 242.80 us | 209.76 us | 9.60 ms | 383.76 us | 420.33 us | 429.81 us | **182.94 us** | 1.30 ms | 1.31 ms | 133.07 ms |
| game-sm-success_2-5 | 1.67 ms | 725.11 us | 626.68 us | 13.55 ms | 1.06 ms | 1.13 ms | 1.29 ms | **579.84 us** | 3.29 ms | 3.39 ms | 394.31 ms |
| game-sm-success_2-6 | 512.88 us | 237.12 us | 207.77 us | 9.90 ms | 380.65 us | 387.24 us | 424.11 us | **198.62 us** | 1.18 ms | 1.31 ms | 147.27 ms |
| guardrail-sorted-large | 811.18 us | 516.45 us | **378.35 us** | 63.18 ms | 580.23 us | 748.36 us | 815.20 us | 439.95 us | 3.66 ms | 2.71 ms | FAIL |
| guardrail-sorted-small | 265.46 us | 124.98 us | 100.06 us | 1.41 ms | 167.05 us | 163.54 us | 176.74 us | **92.51 us** | 733.60 us | 530.80 us | FAIL |
| guardrail-unsorted-large | 960.97 us | 668.68 us | **483.18 us** | 59.49 ms | 844.40 us | 965.46 us | 1.07 ms | 523.61 us | 5.67 ms | 3.99 ms | FAIL |
| guardrail-unsorted-small | 261.73 us | 121.17 us | 94.56 us | 1.37 ms | 167.72 us | 157.20 us | 174.85 us | **88.78 us** | 941.80 us | 573.20 us | FAIL |
| multisig-sm-01 | 1.63 ms | 585.94 us | 452.95 us | 10.72 ms | 832.96 us | 817.19 us | 859.75 us | **421.33 us** | 2.80 ms | 2.60 ms | FAIL |
| multisig-sm-02 | 1.43 ms | 562.70 us | 448.90 us | 11.31 ms | 832.26 us | 924.58 us | 918.24 us | **418.56 us** | 2.68 ms | 2.38 ms | FAIL |
| multisig-sm-03 | 1.45 ms | 561.71 us | 472.87 us | 11.21 ms | 836.56 us | 840.15 us | 822.89 us | **449.88 us** | 2.90 ms | 2.37 ms | FAIL |
| multisig-sm-04 | 1.52 ms | 563.62 us | 453.29 us | 12.12 ms | 850.27 us | 842.86 us | 916.72 us | **445.00 us** | 2.71 ms | 2.40 ms | FAIL |
| multisig-sm-05 | 1.61 ms | 687.17 us | 598.39 us | 12.77 ms | 999.89 us | 1.23 ms | 1.28 ms | **512.49 us** | 3.55 ms | 3.12 ms | FAIL |
| multisig-sm-06 | 1.48 ms | 571.00 us | 477.07 us | 10.80 ms | 805.71 us | 820.33 us | 879.68 us | **423.69 us** | 2.76 ms | 2.38 ms | FAIL |
| multisig-sm-07 | 1.47 ms | 553.91 us | 446.82 us | 10.55 ms | 872.34 us | 811.33 us | 829.09 us | **424.00 us** | 2.68 ms | 2.30 ms | FAIL |
| multisig-sm-08 | 1.54 ms | 592.12 us | 467.68 us | 10.56 ms | 877.97 us | 829.43 us | 843.02 us | **436.56 us** | 2.89 ms | 2.36 ms | FAIL |
| multisig-sm-09 | 1.45 ms | 550.32 us | 464.60 us | 11.07 ms | 806.99 us | 820.59 us | 923.23 us | **457.15 us** | 3.01 ms | 2.46 ms | FAIL |
| multisig-sm-10 | 1.71 ms | 706.12 us | 592.75 us | 12.57 ms | 990.74 us | 1.10 ms | 1.18 ms | **573.57 us** | 3.77 ms | 3.38 ms | FAIL |
| ping-pong-1 | 1.19 ms | 471.78 us | 391.28 us | 9.68 ms | 681.63 us | 660.38 us | 729.03 us | **355.74 us** | 2.53 ms | 2.17 ms | 240.79 ms |
| ping-pong-2 | 1.33 ms | 500.49 us | 388.26 us | 9.87 ms | 677.80 us | 794.07 us | 751.02 us | **346.46 us** | 2.32 ms | 2.15 ms | 228.73 ms |
| ping-pong_2-1 | 1.07 ms | 376.66 us | 295.20 us | 7.06 ms | 519.35 us | 502.56 us | 515.79 us | **260.99 us** | 1.80 ms | 1.61 ms | 171.26 ms |
| prism-1 | 461.21 us | 202.54 us | 173.64 us | 6.94 ms | 316.40 us | 289.83 us | 295.99 us | **142.88 us** | 1.14 ms | 976.70 us | 103.63 ms |
| prism-2 | 1.45 ms | 552.10 us | 434.57 us | 12.14 ms | 877.53 us | 819.44 us | 870.06 us | **403.03 us** | 2.83 ms | 2.69 ms | 284.90 ms |
| prism-3 | 786.04 us | 395.15 us | 324.91 us | 11.05 ms | 620.87 us | 659.70 us | 694.42 us | **314.60 us** | 2.41 ms | 2.12 ms | 213.31 ms |
| pubkey-1 | 431.67 us | 173.14 us | 158.17 us | 6.37 ms | 293.95 us | 270.54 us | 261.02 us | **143.96 us** | 1.01 ms | 946.70 us | 92.02 ms |
| stablecoin_1-1 | 2.75 ms | 1.13 ms | 1.01 ms | 304.69 ms | 1.89 ms | 1.97 ms | 1.89 ms | **756.74 us** | 7.80 ms | 10.15 ms | FAIL |
| stablecoin_1-2 | 525.03 us | 228.16 us | 191.83 us | 8.85 ms | 355.76 us | 328.65 us | 340.56 us | **163.51 us** | 1.25 ms | 1.17 ms | 134.03 ms |
| stablecoin_1-3 | 2.84 ms | 1.24 ms | 1.14 ms | 293.50 ms | 1.99 ms | 2.16 ms | 2.24 ms | **878.17 us** | 8.57 ms | 10.77 ms | FAIL |
| stablecoin_1-4 | 522.82 us | 230.55 us | 215.70 us | 9.62 ms | 353.33 us | 389.17 us | 389.58 us | **177.24 us** | 1.30 ms | 1.35 ms | 134.73 ms |
| stablecoin_1-5 | 3.34 ms | 1.42 ms | 1.38 ms | 297.73 ms | 2.54 ms | 2.56 ms | 2.66 ms | **1.05 ms** | 9.43 ms | 13.83 ms | FAIL |
| stablecoin_1-6 | 594.80 us | 270.74 us | **219.72 us** | 11.25 ms | 414.46 us | 431.58 us | 444.66 us | 219.83 us | 1.47 ms | 1.47 ms | 145.69 ms |
| stablecoin_2-1 | 2.73 ms | 1.13 ms | 978.74 us | 302.10 ms | 1.95 ms | 2.03 ms | 1.93 ms | **787.77 us** | 6.69 ms | 10.79 ms | FAIL |
| stablecoin_2-2 | 516.98 us | 218.81 us | 207.63 us | 10.06 ms | 356.82 us | 321.15 us | 334.32 us | **164.36 us** | 1.20 ms | 1.20 ms | 117.75 ms |
| stablecoin_2-3 | 3.02 ms | 1.28 ms | 1.14 ms | 290.33 ms | 2.01 ms | 2.06 ms | 2.38 ms | **832.32 us** | 7.67 ms | 10.94 ms | FAIL |
| stablecoin_2-4 | 490.38 us | 225.81 us | 188.59 us | 9.29 ms | 359.42 us | 346.01 us | 373.43 us | **170.37 us** | 1.33 ms | 1.27 ms | 127.82 ms |
| token-account-1 | 589.12 us | 253.47 us | 204.53 us | 5.86 ms | 368.55 us | 403.72 us | 440.20 us | **196.29 us** | 1.13 ms | 1.11 ms | 135.05 ms |
| token-account-2 | 709.10 us | 349.80 us | 319.34 us | 9.31 ms | 513.56 us | 626.14 us | 649.59 us | **285.85 us** | 1.86 ms | 1.67 ms | 206.75 ms |
| uniswap-1 | 813.10 us | 423.68 us | **335.34 us** | 10.17 ms | 618.22 us | 752.25 us | 817.21 us | 367.46 us | 2.24 ms | 2.01 ms | 258.35 ms |
| uniswap-2 | 630.21 us | 277.92 us | 227.72 us | 8.77 ms | 408.89 us | 451.42 us | 519.82 us | **213.55 us** | 1.38 ms | 1.26 ms | 142.46 ms |
| uniswap-3 | 3.46 ms | 1.63 ms | 1.38 ms | 31.34 ms | 2.66 ms | 2.88 ms | 3.36 ms | **1.29 ms** | 9.26 ms | 8.86 ms | 942.76 ms |
| uniswap-4 | 668.50 us | 328.92 us | 300.67 us | 15.75 ms | 564.21 us | 564.33 us | 554.02 us | **272.04 us** | 1.91 ms | 1.79 ms | 177.74 ms |
| uniswap-5 | 2.76 ms | 1.21 ms | **940.73 us** | 27.73 ms | 1.82 ms | 2.01 ms | 2.26 ms | 958.33 us | 6.04 ms | 6.12 ms | 608.50 ms |
| uniswap-6 | 626.57 us | 320.42 us | 271.82 us | 15.07 ms | 525.31 us | 556.01 us | 539.59 us | **246.91 us** | 1.86 ms | 1.89 ms | 199.40 ms |
| vesting-1 | 993.86 us | 429.67 us | **348.95 us** | 9.15 ms | 604.21 us | 665.33 us | 701.87 us | 349.85 us | 1.92 ms | 1.99 ms | 237.07 ms |

## Eval tier: evaluate a decoded program

The program is decoded before timing; each iteration evaluates it. JIT VMs compile before timing too.

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

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
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc post-JIT execution (C++ / LLVM) | Amaru UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 165.22 us | **42.42 us** | 122.64 us | 249.13 us | 72.65 us | 120.78 us | 7.25 ms | 214.98 us | 210.12 us | 232.71 us | 107.81 us | 754.60 us | 849.70 us | 98.89 ms |
| auction_1-2 | 545.44 us | 1.04 ms | 447.55 us | 813.41 us | **281.50 us** | 420.58 us | 11.87 ms | 731.52 us | 933.40 us | 1.00 ms | 420.00 us | 2.52 ms | 2.63 ms | 367.47 ms |
| auction_1-3 | 523.76 us | 726.02 us | 463.62 us | 823.13 us | **279.50 us** | 427.13 us | 11.95 ms | 739.05 us | 940.02 us | 991.87 us | 411.01 us | 2.52 ms | 2.64 ms | 355.19 ms |
| auction_1-4 | 207.85 us | **53.22 us** | 152.36 us | 288.44 us | 96.30 us | 157.59 us | 8.85 ms | 312.02 us | 277.46 us | 287.56 us | 130.90 us | 987.50 us | 1.10 ms | 126.79 ms |
| auction_2-1 | 158.85 us | **38.68 us** | 120.09 us | 251.14 us | 72.30 us | 113.72 us | 6.39 ms | 231.24 us | 240.43 us | 253.22 us | 103.93 us | 770.50 us | 916.30 us | 102.38 ms |
| auction_2-2 | 528.37 us | 874.45 us | 464.63 us | 825.52 us | **292.40 us** | 425.37 us | 10.99 ms | 740.68 us | 890.45 us | 1.00 ms | 441.58 us | 2.52 ms | 2.64 ms | 373.70 ms |
| auction_2-3 | 715.69 us | 1.00 ms | 605.83 us | 1.05 ms | **358.14 us** | 578.61 us | 13.44 ms | 987.21 us | 1.21 ms | 1.27 ms | 566.16 us | 3.43 ms | 3.60 ms | 452.75 ms |
| auction_2-4 | 535.85 us | 679.26 us | 465.04 us | 789.99 us | **293.28 us** | 434.26 us | 11.48 ms | 718.73 us | 903.11 us | 1.05 ms | 413.63 us | 2.72 ms | 2.85 ms | 350.93 ms |
| auction_2-5 | 207.85 us | **49.07 us** | 153.50 us | 306.81 us | 89.16 us | 150.29 us | 10.04 ms | 277.71 us | 278.43 us | 292.60 us | 134.52 us | 1.02 ms | 1.16 ms | 118.97 ms |
| coop-1 | 204.16 us | **42.57 us** | 202.34 us | FAIL | 91.29 us | 122.82 us | 9.91 ms | 298.99 us | 303.92 us | 286.56 us | 141.97 us | 1.41 ms | 1.36 ms | FAIL |
| coop-2 | 749.68 us | **163.03 us** | 631.73 us | FAIL | 287.92 us | 449.81 us | 30.37 ms | 921.33 us | 854.50 us | 969.58 us | 457.02 us | 4.30 ms | 3.89 ms | FAIL |
| coop-3 | 1.85 ms | **698.87 us** | 2.05 ms | FAIL | 1.00 ms | 1.22 ms | 36.05 ms | 2.61 ms | 3.23 ms | 3.34 ms | 1.48 ms | 14.08 ms | 9.91 ms | FAIL |
| coop-4 | 916.88 us | **245.93 us** | 771.03 us | FAIL | 399.15 us | 488.10 us | 27.36 ms | 1.01 ms | 1.14 ms | 1.13 ms | 646.20 us | 7.56 ms | 4.52 ms | FAIL |
| coop-5 | 370.65 us | **91.64 us** | 354.31 us | FAIL | 175.72 us | 215.50 us | 14.60 ms | 451.30 us | 461.91 us | 572.00 us | 245.52 us | 2.44 ms | 1.98 ms | FAIL |
| coop-6 | 651.56 us | **150.79 us** | 585.20 us | FAIL | 279.09 us | 363.01 us | 28.85 ms | 811.56 us | 851.81 us | 807.86 us | 423.67 us | 4.18 ms | 3.54 ms | FAIL |
| coop-7 | 294.83 us | **54.97 us** | 269.98 us | FAIL | 127.65 us | 175.99 us | 15.08 ms | 404.48 us | 358.88 us | 377.50 us | 192.10 us | 1.83 ms | 1.76 ms | FAIL |
| crowdfunding-success-1 | 184.55 us | **42.48 us** | 146.13 us | 262.66 us | 88.32 us | 128.18 us | 8.67 ms | 250.83 us | 259.63 us | 292.98 us | 121.52 us | 1.01 ms | 989.90 us | 109.06 ms |
| crowdfunding-success-2 | 191.04 us | **45.22 us** | 140.86 us | 277.64 us | 87.81 us | 133.61 us | 8.01 ms | 267.91 us | 285.82 us | 266.69 us | 121.44 us | 1.02 ms | 1.01 ms | 108.96 ms |
| crowdfunding-success-3 | 188.15 us | **41.69 us** | 144.96 us | 261.77 us | 88.06 us | 130.61 us | 7.99 ms | 256.46 us | 275.74 us | 261.18 us | 131.85 us | 1.03 ms | 992.70 us | 123.40 ms |
| currency-1 | 212.57 us | **65.97 us** | 178.33 us | 345.04 us | 110.78 us | 163.84 us | 5.93 ms | 285.89 us | 348.78 us | 417.56 us | 167.09 us | 1.22 ms | 1.13 ms | 153.17 ms |
| escrow-redeem_1-1 | 294.82 us | **92.18 us** | 268.56 us | 424.71 us | 160.03 us | 217.68 us | 9.15 ms | 394.18 us | 521.01 us | 486.20 us | 224.29 us | 1.68 ms | 1.72 ms | 210.45 ms |
| escrow-redeem_1-2 | 325.87 us | **111.59 us** | 243.38 us | 442.48 us | 159.97 us | 229.70 us | 9.13 ms | 393.07 us | 476.75 us | 482.94 us | 233.32 us | 1.75 ms | 1.65 ms | 196.68 ms |
| escrow-redeem_2-1 | 341.86 us | **109.80 us** | 299.75 us | 480.67 us | 172.76 us | 252.61 us | 10.40 ms | 453.25 us | 549.90 us | 664.33 us | 264.42 us | 1.83 ms | 1.83 ms | 227.67 ms |
| escrow-redeem_2-2 | 380.82 us | **101.55 us** | 285.23 us | 507.03 us | 178.81 us | 251.37 us | 11.58 ms | 462.04 us | 531.18 us | 588.71 us | 257.54 us | 1.73 ms | 1.81 ms | 217.66 ms |
| escrow-redeem_2-3 | 353.73 us | **102.33 us** | 295.55 us | 490.24 us | 185.88 us | 249.98 us | 11.27 ms | 515.45 us | 523.20 us | 579.12 us | 257.65 us | 1.74 ms | 1.82 ms | 213.43 ms |
| escrow-refund-1 | 147.00 us | **36.20 us** | 103.01 us | 228.70 us | 70.84 us | 104.04 us | 5.66 ms | 195.88 us | 189.35 us | 202.59 us | 99.74 us | 653.30 us | 745.30 us | 89.93 ms |
| future-increase-margin-1 | 205.09 us | **65.33 us** | 179.40 us | 334.60 us | 106.16 us | 184.13 us | 6.11 ms | 307.31 us | 341.64 us | 370.83 us | 161.52 us | 1.04 ms | 1.16 ms | 144.09 ms |
| future-increase-margin-2 | 460.76 us | **149.19 us** | 390.67 us | 632.17 us | 232.30 us | 328.32 us | 13.55 ms | 600.30 us | 776.98 us | 766.34 us | 333.51 us | 2.17 ms | 2.37 ms | 315.28 ms |
| future-increase-margin-3 | 478.11 us | **146.05 us** | 372.71 us | 647.67 us | 227.36 us | 326.82 us | 12.60 ms | 596.16 us | 708.76 us | 842.14 us | 336.67 us | 2.28 ms | 2.50 ms | 285.72 ms |
| future-increase-margin-4 | 405.45 us | 577.48 us | 352.51 us | 663.74 us | **227.15 us** | 386.47 us | 9.86 ms | 601.30 us | 674.88 us | 773.21 us | 323.35 us | 2.11 ms | 2.20 ms | FAIL |
| future-increase-margin-5 | 703.43 us | 1.51 ms | 591.75 us | 1.18 ms | **407.95 us** | 590.30 us | 158.71 ms | 1.29 ms | 1.19 ms | 1.37 ms | 492.22 us | 4.45 ms | 6.21 ms | FAIL |
| future-pay-out-1 | 213.75 us | **67.20 us** | 188.56 us | 320.62 us | 107.08 us | 159.07 us | 5.86 ms | 301.59 us | 391.41 us | 378.85 us | 170.45 us | 1.10 ms | 1.17 ms | 140.46 ms |
| future-pay-out-2 | 467.31 us | **154.42 us** | 380.12 us | 640.41 us | 224.74 us | 346.92 us | 12.54 ms | 593.70 us | 771.59 us | 774.89 us | 362.68 us | 2.43 ms | 2.51 ms | 283.50 ms |
| future-pay-out-3 | 442.45 us | **148.63 us** | 394.68 us | 630.70 us | 238.07 us | 355.77 us | 12.65 ms | 594.49 us | 702.41 us | 787.35 us | 363.41 us | 2.33 ms | 2.44 ms | 282.84 ms |
| future-pay-out-4 | 740.85 us | 1.49 ms | 610.03 us | 1.14 ms | **396.15 us** | 583.82 us | 146.98 ms | 1.13 ms | 1.31 ms | 1.28 ms | 519.89 us | 4.32 ms | 5.99 ms | FAIL |
| future-settle-early-1 | 217.55 us | **63.31 us** | 182.98 us | 323.06 us | 116.14 us | 163.00 us | 5.75 ms | 295.97 us | 342.45 us | 385.81 us | 162.74 us | 1.10 ms | 1.32 ms | 144.53 ms |
| future-settle-early-2 | 489.43 us | **191.83 us** | 375.17 us | 644.52 us | 228.59 us | 354.64 us | 13.49 ms | 667.57 us | 737.44 us | 772.12 us | 338.00 us | 2.29 ms | 2.51 ms | 330.09 ms |
| future-settle-early-3 | 449.61 us | **146.75 us** | 382.06 us | 647.72 us | 223.75 us | 327.65 us | 13.51 ms | 659.77 us | 774.06 us | 775.49 us | 344.85 us | 2.18 ms | 2.56 ms | 303.72 ms |
| future-settle-early-4 | 540.48 us | 1.44 ms | 480.63 us | 863.63 us | **298.51 us** | 450.71 us | 145.68 ms | 815.64 us | 917.44 us | 979.33 us | 397.45 us | 3.26 ms | 4.92 ms | FAIL |
| game-sm-success_1-1 | 351.44 us | 321.79 us | 277.33 us | 525.55 us | **184.13 us** | 274.12 us | 9.42 ms | 460.74 us | 508.77 us | 629.68 us | 256.82 us | 1.59 ms | 1.83 ms | 225.25 ms |
| game-sm-success_1-2 | 172.23 us | **37.66 us** | 136.87 us | 249.59 us | 78.75 us | 134.42 us | 7.69 ms | 239.29 us | 269.55 us | 251.20 us | 110.86 us | 871.30 us | 1.00 ms | 104.64 ms |
| game-sm-success_1-3 | 533.39 us | 588.74 us | 448.54 us | 817.55 us | **277.30 us** | 421.25 us | 12.32 ms | 742.27 us | 894.48 us | 964.11 us | 409.28 us | 2.61 ms | 2.95 ms | 343.55 ms |
| game-sm-success_1-4 | 209.67 us | **46.95 us** | 158.63 us | 284.80 us | 103.08 us | 143.84 us | 8.75 ms | 281.60 us | 289.04 us | 329.85 us | 133.94 us | 968.30 us | 1.16 ms | 118.17 ms |
| game-sm-success_2-1 | 342.55 us | 412.33 us | 278.68 us | 536.91 us | **174.10 us** | 255.49 us | 9.57 ms | 506.51 us | 556.99 us | 549.00 us | 258.93 us | 1.55 ms | 1.86 ms | 218.45 ms |
| game-sm-success_2-2 | 170.95 us | **39.31 us** | 139.52 us | 257.17 us | 79.71 us | 137.46 us | 8.09 ms | 237.30 us | 247.41 us | 248.84 us | 122.86 us | 926.30 us | 971.30 us | 110.39 ms |
| game-sm-success_2-3 | 545.17 us | 609.84 us | 458.34 us | 812.75 us | **284.93 us** | 417.03 us | 11.74 ms | 737.12 us | 852.87 us | 995.83 us | 439.45 us | 2.59 ms | 2.82 ms | 362.46 ms |
| game-sm-success_2-4 | 203.67 us | **47.99 us** | 162.76 us | 280.29 us | 88.98 us | 152.55 us | 8.78 ms | 278.48 us | 273.19 us | 290.49 us | 135.90 us | 1.02 ms | 1.18 ms | 116.51 ms |
| game-sm-success_2-5 | 564.13 us | 712.11 us | 448.80 us | 820.17 us | **272.35 us** | 437.14 us | 12.45 ms | 761.06 us | 903.84 us | 937.56 us | 418.67 us | 2.62 ms | 2.93 ms | 353.59 ms |
| game-sm-success_2-6 | 200.97 us | **45.70 us** | 160.25 us | 290.98 us | 89.01 us | 155.28 us | 8.62 ms | 281.26 us | 311.87 us | 304.37 us | 131.07 us | 1.03 ms | 1.09 ms | 124.39 ms |
| guardrail-sorted-large | 422.76 us | **231.50 us** | 389.26 us | FAIL | 305.03 us | 250.93 us | 55.32 ms | 500.27 us | 600.41 us | 608.11 us | 270.04 us | 2.56 ms | 2.19 ms | FAIL |
| guardrail-sorted-small | 64.32 us | 89.91 us | 79.54 us | FAIL | **27.45 us** | 47.16 us | 873.82 us | 94.13 us | 89.05 us | 99.64 us | 50.18 us | 583.80 us | 384.60 us | FAIL |
| guardrail-unsorted-large | 550.26 us | **307.71 us** | 551.81 us | FAIL | 384.00 us | 345.50 us | 61.52 ms | 679.66 us | 888.08 us | 993.97 us | 414.73 us | 5.18 ms | 3.05 ms | FAIL |
| guardrail-unsorted-small | 62.95 us | 84.81 us | 79.74 us | FAIL | **23.86 us** | 43.97 us | 849.63 us | 76.81 us | 84.66 us | 103.84 us | 45.43 us | 532.60 us | 373.70 us | FAIL |
| multisig-sm-01 | 361.50 us | 471.19 us | 297.75 us | 560.81 us | **198.78 us** | 290.00 us | 9.22 ms | 480.53 us | 544.44 us | 581.65 us | 280.37 us | 2.10 ms | 1.67 ms | FAIL |
| multisig-sm-02 | 342.61 us | 618.10 us | 273.27 us | 555.66 us | **176.58 us** | 267.80 us | 9.00 ms | 461.94 us | 580.09 us | 595.36 us | 260.12 us | 2.11 ms | 1.73 ms | FAIL |
| multisig-sm-03 | 336.07 us | 587.33 us | 299.91 us | 559.80 us | **182.97 us** | 284.54 us | 8.88 ms | 467.23 us | 519.26 us | 562.96 us | 270.38 us | 2.04 ms | 1.88 ms | FAIL |
| multisig-sm-04 | 359.42 us | 594.16 us | 291.50 us | 561.31 us | **182.06 us** | 276.88 us | 8.86 ms | 515.89 us | 585.47 us | 577.58 us | 275.83 us | 2.05 ms | 1.74 ms | FAIL |
| multisig-sm-05 | 480.13 us | 874.50 us | 411.96 us | 747.74 us | **247.71 us** | 386.16 us | 10.36 ms | 696.41 us | 784.17 us | 862.99 us | 407.18 us | 2.85 ms | 2.29 ms | FAIL |
| multisig-sm-06 | 350.74 us | 407.58 us | 286.87 us | 577.20 us | **194.32 us** | 289.74 us | 9.50 ms | 476.65 us | 540.48 us | 575.41 us | 284.89 us | 2.02 ms | 1.66 ms | FAIL |
| multisig-sm-07 | 332.39 us | 521.59 us | 290.70 us | 542.00 us | **179.30 us** | 265.16 us | 9.33 ms | 473.19 us | 611.48 us | 637.23 us | 268.12 us | 1.99 ms | 1.62 ms | FAIL |
| multisig-sm-08 | 384.77 us | 518.44 us | 282.04 us | 572.82 us | **175.51 us** | 279.55 us | 8.79 ms | 493.86 us | 531.48 us | 584.01 us | 267.44 us | 2.04 ms | 1.63 ms | FAIL |
| multisig-sm-09 | 334.39 us | 497.66 us | 287.70 us | 546.36 us | **183.74 us** | 275.27 us | 8.68 ms | 537.71 us | 558.41 us | 634.30 us | 265.24 us | 1.85 ms | 1.65 ms | FAIL |
| multisig-sm-10 | 508.66 us | 1.00 ms | 410.34 us | 762.49 us | **245.89 us** | 431.73 us | 9.93 ms | 662.78 us | 861.15 us | 916.64 us | 375.47 us | 2.64 ms | 2.40 ms | FAIL |
| ping-pong-1 | 281.47 us | 275.96 us | 238.03 us | 448.32 us | **166.30 us** | 218.25 us | 7.19 ms | 394.38 us | 456.17 us | 465.47 us | 241.13 us | 1.69 ms | 1.40 ms | 184.89 ms |
| ping-pong-2 | 298.90 us | 267.44 us | 249.06 us | 450.14 us | **149.30 us** | 219.87 us | 7.17 ms | 394.53 us | 460.49 us | 528.03 us | 228.54 us | 1.51 ms | 1.39 ms | 184.82 ms |
| ping-pong_2-1 | 176.88 us | **83.67 us** | 145.44 us | 314.20 us | 97.07 us | 133.43 us | 5.83 ms | 238.52 us | 262.20 us | 267.33 us | 127.48 us | 940.00 us | 878.60 us | 129.38 ms |
| prism-1 | 144.96 us | **31.52 us** | 128.41 us | 221.60 us | 64.15 us | 116.86 us | 6.87 ms | 208.17 us | 206.95 us | 218.08 us | 95.26 us | 800.10 us | 782.70 us | 103.76 ms |
| prism-2 | 372.46 us | 336.95 us | 295.51 us | 559.23 us | **192.88 us** | 277.13 us | 10.71 ms | 545.58 us | 611.30 us | 588.58 us | 267.88 us | 2.01 ms | 1.84 ms | 253.24 ms |
| prism-3 | 310.92 us | **103.45 us** | 275.41 us | 453.73 us | 155.57 us | 257.00 us | 10.23 ms | 461.29 us | 521.37 us | 591.60 us | 234.00 us | 1.90 ms | 1.67 ms | 200.76 ms |
| pubkey-1 | 129.91 us | **28.28 us** | 100.79 us | 198.26 us | 59.30 us | 87.86 us | 5.63 ms | 172.23 us | 178.58 us | 175.93 us | 84.40 us | 647.40 us | 679.50 us | 75.77 ms |
| stablecoin_1-1 | 816.81 us | 2.69 ms | 782.90 us | 1.36 ms | **450.13 us** | 779.02 us | 286.85 ms | 1.27 ms | 1.41 ms | 1.51 ms | 606.41 us | 5.44 ms | 8.35 ms | FAIL |
| stablecoin_1-2 | 180.61 us | **39.30 us** | 130.21 us | 258.14 us | 82.85 us | 123.91 us | 8.89 ms | 237.51 us | 234.92 us | 262.25 us | 115.67 us | 896.40 us | 984.90 us | 101.91 ms |
| stablecoin_1-3 | 953.18 us | 2.58 ms | 835.15 us | 1.62 ms | **488.97 us** | 854.98 us | 288.13 ms | 1.58 ms | 1.54 ms | 1.75 ms | 630.55 us | 5.96 ms | 9.64 ms | FAIL |
| stablecoin_1-4 | 192.12 us | **41.20 us** | 143.20 us | 274.78 us | 80.65 us | 136.02 us | 8.58 ms | 255.50 us | 247.21 us | 273.71 us | 117.38 us | 987.20 us | 1.06 ms | 105.19 ms |
| stablecoin_1-5 | 1.21 ms | 2.83 ms | 1.03 ms | 2.03 ms | **580.72 us** | 1.18 ms | 289.60 ms | 2.18 ms | 2.17 ms | 2.37 ms | 845.29 us | 7.95 ms | 10.72 ms | FAIL |
| stablecoin_1-6 | 243.98 us | **50.18 us** | 172.82 us | 320.13 us | 98.64 us | 163.82 us | 11.65 ms | 318.64 us | 342.95 us | 324.76 us | 142.00 us | 1.31 ms | 1.20 ms | 130.94 ms |
| stablecoin_2-1 | 816.07 us | 2.65 ms | 739.50 us | 1.40 ms | **433.09 us** | 730.58 us | 289.12 ms | 1.30 ms | 1.44 ms | 1.41 ms | 605.32 us | 5.35 ms | 8.21 ms | FAIL |
| stablecoin_2-2 | 170.63 us | **37.47 us** | 139.84 us | 253.51 us | 76.06 us | 132.20 us | 8.00 ms | 237.07 us | 236.56 us | 264.45 us | 113.23 us | 892.90 us | 911.60 us | 99.75 ms |
| stablecoin_2-3 | 1.00 ms | 2.68 ms | 818.21 us | 1.65 ms | **486.07 us** | 868.79 us | 298.73 ms | 1.50 ms | 1.68 ms | 1.85 ms | 629.14 us | 5.97 ms | 8.93 ms | FAIL |
| stablecoin_2-4 | 176.21 us | **39.17 us** | 143.05 us | 255.14 us | 87.54 us | 136.75 us | 8.63 ms | 244.13 us | 252.05 us | 262.62 us | 117.67 us | 952.50 us | 967.30 us | 104.92 ms |
| token-account-1 | 170.20 us | **52.59 us** | 139.15 us | 272.59 us | 83.86 us | 139.87 us | 5.04 ms | 222.19 us | 268.16 us | 298.07 us | 117.88 us | 851.60 us | 873.10 us | 104.84 ms |
| token-account-2 | 282.04 us | **75.96 us** | 243.95 us | 401.36 us | 141.52 us | 217.14 us | 8.30 ms | 394.44 us | 537.53 us | 498.97 us | 208.83 us | 1.56 ms | 1.50 ms | 181.12 ms |
| uniswap-1 | 335.13 us | **105.67 us** | 289.03 us | 496.40 us | 175.70 us | 254.18 us | 8.30 ms | 510.38 us | 562.00 us | 647.51 us | 292.44 us | 1.79 ms | 1.73 ms | 261.04 ms |
| uniswap-2 | 188.72 us | **59.93 us** | 165.20 us | 300.41 us | 101.42 us | 146.57 us | 7.39 ms | 273.54 us | 300.67 us | 342.67 us | 157.39 us | 1.01 ms | 999.50 us | 132.74 ms |
| uniswap-3 | 1.51 ms | 1.00 ms | 1.23 ms | 2.14 ms | **608.65 us** | 1.20 ms | 28.45 ms | 2.09 ms | 2.65 ms | 2.61 ms | 1.14 ms | 7.75 ms | 7.43 ms | 840.70 ms |
| uniswap-4 | 292.64 us | **61.93 us** | 221.44 us | 388.91 us | 137.60 us | 205.59 us | 16.17 ms | 399.71 us | 431.72 us | 422.06 us | 188.90 us | 1.40 ms | 1.56 ms | 167.31 ms |
| uniswap-5 | 1.09 ms | 677.18 us | 827.54 us | 1.39 ms | **428.77 us** | 731.47 us | 25.69 ms | 1.34 ms | 1.43 ms | 1.63 ms | 720.12 us | 4.73 ms | 5.03 ms | 613.34 ms |
| uniswap-6 | 269.91 us | **57.86 us** | 226.16 us | 393.64 us | 131.65 us | 198.24 us | 14.24 ms | 394.91 us | 398.68 us | 399.93 us | 181.61 us | 1.32 ms | 1.49 ms | 163.81 ms |
| vesting-1 | 315.46 us | 178.69 us | 265.63 us | 449.88 us | **168.56 us** | 246.24 us | 7.58 ms | 422.26 us | 452.86 us | 497.46 us | 233.40 us | 1.42 ms | 1.43 ms | 190.54 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*