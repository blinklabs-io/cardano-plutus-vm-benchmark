# Cardano Plutus VM Benchmark Results

**Date:** 2026-10-27-0

## Environment
```
date: 2026-10-27T13:19:28-04:00
kernel: 6.8.0-139-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
comparison: Plutigo v0.10.0 measured twice and Amaru UPLC v0.4.0 from the Amaru monorepo measured on 2026-10-27; other VM measurements carried forward from 2026-10-26
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
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

## Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc UPLC→native JIT (C++ / LLVM) | Amaru UPLC CEK (Rust) | uplc-turbo Bytecode VM (Rust) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 164.18 us | **42.05 us** | 224.08 us | 265.03 us | 70.53 us | 253.11 us | 157.61 us | 331.00 us | 330.65 us | 345.07 us | 239.17 us | 1.08 ms | 1.11 ms | 115.24 ms |
| auction_1-2 | 568.48 us | 990.94 us | 725.19 us | 839.14 us | **274.42 us** | 820.44 us | 488.23 us | 1.10 ms | 1.15 ms | 1.32 ms | 736.03 us | 3.17 ms | 3.30 ms | 437.64 ms |
| auction_1-3 | 577.55 us | 662.30 us | 725.20 us | 826.59 us | **267.28 us** | 828.75 us | 477.79 us | 1.01 ms | 1.16 ms | 1.24 ms | 738.98 us | 3.19 ms | 3.21 ms | 422.81 ms |
| auction_1-4 | 213.00 us | **50.65 us** | 259.23 us | 327.25 us | 88.54 us | 300.70 us | 174.07 us | 392.24 us | 440.37 us | 416.18 us | 265.82 us | 1.28 ms | 1.25 ms | 137.03 ms |
| auction_2-1 | 168.37 us | **41.30 us** | 222.64 us | 264.49 us | 73.46 us | 253.02 us | 135.95 us | 330.36 us | 339.71 us | 383.87 us | 232.03 us | 1.02 ms | 1.00 ms | 115.51 ms |
| auction_2-2 | 568.87 us | 902.84 us | 725.35 us | 826.47 us | **273.71 us** | 820.89 us | 480.85 us | 1.04 ms | 1.20 ms | 1.27 ms | 754.56 us | 3.15 ms | 3.09 ms | 413.96 ms |
| auction_2-3 | 730.67 us | 931.38 us | 871.32 us | 1.06 ms | **357.47 us** | 1.03 ms | 626.41 us | 1.34 ms | 1.48 ms | 1.60 ms | 891.08 us | 3.96 ms | 3.88 ms | 521.80 ms |
| auction_2-4 | 560.21 us | 598.99 us | 717.98 us | 832.00 us | **271.71 us** | 820.33 us | 479.62 us | 1.01 ms | 1.22 ms | 1.24 ms | 727.32 us | 3.17 ms | 3.12 ms | 416.24 ms |
| auction_2-5 | 210.67 us | **47.31 us** | 254.19 us | 329.78 us | 93.63 us | 300.02 us | 171.99 us | 392.09 us | 392.60 us | 414.60 us | 264.65 us | 1.27 ms | 1.25 ms | 138.41 ms |
| coop-1 | 218.66 us | **40.99 us** | 255.18 us | FAIL | 95.35 us | 253.13 us | 168.00 us | 330.38 us | 339.93 us | 373.28 us | 240.90 us | 1.44 ms | 1.37 ms | FAIL |
| coop-2 | 691.00 us | **161.89 us** | 758.80 us | FAIL | 294.37 us | 739.13 us | 537.44 us | 1.04 ms | 1.42 ms | 1.18 ms | 712.33 us | 4.46 ms | 4.29 ms | FAIL |
| coop-3 | 1.97 ms | **665.37 us** | 2.09 ms | FAIL | 943.73 us | 2.27 ms | 1.79 ms | 2.52 ms | 3.80 ms | 3.70 ms | 1.85 ms | 10.92 ms | 11.40 ms | FAIL |
| coop-4 | 915.03 us | **244.48 us** | 951.75 us | FAIL | 394.47 us | 919.39 us | 676.07 us | 1.15 ms | 1.41 ms | 1.49 ms | 868.04 us | 5.34 ms | 5.20 ms | FAIL |
| coop-5 | 385.33 us | **90.33 us** | 466.92 us | FAIL | 168.16 us | 462.94 us | 309.14 us | 605.71 us | 821.72 us | 723.54 us | 468.61 us | 2.49 ms | 2.40 ms | FAIL |
| coop-6 | 641.65 us | **146.19 us** | 674.98 us | FAIL | 285.37 us | 646.49 us | 490.05 us | 893.76 us | 961.84 us | 1.01 ms | 610.00 us | 3.95 ms | 3.80 ms | FAIL |
| coop-7 | 303.35 us | **54.90 us** | 342.32 us | FAIL | 128.77 us | 349.41 us | 238.04 us | 445.09 us | 512.44 us | 502.56 us | 316.71 us | 1.99 ms | 1.88 ms | FAIL |
| crowdfunding-success-1 | 197.29 us | **39.29 us** | 265.15 us | 299.71 us | 87.02 us | 285.43 us | 157.15 us | 382.46 us | 381.24 us | 403.98 us | 273.59 us | 1.24 ms | 1.21 ms | 138.08 ms |
| crowdfunding-success-2 | 196.97 us | **40.59 us** | 263.67 us | 297.06 us | 86.01 us | 285.02 us | 157.19 us | 381.94 us | 378.98 us | 397.08 us | 275.90 us | 1.25 ms | 1.76 ms | 146.38 ms |
| crowdfunding-success-3 | 197.02 us | **42.86 us** | 269.97 us | 295.86 us | 92.61 us | 284.72 us | 158.64 us | 381.60 us | 379.58 us | 425.97 us | 288.86 us | 1.25 ms | 1.21 ms | 135.70 ms |
| currency-1 | 223.42 us | **61.69 us** | 304.28 us | 343.97 us | 107.93 us | 343.61 us | 190.71 us | 460.80 us | 479.31 us | 513.76 us | 314.17 us | 1.37 ms | 1.33 ms | 175.89 ms |
| escrow-redeem_1-1 | 317.61 us | **80.21 us** | 415.62 us | 463.61 us | 147.81 us | 446.02 us | 290.01 us | 573.47 us | 635.04 us | 682.66 us | 419.50 us | 1.91 ms | 1.85 ms | 225.93 ms |
| escrow-redeem_1-2 | 322.45 us | **78.43 us** | 416.72 us | 451.71 us | 147.46 us | 457.52 us | 267.76 us | 573.04 us | 641.40 us | 711.78 us | 431.80 us | 1.90 ms | 1.85 ms | 226.09 ms |
| escrow-redeem_2-1 | 367.91 us | **99.20 us** | 459.84 us | 535.40 us | 183.06 us | 501.83 us | 325.23 us | 635.15 us | 724.06 us | 782.22 us | 467.24 us | 2.16 ms | 2.09 ms | 257.16 ms |
| escrow-redeem_2-2 | 368.35 us | **105.22 us** | 457.92 us | 529.74 us | 169.16 us | 501.51 us | 317.35 us | 634.96 us | 746.27 us | 784.64 us | 465.39 us | 2.16 ms | 2.10 ms | 254.38 ms |
| escrow-redeem_2-3 | 372.51 us | **97.71 us** | 456.03 us | 519.09 us | 168.67 us | 501.75 us | 321.64 us | 634.84 us | 729.15 us | 782.16 us | 459.83 us | 2.17 ms | 2.10 ms | 257.14 ms |
| escrow-refund-1 | 145.01 us | **33.41 us** | 265.71 us | 247.51 us | 67.47 us | 258.21 us | 114.09 us | 362.99 us | 333.44 us | 414.64 us | 274.92 us | 1.06 ms | 1.03 ms | 123.65 ms |
| future-increase-margin-1 | 220.60 us | **62.86 us** | 302.40 us | 341.81 us | 107.47 us | 337.05 us | 192.47 us | 460.73 us | 486.47 us | 511.13 us | 313.72 us | 1.37 ms | 1.33 ms | 168.75 ms |
| future-increase-margin-2 | 510.60 us | **140.92 us** | 547.74 us | 683.13 us | 238.03 us | 629.53 us | 407.56 us | 798.00 us | 925.66 us | 1.00 ms | 554.89 us | 4.55 ms | 2.66 ms | 351.79 ms |
| future-increase-margin-3 | 475.45 us | **161.67 us** | 550.36 us | 674.22 us | 233.57 us | 640.90 us | 410.34 us | 776.71 us | 946.98 us | 1.07 ms | 570.94 us | 3.11 ms | 2.66 ms | 332.05 ms |
| future-increase-margin-4 | 439.57 us | 517.41 us | 685.37 us | 690.96 us | **227.81 us** | 716.34 us | 369.04 us | 955.90 us | 1.30 ms | 1.08 ms | 682.94 us | 2.78 ms | 2.70 ms | FAIL |
| future-increase-margin-5 | 725.78 us | 1.47 ms | 932.72 us | 1.12 ms | **379.94 us** | 1.08 ms | 625.66 us | 1.49 ms | 1.54 ms | 1.69 ms | 876.31 us | 6.89 ms | 6.50 ms | FAIL |
| future-pay-out-1 | 224.04 us | **63.87 us** | 301.74 us | 344.20 us | 110.17 us | 338.50 us | 197.16 us | 424.86 us | 473.86 us | 511.59 us | 312.85 us | 1.35 ms | 1.35 ms | 173.64 ms |
| future-pay-out-2 | 482.86 us | **133.41 us** | 551.68 us | 685.61 us | 221.22 us | 630.82 us | 449.69 us | 840.71 us | 949.20 us | 1.01 ms | 577.22 us | 2.69 ms | 2.69 ms | 333.82 ms |
| future-pay-out-3 | 485.49 us | **142.32 us** | 549.02 us | 658.88 us | 220.85 us | 629.95 us | 424.18 us | 775.96 us | 1.09 ms | 1.04 ms | 559.84 us | 2.70 ms | 2.69 ms | 330.66 ms |
| future-pay-out-4 | 726.00 us | 1.49 ms | 940.24 us | 1.13 ms | **405.61 us** | 1.08 ms | 624.69 us | 1.49 ms | 1.60 ms | 1.71 ms | 878.01 us | 6.40 ms | 6.37 ms | FAIL |
| future-settle-early-1 | 225.40 us | **66.19 us** | 302.50 us | 347.72 us | 107.85 us | 342.32 us | 196.63 us | 424.39 us | 477.38 us | 546.57 us | 313.22 us | 1.35 ms | 1.34 ms | 170.71 ms |
| future-settle-early-2 | 481.14 us | **151.59 us** | 548.44 us | 657.07 us | 236.47 us | 631.50 us | 411.22 us | 813.92 us | 930.35 us | 1.01 ms | 553.54 us | 2.70 ms | 2.70 ms | 330.39 ms |
| future-settle-early-3 | 527.61 us | **169.46 us** | 549.03 us | 676.61 us | 222.34 us | 631.78 us | 411.92 us | 797.98 us | 1.00 ms | 1.01 ms | 555.04 us | 2.69 ms | 2.69 ms | 330.46 ms |
| future-settle-early-4 | 562.21 us | 1.20 ms | 789.10 us | 876.57 us | **305.23 us** | 852.91 us | 470.32 us | 1.19 ms | 1.21 ms | 1.51 ms | 731.56 us | 5.47 ms | 5.47 ms | FAIL |
| game-sm-success_1-1 | 360.56 us | 349.08 us | 533.35 us | 546.72 us | **168.89 us** | 549.65 us | 306.51 us | 783.72 us | 748.03 us | 835.50 us | 543.53 us | 2.28 ms | 2.28 ms | 268.17 ms |
| game-sm-success_1-2 | 190.49 us | **38.98 us** | 219.47 us | 277.47 us | 77.18 us | 261.85 us | 153.20 us | 346.89 us | 336.61 us | 344.63 us | 227.67 us | 1.13 ms | 1.13 ms | 120.98 ms |
| game-sm-success_1-3 | 563.85 us | 558.63 us | 718.88 us | 824.22 us | **271.99 us** | 824.69 us | 487.61 us | 1.03 ms | 1.16 ms | 1.22 ms | 739.27 us | 3.40 ms | 3.39 ms | 408.86 ms |
| game-sm-success_1-4 | 214.84 us | **44.26 us** | 242.58 us | 313.27 us | 96.23 us | 291.48 us | 184.70 us | 379.12 us | 376.49 us | 390.36 us | 252.54 us | 1.29 ms | 1.29 ms | 134.81 ms |
| game-sm-success_2-1 | 369.10 us | 316.31 us | 537.36 us | 545.66 us | **169.01 us** | 551.75 us | 298.27 us | 749.95 us | 893.81 us | 815.02 us | 550.18 us | 2.28 ms | 2.29 ms | 273.43 ms |
| game-sm-success_2-2 | 186.86 us | **38.64 us** | 220.79 us | 280.99 us | 84.33 us | 260.34 us | 147.85 us | 339.13 us | 340.62 us | 349.07 us | 230.50 us | 1.13 ms | 1.13 ms | 121.21 ms |
| game-sm-success_2-3 | 580.61 us | 583.84 us | 708.61 us | 829.96 us | **272.00 us** | 804.31 us | 495.21 us | 1.10 ms | 1.16 ms | 1.22 ms | 720.33 us | 3.39 ms | 3.38 ms | 412.22 ms |
| game-sm-success_2-4 | 229.18 us | **43.86 us** | 238.17 us | 317.09 us | 91.12 us | 293.44 us | 175.59 us | 376.86 us | 396.65 us | 391.56 us | 250.11 us | 1.30 ms | 1.49 ms | 134.87 ms |
| game-sm-success_2-5 | 601.28 us | 622.97 us | 706.07 us | 824.34 us | **271.45 us** | 813.91 us | 485.20 us | 1.02 ms | 1.15 ms | 1.35 ms | 723.54 us | 3.38 ms | 3.63 ms | 410.41 ms |
| game-sm-success_2-6 | 208.41 us | **43.82 us** | 244.68 us | 325.12 us | 89.21 us | 295.37 us | 180.26 us | 376.11 us | 374.50 us | 389.79 us | 250.48 us | 1.30 ms | 1.29 ms | 134.70 ms |
| guardrail-sorted-large | 401.35 us | **231.07 us** | 492.25 us | FAIL | 301.31 us | 506.60 us | 374.06 us | 559.23 us | 854.64 us | 776.48 us | 513.15 us | 2.66 ms | 2.64 ms | FAIL |
| guardrail-sorted-small | 74.49 us | 86.35 us | 125.67 us | FAIL | **26.75 us** | 126.00 us | 64.60 us | 158.72 us | 162.88 us | 178.37 us | 125.07 us | 528.70 us | 530.00 us | FAIL |
| guardrail-unsorted-large | 557.78 us | **303.89 us** | 652.30 us | FAIL | 366.45 us | 651.29 us | 481.42 us | 788.55 us | 931.71 us | 1.02 ms | 626.24 us | 3.35 ms | 3.36 ms | FAIL |
| guardrail-unsorted-small | 65.23 us | 84.66 us | 118.42 us | FAIL | **28.76 us** | 123.33 us | 63.02 us | 155.67 us | 163.15 us | 169.36 us | 123.92 us | 520.30 us | 521.60 us | FAIL |
| multisig-sm-01 | 366.15 us | 385.31 us | 578.71 us | 584.07 us | **174.89 us** | 594.81 us | 301.67 us | 800.72 us | 820.08 us | 866.55 us | 595.50 us | 2.39 ms | 2.39 ms | FAIL |
| multisig-sm-02 | 358.07 us | 495.95 us | 564.41 us | 561.49 us | **173.06 us** | 590.06 us | 291.37 us | 810.13 us | 886.99 us | 827.13 us | 582.53 us | 2.33 ms | 2.33 ms | FAIL |
| multisig-sm-03 | 360.22 us | 448.47 us | 576.24 us | 574.03 us | **174.79 us** | 589.06 us | 293.14 us | 789.39 us | 792.62 us | 836.61 us | 579.98 us | 2.33 ms | 2.34 ms | FAIL |
| multisig-sm-04 | 365.15 us | 495.67 us | 571.16 us | 574.11 us | **176.67 us** | 588.33 us | 302.44 us | 799.84 us | 820.91 us | 847.96 us | 583.91 us | 2.36 ms | 2.37 ms | FAIL |
| multisig-sm-05 | 502.89 us | 869.46 us | 696.12 us | 765.92 us | **244.86 us** | 782.67 us | 467.31 us | 979.60 us | 1.37 ms | 1.16 ms | 724.71 us | 3.07 ms | 3.07 ms | FAIL |
| multisig-sm-06 | 366.35 us | 378.09 us | 581.25 us | 590.53 us | **176.47 us** | 600.57 us | 304.03 us | 805.74 us | 798.96 us | 866.86 us | 583.34 us | 2.37 ms | 2.37 ms | FAIL |
| multisig-sm-07 | 361.50 us | 502.59 us | 567.62 us | 565.07 us | **173.84 us** | 580.73 us | 290.94 us | 790.13 us | 781.99 us | 845.97 us | 575.64 us | 2.33 ms | 2.33 ms | FAIL |
| multisig-sm-08 | 357.66 us | 476.98 us | 582.31 us | 567.51 us | **180.36 us** | 592.69 us | 292.72 us | 786.52 us | 937.45 us | 910.18 us | 594.85 us | 2.34 ms | 2.34 ms | FAIL |
| multisig-sm-09 | 374.81 us | 460.17 us | 582.88 us | 575.86 us | **178.16 us** | 605.97 us | 297.29 us | 797.39 us | 807.65 us | 851.78 us | 586.18 us | 2.36 ms | 2.36 ms | FAIL |
| multisig-sm-10 | 512.63 us | 851.12 us | 689.16 us | 765.31 us | **246.09 us** | 771.50 us | 420.23 us | 978.26 us | 1.10 ms | 1.17 ms | 695.14 us | 3.08 ms | 3.07 ms | FAIL |
| ping-pong-1 | 308.89 us | 202.73 us | 485.08 us | 471.54 us | **147.31 us** | 485.83 us | 244.31 us | 666.63 us | 665.99 us | 759.01 us | 513.98 us | 1.97 ms | 1.97 ms | 239.04 ms |
| ping-pong-2 | 304.64 us | 225.52 us | 486.37 us | 480.94 us | **147.83 us** | 489.92 us | 267.34 us | 691.27 us | 808.14 us | 710.18 us | 492.83 us | 1.99 ms | 1.97 ms | 260.59 ms |
| ping-pong_2-1 | 187.00 us | **83.81 us** | 388.54 us | 327.75 us | 100.27 us | 354.15 us | 152.56 us | 504.92 us | 474.36 us | 503.05 us | 389.25 us | 2.43 ms | 1.39 ms | 172.71 ms |
| prism-1 | 152.44 us | **30.50 us** | 200.70 us | 237.31 us | 65.25 us | 226.22 us | 132.03 us | 300.35 us | 289.73 us | 297.68 us | 203.82 us | 974.20 us | 981.60 us | 104.33 ms |
| prism-2 | 379.64 us | 299.72 us | 561.18 us | 582.57 us | **180.57 us** | 582.61 us | 339.06 us | 791.65 us | 806.38 us | 846.44 us | 558.50 us | 2.33 ms | 2.33 ms | 298.87 ms |
| prism-3 | 336.36 us | **95.09 us** | 396.14 us | 497.48 us | 153.36 us | 465.20 us | 281.32 us | 573.80 us | 652.70 us | 693.56 us | 397.77 us | 1.94 ms | 1.94 ms | 225.30 ms |
| pubkey-1 | 132.76 us | **25.66 us** | 183.76 us | 207.06 us | 56.90 us | 200.44 us | 109.24 us | 267.12 us | 249.16 us | 258.96 us | 192.60 us | 848.60 us | 847.50 us | 92.49 ms |
| stablecoin_1-1 | 860.74 us | 2.48 ms | 1.16 ms | 1.40 ms | **436.35 us** | 1.28 ms | 708.77 us | 1.74 ms | 1.82 ms | 1.91 ms | 990.12 us | 9.54 ms | 9.55 ms | FAIL |
| stablecoin_1-2 | 179.35 us | **37.72 us** | 216.71 us | 274.01 us | 79.03 us | 266.47 us | 149.83 us | 333.50 us | 329.55 us | 337.56 us | 231.97 us | 1.12 ms | 1.12 ms | 118.04 ms |
| stablecoin_1-3 | 1.02 ms | 2.53 ms | 1.23 ms | 1.63 ms | **477.11 us** | 1.53 ms | 822.77 us | 2.05 ms | 2.07 ms | 2.15 ms | 1.09 ms | 10.34 ms | 10.32 ms | FAIL |
| stablecoin_1-4 | 188.64 us | **39.02 us** | 225.45 us | 285.35 us | 88.69 us | 268.43 us | 155.81 us | 347.74 us | 345.77 us | 366.33 us | 236.42 us | 1.18 ms | 1.18 ms | 124.85 ms |
| stablecoin_1-5 | 1.25 ms | 2.64 ms | 1.43 ms | 2.06 ms | **554.03 us** | 1.89 ms | 1.03 ms | 2.42 ms | 3.05 ms | 2.78 ms | 1.31 ms | 12.16 ms | 12.17 ms | FAIL |
| stablecoin_1-6 | 233.84 us | **45.28 us** | 256.88 us | 357.72 us | 101.14 us | 317.70 us | 200.25 us | 423.62 us | 406.12 us | 438.98 us | 266.46 us | 1.40 ms | 1.40 ms | 146.30 ms |
| stablecoin_2-1 | 880.33 us | 2.40 ms | 1.16 ms | 1.36 ms | **434.93 us** | 1.29 ms | 709.08 us | 1.73 ms | 1.80 ms | 1.90 ms | 990.52 us | 9.57 ms | 9.56 ms | FAIL |
| stablecoin_2-2 | 185.63 us | **36.55 us** | 213.88 us | 272.16 us | 78.48 us | 256.76 us | 146.21 us | 333.84 us | 336.99 us | 336.13 us | 225.46 us | 1.13 ms | 1.12 ms | 119.17 ms |
| stablecoin_2-3 | 977.84 us | 2.58 ms | 1.24 ms | 1.64 ms | **475.97 us** | 1.50 ms | 823.15 us | 1.92 ms | 2.11 ms | 2.14 ms | 1.10 ms | 10.36 ms | 10.30 ms | FAIL |
| stablecoin_2-4 | 212.38 us | **38.53 us** | 227.75 us | 288.29 us | 82.14 us | 271.07 us | 155.79 us | 348.40 us | 341.28 us | 369.96 us | 233.73 us | 1.18 ms | 1.18 ms | 127.58 ms |
| token-account-1 | 169.90 us | **49.12 us** | 255.21 us | 275.80 us | 87.11 us | 284.42 us | 150.94 us | 378.31 us | 381.75 us | 468.39 us | 269.65 us | 1.10 ms | 1.10 ms | 133.65 ms |
| token-account-2 | 296.37 us | **69.44 us** | 352.12 us | 433.26 us | 142.44 us | 408.66 us | 254.51 us | 514.54 us | 581.99 us | 625.47 us | 362.61 us | 1.69 ms | 1.70 ms | 213.18 ms |
| uniswap-1 | 370.66 us | **95.77 us** | 411.83 us | 515.59 us | 170.51 us | 490.28 us | 321.33 us | 596.39 us | 747.64 us | 876.86 us | 428.96 us | 2.03 ms | 2.02 ms | 271.57 ms |
| uniswap-2 | 200.90 us | **55.99 us** | 287.79 us | 320.88 us | 96.93 us | 313.54 us | 168.93 us | 401.91 us | 422.19 us | 454.44 us | 297.69 us | 1.28 ms | 1.28 ms | 159.71 ms |
| uniswap-3 | 1.52 ms | 844.99 us | 1.57 ms | 2.09 ms | **618.34 us** | 2.07 ms | 1.28 ms | 2.46 ms | 2.83 ms | 3.06 ms | 1.61 ms | 9.01 ms | 8.96 ms | 947.06 ms |
| uniswap-4 | 298.02 us | **59.97 us** | 324.61 us | 447.35 us | 131.34 us | 399.24 us | 284.76 us | 546.79 us | 539.57 us | 560.39 us | 333.61 us | 1.81 ms | 1.80 ms | 185.78 ms |
| uniswap-5 | 1.04 ms | 670.69 us | 1.18 ms | 1.39 ms | **424.53 us** | 1.37 ms | 849.28 us | 1.64 ms | 2.21 ms | 2.06 ms | 1.17 ms | 6.22 ms | 6.22 ms | 653.73 ms |
| uniswap-6 | 283.86 us | **58.52 us** | 317.39 us | 431.16 us | 125.82 us | 388.62 us | 246.11 us | 489.71 us | 517.77 us | 537.76 us | 323.35 us | 1.78 ms | 1.74 ms | 179.82 ms |
| vesting-1 | 316.78 us | 180.74 us | 421.26 us | 451.64 us | **155.66 us** | 460.02 us | 261.53 us | 570.04 us | 721.69 us | 686.61 us | 443.57 us | 2.27 ms | 1.83 ms | 230.33 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/saib-inc/cardano-plutus-vm-benchmark)*