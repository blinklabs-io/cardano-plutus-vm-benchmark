# Cardano Plutus VM Benchmark Results

**Date:** 2026-11-16

**Corpus:** Plutus use cases (`plutus_use_cases`): all 89 programs. The per-script tables list every program measured.

## Environment
```
date: 2026-11-16T02:05:29+00:00
kernel: 6.8.0-147-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
corpus: plutus_use_cases (89 of 89 programs, sample all, seed 1; list in corpus.txt)
```

## VM Versions

| VM | Source revision | Toolchain |
|---|---|---|
| plutus-core CEK (Haskell / GHC) | master@0e8f167 ([0e8f167](https://github.com/IntersectMBO/plutus/commit/0e8f16796dc5cb45cc68c2613a7520f219b0c7f8)) | GHC 9.6.4 |
| Scalus UPLC→JVM JIT (Scala / JVM) | master@92a8170 ([92a8170](https://github.com/scalus3/scalus/commit/92a81700b34ee531fa0adf210138df6b61df9cd1)) | JDK 21 / Scala 3 |
| Scalus CEK (Scala / JVM) | master@92a8170 ([92a8170](https://github.com/scalus3/scalus/commit/92a81700b34ee531fa0adf210138df6b61df9cd1)) | JDK 21 / Scala 3 |
| Julc CEK (Java / GraalVM) | v0.1.0-pre21-rc1 ([5483ecb](https://github.com/bloxbean/julc/commit/5483ecbca8e62a91e0719455d695af24872c2409)) | GraalVM 25.0.2-graal |
| llvm-uplc post-JIT execution (C++ / LLVM) | master@6bcef67 ([6bcef67](https://github.com/SeungheonOh/llvm-uplc/commit/6bcef67ce1995d232327f13d9080fe2f0261a55c)) | LLVM 22.1.0 |
| Amaru UPLC CEK (Rust) | [0.6.0](https://crates.io/crates/amaru-uplc/0.6.0) | rustc nightly-2026-09-04 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | [3.0.5](https://www.npmjs.com/package/@harmoniclabs/plutus-machine/v/3.0.5) | Node.js 22 |
| Plutuz CEK (Zig) | main@33b812d ([33b812d](https://github.com/utxo-company/plutuz/commit/33b812dbcf88f6851286e54cb93a4a443353f94c)) | Zig 0.15.2 |
| Chrysalis CEK (C# / .NET) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Chrysalis CEK (C# / .NET AOT) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Plutigo CEK (Go) | main@c4a50c1 ([c4a50c1](https://github.com/blinklabs-io/plutigo/commit/c4a50c15c86e7a3d57348a478d72f410e7ce75a9)) | Go 1.27.3 |
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
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus CEK (Scala / JVM) | Amaru UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 597.83 us | 222.72 us | 216.99 us | 7.25 ms | 334.56 us | 336.16 us | 384.33 us | **189.17 us** | 936.90 us | 1.05 ms | 110.61 ms |
| auction_1-2 | 1.69 ms | 752.73 us | 624.36 us | 12.85 ms | 1.11 ms | 1.17 ms | 1.29 ms | **592.69 us** | 3.09 ms | 3.16 ms | 418.69 ms |
| auction_1-3 | 1.82 ms | 712.33 us | 601.68 us | 13.24 ms | 1.01 ms | 1.26 ms | 1.29 ms | **549.60 us** | 3.04 ms | 3.19 ms | 400.50 ms |
| auction_1-4 | 596.93 us | 255.06 us | 235.11 us | 11.63 ms | 396.35 us | 408.83 us | 437.96 us | **204.74 us** | 1.22 ms | 1.26 ms | 137.01 ms |
| auction_2-1 | 574.25 us | 224.91 us | 195.67 us | 7.39 ms | 338.49 us | 346.52 us | 361.13 us | **162.29 us** | 1.01 ms | 1.01 ms | 125.05 ms |
| auction_2-2 | 1.70 ms | 731.16 us | 610.98 us | 12.89 ms | 1.09 ms | 1.18 ms | 1.26 ms | **557.99 us** | 2.94 ms | 3.16 ms | 454.43 ms |
| auction_2-3 | 2.27 ms | 882.07 us | 777.14 us | 16.12 ms | 1.40 ms | 1.48 ms | 1.70 ms | **708.12 us** | 3.73 ms | 3.97 ms | 489.89 ms |
| auction_2-4 | 1.69 ms | 711.97 us | 659.47 us | 13.09 ms | 1.04 ms | 1.28 ms | 1.26 ms | **593.66 us** | 3.11 ms | 3.19 ms | 391.05 ms |
| auction_2-5 | 599.90 us | 271.96 us | 223.52 us | 9.55 ms | 443.23 us | 408.67 us | 422.30 us | **191.98 us** | 1.21 ms | 1.26 ms | 131.99 ms |
| coop-1 | 479.24 us | 243.24 us | **169.08 us** | 11.65 ms | 370.81 us | 340.65 us | 421.51 us | 198.23 us | 1.76 ms | 1.40 ms | FAIL |
| coop-2 | 1.41 ms | 801.46 us | **494.39 us** | 36.16 ms | 965.10 us | 1.29 ms | 1.23 ms | 576.29 us | 5.23 ms | 4.33 ms | FAIL |
| coop-3 | 3.35 ms | 2.22 ms | **1.30 ms** | 40.99 ms | 2.59 ms | 3.76 ms | 3.69 ms | 1.65 ms | 17.01 ms | 11.25 ms | FAIL |
| coop-4 | 1.73 ms | 971.82 us | **624.41 us** | 29.95 ms | 1.27 ms | 1.58 ms | 1.56 ms | 737.07 us | 7.27 ms | 5.64 ms | FAIL |
| coop-5 | 899.76 us | 488.32 us | **339.72 us** | 15.33 ms | 689.57 us | 704.80 us | 719.56 us | 400.99 us | 3.68 ms | 2.40 ms | FAIL |
| coop-6 | 1.05 ms | 696.04 us | **482.40 us** | 30.38 ms | 1.02 ms | 962.86 us | 1.02 ms | 546.34 us | 4.90 ms | 3.79 ms | FAIL |
| coop-7 | 690.38 us | 351.82 us | **226.30 us** | 15.97 ms | 524.99 us | 511.14 us | 558.13 us | 252.23 us | 2.32 ms | 1.91 ms | FAIL |
| crowdfunding-success-1 | 637.00 us | 265.57 us | 213.57 us | 9.33 ms | 383.92 us | 384.21 us | 431.08 us | **191.77 us** | 1.33 ms | 1.22 ms | 148.49 ms |
| crowdfunding-success-2 | 719.28 us | 270.50 us | 212.60 us | 9.07 ms | 400.39 us | 382.19 us | 394.18 us | **193.31 us** | 1.35 ms | 1.21 ms | 164.71 ms |
| crowdfunding-success-3 | 644.54 us | 261.05 us | 225.94 us | 9.83 ms | 391.61 us | 383.26 us | 432.01 us | **197.83 us** | 1.28 ms | 1.21 ms | 138.11 ms |
| currency-1 | 663.05 us | 324.46 us | **238.07 us** | 6.92 ms | 438.62 us | 478.84 us | 514.65 us | 245.34 us | 1.52 ms | 1.34 ms | 162.66 ms |
| escrow-redeem_1-1 | 988.11 us | 414.50 us | **319.26 us** | 10.14 ms | 598.91 us | 698.08 us | 682.28 us | 336.75 us | 2.03 ms | 1.86 ms | 214.42 ms |
| escrow-redeem_1-2 | 958.14 us | 420.71 us | 372.78 us | 10.19 ms | 616.09 us | 654.29 us | 723.91 us | **312.13 us** | 2.14 ms | 1.85 ms | 213.46 ms |
| escrow-redeem_2-1 | 1.05 ms | 469.40 us | 367.51 us | 12.39 ms | 763.36 us | 718.94 us | 771.78 us | **353.04 us** | 2.34 ms | 2.10 ms | 242.51 ms |
| escrow-redeem_2-2 | 997.29 us | 466.37 us | 355.60 us | 11.87 ms | 654.47 us | 829.32 us | 909.51 us | **347.47 us** | 2.39 ms | 2.11 ms | 239.58 ms |
| escrow-redeem_2-3 | 1.09 ms | 446.00 us | 391.33 us | 12.08 ms | 649.83 us | 777.24 us | 779.82 us | **366.05 us** | 2.39 ms | 2.15 ms | 296.97 ms |
| escrow-refund-1 | 726.11 us | 268.81 us | 221.03 us | 7.22 ms | 366.81 us | 340.43 us | 358.55 us | **208.81 us** | 1.04 ms | 1.09 ms | 136.49 ms |
| future-increase-margin-1 | 728.22 us | 306.76 us | **245.00 us** | 7.31 ms | 429.09 us | 550.64 us | 541.33 us | 245.03 us | 1.36 ms | 1.39 ms | 169.82 ms |
| future-increase-margin-2 | 1.16 ms | 528.24 us | 448.12 us | 14.42 ms | 785.27 us | 946.98 us | 1.05 ms | **426.01 us** | 2.75 ms | 2.83 ms | 315.88 ms |
| future-increase-margin-3 | 1.26 ms | 562.05 us | 443.42 us | 15.06 ms | 831.14 us | 929.58 us | 1.05 ms | **427.82 us** | 2.51 ms | 2.85 ms | 320.61 ms |
| future-increase-margin-4 | 1.83 ms | 669.43 us | 618.90 us | 12.12 ms | 1.12 ms | 1.03 ms | 1.12 ms | **500.83 us** | 2.83 ms | 2.83 ms | FAIL |
| future-increase-margin-5 | 1.95 ms | 965.62 us | 809.92 us | 150.49 ms | 1.76 ms | 1.57 ms | 1.72 ms | **698.08 us** | 5.29 ms | 7.02 ms | FAIL |
| future-pay-out-1 | 698.19 us | 301.49 us | 239.22 us | 6.60 ms | 436.82 us | 524.95 us | 523.45 us | **232.05 us** | 1.43 ms | 1.43 ms | 159.07 ms |
| future-pay-out-2 | 1.14 ms | 563.91 us | **459.49 us** | 15.08 ms | 785.52 us | 972.84 us | 1.13 ms | 469.54 us | 2.77 ms | 2.84 ms | 341.75 ms |
| future-pay-out-3 | 1.18 ms | 558.41 us | 453.41 us | 14.96 ms | 815.34 us | 982.46 us | 1.04 ms | **434.44 us** | 2.96 ms | 2.82 ms | 338.36 ms |
| future-pay-out-4 | 2.04 ms | 971.74 us | 789.02 us | 160.74 ms | 1.50 ms | 1.75 ms | 1.69 ms | **663.58 us** | 5.19 ms | 6.74 ms | FAIL |
| future-settle-early-1 | 746.43 us | 293.23 us | 248.34 us | 6.88 ms | 459.16 us | 504.36 us | 556.06 us | **224.85 us** | 1.43 ms | 1.55 ms | 159.78 ms |
| future-settle-early-2 | 1.18 ms | 563.22 us | 492.84 us | 14.03 ms | 784.37 us | 1.03 ms | 1.00 ms | **462.32 us** | 2.76 ms | 3.07 ms | 309.23 ms |
| future-settle-early-3 | 1.25 ms | 591.06 us | **438.13 us** | 14.69 ms | 869.48 us | 926.66 us | 997.01 us | 445.64 us | 2.77 ms | 4.02 ms | 333.89 ms |
| future-settle-early-4 | 1.95 ms | 791.46 us | 633.72 us | 159.00 ms | 1.29 ms | 1.21 ms | 1.40 ms | **604.71 us** | 4.59 ms | 8.00 ms | FAIL |
| game-sm-success_1-1 | 1.57 ms | 561.60 us | 445.05 us | 12.80 ms | 775.20 us | 798.49 us | 913.57 us | **423.12 us** | 2.20 ms | 2.81 ms | 256.30 ms |
| game-sm-success_1-2 | 500.00 us | 227.98 us | 194.43 us | 8.34 ms | 340.30 us | 356.60 us | 351.59 us | **164.37 us** | 1.21 ms | 1.29 ms | 134.31 ms |
| game-sm-success_1-3 | 1.66 ms | 749.56 us | 612.69 us | 13.72 ms | 1.04 ms | 1.20 ms | 1.27 ms | **594.83 us** | 3.62 ms | 4.11 ms | 431.39 ms |
| game-sm-success_1-4 | 566.12 us | 248.99 us | 204.43 us | 9.44 ms | 409.54 us | 440.79 us | 410.02 us | **184.01 us** | 1.40 ms | 1.51 ms | 130.00 ms |
| game-sm-success_2-1 | 1.36 ms | 574.77 us | 483.28 us | 10.53 ms | 787.57 us | 809.85 us | 820.52 us | **404.48 us** | 2.24 ms | 2.94 ms | 270.32 ms |
| game-sm-success_2-2 | 507.13 us | 224.53 us | 187.53 us | 8.10 ms | 362.01 us | 333.09 us | 338.26 us | **174.94 us** | 1.27 ms | 1.30 ms | 123.15 ms |
| game-sm-success_2-3 | 1.68 ms | 746.22 us | **580.65 us** | 15.19 ms | 1.14 ms | 1.18 ms | 1.37 ms | 597.91 us | 3.45 ms | 3.74 ms | 382.73 ms |
| game-sm-success_2-4 | 589.83 us | 241.73 us | 217.04 us | 10.38 ms | 452.96 us | 375.44 us | 391.20 us | **193.99 us** | 1.42 ms | 1.58 ms | 128.91 ms |
| game-sm-success_2-5 | 1.68 ms | 724.62 us | 645.44 us | 14.18 ms | 1.08 ms | 1.27 ms | 1.25 ms | **548.55 us** | 3.45 ms | 4.00 ms | 415.67 ms |
| game-sm-success_2-6 | 569.33 us | 260.55 us | 202.39 us | 9.35 ms | 379.92 us | 378.90 us | 419.58 us | **185.29 us** | 1.33 ms | 1.39 ms | 128.35 ms |
| guardrail-sorted-large | 760.06 us | 506.79 us | **369.36 us** | 57.72 ms | 606.86 us | 710.62 us | 757.50 us | 408.76 us | 3.76 ms | 2.83 ms | FAIL |
| guardrail-sorted-small | 305.62 us | 131.64 us | 100.39 us | 1.39 ms | 158.84 us | 189.22 us | 174.97 us | **94.38 us** | 714.00 us | 546.30 us | FAIL |
| guardrail-unsorted-large | 950.95 us | 660.18 us | **490.48 us** | 65.22 ms | 738.64 us | 944.63 us | 1.07 ms | 593.49 us | 5.58 ms | 3.58 ms | FAIL |
| guardrail-unsorted-small | 262.75 us | 125.31 us | 97.29 us | 1.45 ms | 155.68 us | 175.13 us | 172.56 us | **95.15 us** | 806.70 us | 551.90 us | FAIL |
| multisig-sm-01 | 1.67 ms | 551.58 us | 466.85 us | 11.96 ms | 807.45 us | 838.00 us | 945.00 us | **420.82 us** | 2.65 ms | 2.41 ms | FAIL |
| multisig-sm-02 | 1.46 ms | 575.96 us | 452.08 us | 11.27 ms | 821.89 us | 781.28 us | 838.50 us | **410.97 us** | 2.62 ms | 2.34 ms | FAIL |
| multisig-sm-03 | 1.50 ms | 578.53 us | 466.38 us | 10.59 ms | 873.77 us | 846.90 us | 835.93 us | **414.86 us** | 2.64 ms | 2.35 ms | FAIL |
| multisig-sm-04 | 1.49 ms | 561.67 us | 450.95 us | 10.58 ms | 845.11 us | 817.29 us | 1.00 ms | **417.57 us** | 2.43 ms | 2.38 ms | FAIL |
| multisig-sm-05 | 1.86 ms | 685.52 us | **568.78 us** | 12.61 ms | 1.04 ms | 1.11 ms | 1.22 ms | 592.27 us | 3.13 ms | 3.09 ms | FAIL |
| multisig-sm-06 | 1.46 ms | 562.41 us | 537.81 us | 11.58 ms | 815.14 us | 905.75 us | 891.61 us | **431.77 us** | 2.30 ms | 2.39 ms | FAIL |
| multisig-sm-07 | 1.66 ms | 576.65 us | 442.89 us | 10.64 ms | 797.98 us | 775.39 us | 833.60 us | **429.65 us** | 2.24 ms | 2.35 ms | FAIL |
| multisig-sm-08 | 1.49 ms | 571.84 us | 443.80 us | 11.11 ms | 827.79 us | 825.27 us | 827.15 us | **415.40 us** | 2.19 ms | 2.35 ms | FAIL |
| multisig-sm-09 | 1.78 ms | 580.85 us | 469.36 us | 11.61 ms | 843.24 us | 886.71 us | 921.42 us | **428.38 us** | 2.24 ms | 2.40 ms | FAIL |
| multisig-sm-10 | 1.71 ms | 690.93 us | 576.13 us | 12.32 ms | 1.13 ms | 1.16 ms | 1.21 ms | **558.49 us** | 3.01 ms | 3.40 ms | FAIL |
| ping-pong-1 | 1.21 ms | 499.54 us | **368.19 us** | 8.61 ms | 787.59 us | 763.14 us | 743.88 us | 395.57 us | 1.91 ms | 2.02 ms | 248.05 ms |
| ping-pong-2 | 1.32 ms | 467.72 us | 374.80 us | 9.39 ms | 686.00 us | 661.71 us | 707.87 us | **370.62 us** | 2.15 ms | 1.99 ms | 231.77 ms |
| ping-pong_2-1 | 1.08 ms | 400.30 us | 325.14 us | 7.30 ms | 516.82 us | 492.92 us | 504.15 us | **262.34 us** | 1.69 ms | 1.40 ms | 171.59 ms |
| prism-1 | 453.77 us | 204.85 us | 162.57 us | 7.39 ms | 311.08 us | 283.64 us | 306.73 us | **141.83 us** | 967.80 us | 975.00 us | 100.17 ms |
| prism-2 | 1.40 ms | 559.17 us | 435.14 us | 12.76 ms | 785.47 us | 850.74 us | 917.52 us | **402.12 us** | 2.36 ms | 2.34 ms | 290.57 ms |
| prism-3 | 871.74 us | 397.42 us | 328.25 us | 12.41 ms | 575.29 us | 724.26 us | 697.67 us | **318.65 us** | 1.87 ms | 1.96 ms | 248.29 ms |
| pubkey-1 | 431.55 us | 171.87 us | 157.22 us | 6.52 ms | 269.35 us | 256.92 us | 257.28 us | **137.03 us** | 822.50 us | 850.50 us | 94.05 ms |
| stablecoin_1-1 | 3.15 ms | 1.19 ms | 1.02 ms | 294.70 ms | 1.95 ms | 2.10 ms | 1.99 ms | **814.88 us** | 6.52 ms | 10.05 ms | FAIL |
| stablecoin_1-2 | 513.14 us | 214.15 us | 183.28 us | 8.82 ms | 387.65 us | 325.88 us | 331.48 us | **165.38 us** | 1.15 ms | 1.14 ms | 148.24 ms |
| stablecoin_1-3 | 3.28 ms | 1.29 ms | 1.25 ms | 305.07 ms | 1.99 ms | 2.12 ms | 2.26 ms | **831.95 us** | 7.21 ms | 10.85 ms | FAIL |
| stablecoin_1-4 | 512.81 us | 225.54 us | 201.13 us | 10.15 ms | 384.00 us | 346.23 us | 381.91 us | **179.11 us** | 1.15 ms | 1.26 ms | 119.48 ms |
| stablecoin_1-5 | 3.37 ms | 1.49 ms | 1.35 ms | 289.30 ms | 2.40 ms | 2.74 ms | 2.66 ms | **1.04 ms** | 8.63 ms | 12.63 ms | FAIL |
| stablecoin_1-6 | 620.50 us | 252.06 us | 218.75 us | 12.76 ms | 407.05 us | 436.10 us | 477.69 us | **210.75 us** | 1.35 ms | 1.56 ms | 142.90 ms |
| stablecoin_2-1 | 2.84 ms | 1.16 ms | 1.07 ms | 313.68 ms | 1.74 ms | 1.84 ms | 1.90 ms | **867.34 us** | 6.50 ms | 9.60 ms | FAIL |
| stablecoin_2-2 | 513.70 us | 225.00 us | 194.56 us | 8.89 ms | 387.58 us | 355.37 us | 336.19 us | **162.92 us** | 1.11 ms | 1.12 ms | 118.64 ms |
| stablecoin_2-3 | 3.06 ms | 1.23 ms | 1.10 ms | 289.31 ms | 2.10 ms | 2.17 ms | 2.30 ms | **874.32 us** | 6.91 ms | 10.40 ms | FAIL |
| stablecoin_2-4 | 557.29 us | 232.56 us | 195.03 us | 10.92 ms | 397.18 us | 399.88 us | 432.49 us | **170.66 us** | 1.19 ms | 1.19 ms | 119.21 ms |
| token-account-1 | 583.33 us | 256.25 us | 233.46 us | 6.14 ms | 404.99 us | 382.90 us | 419.22 us | **193.99 us** | 1.07 ms | 1.11 ms | 125.93 ms |
| token-account-2 | 789.85 us | 364.84 us | 278.47 us | 9.19 ms | 516.30 us | 649.87 us | 615.50 us | **278.05 us** | 1.69 ms | 1.71 ms | 198.66 ms |
| uniswap-1 | 863.86 us | 408.33 us | **330.43 us** | 9.61 ms | 604.05 us | 768.94 us | 803.73 us | 361.28 us | 2.04 ms | 2.06 ms | 262.37 ms |
| uniswap-2 | 694.44 us | 301.12 us | 249.20 us | 8.56 ms | 408.10 us | 458.78 us | 524.08 us | **213.38 us** | 1.28 ms | 1.28 ms | 165.88 ms |
| uniswap-3 | 3.56 ms | 1.63 ms | **1.31 ms** | 32.21 ms | 2.72 ms | 2.88 ms | 3.04 ms | 1.41 ms | 8.71 ms | 9.08 ms | 874.73 ms |
| uniswap-4 | 681.65 us | 332.60 us | 277.06 us | 17.31 ms | 514.18 us | 561.52 us | 580.25 us | **255.22 us** | 1.93 ms | 1.81 ms | 176.05 ms |
| uniswap-5 | 3.11 ms | 1.18 ms | 998.19 us | 29.80 ms | 1.76 ms | 2.16 ms | 2.31 ms | **930.70 us** | 6.39 ms | 6.25 ms | 684.86 ms |
| uniswap-6 | 651.80 us | 317.80 us | 288.65 us | 15.52 ms | 542.95 us | 521.00 us | 535.43 us | **256.45 us** | 1.85 ms | 1.75 ms | 178.25 ms |
| vesting-1 | 1.01 ms | 439.52 us | **341.50 us** | 8.84 ms | 604.57 us | 685.01 us | 680.82 us | 361.16 us | 1.86 ms | 1.85 ms | 215.95 ms |

## Eval tier: evaluate a decoded program

The program is decoded before timing; each iteration evaluates it. JIT VMs compile before timing too.

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

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
| auction_1-1 | 183.56 us | **44.52 us** | 121.69 us | 283.88 us | 67.49 us | 128.47 us | 6.63 ms | 215.04 us | 212.59 us | 231.39 us | 113.78 us | 799.60 us | 850.10 us | 92.33 ms |
| auction_1-2 | 623.76 us | 1.12 ms | 450.41 us | 835.24 us | **285.84 us** | 463.24 us | 11.54 ms | 747.63 us | 917.07 us | 1.01 ms | 416.60 us | 2.78 ms | 2.62 ms | 348.32 ms |
| auction_1-3 | 560.42 us | 708.53 us | 479.14 us | 874.47 us | **276.30 us** | 421.50 us | 12.30 ms | 749.86 us | 890.63 us | 958.62 us | 411.58 us | 2.86 ms | 2.62 ms | 392.39 ms |
| auction_1-4 | 238.15 us | **53.44 us** | 149.93 us | 334.42 us | 95.51 us | 151.55 us | 8.90 ms | 291.29 us | 275.58 us | 324.74 us | 128.03 us | 1.13 ms | 1.17 ms | 119.24 ms |
| auction_2-1 | 168.59 us | **45.14 us** | 122.83 us | 270.40 us | 73.76 us | 116.21 us | 6.64 ms | 225.28 us | 254.45 us | 242.28 us | 101.50 us | 906.90 us | 872.90 us | 91.79 ms |
| auction_2-2 | 593.31 us | 1.06 ms | 474.67 us | 850.73 us | **308.18 us** | 480.26 us | 12.21 ms | 845.24 us | 893.53 us | 962.05 us | 460.95 us | 2.84 ms | 2.80 ms | 336.09 ms |
| auction_2-3 | 778.13 us | 1.08 ms | 603.07 us | 1.12 ms | **342.34 us** | 569.67 us | 14.63 ms | 1.01 ms | 1.26 ms | 1.34 ms | 570.79 us | 4.17 ms | 3.81 ms | 463.38 ms |
| auction_2-4 | 560.20 us | 711.55 us | 443.38 us | 873.92 us | **283.54 us** | 421.18 us | 11.91 ms | 776.97 us | 864.59 us | 955.02 us | 405.20 us | 2.83 ms | 2.88 ms | 372.71 ms |
| auction_2-5 | 223.49 us | **51.66 us** | 158.60 us | 334.06 us | 89.46 us | 153.41 us | 8.96 ms | 288.25 us | 276.98 us | 311.23 us | 128.22 us | 1.20 ms | 1.22 ms | 133.35 ms |
| coop-1 | 219.62 us | **43.34 us** | 199.12 us | FAIL | 94.77 us | 124.01 us | 10.55 ms | 293.42 us | 294.40 us | 308.28 us | 135.76 us | 1.59 ms | 1.41 ms | FAIL |
| coop-2 | 715.00 us | **157.87 us** | 636.85 us | FAIL | 289.51 us | 374.27 us | 30.69 ms | 794.70 us | 866.84 us | 893.98 us | 480.08 us | 4.87 ms | 4.13 ms | FAIL |
| coop-3 | 2.06 ms | **688.01 us** | 2.10 ms | FAIL | 993.35 us | 1.20 ms | 36.71 ms | 2.45 ms | 3.01 ms | 3.36 ms | 1.65 ms | 16.67 ms | 11.10 ms | FAIL |
| coop-4 | 1.05 ms | **271.66 us** | 777.43 us | FAIL | 388.34 us | 549.98 us | 29.73 ms | 1.07 ms | 1.14 ms | 1.18 ms | 637.37 us | 6.25 ms | 4.82 ms | FAIL |
| coop-5 | 387.47 us | **89.33 us** | 355.20 us | FAIL | 167.32 us | 219.26 us | 14.53 ms | 477.70 us | 462.24 us | 490.01 us | 235.44 us | 3.43 ms | 2.29 ms | FAIL |
| coop-6 | 699.41 us | **143.68 us** | 570.65 us | FAIL | 270.82 us | 341.55 us | 28.60 ms | 811.07 us | 908.84 us | 852.66 us | 408.33 us | 4.41 ms | 3.59 ms | FAIL |
| coop-7 | 317.22 us | **58.88 us** | 276.26 us | FAIL | 147.82 us | 178.60 us | 15.11 ms | 403.25 us | 367.52 us | 405.12 us | 192.28 us | 2.18 ms | 1.79 ms | FAIL |
| crowdfunding-success-1 | 196.40 us | **42.55 us** | 148.47 us | 299.65 us | 93.30 us | 126.03 us | 8.08 ms | 238.38 us | 254.62 us | 254.67 us | 129.98 us | 1.11 ms | 1.04 ms | 113.64 ms |
| crowdfunding-success-2 | 207.79 us | **43.08 us** | 141.22 us | 319.46 us | 84.53 us | 124.99 us | 7.93 ms | 240.67 us | 267.52 us | 269.05 us | 123.99 us | 1.08 ms | 980.70 us | 111.88 ms |
| crowdfunding-success-3 | 202.14 us | **47.24 us** | 136.75 us | 310.22 us | 92.73 us | 123.78 us | 8.04 ms | 251.19 us | 249.82 us | 273.09 us | 132.94 us | 1.04 ms | 1.05 ms | 109.74 ms |
| currency-1 | 239.64 us | **74.70 us** | 182.80 us | 369.52 us | 113.15 us | 181.97 us | 6.31 ms | 327.96 us | 340.35 us | 366.90 us | 161.41 us | 1.20 ms | 1.24 ms | 136.95 ms |
| escrow-redeem_1-1 | 321.82 us | **96.32 us** | 255.11 us | 467.73 us | 151.45 us | 233.91 us | 9.99 ms | 459.55 us | 503.26 us | 524.54 us | 217.30 us | 1.67 ms | 1.58 ms | 180.44 ms |
| escrow-redeem_1-2 | 332.15 us | **93.14 us** | 242.37 us | 477.65 us | 174.00 us | 216.71 us | 9.74 ms | 388.22 us | 452.15 us | 579.20 us | 233.13 us | 1.66 ms | 1.56 ms | 203.06 ms |
| escrow-redeem_2-1 | 367.76 us | **103.24 us** | 302.31 us | 545.02 us | 176.59 us | 247.62 us | 10.58 ms | 450.95 us | 539.87 us | 562.77 us | 258.28 us | 1.99 ms | 1.84 ms | 213.86 ms |
| escrow-redeem_2-2 | 419.01 us | **125.17 us** | 289.56 us | 540.46 us | 168.18 us | 278.16 us | 10.27 ms | 448.53 us | 561.51 us | 619.68 us | 264.36 us | 1.70 ms | 1.71 ms | 222.35 ms |
| escrow-redeem_2-3 | 371.52 us | **99.11 us** | 302.67 us | 545.60 us | 176.63 us | 246.78 us | 10.39 ms | 454.88 us | 555.85 us | 564.28 us | 282.29 us | 2.08 ms | 1.72 ms | 228.32 ms |
| escrow-refund-1 | 170.28 us | **35.53 us** | 103.71 us | 254.75 us | 65.57 us | 110.17 us | 5.96 ms | 206.35 us | 209.31 us | 197.99 us | 95.37 us | 793.10 us | 696.20 us | 92.36 ms |
| future-increase-margin-1 | 228.65 us | **62.95 us** | 185.62 us | 360.71 us | 106.02 us | 162.29 us | 6.20 ms | 325.65 us | 353.11 us | 411.65 us | 167.00 us | 1.07 ms | 1.07 ms | 138.10 ms |
| future-increase-margin-2 | 484.17 us | **192.71 us** | 394.75 us | 674.03 us | 233.30 us | 362.90 us | 14.40 ms | 599.46 us | 706.95 us | 799.59 us | 331.37 us | 2.20 ms | 2.22 ms | 280.19 ms |
| future-increase-margin-3 | 492.01 us | **195.15 us** | 386.60 us | 712.25 us | 224.92 us | 378.82 us | 14.33 ms | 590.86 us | 793.84 us | 770.82 us | 330.25 us | 2.11 ms | 2.23 ms | 302.70 ms |
| future-increase-margin-4 | 446.60 us | 639.73 us | 342.73 us | 731.67 us | **220.14 us** | 344.52 us | 9.90 ms | 615.62 us | 654.82 us | 761.76 us | 320.42 us | 1.97 ms | 2.04 ms | FAIL |
| future-increase-margin-5 | 778.24 us | 1.69 ms | 603.36 us | 1.35 ms | **431.86 us** | 622.19 us | 148.74 ms | 1.26 ms | 1.24 ms | 1.28 ms | 517.37 us | 4.07 ms | 6.04 ms | FAIL |
| future-pay-out-1 | 227.91 us | **67.21 us** | 188.00 us | 352.19 us | 114.02 us | 161.33 us | 6.12 ms | 332.29 us | 392.71 us | 376.87 us | 173.50 us | 1.04 ms | 1.09 ms | 135.39 ms |
| future-pay-out-2 | 489.51 us | **165.11 us** | 371.06 us | 722.02 us | 225.18 us | 341.04 us | 12.60 ms | 664.52 us | 704.19 us | 848.22 us | 365.90 us | 2.32 ms | 2.40 ms | 278.55 ms |
| future-pay-out-3 | 476.10 us | **199.54 us** | 389.86 us | 696.60 us | 252.68 us | 329.89 us | 13.33 ms | 592.44 us | 730.19 us | 776.14 us | 335.49 us | 2.22 ms | 2.31 ms | 330.54 ms |
| future-pay-out-4 | 792.00 us | 1.65 ms | 608.10 us | 1.33 ms | **383.51 us** | 668.98 us | 156.03 ms | 1.15 ms | 1.22 ms | 1.27 ms | 493.37 us | 4.04 ms | 5.56 ms | FAIL |
| future-settle-early-1 | 224.34 us | **74.28 us** | 184.18 us | 347.11 us | 119.79 us | 162.03 us | 5.83 ms | 304.47 us | 341.77 us | 397.42 us | 162.76 us | 1.06 ms | 1.16 ms | 156.12 ms |
| future-settle-early-2 | 569.96 us | **137.92 us** | 381.11 us | 720.22 us | 229.94 us | 331.74 us | 12.61 ms | 604.71 us | 832.77 us | 892.37 us | 365.66 us | 2.22 ms | 2.25 ms | 297.72 ms |
| future-settle-early-3 | 500.19 us | **158.16 us** | 380.38 us | 684.38 us | 236.06 us | 363.30 us | 12.63 ms | 636.08 us | 712.12 us | 793.96 us | 407.28 us | 2.24 ms | 2.24 ms | 280.24 ms |
| future-settle-early-4 | 626.10 us | 1.33 ms | 486.11 us | 1.02 ms | **335.64 us** | 433.52 us | 147.19 ms | 851.66 us | 870.18 us | 1.05 ms | 377.34 us | 3.44 ms | 4.52 ms | FAIL |
| game-sm-success_1-1 | 370.68 us | 389.68 us | 283.82 us | 577.97 us | **186.10 us** | 253.84 us | 10.24 ms | 473.00 us | 501.06 us | 539.07 us | 250.47 us | 1.65 ms | 1.62 ms | 208.88 ms |
| game-sm-success_1-2 | 196.82 us | **41.59 us** | 134.92 us | 288.12 us | 84.97 us | 127.60 us | 8.65 ms | 241.37 us | 242.10 us | 249.15 us | 111.40 us | 860.10 us | 927.90 us | 97.94 ms |
| game-sm-success_1-3 | 581.43 us | 640.21 us | 457.79 us | 856.47 us | **295.84 us** | 471.00 us | 12.86 ms | 770.93 us | 947.57 us | 1.05 ms | 409.51 us | 2.36 ms | 2.62 ms | 369.85 ms |
| game-sm-success_1-4 | 218.99 us | **43.98 us** | 161.94 us | 325.91 us | 97.33 us | 142.66 us | 8.66 ms | 279.55 us | 277.42 us | 288.03 us | 140.49 us | 928.50 us | 1.11 ms | 128.11 ms |
| game-sm-success_2-1 | 388.48 us | 315.60 us | 274.69 us | 567.18 us | **175.13 us** | 281.50 us | 8.89 ms | 513.14 us | 572.87 us | 541.67 us | 277.84 us | 1.47 ms | 1.62 ms | 215.96 ms |
| game-sm-success_2-2 | 180.16 us | **40.81 us** | 141.16 us | 295.36 us | 94.08 us | 129.47 us | 7.39 ms | 264.66 us | 269.50 us | 313.27 us | 113.85 us | 812.30 us | 935.90 us | 107.12 ms |
| game-sm-success_2-3 | 613.22 us | 742.71 us | 456.81 us | 872.81 us | **276.80 us** | 428.42 us | 12.76 ms | 744.72 us | 895.76 us | 993.03 us | 409.50 us | 2.42 ms | 2.81 ms | 334.56 ms |
| game-sm-success_2-4 | 208.24 us | **44.52 us** | 157.84 us | 320.71 us | 98.99 us | 155.47 us | 8.61 ms | 308.66 us | 285.51 us | 285.76 us | 129.24 us | 967.80 us | 1.11 ms | 115.28 ms |
| game-sm-success_2-5 | 590.55 us | 665.51 us | 453.44 us | 888.47 us | **274.93 us** | 421.75 us | 12.95 ms | 729.55 us | 873.56 us | 1.04 ms | 429.71 us | 2.53 ms | 2.94 ms | 343.04 ms |
| game-sm-success_2-6 | 216.66 us | **44.85 us** | 155.69 us | 328.28 us | 94.32 us | 168.25 us | 9.42 ms | 271.94 us | 277.33 us | 289.77 us | 137.97 us | 970.10 us | 1.42 ms | 116.45 ms |
| guardrail-sorted-large | 473.00 us | **250.06 us** | 413.99 us | FAIL | 320.52 us | 253.57 us | 54.15 ms | 449.88 us | 576.85 us | 613.01 us | 307.88 us | 2.53 ms | 2.57 ms | FAIL |
| guardrail-sorted-small | 72.14 us | 90.98 us | 80.75 us | FAIL | **29.67 us** | 47.10 us | 868.96 us | 96.20 us | 83.36 us | 106.83 us | 48.98 us | 595.20 us | 405.40 us | FAIL |
| guardrail-unsorted-large | 618.31 us | **298.70 us** | 555.23 us | FAIL | 386.74 us | 331.87 us | 57.35 ms | 698.76 us | 830.81 us | 858.60 us | 394.47 us | 4.83 ms | 3.13 ms | FAIL |
| guardrail-unsorted-small | 67.95 us | 88.73 us | 77.64 us | FAIL | **25.69 us** | 48.37 us | 877.42 us | 79.68 us | 94.67 us | 90.60 us | 45.99 us | 531.00 us | 353.40 us | FAIL |
| multisig-sm-01 | 398.80 us | 470.74 us | 302.49 us | 579.20 us | **187.36 us** | 274.81 us | 9.40 ms | 508.92 us | 540.77 us | 602.45 us | 300.29 us | 2.07 ms | 1.72 ms | FAIL |
| multisig-sm-02 | 369.68 us | 528.25 us | 272.83 us | 587.26 us | **179.35 us** | 265.93 us | 9.62 ms | 462.87 us | 507.25 us | 609.20 us | 260.19 us | 1.99 ms | 1.70 ms | FAIL |
| multisig-sm-03 | 369.55 us | 554.30 us | 298.24 us | 577.03 us | **179.00 us** | 275.33 us | 10.06 ms | 471.10 us | 582.60 us | 598.92 us | 280.91 us | 2.02 ms | 1.70 ms | FAIL |
| multisig-sm-04 | 393.30 us | 548.54 us | 294.61 us | 605.18 us | **195.31 us** | 295.77 us | 9.05 ms | 521.32 us | 572.91 us | 602.72 us | 281.00 us | 2.03 ms | 1.70 ms | FAIL |
| multisig-sm-05 | 507.51 us | 932.18 us | 408.50 us | 756.74 us | **248.77 us** | 399.42 us | 10.04 ms | 750.17 us | 820.32 us | 841.16 us | 377.83 us | 2.68 ms | 2.43 ms | FAIL |
| multisig-sm-06 | 374.65 us | 406.06 us | 288.69 us | 614.50 us | **188.37 us** | 283.65 us | 9.31 ms | 473.07 us | 536.86 us | 625.74 us | 286.08 us | 1.91 ms | 1.68 ms | FAIL |
| multisig-sm-07 | 367.04 us | 568.58 us | 273.05 us | 586.05 us | **177.74 us** | 281.22 us | 8.68 ms | 474.70 us | 505.96 us | 561.15 us | 263.03 us | 1.79 ms | 1.69 ms | FAIL |
| multisig-sm-08 | 400.20 us | 574.49 us | 299.31 us | 592.88 us | **184.11 us** | 282.04 us | 8.62 ms | 466.20 us | 536.24 us | 566.36 us | 273.03 us | 1.90 ms | 1.75 ms | FAIL |
| multisig-sm-09 | 386.13 us | 631.19 us | 291.24 us | 581.91 us | **200.72 us** | 283.75 us | 8.73 ms | 544.20 us | 607.65 us | 619.00 us | 296.28 us | 1.90 ms | 1.71 ms | FAIL |
| multisig-sm-10 | 544.35 us | 997.32 us | 413.90 us | 820.75 us | **252.08 us** | 399.98 us | 11.17 ms | 669.53 us | 808.81 us | 848.40 us | 408.08 us | 2.75 ms | 2.49 ms | FAIL |
| ping-pong-1 | 314.03 us | 238.80 us | 244.77 us | 483.23 us | **159.75 us** | 220.39 us | 7.67 ms | 395.12 us | 469.06 us | 484.84 us | 227.09 us | 1.61 ms | 1.43 ms | 215.45 ms |
| ping-pong-2 | 324.57 us | 292.75 us | 253.15 us | 476.03 us | **149.10 us** | 228.59 us | 7.27 ms | 397.01 us | 429.39 us | 532.60 us | 216.03 us | 1.72 ms | 1.50 ms | 218.10 ms |
| ping-pong_2-1 | 191.49 us | **84.35 us** | 143.47 us | 339.85 us | 92.51 us | 142.01 us | 6.08 ms | 238.80 us | 270.66 us | 277.78 us | 127.24 us | 1.05 ms | 997.50 us | 129.44 ms |
| prism-1 | 160.14 us | **31.23 us** | 128.27 us | 246.15 us | 64.79 us | 117.14 us | 6.13 ms | 234.91 us | 215.18 us | 222.44 us | 93.17 us | 896.20 us | 852.70 us | 84.40 ms |
| prism-2 | 404.40 us | 452.19 us | 310.45 us | 624.66 us | **182.29 us** | 271.39 us | 9.90 ms | 565.35 us | 547.25 us | 606.45 us | 276.61 us | 1.81 ms | 2.01 ms | 226.93 ms |
| prism-3 | 335.13 us | **97.76 us** | 265.10 us | 504.80 us | 152.71 us | 255.66 us | 10.09 ms | 481.79 us | 525.29 us | 524.82 us | 257.34 us | 1.88 ms | 1.75 ms | 189.07 ms |
| pubkey-1 | 133.58 us | **26.86 us** | 104.11 us | 217.07 us | 61.64 us | 99.62 us | 5.84 ms | 171.45 us | 185.53 us | 184.40 us | 80.58 us | 649.20 us | 760.60 us | 71.65 ms |
| stablecoin_1-1 | 879.40 us | 2.55 ms | 737.25 us | 1.73 ms | **476.19 us** | 731.04 us | 302.96 ms | 1.29 ms | 1.48 ms | 1.41 ms | 539.03 us | 5.78 ms | 9.64 ms | FAIL |
| stablecoin_1-2 | 193.89 us | **39.00 us** | 134.70 us | 289.79 us | 82.70 us | 129.31 us | 8.02 ms | 232.75 us | 239.03 us | 242.08 us | 109.44 us | 930.10 us | 1.06 ms | 96.21 ms |
| stablecoin_1-3 | 998.43 us | 2.63 ms | 840.93 us | 1.91 ms | **475.19 us** | 1.01 ms | 289.80 ms | 1.56 ms | 1.71 ms | 1.89 ms | 643.57 us | 6.36 ms | 10.79 ms | FAIL |
| stablecoin_1-4 | 202.96 us | **41.98 us** | 141.76 us | 312.10 us | 91.59 us | 136.08 us | 9.89 ms | 248.42 us | 252.21 us | 257.57 us | 123.84 us | 1.05 ms | 1.12 ms | 102.93 ms |
| stablecoin_1-5 | 1.25 ms | 2.95 ms | 1.03 ms | 2.35 ms | **549.63 us** | 1.11 ms | 286.75 ms | 2.14 ms | 2.18 ms | 2.22 ms | 981.64 us | 8.15 ms | 12.59 ms | FAIL |
| stablecoin_1-6 | 274.95 us | **51.28 us** | 183.29 us | 369.69 us | 111.54 us | 159.20 us | 10.35 ms | 313.46 us | 319.40 us | 327.87 us | 147.03 us | 1.31 ms | 1.32 ms | 127.67 ms |
| stablecoin_2-1 | 869.63 us | 2.68 ms | 732.96 us | 1.73 ms | **459.27 us** | 775.85 us | 306.49 ms | 1.26 ms | 1.39 ms | 1.44 ms | 539.83 us | 6.20 ms | 9.82 ms | FAIL |
| stablecoin_2-2 | 183.32 us | **40.61 us** | 134.05 us | 284.14 us | 92.19 us | 125.54 us | 8.88 ms | 230.20 us | 260.01 us | 275.60 us | 109.03 us | 1.12 ms | 1.00 ms | 113.98 ms |
| stablecoin_2-3 | 1.09 ms | 2.68 ms | 880.97 us | 2.01 ms | **511.45 us** | 918.16 us | 284.10 ms | 1.56 ms | 1.62 ms | 1.64 ms | 646.89 us | 6.88 ms | 9.48 ms | FAIL |
| stablecoin_2-4 | 190.05 us | **41.89 us** | 137.72 us | 299.25 us | 88.19 us | 158.14 us | 8.66 ms | 245.32 us | 258.50 us | 258.45 us | 125.19 us | 892.50 us | 1.02 ms | 119.52 ms |
| token-account-1 | 172.61 us | **55.67 us** | 140.77 us | 289.32 us | 84.08 us | 124.98 us | 5.48 ms | 226.94 us | 296.18 us | 300.01 us | 126.58 us | 790.00 us | 865.20 us | 110.02 ms |
| token-account-2 | 312.87 us | **71.51 us** | 240.43 us | 455.70 us | 148.93 us | 223.19 us | 8.69 ms | 421.62 us | 458.62 us | 512.59 us | 220.68 us | 1.37 ms | 1.52 ms | 176.37 ms |
| uniswap-1 | 372.17 us | **92.31 us** | 306.50 us | 524.13 us | 193.33 us | 258.22 us | 9.23 ms | 515.37 us | 583.12 us | 646.36 us | 263.39 us | 1.64 ms | 1.74 ms | 233.36 ms |
| uniswap-2 | 200.07 us | **56.19 us** | 162.92 us | 326.99 us | 95.53 us | 159.25 us | 7.50 ms | 275.76 us | 318.84 us | 354.15 us | 137.74 us | 913.70 us | 1.00 ms | 124.60 ms |
| uniswap-3 | 1.70 ms | 1.13 ms | 1.25 ms | 2.33 ms | **656.85 us** | 1.16 ms | 27.98 ms | 2.18 ms | 2.47 ms | 2.57 ms | 1.11 ms | 7.15 ms | 7.39 ms | 865.11 ms |
| uniswap-4 | 308.19 us | **62.00 us** | 225.81 us | 459.05 us | 130.01 us | 206.98 us | 14.43 ms | 406.65 us | 402.13 us | 415.72 us | 203.85 us | 1.41 ms | 1.55 ms | 187.63 ms |
| uniswap-5 | 1.14 ms | 748.49 us | 857.46 us | 1.50 ms | **449.22 us** | 762.12 us | 23.82 ms | 1.27 ms | 1.43 ms | 1.67 ms | 785.37 us | 4.78 ms | 4.94 ms | 554.86 ms |
| uniswap-6 | 287.80 us | **59.17 us** | 219.73 us | 448.72 us | 128.74 us | 217.26 us | 15.06 ms | 379.06 us | 413.32 us | 411.25 us | 205.06 us | 1.40 ms | 1.49 ms | 153.39 ms |
| vesting-1 | 332.19 us | 216.97 us | 254.88 us | 492.41 us | **155.68 us** | 219.56 us | 7.94 ms | 431.68 us | 452.34 us | 516.88 us | 231.10 us | 1.43 ms | 1.43 ms | 186.83 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*