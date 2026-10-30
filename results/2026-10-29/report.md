# Cardano Plutus VM Benchmark Results

**Date:** 2026-10-29

## Environment
```
date: 2026-10-29T20:14:01+00:00
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
| Plutigo CEK (Go) | v0.10.1 ([6ac112f](https://github.com/blinklabs-io/plutigo/commit/6ac112f17d22f8b130952a53f979c571e5a2a357)) | Go 1.27.3 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 0.5.3 ([320fc36](https://github.com/butaneprotocol/blaze-cardano/commit/320fc3604cfeac640013fd8206efaecfe8a2360f)) | Bun 1.3.14 |
| blaze-plutus CEK (TypeScript / Node V8) | 0.5.3 ([320fc36](https://github.com/butaneprotocol/blaze-cardano/commit/320fc3604cfeac640013fd8206efaecfe8a2360f)) | Node.js 22 |
| opshin CEK (Python / CPython) | 1.3.3 ([eda2fba](https://github.com/OpShin/uplc/commit/eda2fbaa89c1a2db4ec6c6c1fa5eea2a8b2671d4)) | Python 3.14 |

## Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc UPLC→native JIT (C++ / LLVM)** | C++ / LLVM | 164.19 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 176.73 us | 1.08x |
| **uplc-turbo Bytecode VM (Rust)** | Rust | 300.59 us | 1.83x |
| **Plutigo CEK (Go)** | Go | 351.62 us | 2.14x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 352.89 us | 2.15x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 459.10 us | 2.80x |
| **Amaru UPLC CEK (Rust)** | Rust | 529.00 us | 3.22x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 647.37 us | 3.94x |
| **Plutuz CEK (Zig)** | Zig | 659.83 us | 4.02x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 712.58 us | 4.34x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 754.92 us | 4.60x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.33 ms | 14.22x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.34 ms | 14.27x |
| **opshin CEK (Python / CPython)** | Python / CPython | 54.90 ms | 334.36x |

### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| llvm-uplc UPLC→native JIT (C++ / LLVM) | 89 | 0 | 0 | 89 |
| Scalus UPLC→JVM JIT (Scala / JVM) | 89 | 0 | 0 | 89 |
| uplc-turbo Bytecode VM (Rust) | 89 | 0 | 0 | 89 |
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
| plutus-core CEK (Haskell / GHC) | 89 | 0 | 0 | 89 |
| Scalus CEK (Scala / JVM) | 89 | 0 | 0 | 89 |
| Amaru UPLC CEK (Rust) | 89 | 0 | 0 | 89 |
| Julc CEK (Java / GraalVM) | 78 | 11 | 0 | 89 |
| Plutuz CEK (Zig) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET AOT) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

## Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc UPLC→native JIT (C++ / LLVM) | Amaru UPLC CEK (Rust) | uplc-turbo Bytecode VM (Rust) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 162.22 us | **42.03 us** | 220.21 us | 263.29 us | 69.04 us | 266.88 us | 137.18 us | 342.27 us | 328.68 us | 338.94 us | 181.28 us | 1.11 ms | 1.07 ms | 115.72 ms |
| auction_1-2 | 576.24 us | 1.02 ms | 743.42 us | 815.89 us | **273.50 us** | 841.03 us | 510.03 us | 1.03 ms | 1.42 ms | 1.28 ms | 577.72 us | 3.35 ms | 3.15 ms | 435.38 ms |
| auction_1-3 | 563.27 us | 798.24 us | 717.20 us | 843.24 us | **268.35 us** | 835.43 us | 496.52 us | 1.01 ms | 1.17 ms | 1.24 ms | 559.29 us | 3.29 ms | 3.16 ms | 416.03 ms |
| auction_1-4 | 213.77 us | **48.36 us** | 260.81 us | 331.26 us | 86.97 us | 343.75 us | 176.81 us | 392.38 us | 401.55 us | 434.94 us | 195.60 us | 1.29 ms | 1.25 ms | 137.85 ms |
| auction_2-1 | 163.77 us | **42.44 us** | 223.86 us | 261.92 us | 71.16 us | 264.22 us | 135.94 us | 348.10 us | 336.93 us | 342.51 us | 167.95 us | 1.07 ms | 1.01 ms | 115.89 ms |
| auction_2-2 | 566.14 us | 959.37 us | 724.32 us | 844.43 us | **277.34 us** | 837.56 us | 484.95 us | 1.03 ms | 1.17 ms | 1.27 ms | 591.56 us | 3.29 ms | 3.12 ms | 412.57 ms |
| auction_2-3 | 747.17 us | 1.02 ms | 889.90 us | 1.04 ms | **343.99 us** | 1.07 ms | 621.90 us | 1.25 ms | 1.57 ms | 1.67 ms | 703.31 us | 4.00 ms | 3.93 ms | 532.56 ms |
| auction_2-4 | 558.53 us | 628.61 us | 722.16 us | 839.54 us | **266.67 us** | 861.01 us | 478.36 us | 1.01 ms | 1.16 ms | 1.26 ms | 559.45 us | 3.15 ms | 3.15 ms | 429.92 ms |
| auction_2-5 | 210.14 us | **48.39 us** | 256.26 us | 333.69 us | 88.94 us | 320.57 us | 185.90 us | 413.34 us | 396.25 us | 414.72 us | 195.71 us | 1.27 ms | 1.26 ms | 142.27 ms |
| coop-1 | 227.51 us | **40.55 us** | 251.35 us | FAIL | 93.61 us | 276.40 us | 169.71 us | 331.52 us | 335.53 us | 376.37 us | 194.31 us | 1.45 ms | 1.61 ms | FAIL |
| coop-2 | 686.08 us | **159.50 us** | 772.84 us | FAIL | 289.70 us | 780.82 us | 536.58 us | 1.00 ms | 1.16 ms | 1.20 ms | 598.84 us | 4.47 ms | 4.67 ms | FAIL |
| coop-3 | 1.98 ms | **662.89 us** | 2.12 ms | FAIL | 932.72 us | 2.37 ms | 1.79 ms | 2.54 ms | 3.95 ms | 3.99 ms | 1.73 ms | 11.10 ms | 11.07 ms | FAIL |
| coop-4 | 925.51 us | **243.32 us** | 938.19 us | FAIL | 390.12 us | 999.24 us | 681.52 us | 1.15 ms | 1.44 ms | 1.50 ms | 720.01 us | 5.27 ms | 5.35 ms | FAIL |
| coop-5 | 382.63 us | **85.18 us** | 483.29 us | FAIL | 169.61 us | 489.27 us | 303.68 us | 645.24 us | 675.46 us | 719.40 us | 375.33 us | 2.47 ms | 2.65 ms | FAIL |
| coop-6 | 644.54 us | **145.80 us** | 682.93 us | FAIL | 266.17 us | 690.29 us | 505.34 us | 832.25 us | 968.01 us | 1.02 ms | 514.00 us | 3.93 ms | 4.02 ms | FAIL |
| coop-7 | 306.58 us | **55.19 us** | 338.94 us | FAIL | 133.93 us | 370.96 us | 234.68 us | 444.31 us | 477.64 us | 518.39 us | 258.74 us | 1.99 ms | 2.08 ms | FAIL |
| crowdfunding-success-1 | 197.06 us | **40.32 us** | 266.63 us | 298.84 us | 85.40 us | 298.52 us | 158.75 us | 381.16 us | 376.89 us | 417.53 us | 197.61 us | 1.25 ms | 1.22 ms | 136.43 ms |
| crowdfunding-success-2 | 199.25 us | **41.41 us** | 267.88 us | 296.81 us | 87.05 us | 303.99 us | 164.34 us | 381.09 us | 380.72 us | 401.21 us | 201.91 us | 1.26 ms | 1.22 ms | 159.09 ms |
| crowdfunding-success-3 | 200.45 us | **40.50 us** | 265.21 us | 296.53 us | 84.78 us | 298.27 us | 160.41 us | 381.62 us | 431.83 us | 425.79 us | 205.94 us | 1.26 ms | 1.22 ms | 142.35 ms |
| currency-1 | 221.57 us | **63.88 us** | 302.95 us | 342.21 us | 108.10 us | 353.09 us | 193.86 us | 424.44 us | 486.77 us | 541.45 us | 235.34 us | 1.38 ms | 1.34 ms | 169.52 ms |
| escrow-redeem_1-1 | 327.34 us | **90.70 us** | 417.04 us | 467.24 us | 148.40 us | 460.38 us | 265.10 us | 572.70 us | 643.72 us | 697.39 us | 325.98 us | 1.91 ms | 1.87 ms | 226.90 ms |
| escrow-redeem_1-2 | 317.41 us | **86.83 us** | 412.77 us | 458.91 us | 147.44 us | 466.48 us | 269.10 us | 618.66 us | 631.59 us | 683.39 us | 315.37 us | 1.91 ms | 1.86 ms | 226.29 ms |
| escrow-redeem_2-1 | 368.22 us | **102.76 us** | 460.70 us | 526.38 us | 169.76 us | 520.95 us | 307.22 us | 668.15 us | 737.36 us | 788.89 us | 350.62 us | 2.18 ms | 2.12 ms | 257.69 ms |
| escrow-redeem_2-2 | 365.56 us | **97.05 us** | 466.22 us | 535.76 us | 182.21 us | 530.08 us | 312.74 us | 645.40 us | 730.72 us | 782.00 us | 350.06 us | 2.18 ms | 2.12 ms | 255.11 ms |
| escrow-redeem_2-3 | 368.81 us | **97.12 us** | 453.84 us | 516.46 us | 168.86 us | 516.50 us | 318.85 us | 635.35 us | 743.04 us | 782.21 us | 351.34 us | 2.17 ms | 2.12 ms | 272.22 ms |
| escrow-refund-1 | 145.87 us | **32.83 us** | 268.69 us | 246.27 us | 68.59 us | 270.35 us | 117.66 us | 381.38 us | 343.55 us | 367.50 us | 185.16 us | 1.06 ms | 1.04 ms | 131.80 ms |
| future-increase-margin-1 | 220.42 us | **58.78 us** | 300.63 us | 344.74 us | 107.99 us | 352.45 us | 192.39 us | 432.83 us | 488.27 us | 525.42 us | 232.88 us | 1.38 ms | 1.34 ms | 176.39 ms |
| future-increase-margin-2 | 490.19 us | **141.84 us** | 544.81 us | 666.29 us | 227.97 us | 649.28 us | 415.17 us | 785.05 us | 979.93 us | 1.05 ms | 467.11 us | 2.77 ms | 2.69 ms | 340.94 ms |
| future-increase-margin-3 | 481.44 us | **141.39 us** | 551.47 us | 678.41 us | 221.95 us | 648.88 us | 415.75 us | 776.92 us | 953.84 us | 1.02 ms | 440.31 us | 2.78 ms | 3.27 ms | 339.71 ms |
| future-increase-margin-4 | 435.49 us | 545.93 us | 667.95 us | 691.98 us | **212.52 us** | 765.04 us | 430.70 us | 954.03 us | 1.01 ms | 1.10 ms | 502.23 us | 2.79 ms | 4.14 ms | FAIL |
| future-increase-margin-5 | 761.28 us | 1.52 ms | 946.72 us | 1.10 ms | **381.14 us** | 1.09 ms | 625.27 us | 1.49 ms | 1.69 ms | 1.69 ms | 674.25 us | 6.65 ms | 6.55 ms | FAIL |
| future-pay-out-1 | 221.09 us | **65.25 us** | 304.18 us | 343.09 us | 106.41 us | 345.92 us | 193.98 us | 425.58 us | 476.37 us | 511.52 us | 230.96 us | 1.50 ms | 1.36 ms | 168.57 ms |
| future-pay-out-2 | 474.29 us | **168.69 us** | 548.68 us | 670.89 us | 228.57 us | 660.09 us | 411.36 us | 780.42 us | 961.53 us | 1.00 ms | 436.88 us | 2.79 ms | 2.70 ms | 336.14 ms |
| future-pay-out-3 | 532.19 us | **149.97 us** | 561.50 us | 673.95 us | 231.81 us | 657.55 us | 422.55 us | 803.96 us | 953.32 us | 1.01 ms | 447.56 us | 2.81 ms | 2.71 ms | 332.10 ms |
| future-pay-out-4 | 730.65 us | 1.53 ms | 918.54 us | 1.10 ms | **379.44 us** | 1.09 ms | 641.64 us | 1.58 ms | 1.64 ms | 1.70 ms | 675.55 us | 6.53 ms | 6.41 ms | FAIL |
| future-settle-early-1 | 221.69 us | **64.12 us** | 297.97 us | 341.36 us | 106.72 us | 351.79 us | 195.98 us | 428.61 us | 479.32 us | 511.80 us | 231.66 us | 1.41 ms | 1.36 ms | 170.11 ms |
| future-settle-early-2 | 492.78 us | **145.99 us** | 552.24 us | 687.99 us | 227.16 us | 649.42 us | 409.89 us | 784.17 us | 947.54 us | 1.08 ms | 453.91 us | 2.79 ms | 2.72 ms | 342.59 ms |
| future-settle-early-3 | 476.69 us | **149.07 us** | 559.22 us | 672.26 us | 222.20 us | 651.44 us | 408.04 us | 777.24 us | 953.96 us | 1.06 ms | 445.31 us | 2.79 ms | 2.71 ms | 332.17 ms |
| future-settle-early-4 | 586.13 us | 1.30 ms | 797.67 us | 868.85 us | **305.84 us** | 924.53 us | 482.95 us | 1.24 ms | 1.22 ms | 1.32 ms | 545.21 us | 5.55 ms | 5.48 ms | FAIL |
| game-sm-success_1-1 | 356.04 us | 309.58 us | 535.39 us | 548.37 us | **169.70 us** | 570.36 us | 292.89 us | 763.97 us | 746.03 us | 810.58 us | 403.20 us | 2.34 ms | 2.30 ms | 280.82 ms |
| game-sm-success_1-2 | 184.40 us | **38.13 us** | 220.59 us | 273.45 us | 77.24 us | 273.25 us | 157.82 us | 339.07 us | 346.90 us | 341.00 us | 173.46 us | 1.21 ms | 1.14 ms | 121.75 ms |
| game-sm-success_1-3 | 559.12 us | 549.64 us | 718.94 us | 829.06 us | **272.32 us** | 832.53 us | 500.77 us | 1.02 ms | 1.18 ms | 1.23 ms | 561.90 us | 3.55 ms | 3.43 ms | 414.96 ms |
| game-sm-success_1-4 | 208.77 us | **44.66 us** | 243.48 us | 318.89 us | 97.66 us | 307.73 us | 176.82 us | 376.50 us | 378.01 us | 389.59 us | 187.18 us | 1.34 ms | 1.30 ms | 135.33 ms |
| game-sm-success_2-1 | 362.90 us | 316.43 us | 544.05 us | 551.98 us | **167.49 us** | 566.63 us | 302.67 us | 751.16 us | 797.98 us | 826.86 us | 412.08 us | 2.35 ms | 2.30 ms | 268.75 ms |
| game-sm-success_2-2 | 182.34 us | **38.59 us** | 215.58 us | 283.32 us | 75.27 us | 280.31 us | 180.56 us | 349.68 us | 337.11 us | 342.54 us | 169.56 us | 1.16 ms | 1.20 ms | 121.84 ms |
| game-sm-success_2-3 | 561.76 us | 642.29 us | 712.45 us | 817.77 us | **279.72 us** | 823.32 us | 480.02 us | 1.06 ms | 1.17 ms | 1.22 ms | 585.23 us | 3.51 ms | 3.40 ms | 417.76 ms |
| game-sm-success_2-4 | 210.32 us | **43.95 us** | 248.92 us | 324.10 us | 87.20 us | 308.51 us | 187.23 us | 376.14 us | 382.07 us | 395.52 us | 187.86 us | 1.34 ms | 1.30 ms | 142.60 ms |
| game-sm-success_2-5 | 566.86 us | 560.13 us | 700.59 us | 814.16 us | **272.54 us** | 823.57 us | 489.93 us | 1.02 ms | 1.16 ms | 1.26 ms | 603.64 us | 3.47 ms | 3.39 ms | 409.33 ms |
| game-sm-success_2-6 | 210.91 us | **44.01 us** | 244.49 us | 314.25 us | 88.49 us | 307.51 us | 178.94 us | 376.70 us | 393.46 us | 393.47 us | 187.81 us | 1.35 ms | 1.30 ms | 135.47 ms |
| guardrail-sorted-large | 402.76 us | **227.14 us** | 495.97 us | FAIL | 299.04 us | 529.75 us | 371.47 us | 608.13 us | 704.43 us | 768.64 us | 392.22 us | 2.73 ms | 2.92 ms | FAIL |
| guardrail-sorted-small | 67.26 us | 83.75 us | 124.83 us | FAIL | **27.05 us** | 130.04 us | 64.54 us | 158.43 us | 164.07 us | 174.02 us | 94.12 us | 539.20 us | 692.70 us | FAIL |
| guardrail-unsorted-large | 562.32 us | **293.06 us** | 662.18 us | FAIL | 365.52 us | 683.38 us | 511.59 us | 734.43 us | 923.00 us | 1.03 ms | 527.94 us | 3.62 ms | 3.74 ms | FAIL |
| guardrail-unsorted-small | 65.85 us | 84.06 us | 118.33 us | FAIL | **25.25 us** | 126.67 us | 65.24 us | 155.92 us | 157.13 us | 168.50 us | 92.02 us | 530.50 us | 677.70 us | FAIL |
| multisig-sm-01 | 368.80 us | 381.20 us | 575.21 us | 579.73 us | **177.35 us** | 605.28 us | 308.33 us | 806.59 us | 803.03 us | 889.85 us | 431.41 us | 2.45 ms | 2.39 ms | FAIL |
| multisig-sm-02 | 356.50 us | 468.40 us | 557.09 us | 578.29 us | **174.92 us** | 614.43 us | 301.73 us | 800.27 us | 788.97 us | 829.61 us | 435.53 us | 2.39 ms | 2.33 ms | FAIL |
| multisig-sm-03 | 364.85 us | 512.20 us | 571.83 us | 575.83 us | **177.44 us** | 598.77 us | 297.28 us | 786.41 us | 840.13 us | 901.64 us | 424.87 us | 2.40 ms | 2.34 ms | FAIL |
| multisig-sm-04 | 368.23 us | 520.13 us | 579.10 us | 565.87 us | **183.90 us** | 603.65 us | 300.06 us | 809.60 us | 825.46 us | 849.76 us | 427.29 us | 2.42 ms | 2.37 ms | FAIL |
| multisig-sm-05 | 499.88 us | 830.28 us | 688.03 us | 788.25 us | **245.63 us** | 805.24 us | 426.91 us | 1.01 ms | 1.13 ms | 1.16 ms | 541.40 us | 3.16 ms | 3.09 ms | FAIL |
| multisig-sm-06 | 376.62 us | 402.01 us | 572.52 us | 580.63 us | **185.61 us** | 616.52 us | 337.09 us | 829.28 us | 839.27 us | 865.72 us | 426.58 us | 2.43 ms | 2.39 ms | FAIL |
| multisig-sm-07 | 357.59 us | 491.16 us | 559.41 us | 570.20 us | **175.06 us** | 595.62 us | 295.16 us | 784.44 us | 799.33 us | 829.49 us | 421.92 us | 2.39 ms | 2.32 ms | FAIL |
| multisig-sm-08 | 359.36 us | 566.87 us | 561.08 us | 566.59 us | **182.24 us** | 622.86 us | 299.12 us | 789.46 us | 791.85 us | 847.41 us | 427.69 us | 2.40 ms | 2.34 ms | FAIL |
| multisig-sm-09 | 362.53 us | 497.83 us | 577.63 us | 575.28 us | **196.83 us** | 607.91 us | 332.35 us | 803.21 us | 819.01 us | 852.54 us | 426.77 us | 2.42 ms | 2.36 ms | FAIL |
| multisig-sm-10 | 504.82 us | 831.52 us | 692.39 us | 760.14 us | **247.27 us** | 789.29 us | 425.40 us | 979.58 us | 1.12 ms | 1.18 ms | 537.26 us | 3.16 ms | 3.10 ms | FAIL |
| ping-pong-1 | 301.32 us | 207.51 us | 481.66 us | 473.64 us | **151.14 us** | 511.71 us | 249.61 us | 668.88 us | 677.69 us | 845.78 us | 364.52 us | 2.86 ms | 1.97 ms | 252.10 ms |
| ping-pong-2 | 303.41 us | 225.48 us | 486.24 us | 484.09 us | **149.67 us** | 555.28 us | 249.07 us | 674.00 us | 674.34 us | 725.53 us | 354.80 us | 2.03 ms | 1.97 ms | 239.32 ms |
| ping-pong_2-1 | 189.61 us | **81.11 us** | 387.85 us | 331.27 us | 92.06 us | 367.79 us | 157.11 us | 515.13 us | 468.59 us | 522.17 us | 263.69 us | 1.43 ms | 1.40 ms | 173.89 ms |
| prism-1 | 151.38 us | **30.25 us** | 193.33 us | 233.98 us | 65.28 us | 239.37 us | 126.92 us | 297.12 us | 289.35 us | 300.78 us | 145.88 us | 1.01 ms | 1.41 ms | 116.23 ms |
| prism-2 | 376.14 us | 289.45 us | 557.31 us | 597.22 us | **178.56 us** | 597.44 us | 319.45 us | 799.25 us | 837.26 us | 844.03 us | 431.65 us | 2.42 ms | 2.95 ms | 286.90 ms |
| prism-3 | 334.97 us | **92.70 us** | 399.89 us | 497.45 us | 154.26 us | 482.88 us | 299.02 us | 595.32 us | 661.67 us | 704.23 us | 309.63 us | 2.01 ms | 1.95 ms | 225.10 ms |
| pubkey-1 | 131.63 us | **25.80 us** | 177.16 us | 202.83 us | 56.67 us | 211.72 us | 113.22 us | 267.11 us | 249.88 us | 256.67 us | 132.10 us | 871.30 us | 853.10 us | 96.88 ms |
| stablecoin_1-1 | 855.45 us | 2.40 ms | 1.17 ms | 1.43 ms | **435.73 us** | 1.33 ms | 730.21 us | 1.73 ms | 1.88 ms | 2.05 ms | 765.10 us | 9.67 ms | 9.53 ms | FAIL |
| stablecoin_1-2 | 184.80 us | **38.55 us** | 219.38 us | 275.91 us | 76.88 us | 281.81 us | 158.03 us | 333.41 us | 329.66 us | 342.40 us | 172.12 us | 1.16 ms | 1.12 ms | 124.64 ms |
| stablecoin_1-3 | 983.48 us | 2.60 ms | 1.24 ms | 1.61 ms | **486.57 us** | 1.54 ms | 821.21 us | 1.93 ms | 2.06 ms | 2.23 ms | 863.90 us | 10.57 ms | 10.34 ms | FAIL |
| stablecoin_1-4 | 186.85 us | **39.56 us** | 228.03 us | 291.46 us | 81.51 us | 285.31 us | 165.55 us | 348.20 us | 339.32 us | 366.63 us | 173.65 us | 1.22 ms | 1.17 ms | 131.57 ms |
| stablecoin_1-5 | 1.36 ms | 2.70 ms | 1.47 ms | 2.04 ms | **564.59 us** | 1.88 ms | 1.04 ms | 2.48 ms | 2.55 ms | 2.67 ms | 1.03 ms | 12.30 ms | 12.64 ms | FAIL |
| stablecoin_1-6 | 233.17 us | **47.77 us** | 259.92 us | 352.99 us | 103.42 us | 334.23 us | 197.52 us | 404.18 us | 410.83 us | 432.88 us | 207.39 us | 1.46 ms | 1.47 ms | 158.40 ms |
| stablecoin_2-1 | 859.82 us | 2.51 ms | 1.17 ms | 1.40 ms | **434.59 us** | 1.46 ms | 723.31 us | 1.73 ms | 1.87 ms | 1.90 ms | 764.91 us | 9.69 ms | 9.89 ms | FAIL |
| stablecoin_2-2 | 178.88 us | **39.22 us** | 217.48 us | 274.85 us | 77.52 us | 272.23 us | 151.57 us | 333.61 us | 344.01 us | 338.10 us | 167.62 us | 1.16 ms | 1.14 ms | 120.55 ms |
| stablecoin_2-3 | 976.29 us | 2.64 ms | 1.24 ms | 1.62 ms | **481.33 us** | 1.54 ms | 842.67 us | 1.92 ms | 2.13 ms | 2.14 ms | 856.75 us | 10.47 ms | 10.77 ms | FAIL |
| stablecoin_2-4 | 190.84 us | **38.88 us** | 233.00 us | 286.00 us | 81.22 us | 282.60 us | 160.74 us | 376.72 us | 345.36 us | 395.94 us | 173.00 us | 1.22 ms | 1.19 ms | 125.91 ms |
| token-account-1 | 168.79 us | **49.81 us** | 256.93 us | 281.11 us | 83.38 us | 286.66 us | 152.70 us | 383.15 us | 381.69 us | 422.53 us | 199.12 us | 1.17 ms | 1.19 ms | 133.59 ms |
| token-account-2 | 296.28 us | **73.04 us** | 350.74 us | 433.70 us | 146.49 us | 429.93 us | 256.51 us | 515.70 us | 588.67 us | 620.41 us | 282.62 us | 1.83 ms | 1.76 ms | 211.79 ms |
| uniswap-1 | 351.48 us | **98.11 us** | 407.75 us | 504.57 us | 170.29 us | 500.27 us | 322.71 us | 596.68 us | 750.29 us | 837.16 us | 353.16 us | 2.20 ms | 2.12 ms | 267.91 ms |
| uniswap-2 | 198.68 us | **51.52 us** | 290.94 us | 331.58 us | 98.99 us | 323.48 us | 173.23 us | 422.40 us | 420.14 us | 454.12 us | 213.34 us | 1.39 ms | 1.32 ms | 160.79 ms |
| uniswap-3 | 1.55 ms | 959.55 us | 1.60 ms | 2.05 ms | **611.56 us** | 2.06 ms | 1.31 ms | 2.45 ms | 2.90 ms | 3.06 ms | 1.32 ms | 10.08 ms | 9.58 ms | 946.97 ms |
| uniswap-4 | 296.22 us | **61.24 us** | 331.76 us | 455.25 us | 132.70 us | 448.15 us | 259.78 us | 508.24 us | 577.66 us | 565.86 us | 265.98 us | 2.13 ms | 1.89 ms | 189.83 ms |
| uniswap-5 | 1.03 ms | 699.71 us | 1.19 ms | 1.41 ms | **420.23 us** | 1.40 ms | 871.17 us | 1.64 ms | 1.98 ms | 2.07 ms | 934.25 us | 6.90 ms | 6.26 ms | 634.62 ms |
| uniswap-6 | 290.56 us | **59.20 us** | 328.20 us | 435.94 us | 123.87 us | 409.70 us | 262.52 us | 510.38 us | 516.86 us | 539.18 us | 261.25 us | 1.86 ms | 1.74 ms | 195.02 ms |
| vesting-1 | 316.73 us | **150.95 us** | 422.82 us | 464.74 us | 158.94 us | 485.24 us | 263.02 us | 572.98 us | 648.26 us | 765.16 us | 328.18 us | 1.92 ms | 2.27 ms | 230.46 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/saib-inc/cardano-plutus-vm-benchmark)*