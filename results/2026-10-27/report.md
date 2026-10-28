# Cardano Plutus VM Benchmark Results

**Date:** 2026-10-27

## Environment
```
date: 2026-10-27T18:14:37+00:00
kernel: 6.8.0-139-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
```

## VM Versions

| VM | Source revision | Toolchain |
|---|---|---|
| plutus-core CEK (Haskell / GHC) | 1.72.0.0 ([152220a](https://github.com/IntersectMBO/plutus/commit/152220ae3da8cd6ceaf2688094af541ac1245f58)) | GHC 9.6.4 |
| Scalus UPLC→JVM JIT (Scala / JVM) | v1.4.1 ([985e834](https://github.com/scalus3/scalus/commit/985e8341247cfa40c6326a8167ab4c9876104f8b)) | JDK 21 / Scala 3 |
| Scalus CEK (Scala / JVM) | v1.4.1 ([985e834](https://github.com/scalus3/scalus/commit/985e8341247cfa40c6326a8167ab4c9876104f8b)) | JDK 21 / Scala 3 |
| Julc CEK (Java / GraalVM) | v0.1.0-pre19 ([ed3f584](https://github.com/bloxbean/julc/commit/ed3f584886bb8f1f3ea4ada8784efcc1fa363a31)) | GraalVM 25.0.2-graal |
| llvm-uplc UPLC→native JIT (C++ / LLVM) | commit:6bcef67 ([6bcef67](https://github.com/SeungheonOh/llvm-uplc/commit/6bcef67ce1995d232327f13d9080fe2f0261a55c)) | LLVM 22.1.0 |
| Amaru UPLC CEK (Rust) | 0.4.0 ([7378376](https://github.com/pragma-org/amaru/commit/7378376ae7503f03c0e17893f41496537882f283)) | rustc nightly-2026-09-04 |
| uplc-turbo Bytecode VM (Rust) | commit:069cef5 ([069cef5](https://github.com/jonathanlim222/uplc/commit/069cef5684d57064d040ab498a5d2eac01e63275)) | rustc 1.94 |
| Plutuz CEK (Zig) | commit:33b812d ([33b812d](https://github.com/utxo-company/plutuz/commit/33b812dbcf88f6851286e54cb93a4a443353f94c)) | Zig 0.15.2 |
| Chrysalis CEK (C# / .NET) | commit:7c45d47 ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Chrysalis CEK (C# / .NET AOT) | commit:7c45d47 ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Plutigo CEK (Go) | v0.10.0 ([db23952](https://github.com/blinklabs-io/plutigo/commit/db23952640c4d581afb914d97ccc75bc0c4ddf1a)) | Go 1.27.3 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 0.5.3 ([320fc36](https://github.com/butaneprotocol/blaze-cardano/commit/320fc3604cfeac640013fd8206efaecfe8a2360f)) | Bun 1.3.14 |
| blaze-plutus CEK (TypeScript / Node V8) | 0.5.3 ([320fc36](https://github.com/butaneprotocol/blaze-cardano/commit/320fc3604cfeac640013fd8206efaecfe8a2360f)) | Node.js 22 |
| opshin CEK (Python / CPython) | 1.3.3 ([eda2fba](https://github.com/OpShin/uplc/commit/eda2fbaa89c1a2db4ec6c6c1fa5eea2a8b2671d4)) | Python 3.14 |

## Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc UPLC→native JIT (C++ / LLVM)** | C++ / LLVM | 162.88 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 173.91 us | 1.07x |
| **uplc-turbo Bytecode VM (Rust)** | Rust | 296.71 us | 1.82x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 355.85 us | 2.18x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 457.63 us | 2.81x |
| **Plutigo CEK (Go)** | Go | 460.51 us | 2.83x |
| **Amaru UPLC CEK (Rust)** | Rust | 525.82 us | 3.23x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 646.01 us | 3.97x |
| **Plutuz CEK (Zig)** | Zig | 657.95 us | 4.04x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 710.05 us | 4.36x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 755.69 us | 4.64x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.28 ms | 13.99x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.32 ms | 14.26x |
| **opshin CEK (Python / CPython)** | Python / CPython | 55.22 ms | 338.99x |

### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| llvm-uplc UPLC→native JIT (C++ / LLVM) | 89 | 0 | 0 | 89 |
| Scalus UPLC→JVM JIT (Scala / JVM) | 89 | 0 | 0 | 89 |
| uplc-turbo Bytecode VM (Rust) | 89 | 0 | 0 | 89 |
| plutus-core CEK (Haskell / GHC) | 89 | 0 | 0 | 89 |
| Scalus CEK (Scala / JVM) | 89 | 0 | 0 | 89 |
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
| Amaru UPLC CEK (Rust) | 89 | 0 | 0 | 89 |
| Julc CEK (Java / GraalVM) | 78 | 11 | 0 | 89 |
| Plutuz CEK (Zig) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET AOT) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

## Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc UPLC→native JIT (C++ / LLVM) | Amaru UPLC CEK (Rust) | uplc-turbo Bytecode VM (Rust) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 165.47 us | **40.34 us** | 225.12 us | 262.75 us | 71.97 us | 267.38 us | 132.89 us | 331.80 us | 370.38 us | 379.68 us | 237.85 us | 1.07 ms | 1.05 ms | 118.37 ms |
| auction_1-2 | 564.30 us | 1.02 ms | 733.41 us | 825.00 us | **272.71 us** | 838.60 us | 477.42 us | 1.03 ms | 1.16 ms | 1.27 ms | 734.08 us | 3.15 ms | 3.14 ms | 424.34 ms |
| auction_1-3 | 559.25 us | 636.18 us | 724.88 us | 852.62 us | **267.85 us** | 842.58 us | 493.24 us | 1.03 ms | 1.19 ms | 1.28 ms | 725.66 us | 3.25 ms | 3.18 ms | 457.62 ms |
| auction_1-4 | 262.94 us | **48.98 us** | 260.08 us | 323.03 us | 85.81 us | 316.05 us | 174.00 us | 393.60 us | 397.57 us | 415.46 us | 263.46 us | 1.30 ms | 1.26 ms | 141.36 ms |
| auction_2-1 | 162.64 us | **42.23 us** | 226.62 us | 256.53 us | 71.80 us | 270.56 us | 134.28 us | 343.16 us | 330.23 us | 338.49 us | 233.00 us | 1.02 ms | 1.00 ms | 118.24 ms |
| auction_2-2 | 562.42 us | 851.14 us | 726.31 us | 844.73 us | **272.18 us** | 851.51 us | 478.29 us | 1.03 ms | 1.16 ms | 1.30 ms | 744.60 us | 3.15 ms | 3.41 ms | 424.22 ms |
| auction_2-3 | 730.43 us | 988.10 us | 876.13 us | 1.05 ms | **344.15 us** | 1.05 ms | 621.06 us | 1.25 ms | 1.47 ms | 1.61 ms | 890.00 us | 4.19 ms | 4.22 ms | 555.64 ms |
| auction_2-4 | 559.54 us | 564.47 us | 722.98 us | 817.12 us | **269.60 us** | 840.99 us | 483.89 us | 1.01 ms | 1.18 ms | 1.25 ms | 738.92 us | 3.33 ms | 3.33 ms | 429.03 ms |
| auction_2-5 | 209.95 us | **46.17 us** | 260.67 us | 323.99 us | 85.99 us | 315.05 us | 172.31 us | 433.66 us | 468.35 us | 421.33 us | 263.64 us | 1.26 ms | 1.26 ms | 141.92 ms |
| coop-1 | 219.38 us | **40.41 us** | 247.60 us | FAIL | 89.91 us | 270.78 us | 169.62 us | 328.55 us | 332.73 us | 396.82 us | 231.25 us | 1.40 ms | 1.58 ms | FAIL |
| coop-2 | 688.41 us | **155.94 us** | 772.53 us | FAIL | 288.75 us | 775.66 us | 552.95 us | 960.69 us | 1.15 ms | 1.19 ms | 710.25 us | 4.35 ms | 4.62 ms | FAIL |
| coop-3 | 1.98 ms | **667.38 us** | 2.11 ms | FAIL | 931.02 us | 2.43 ms | 1.75 ms | 2.52 ms | 4.32 ms | 3.86 ms | 1.84 ms | 10.81 ms | 10.97 ms | FAIL |
| coop-4 | 914.12 us | **245.56 us** | 941.11 us | FAIL | 383.44 us | 1.01 ms | 704.22 us | 1.14 ms | 1.41 ms | 1.51 ms | 852.05 us | 5.18 ms | 5.45 ms | FAIL |
| coop-5 | 380.90 us | **87.14 us** | 467.01 us | FAIL | 166.98 us | 490.82 us | 299.58 us | 628.72 us | 676.00 us | 718.60 us | 459.85 us | 2.41 ms | 2.68 ms | FAIL |
| coop-6 | 631.30 us | **138.94 us** | 674.66 us | FAIL | 263.71 us | 754.09 us | 488.14 us | 844.40 us | 960.58 us | 1.05 ms | 608.40 us | 3.84 ms | 4.15 ms | FAIL |
| coop-7 | 333.84 us | **54.15 us** | 339.22 us | FAIL | 125.18 us | 365.57 us | 242.54 us | 460.44 us | 484.44 us | 503.17 us | 322.77 us | 1.92 ms | 2.13 ms | FAIL |
| crowdfunding-success-1 | 197.00 us | **41.74 us** | 262.58 us | 299.98 us | 84.73 us | 294.37 us | 157.39 us | 382.31 us | 378.89 us | 399.26 us | 273.98 us | 1.23 ms | 1.31 ms | 139.41 ms |
| crowdfunding-success-2 | 195.88 us | **41.63 us** | 264.21 us | 296.89 us | 86.32 us | 308.80 us | 157.24 us | 386.87 us | 381.87 us | 394.27 us | 273.09 us | 1.23 ms | 1.29 ms | 139.45 ms |
| crowdfunding-success-3 | 198.77 us | **43.10 us** | 263.73 us | 296.90 us | 84.74 us | 300.20 us | 156.25 us | 387.42 us | 371.16 us | 395.55 us | 278.47 us | 1.23 ms | 1.29 ms | 139.93 ms |
| currency-1 | 224.29 us | **62.88 us** | 302.61 us | 346.09 us | 106.82 us | 348.62 us | 190.93 us | 423.63 us | 477.85 us | 512.86 us | 312.08 us | 1.35 ms | 1.34 ms | 188.51 ms |
| escrow-redeem_1-1 | 317.96 us | **88.47 us** | 413.79 us | 465.18 us | 148.68 us | 462.15 us | 265.41 us | 573.09 us | 643.93 us | 687.58 us | 419.06 us | 1.87 ms | 1.85 ms | 232.52 ms |
| escrow-redeem_1-2 | 328.22 us | **88.62 us** | 413.27 us | 468.38 us | 147.73 us | 464.75 us | 274.99 us | 596.87 us | 643.45 us | 802.33 us | 443.47 us | 1.88 ms | 1.87 ms | 233.07 ms |
| escrow-redeem_2-1 | 374.06 us | **95.18 us** | 452.83 us | 515.33 us | 167.50 us | 517.36 us | 313.46 us | 636.45 us | 728.23 us | 782.39 us | 459.28 us | 2.13 ms | 2.11 ms | 280.19 ms |
| escrow-redeem_2-2 | 366.76 us | **98.55 us** | 449.16 us | 526.10 us | 169.89 us | 516.35 us | 307.89 us | 635.09 us | 745.51 us | 782.14 us | 459.41 us | 2.13 ms | 2.12 ms | 262.12 ms |
| escrow-redeem_2-3 | 371.83 us | **92.93 us** | 456.59 us | 536.46 us | 173.62 us | 515.70 us | 316.90 us | 635.79 us | 729.45 us | 790.16 us | 470.98 us | 2.13 ms | 2.11 ms | 266.19 ms |
| escrow-refund-1 | 148.96 us | **30.67 us** | 264.95 us | 243.20 us | 66.19 us | 278.29 us | 115.78 us | 363.85 us | 338.69 us | 358.93 us | 275.91 us | 1.11 ms | 1.04 ms | 131.21 ms |
| future-increase-margin-1 | 223.07 us | **64.41 us** | 301.53 us | 338.07 us | 114.02 us | 349.39 us | 195.21 us | 423.68 us | 493.55 us | 511.90 us | 318.12 us | 1.35 ms | 1.34 ms | 175.00 ms |
| future-increase-margin-2 | 493.88 us | **147.93 us** | 549.98 us | 671.02 us | 220.48 us | 646.80 us | 412.04 us | 774.99 us | 930.61 us | 1.04 ms | 555.29 us | 2.70 ms | 2.67 ms | 340.44 ms |
| future-increase-margin-3 | 483.06 us | **140.01 us** | 550.46 us | 679.68 us | 220.59 us | 651.65 us | 408.06 us | 793.98 us | 988.06 us | 1.01 ms | 565.19 us | 2.70 ms | 2.68 ms | 340.91 ms |
| future-increase-margin-4 | 435.21 us | 537.37 us | 674.00 us | 691.69 us | **213.02 us** | 734.11 us | 377.21 us | 955.51 us | 1.02 ms | 1.09 ms | 680.33 us | 2.75 ms | 2.74 ms | FAIL |
| future-increase-margin-5 | 836.90 us | 1.46 ms | 930.61 us | 1.13 ms | **380.57 us** | 1.08 ms | 635.36 us | 1.49 ms | 1.56 ms | 1.80 ms | 886.22 us | 6.82 ms | 6.59 ms | FAIL |
| future-pay-out-1 | 224.90 us | **62.75 us** | 298.14 us | 338.79 us | 112.67 us | 354.04 us | 194.00 us | 436.13 us | 483.58 us | 514.18 us | 313.35 us | 1.33 ms | 1.35 ms | 186.00 ms |
| future-pay-out-2 | 497.97 us | **150.29 us** | 547.59 us | 658.96 us | 230.32 us | 655.61 us | 411.83 us | 777.37 us | 928.22 us | 1.01 ms | 552.87 us | 2.65 ms | 2.68 ms | 340.94 ms |
| future-pay-out-3 | 493.19 us | **158.72 us** | 548.82 us | 664.55 us | 227.31 us | 644.85 us | 412.59 us | 776.52 us | 958.77 us | 999.79 us | 587.02 us | 2.67 ms | 2.69 ms | 340.77 ms |
| future-pay-out-4 | 735.00 us | 1.45 ms | 927.47 us | 1.12 ms | **380.63 us** | 1.11 ms | 628.13 us | 1.54 ms | 1.57 ms | 1.70 ms | 876.74 us | 6.36 ms | 6.43 ms | FAIL |
| future-settle-early-1 | 228.96 us | **59.63 us** | 302.81 us | 338.55 us | 106.67 us | 351.57 us | 195.32 us | 425.20 us | 529.06 us | 513.53 us | 311.00 us | 1.33 ms | 1.35 ms | 174.26 ms |
| future-settle-early-2 | 486.02 us | **154.29 us** | 540.61 us | 668.44 us | 219.41 us | 645.81 us | 416.21 us | 777.72 us | 957.33 us | 1.01 ms | 561.15 us | 2.67 ms | 2.70 ms | 339.56 ms |
| future-settle-early-3 | 493.83 us | **151.14 us** | 547.64 us | 660.20 us | 220.16 us | 645.38 us | 413.99 us | 775.60 us | 925.36 us | 1.01 ms | 589.73 us | 2.66 ms | 2.68 ms | 346.28 ms |
| future-settle-early-4 | 562.75 us | 1.28 ms | 794.02 us | 864.42 us | **300.33 us** | 864.50 us | 490.26 us | 1.23 ms | 1.21 ms | 1.28 ms | 741.64 us | 5.43 ms | 5.52 ms | FAIL |
| game-sm-success_1-1 | 356.45 us | 346.84 us | 535.58 us | 550.41 us | **167.49 us** | 573.33 us | 297.79 us | 748.12 us | 745.64 us | 814.22 us | 542.40 us | 2.25 ms | 2.33 ms | 286.67 ms |
| game-sm-success_1-2 | 180.63 us | **39.09 us** | 217.80 us | 278.45 us | 77.09 us | 273.34 us | 158.77 us | 344.99 us | 333.13 us | 340.83 us | 226.43 us | 1.11 ms | 1.14 ms | 124.80 ms |
| game-sm-success_1-3 | 568.98 us | 602.71 us | 717.38 us | 817.37 us | **291.50 us** | 836.31 us | 479.47 us | 1.03 ms | 1.16 ms | 1.24 ms | 719.14 us | 3.35 ms | 3.39 ms | 420.71 ms |
| game-sm-success_1-4 | 209.20 us | **44.14 us** | 239.47 us | 314.55 us | 86.57 us | 306.50 us | 177.87 us | 377.07 us | 366.37 us | 391.58 us | 248.84 us | 1.28 ms | 2.31 ms | 144.56 ms |
| game-sm-success_2-1 | 354.66 us | 282.28 us | 547.49 us | 542.97 us | **166.84 us** | 570.73 us | 303.11 us | 749.28 us | 792.63 us | 818.93 us | 541.82 us | 2.26 ms | 2.41 ms | 275.96 ms |
| game-sm-success_2-2 | 199.19 us | **38.23 us** | 221.43 us | 274.25 us | 76.85 us | 272.71 us | 149.78 us | 346.80 us | 387.77 us | 341.60 us | 226.51 us | 1.11 ms | 1.13 ms | 124.90 ms |
| game-sm-success_2-3 | 568.66 us | 556.48 us | 711.27 us | 825.15 us | **270.52 us** | 819.43 us | 477.18 us | 1.03 ms | 1.19 ms | 1.22 ms | 719.22 us | 4.42 ms | 3.38 ms | 419.56 ms |
| game-sm-success_2-4 | 208.50 us | **43.43 us** | 241.26 us | 321.96 us | 87.47 us | 307.55 us | 172.37 us | 376.55 us | 375.94 us | 394.50 us | 248.77 us | 1.83 ms | 1.30 ms | 160.68 ms |
| game-sm-success_2-5 | 567.46 us | 563.20 us | 712.89 us | 812.65 us | **274.47 us** | 828.93 us | 533.96 us | 1.02 ms | 1.13 ms | 1.22 ms | 736.88 us | 3.34 ms | 3.35 ms | 423.81 ms |
| game-sm-success_2-6 | 209.46 us | **42.29 us** | 240.75 us | 312.56 us | 89.89 us | 306.28 us | 177.92 us | 413.25 us | 374.36 us | 391.73 us | 254.62 us | 1.28 ms | 1.31 ms | 138.94 ms |
| guardrail-sorted-large | 402.34 us | **230.04 us** | 492.78 us | FAIL | 304.59 us | 516.17 us | 368.96 us | 560.75 us | 694.49 us | 762.22 us | 498.03 us | 2.68 ms | 2.93 ms | FAIL |
| guardrail-sorted-small | 67.84 us | 85.13 us | 123.75 us | FAIL | **25.01 us** | 132.79 us | 65.98 us | 158.41 us | 163.03 us | 178.95 us | 124.47 us | 523.60 us | 745.40 us | FAIL |
| guardrail-unsorted-large | 592.12 us | **300.73 us** | 645.79 us | FAIL | 366.15 us | 682.49 us | 493.35 us | 725.47 us | 942.55 us | 1.05 ms | 629.02 us | 3.37 ms | 3.75 ms | FAIL |
| guardrail-unsorted-small | 66.80 us | 85.01 us | 120.11 us | FAIL | **23.85 us** | 128.45 us | 64.45 us | 159.11 us | 158.32 us | 170.13 us | 123.00 us | 515.80 us | 672.20 us | FAIL |
| multisig-sm-01 | 366.91 us | 377.74 us | 583.08 us | 582.26 us | **185.44 us** | 604.00 us | 298.83 us | 802.70 us | 866.78 us | 979.50 us | 579.59 us | 2.36 ms | 2.37 ms | FAIL |
| multisig-sm-02 | 358.32 us | 446.77 us | 557.59 us | 571.40 us | **172.58 us** | 599.67 us | 290.73 us | 806.81 us | 776.75 us | 825.83 us | 577.96 us | 2.31 ms | 2.31 ms | FAIL |
| multisig-sm-03 | 380.75 us | 481.54 us | 571.98 us | 567.52 us | **174.10 us** | 596.54 us | 293.46 us | 811.05 us | 796.33 us | 868.05 us | 578.06 us | 2.32 ms | 2.32 ms | FAIL |
| multisig-sm-04 | 364.87 us | 493.18 us | 583.48 us | 567.31 us | **180.53 us** | 602.26 us | 301.03 us | 798.07 us | 819.79 us | 848.94 us | 580.76 us | 2.34 ms | 2.37 ms | FAIL |
| multisig-sm-05 | 504.04 us | 825.70 us | 685.28 us | 775.02 us | **243.63 us** | 785.47 us | 434.34 us | 978.72 us | 1.09 ms | 1.16 ms | 692.00 us | 3.05 ms | 3.06 ms | FAIL |
| multisig-sm-06 | 375.19 us | 408.87 us | 565.98 us | 574.35 us | **175.91 us** | 608.27 us | 304.19 us | 798.57 us | 815.27 us | 979.24 us | 612.79 us | 2.52 ms | 2.36 ms | FAIL |
| multisig-sm-07 | 360.31 us | 500.22 us | 562.75 us | 558.34 us | **173.41 us** | 637.96 us | 290.24 us | 868.62 us | 804.32 us | 863.38 us | 585.40 us | 2.31 ms | 2.31 ms | FAIL |
| multisig-sm-08 | 357.21 us | 440.73 us | 561.50 us | 568.72 us | **174.77 us** | 612.88 us | 300.70 us | 787.83 us | 808.69 us | 833.44 us | 580.61 us | 2.32 ms | 2.32 ms | FAIL |
| multisig-sm-09 | 371.05 us | 488.05 us | 572.98 us | 579.43 us | **176.59 us** | 603.26 us | 307.93 us | 798.56 us | 831.58 us | 965.65 us | 579.08 us | 2.35 ms | 2.35 ms | FAIL |
| multisig-sm-10 | 509.75 us | 820.54 us | 702.50 us | 755.50 us | **243.93 us** | 780.35 us | 422.51 us | 976.63 us | 1.08 ms | 1.16 ms | 710.47 us | 3.06 ms | 3.06 ms | FAIL |
| ping-pong-1 | 305.42 us | 192.39 us | 488.43 us | 478.55 us | **145.42 us** | 499.40 us | 247.67 us | 672.29 us | 680.87 us | 710.50 us | 486.79 us | 1.96 ms | 1.95 ms | 249.63 ms |
| ping-pong-2 | 306.40 us | 198.74 us | 490.05 us | 482.40 us | **147.31 us** | 504.84 us | 251.17 us | 717.70 us | 663.81 us | 713.55 us | 487.07 us | 1.95 ms | 1.95 ms | 252.25 ms |
| ping-pong_2-1 | 190.54 us | **83.35 us** | 393.74 us | 325.47 us | 91.61 us | 366.51 us | 152.80 us | 504.90 us | 466.83 us | 503.82 us | 387.32 us | 1.38 ms | 1.39 ms | 177.85 ms |
| prism-1 | 152.97 us | **29.83 us** | 199.08 us | 232.14 us | 65.79 us | 236.74 us | 126.69 us | 296.48 us | 287.89 us | 297.84 us | 199.72 us | 962.60 us | 976.60 us | 117.47 ms |
| prism-2 | 377.36 us | 322.29 us | 561.90 us | 584.34 us | **177.56 us** | 600.56 us | 337.83 us | 797.33 us | 952.06 us | 848.12 us | 587.62 us | 2.31 ms | 2.32 ms | 296.16 ms |
| prism-3 | 330.20 us | **92.64 us** | 397.22 us | 501.75 us | 155.01 us | 479.19 us | 288.83 us | 573.53 us | 660.33 us | 731.03 us | 405.84 us | 1.92 ms | 1.93 ms | 232.90 ms |
| pubkey-1 | 133.85 us | **26.82 us** | 176.92 us | 202.25 us | 55.66 us | 219.15 us | 109.65 us | 267.52 us | 251.16 us | 290.16 us | 188.31 us | 835.80 us | 845.60 us | 95.05 ms |
| stablecoin_1-1 | 875.66 us | 2.42 ms | 1.15 ms | 1.39 ms | **458.49 us** | 1.30 ms | 714.12 us | 1.74 ms | 1.79 ms | 1.89 ms | 986.15 us | 9.52 ms | 9.60 ms | FAIL |
| stablecoin_1-2 | 182.04 us | **38.42 us** | 218.03 us | 274.18 us | 76.57 us | 274.05 us | 148.93 us | 352.19 us | 323.05 us | 336.04 us | 224.80 us | 1.11 ms | 1.12 ms | 121.16 ms |
| stablecoin_1-3 | 1.02 ms | 2.55 ms | 1.25 ms | 1.59 ms | **473.76 us** | 1.56 ms | 824.05 us | 1.96 ms | 2.05 ms | 2.14 ms | 1.11 ms | 10.29 ms | 10.35 ms | FAIL |
| stablecoin_1-4 | 192.65 us | **40.64 us** | 224.32 us | 295.64 us | 79.91 us | 281.90 us | 159.06 us | 349.95 us | 347.68 us | 370.24 us | 232.63 us | 1.16 ms | 1.18 ms | 128.16 ms |
| stablecoin_1-5 | 1.26 ms | 2.65 ms | 1.44 ms | 2.05 ms | **582.93 us** | 1.93 ms | 1.04 ms | 2.40 ms | 2.54 ms | 2.66 ms | 1.27 ms | 12.12 ms | 12.13 ms | FAIL |
| stablecoin_1-6 | 242.54 us | **46.50 us** | 259.92 us | 350.44 us | 99.47 us | 328.63 us | 194.50 us | 402.96 us | 409.87 us | 428.11 us | 265.35 us | 1.39 ms | 1.41 ms | 150.28 ms |
| stablecoin_2-1 | 878.51 us | 2.43 ms | 1.18 ms | 1.42 ms | **445.00 us** | 1.33 ms | 714.06 us | 1.73 ms | 1.79 ms | 1.90 ms | 1.04 ms | 9.51 ms | 9.60 ms | FAIL |
| stablecoin_2-2 | 177.60 us | **37.94 us** | 215.07 us | 290.75 us | 76.30 us | 270.44 us | 157.21 us | 332.95 us | 324.07 us | 351.22 us | 224.82 us | 1.11 ms | 1.12 ms | 120.96 ms |
| stablecoin_2-3 | 976.76 us | 2.51 ms | 1.25 ms | 1.60 ms | **471.08 us** | 1.52 ms | 827.34 us | 1.92 ms | 2.08 ms | 2.15 ms | 1.11 ms | 10.33 ms | 10.34 ms | FAIL |
| stablecoin_2-4 | 190.04 us | **41.57 us** | 225.77 us | 287.63 us | 87.72 us | 287.32 us | 157.50 us | 347.03 us | 346.98 us | 425.89 us | 242.16 us | 1.17 ms | 1.18 ms | 128.37 ms |
| token-account-1 | 168.49 us | **51.16 us** | 255.80 us | 276.08 us | 81.71 us | 286.52 us | 144.28 us | 359.27 us | 381.21 us | 404.90 us | 273.60 us | 1.09 ms | 1.37 ms | 136.94 ms |
| token-account-2 | 303.54 us | **66.86 us** | 353.81 us | 428.96 us | 144.58 us | 421.08 us | 269.12 us | 535.70 us | 579.22 us | 633.06 us | 360.77 us | 1.68 ms | 2.47 ms | 237.63 ms |
| uniswap-1 | 354.00 us | **100.37 us** | 411.36 us | 506.29 us | 170.31 us | 501.91 us | 313.36 us | 596.50 us | 742.90 us | 842.02 us | 429.24 us | 2.02 ms | 2.02 ms | 282.33 ms |
| uniswap-2 | 199.03 us | **56.41 us** | 285.73 us | 329.39 us | 95.07 us | 326.37 us | 177.50 us | 402.29 us | 429.07 us | 452.47 us | 288.72 us | 1.27 ms | 1.27 ms | 153.07 ms |
| uniswap-3 | 1.57 ms | 873.48 us | 1.60 ms | 2.05 ms | **656.95 us** | 2.08 ms | 1.28 ms | 2.45 ms | 2.83 ms | 3.06 ms | 1.67 ms | 15.69 ms | 8.92 ms | 971.33 ms |
| uniswap-4 | 312.08 us | **61.68 us** | 324.77 us | 454.72 us | 126.29 us | 419.49 us | 254.24 us | 525.77 us | 535.45 us | 557.38 us | 332.50 us | 1.82 ms | 1.80 ms | 190.60 ms |
| uniswap-5 | 1.03 ms | 651.86 us | 1.15 ms | 1.40 ms | **420.31 us** | 1.41 ms | 851.48 us | 1.67 ms | 1.90 ms | 2.06 ms | 1.17 ms | 6.19 ms | 6.17 ms | 648.04 ms |
| uniswap-6 | 287.60 us | **58.93 us** | 326.51 us | 435.14 us | 133.63 us | 402.58 us | 259.65 us | 494.44 us | 594.67 us | 542.25 us | 321.77 us | 1.73 ms | 1.73 ms | 207.24 ms |
| vesting-1 | 321.50 us | 165.09 us | 427.49 us | 463.66 us | **154.67 us** | 475.35 us | 271.53 us | 574.22 us | 645.81 us | 767.39 us | 453.65 us | 1.82 ms | 1.82 ms | 236.81 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/saib-inc/cardano-plutus-vm-benchmark)*