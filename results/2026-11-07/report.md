# Cardano Plutus VM Benchmark Results

**Date:** 2026-11-07

## Environment
```
date: 2026-11-07T09:17:28+00:00
kernel: 6.8.0-147-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
```

## VM Versions

| VM | Source revision | Toolchain |
|---|---|---|
| plutus-core CEK (Haskell / GHC) | 1.72.0.0 ([152220a](https://github.com/IntersectMBO/plutus/commit/152220ae3da8cd6ceaf2688094af541ac1245f58)) | GHC 9.6.4 |
| Scalus UPLC→JVM JIT (Scala / JVM) | v1.5.0 ([5bf331b](https://github.com/scalus3/scalus/commit/5bf331bc5f0a4e5100bf5ea033468ed771d71ea9)) | JDK 21 / Scala 3 |
| Scalus CEK (Scala / JVM) | v1.5.0 ([5bf331b](https://github.com/scalus3/scalus/commit/5bf331bc5f0a4e5100bf5ea033468ed771d71ea9)) | JDK 21 / Scala 3 |
| Julc CEK (Java / GraalVM) | v0.1.0-pre20 ([b5ff39a](https://github.com/bloxbean/julc/commit/b5ff39a84150ff9d53ba431a7f45d31a5a366d1f)) | GraalVM 25.0.2-graal |
| llvm-uplc post-JIT execution (C++ / LLVM) | commit:6bcef67 ([6bcef67](https://github.com/SeungheonOh/llvm-uplc/commit/6bcef67ce1995d232327f13d9080fe2f0261a55c)) | LLVM 22.1.0 |
| Amaru UPLC CEK (Rust) | [0.6.0](https://crates.io/crates/amaru-uplc/0.6.0) | rustc nightly-2026-09-04 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | [3.0.5](https://www.npmjs.com/package/@harmoniclabs/plutus-machine/v/3.0.5) | Node.js 22 |
| Plutuz CEK (Zig) | commit:33b812d ([33b812d](https://github.com/utxo-company/plutuz/commit/33b812dbcf88f6851286e54cb93a4a443353f94c)) | Zig 0.15.2 |
| Chrysalis CEK (C# / .NET) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Chrysalis CEK (C# / .NET AOT) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Plutigo CEK (Go) | v0.11.4 ([3edb481](https://github.com/blinklabs-io/plutigo/commit/3edb481b4b8acd235c14a43146b5ac085a009d86)) | Go 1.27.3 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 0.5.3 ([320fc36](https://github.com/butaneprotocol/blaze-cardano/commit/320fc3604cfeac640013fd8206efaecfe8a2360f)) | Bun 1.3.14 |
| blaze-plutus CEK (TypeScript / Node V8) | 0.5.3 ([320fc36](https://github.com/butaneprotocol/blaze-cardano/commit/320fc3604cfeac640013fd8206efaecfe8a2360f)) | Node.js 22 |
| opshin CEK (Python / CPython) | 1.3.3 ([eda2fba](https://github.com/OpShin/uplc/commit/eda2fbaa89c1a2db4ec6c6c1fa5eea2a8b2671d4)) | Python 3.14 |

## Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

*Measurement caveats: llvm-uplc reports steady-state execution after JIT compilation; its per-script compilation time is retained only in the raw JSON. Scalus JIT and Chrysalis use three measurement samples, and their raw framework output should be consulted for uncertainty.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 169.64 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 342.91 us | 2.02x |
| **Plutigo CEK (Go)** | Go | 368.03 us | 2.17x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 387.76 us | 2.29x |
| **Amaru UPLC CEK (Rust)** | Rust | 388.78 us | 2.29x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 480.91 us | 2.83x |
| **Plutuz CEK (Zig)** | Zig | 682.81 us | 4.03x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 766.45 us | 4.52x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 792.41 us | 4.67x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 883.41 us | 5.21x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.46 ms | 14.50x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.47 ms | 14.57x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 20.50 ms | 120.83x |
| **opshin CEK (Python / CPython)** | Python / CPython | 118.18 ms | 696.65x |

### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| llvm-uplc post-JIT execution (C++ / LLVM) | 89 | 0 | 0 | 89 |
| Scalus UPLC→JVM JIT (Scala / JVM) | 89 | 0 | 0 | 89 |
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
| plutus-core CEK (Haskell / GHC) | 89 | 0 | 0 | 89 |
| Amaru UPLC CEK (Rust) | 89 | 0 | 0 | 89 |
| Scalus CEK (Scala / JVM) | 89 | 0 | 0 | 89 |
| Plutuz CEK (Zig) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET AOT) | 89 | 0 | 0 | 89 |
| Julc CEK (Java / GraalVM) | 78 | 11 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

## Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc post-JIT execution (C++ / LLVM) | Amaru UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 180.14 us | 90.11 us | 231.08 us | 278.29 us | **69.89 us** | 193.53 us | 9.69 ms | 341.12 us | 365.95 us | 362.30 us | 178.91 us | 1.16 ms | 1.15 ms | 115.45 ms |
| auction_1-2 | 605.93 us | 1.66 ms | 763.49 us | 885.22 us | **285.82 us** | 640.28 us | 22.00 ms | 1.12 ms | 1.28 ms | 1.40 ms | 606.13 us | 3.47 ms | 3.42 ms | 406.33 ms |
| auction_1-3 | 606.27 us | 1.60 ms | 758.78 us | 883.48 us | **285.23 us** | 628.36 us | 22.57 ms | 1.06 ms | 1.24 ms | 1.35 ms | 587.62 us | 3.45 ms | 3.44 ms | 408.65 ms |
| auction_1-4 | 232.64 us | **72.63 us** | 265.66 us | 347.25 us | 91.97 us | 230.73 us | 12.68 ms | 409.28 us | 411.82 us | 457.21 us | 210.72 us | 1.37 ms | 1.37 ms | 136.82 ms |
| auction_2-1 | 176.33 us | 82.33 us | 230.18 us | 281.56 us | **75.10 us** | 194.34 us | 9.50 ms | 346.25 us | 349.83 us | 361.56 us | 176.11 us | 1.09 ms | 1.10 ms | 115.50 ms |
| auction_2-2 | 606.43 us | 1.69 ms | 761.64 us | 887.64 us | **286.34 us** | 641.98 us | 22.38 ms | 1.13 ms | 1.23 ms | 1.36 ms | 605.41 us | 3.45 ms | 3.41 ms | 405.26 ms |
| auction_2-3 | 787.14 us | 1.45 ms | 924.46 us | 1.11 ms | **351.25 us** | 781.57 us | 27.72 ms | 1.33 ms | 1.56 ms | 1.70 ms | 716.05 us | 4.35 ms | 4.33 ms | 516.21 ms |
| auction_2-4 | 612.04 us | 1.51 ms | 760.15 us | 874.76 us | **273.46 us** | 636.20 us | 22.42 ms | 1.08 ms | 1.26 ms | 1.32 ms | 588.99 us | 3.46 ms | 3.42 ms | 411.35 ms |
| auction_2-5 | 231.83 us | **75.78 us** | 273.08 us | 343.78 us | 90.69 us | 222.70 us | 12.83 ms | 421.60 us | 417.48 us | 445.72 us | 205.55 us | 1.39 ms | 1.37 ms | 140.73 ms |
| coop-1 | 236.25 us | **52.41 us** | 268.07 us | FAIL | 97.81 us | 176.58 us | 13.54 ms | 343.52 us | 359.99 us | 403.79 us | 196.91 us | 1.52 ms | 1.53 ms | FAIL |
| coop-2 | 762.24 us | **213.18 us** | 831.23 us | FAIL | 308.66 us | 522.35 us | 41.42 ms | 1.02 ms | 1.24 ms | 1.27 ms | 619.63 us | 4.83 ms | 4.88 ms | FAIL |
| coop-3 | 2.18 ms | **858.90 us** | 2.28 ms | FAIL | 976.50 us | 1.41 ms | 67.73 ms | 2.70 ms | 4.08 ms | 3.98 ms | 1.67 ms | 11.91 ms | 11.79 ms | FAIL |
| coop-4 | 992.28 us | **369.53 us** | 998.10 us | FAIL | 403.33 us | 679.35 us | 39.76 ms | 1.26 ms | 1.50 ms | 1.60 ms | 756.80 us | 6.21 ms | 5.65 ms | FAIL |
| coop-5 | 413.68 us | **124.42 us** | 505.43 us | FAIL | 174.56 us | 352.04 us | 20.85 ms | 633.24 us | 736.34 us | 754.25 us | 388.25 us | 2.72 ms | 2.63 ms | FAIL |
| coop-6 | 688.65 us | **189.50 us** | 737.21 us | FAIL | 270.96 us | 463.94 us | 38.94 ms | 891.49 us | 1.05 ms | 1.07 ms | 545.12 us | 4.49 ms | 4.18 ms | FAIL |
| coop-7 | 327.72 us | **67.67 us** | 359.83 us | FAIL | 131.45 us | 237.91 us | 19.74 ms | 458.97 us | 519.60 us | 535.70 us | 271.57 us | 2.29 ms | 2.09 ms | FAIL |
| crowdfunding-success-1 | 214.15 us | **58.84 us** | 276.13 us | 311.96 us | 88.09 us | 222.53 us | 11.98 ms | 390.63 us | 406.50 us | 422.23 us | 209.52 us | 1.51 ms | 1.32 ms | 137.29 ms |
| crowdfunding-success-2 | 212.75 us | **70.05 us** | 273.71 us | 318.24 us | 89.45 us | 223.89 us | 11.84 ms | 390.32 us | 412.93 us | 424.56 us | 210.55 us | 1.59 ms | 1.31 ms | 136.40 ms |
| crowdfunding-success-3 | 216.92 us | **66.61 us** | 275.56 us | 316.79 us | 89.03 us | 216.87 us | 12.05 ms | 391.80 us | 411.39 us | 440.25 us | 208.41 us | 1.42 ms | 1.32 ms | 137.31 ms |
| currency-1 | 239.66 us | 132.86 us | 316.88 us | 365.73 us | **110.69 us** | 257.72 us | 10.34 ms | 439.97 us | 494.94 us | 536.40 us | 243.47 us | 1.57 ms | 1.46 ms | 167.94 ms |
| escrow-redeem_1-1 | 350.90 us | 262.57 us | 439.78 us | 497.71 us | **153.10 us** | 350.17 us | 15.11 ms | 600.42 us | 694.59 us | 728.79 us | 333.01 us | 2.05 ms | 2.04 ms | 233.76 ms |
| escrow-redeem_1-2 | 352.40 us | 281.29 us | 432.26 us | 491.08 us | **157.34 us** | 341.85 us | 15.09 ms | 591.68 us | 678.05 us | 732.88 us | 329.22 us | 2.06 ms | 2.03 ms | 225.36 ms |
| escrow-redeem_2-1 | 398.60 us | 244.34 us | 476.55 us | 563.71 us | **178.47 us** | 378.21 us | 17.28 ms | 670.22 us | 770.99 us | 840.39 us | 364.96 us | 2.34 ms | 2.30 ms | 253.15 ms |
| escrow-redeem_2-2 | 398.92 us | 323.35 us | 476.10 us | 564.79 us | **174.78 us** | 383.24 us | 17.26 ms | 663.37 us | 775.58 us | 833.21 us | 375.94 us | 2.35 ms | 2.32 ms | 249.95 ms |
| escrow-redeem_2-3 | 406.46 us | 301.53 us | 481.60 us | 576.69 us | **179.58 us** | 379.62 us | 17.25 ms | 654.41 us | 771.99 us | 826.01 us | 368.45 us | 2.35 ms | 2.29 ms | 266.31 ms |
| escrow-refund-1 | 156.81 us | **49.10 us** | 274.87 us | 256.95 us | 71.46 us | 217.84 us | 8.52 ms | 379.26 us | 382.79 us | 379.97 us | 197.06 us | 1.14 ms | 1.13 ms | 131.58 ms |
| future-increase-margin-1 | 243.10 us | 153.65 us | 317.79 us | 358.78 us | **111.83 us** | 259.27 us | 10.25 ms | 448.17 us | 512.53 us | 547.85 us | 244.66 us | 1.48 ms | 1.45 ms | 167.73 ms |
| future-increase-margin-2 | 524.75 us | 349.59 us | 575.19 us | 713.34 us | **236.83 us** | 470.25 us | 21.70 ms | 839.42 us | 1.01 ms | 1.08 ms | 457.86 us | 3.04 ms | 2.95 ms | 321.23 ms |
| future-increase-margin-3 | 517.96 us | 450.95 us | 579.29 us | 703.51 us | **231.75 us** | 465.53 us | 22.22 ms | 816.55 us | 1.01 ms | 1.06 ms | 463.13 us | 2.98 ms | 2.93 ms | 325.80 ms |
| future-increase-margin-4 | 485.44 us | 1.29 ms | 712.00 us | 736.56 us | **221.29 us** | 591.65 us | 18.83 ms | 1.00 ms | 1.15 ms | 1.14 ms | 534.43 us | 3.01 ms | 2.94 ms | FAIL |
| future-increase-margin-5 | 809.53 us | 2.38 ms | 983.11 us | 1.19 ms | **399.44 us** | 839.83 us | 157.70 ms | 1.57 ms | 1.76 ms | 1.79 ms | 705.34 us | 7.17 ms | 7.11 ms | FAIL |
| future-pay-out-1 | 238.46 us | 144.95 us | 317.53 us | 363.34 us | **112.28 us** | 259.49 us | 10.40 ms | 464.12 us | 520.59 us | 539.17 us | 245.27 us | 1.47 ms | 1.47 ms | 165.11 ms |
| future-pay-out-2 | 531.00 us | 354.77 us | 575.77 us | 722.93 us | **236.21 us** | 473.21 us | 21.83 ms | 823.39 us | 1.02 ms | 1.11 ms | 454.93 us | 2.94 ms | 2.90 ms | 324.76 ms |
| future-pay-out-3 | 522.80 us | 385.46 us | 573.43 us | 724.30 us | **235.37 us** | 464.06 us | 21.77 ms | 822.43 us | 996.33 us | 1.10 ms | 462.31 us | 2.95 ms | 2.94 ms | 327.02 ms |
| future-pay-out-4 | 807.46 us | 2.51 ms | 980.46 us | 1.19 ms | **398.24 us** | 841.51 us | 157.56 ms | 1.62 ms | 1.65 ms | 1.80 ms | 709.08 us | 7.63 ms | 6.87 ms | FAIL |
| future-settle-early-1 | 248.80 us | 138.31 us | 314.58 us | 363.58 us | **113.51 us** | 257.01 us | 10.40 ms | 444.64 us | 544.33 us | 541.25 us | 242.86 us | 1.51 ms | 1.47 ms | 167.16 ms |
| future-settle-early-2 | 519.69 us | 481.88 us | 577.04 us | 728.32 us | **230.20 us** | 470.49 us | 22.02 ms | 819.19 us | 991.50 us | 1.10 ms | 495.44 us | 2.99 ms | 2.95 ms | 323.38 ms |
| future-settle-early-3 | 510.23 us | **224.63 us** | 575.96 us | 707.79 us | 231.21 us | 479.14 us | 22.03 ms | 821.62 us | 1.01 ms | 1.08 ms | 473.50 us | 2.97 ms | 3.01 ms | 331.89 ms |
| future-settle-early-4 | 602.17 us | 2.33 ms | 841.24 us | 930.34 us | **313.18 us** | 684.70 us | 155.30 ms | 1.26 ms | 1.29 ms | 1.42 ms | 611.76 us | 5.84 ms | 5.99 ms | FAIL |
| game-sm-success_1-1 | 381.89 us | 1.09 ms | 562.03 us | 584.71 us | **176.21 us** | 451.04 us | 15.89 ms | 781.76 us | 806.86 us | 844.40 us | 426.13 us | 2.44 ms | 2.52 ms | 268.42 ms |
| game-sm-success_1-2 | 196.53 us | **58.74 us** | 227.19 us | 301.07 us | 81.14 us | 199.36 us | 11.28 ms | 352.15 us | 362.22 us | 378.60 us | 176.77 us | 1.21 ms | 1.24 ms | 123.75 ms |
| game-sm-success_1-3 | 604.39 us | 1.47 ms | 751.75 us | 881.27 us | **283.68 us** | 631.40 us | 23.16 ms | 1.08 ms | 1.24 ms | 1.31 ms | 585.29 us | 3.72 ms | 3.79 ms | 407.60 ms |
| game-sm-success_1-4 | 232.78 us | **71.25 us** | 254.02 us | 348.00 us | 93.11 us | 214.32 us | 12.64 ms | 398.83 us | 411.17 us | 417.56 us | 198.89 us | 1.39 ms | 1.42 ms | 134.58 ms |
| game-sm-success_2-1 | 386.00 us | 1.22 ms | 567.60 us | 581.81 us | **175.28 us** | 444.50 us | 16.00 ms | 779.82 us | 886.17 us | 851.19 us | 433.76 us | 2.47 ms | 2.52 ms | 268.69 ms |
| game-sm-success_2-2 | 195.25 us | **57.76 us** | 225.35 us | 292.98 us | 80.43 us | 196.58 us | 10.86 ms | 352.53 us | 655.71 us | 367.17 us | 177.56 us | 1.22 ms | 1.24 ms | 124.01 ms |
| game-sm-success_2-3 | 618.13 us | 1.29 ms | 747.52 us | 859.15 us | **277.46 us** | 635.44 us | 22.92 ms | 1.08 ms | 1.25 ms | 1.31 ms | 584.02 us | 3.65 ms | 3.76 ms | 412.20 ms |
| game-sm-success_2-4 | 227.60 us | **60.44 us** | 255.49 us | 337.85 us | 94.17 us | 212.11 us | 12.54 ms | 392.60 us | 401.52 us | 410.90 us | 198.33 us | 1.39 ms | 1.43 ms | 135.64 ms |
| game-sm-success_2-5 | 619.32 us | 941.00 us | 759.97 us | 874.48 us | **287.96 us** | 619.04 us | 22.91 ms | 1.10 ms | 1.27 ms | 1.30 ms | 597.73 us | 3.65 ms | 3.75 ms | 406.76 ms |
| game-sm-success_2-6 | 232.86 us | **50.16 us** | 252.31 us | 342.37 us | 92.01 us | 220.94 us | 12.53 ms | 394.26 us | 397.47 us | 429.29 us | 199.74 us | 1.40 ms | 1.42 ms | 136.55 ms |
| guardrail-sorted-large | 428.42 us | **291.85 us** | 516.44 us | FAIL | 319.71 us | 378.04 us | 61.74 ms | 585.95 us | 759.12 us | 812.74 us | 469.01 us | 3.06 ms | 2.93 ms | FAIL |
| guardrail-sorted-small | 71.85 us | 105.94 us | 132.66 us | FAIL | **27.43 us** | 103.25 us | 2.22 ms | 162.81 us | 170.49 us | 183.48 us | 98.90 us | 612.50 us | 589.70 us | FAIL |
| guardrail-unsorted-large | 611.22 us | **384.03 us** | 684.66 us | FAIL | 384.31 us | 456.92 us | 65.98 ms | 766.73 us | 1.01 ms | 1.10 ms | 602.48 us | 3.83 ms | 3.86 ms | FAIL |
| guardrail-unsorted-small | 71.26 us | 96.06 us | 130.74 us | FAIL | **27.36 us** | 104.89 us | 2.08 ms | 160.78 us | 169.89 us | 182.31 us | 97.11 us | 551.00 us | 574.80 us | FAIL |
| multisig-sm-01 | 401.00 us | 1.26 ms | 603.26 us | 610.65 us | **184.09 us** | 479.31 us | 15.96 ms | 828.74 us | 879.98 us | 931.09 us | 461.63 us | 2.55 ms | 2.66 ms | FAIL |
| multisig-sm-02 | 397.57 us | 1.43 ms | 588.60 us | 613.84 us | **181.74 us** | 477.66 us | 16.01 ms | 831.27 us | 844.05 us | 879.16 us | 451.05 us | 2.48 ms | 2.68 ms | FAIL |
| multisig-sm-03 | 395.59 us | 1.39 ms | 600.25 us | 605.10 us | **182.09 us** | 477.96 us | 15.91 ms | 818.88 us | 865.20 us | 899.93 us | 448.50 us | 2.49 ms | 2.77 ms | FAIL |
| multisig-sm-04 | 396.88 us | 1.42 ms | 606.32 us | 604.95 us | **184.34 us** | 475.19 us | 15.94 ms | 821.90 us | 883.21 us | 910.35 us | 449.90 us | 2.57 ms | 2.77 ms | FAIL |
| multisig-sm-05 | 544.67 us | 1.78 ms | 728.82 us | 824.61 us | **256.82 us** | 610.33 us | 19.86 ms | 1.01 ms | 1.14 ms | 1.22 ms | 551.03 us | 3.27 ms | 3.52 ms | FAIL |
| multisig-sm-06 | 404.45 us | 1.24 ms | 601.57 us | 628.17 us | **185.59 us** | 483.19 us | 15.89 ms | 845.23 us | 869.57 us | 919.84 us | 448.36 us | 2.48 ms | 2.67 ms | FAIL |
| multisig-sm-07 | 389.81 us | 1.37 ms | 584.05 us | 613.75 us | **181.30 us** | 473.83 us | 16.10 ms | 840.03 us | 830.62 us | 886.48 us | 446.08 us | 2.40 ms | 2.72 ms | FAIL |
| multisig-sm-08 | 400.28 us | 1.54 ms | 599.86 us | 617.37 us | **183.56 us** | 482.23 us | 16.08 ms | 822.11 us | 863.19 us | 914.59 us | 448.50 us | 2.43 ms | 2.66 ms | FAIL |
| multisig-sm-09 | 396.73 us | 1.48 ms | 592.25 us | 618.10 us | **186.69 us** | 481.56 us | 16.37 ms | 836.56 us | 869.08 us | 899.91 us | 447.52 us | 2.45 ms | 2.60 ms | FAIL |
| multisig-sm-10 | 548.86 us | 1.79 ms | 722.03 us | 815.08 us | **257.92 us** | 595.87 us | 20.05 ms | 1.02 ms | 1.14 ms | 1.23 ms | 556.95 us | 3.29 ms | 3.33 ms | FAIL |
| ping-pong-1 | 330.76 us | 752.63 us | 507.21 us | 495.39 us | **152.88 us** | 405.76 us | 13.24 ms | 691.22 us | 709.01 us | 756.17 us | 377.14 us | 2.08 ms | 2.13 ms | 243.16 ms |
| ping-pong-2 | 332.25 us | 1.05 ms | 507.38 us | 512.82 us | **153.66 us** | 395.52 us | 13.45 ms | 691.24 us | 711.44 us | 754.71 us | 379.08 us | 2.09 ms | 2.15 ms | 238.77 ms |
| ping-pong_2-1 | 204.45 us | 529.11 us | 408.05 us | 350.94 us | **99.47 us** | 303.46 us | 9.76 ms | 522.64 us | 502.07 us | 541.60 us | 279.66 us | 1.48 ms | 1.52 ms | 175.68 ms |
| prism-1 | 170.56 us | **39.46 us** | 197.70 us | 257.70 us | 68.08 us | 170.25 us | 9.05 ms | 305.14 us | 320.72 us | 337.15 us | 152.76 us | 1.06 ms | 1.06 ms | 105.23 ms |
| prism-2 | 419.20 us | 1.32 ms | 583.23 us | 624.45 us | **187.54 us** | 459.79 us | 17.31 ms | 808.53 us | 867.06 us | 907.46 us | 442.32 us | 2.57 ms | 2.58 ms | 282.09 ms |
| prism-3 | 360.86 us | 199.45 us | 407.49 us | 530.41 us | **160.34 us** | 347.86 us | 15.91 ms | 589.94 us | 693.92 us | 742.20 us | 321.26 us | 2.11 ms | 2.43 ms | 222.16 ms |
| pubkey-1 | 142.07 us | **30.17 us** | 185.57 us | 216.21 us | 60.06 us | 154.74 us | 7.83 ms | 276.56 us | 269.02 us | 272.49 us | 138.98 us | 918.40 us | 969.70 us | 93.98 ms |
| stablecoin_1-1 | 985.76 us | 3.78 ms | 1.24 ms | 1.53 ms | **458.84 us** | 1.04 ms | 294.14 ms | 1.82 ms | 1.95 ms | 2.04 ms | 803.59 us | 10.42 ms | 10.42 ms | FAIL |
| stablecoin_1-2 | 192.92 us | **42.97 us** | 224.01 us | 289.69 us | 81.74 us | 196.03 us | 11.65 ms | 350.66 us | 361.20 us | 354.90 us | 174.18 us | 1.20 ms | 1.24 ms | 118.33 ms |
| stablecoin_1-3 | 1.09 ms | 3.88 ms | 1.33 ms | 1.73 ms | **489.32 us** | 1.19 ms | 297.11 ms | 2.07 ms | 2.33 ms | 2.29 ms | 893.19 us | 11.33 ms | 11.27 ms | FAIL |
| stablecoin_1-4 | 201.92 us | **50.07 us** | 236.76 us | 304.91 us | 86.03 us | 204.05 us | 12.21 ms | 363.06 us | 376.01 us | 395.75 us | 182.08 us | 1.27 ms | 1.29 ms | 124.85 ms |
| stablecoin_1-5 | 1.35 ms | 3.95 ms | 1.53 ms | 2.20 ms | **592.38 us** | 1.46 ms | 300.32 ms | 2.60 ms | 2.84 ms | 2.83 ms | 1.09 ms | 13.20 ms | 13.25 ms | FAIL |
| stablecoin_1-6 | 253.91 us | **52.55 us** | 270.47 us | 374.84 us | 103.19 us | 243.05 us | 14.63 ms | 430.30 us | 437.88 us | 476.02 us | 211.17 us | 1.50 ms | 1.55 ms | 146.32 ms |
| stablecoin_2-1 | 964.51 us | 3.82 ms | 1.24 ms | 1.50 ms | **456.33 us** | 1.03 ms | 301.02 ms | 1.83 ms | 1.92 ms | 1.98 ms | 826.03 us | 10.24 ms | 10.45 ms | FAIL |
| stablecoin_2-2 | 193.87 us | **53.04 us** | 228.78 us | 295.77 us | 82.25 us | 204.01 us | 11.29 ms | 346.27 us | 351.97 us | 361.61 us | 176.11 us | 1.20 ms | 1.23 ms | 117.31 ms |
| stablecoin_2-3 | 1.09 ms | 3.84 ms | 1.33 ms | 1.73 ms | **498.78 us** | 1.18 ms | 301.70 ms | 2.01 ms | 2.26 ms | 2.30 ms | 881.42 us | 11.26 ms | 11.20 ms | FAIL |
| stablecoin_2-4 | 204.13 us | **61.68 us** | 238.30 us | 314.19 us | 89.91 us | 202.83 us | 12.03 ms | 361.78 us | 364.30 us | 378.03 us | 184.47 us | 1.26 ms | 1.28 ms | 126.26 ms |
| token-account-1 | 183.45 us | 208.19 us | 266.57 us | 294.04 us | **87.64 us** | 218.12 us | 8.49 ms | 374.67 us | 468.84 us | 425.95 us | 203.79 us | 1.17 ms | 1.19 ms | 134.17 ms |
| token-account-2 | 321.63 us | **106.39 us** | 372.40 us | 452.73 us | 149.16 us | 301.86 us | 14.05 ms | 540.70 us | 760.62 us | 655.29 us | 296.73 us | 1.81 ms | 1.85 ms | 211.67 ms |
| uniswap-1 | 386.15 us | **154.66 us** | 432.51 us | 544.51 us | 169.41 us | 355.69 us | 15.68 ms | 619.62 us | 826.89 us | 857.78 us | 352.00 us | 2.11 ms | 2.17 ms | 273.34 ms |
| uniswap-2 | 215.93 us | 147.55 us | 301.80 us | 343.80 us | **97.64 us** | 245.75 us | 11.32 ms | 414.84 us | 534.50 us | 476.04 us | 229.18 us | 1.34 ms | 1.36 ms | 149.53 ms |
| uniswap-3 | 1.71 ms | 2.21 ms | 1.68 ms | 2.19 ms | **612.02 us** | 1.42 ms | 54.59 ms | 2.58 ms | 3.32 ms | 3.35 ms | 1.40 ms | 9.57 ms | 9.63 ms | 922.24 ms |
| uniswap-4 | 355.46 us | **75.01 us** | 342.01 us | 476.67 us | 129.00 us | 305.77 us | 19.45 ms | 528.56 us | 612.76 us | 585.95 us | 279.95 us | 1.92 ms | 1.95 ms | 185.68 ms |
| uniswap-5 | 1.77 ms | 934.87 us | 1.22 ms | 1.46 ms | **424.24 us** | 1.02 ms | 42.71 ms | 1.79 ms | 2.05 ms | 2.17 ms | 983.70 us | 6.56 ms | 6.61 ms | 639.93 ms |
| uniswap-6 | 459.35 us | **63.88 us** | 340.57 us | 452.28 us | 124.56 us | 285.97 us | 18.70 ms | 510.16 us | 583.42 us | 558.76 us | 264.47 us | 1.81 ms | 1.86 ms | 180.06 ms |
| vesting-1 | 452.87 us | 258.86 us | 443.69 us | 477.39 us | **157.47 us** | 347.77 us | 13.76 ms | 586.79 us | 736.22 us | 721.11 us | 350.86 us | 1.90 ms | 1.96 ms | 233.55 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*