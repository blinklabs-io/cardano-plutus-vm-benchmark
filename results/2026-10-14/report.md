# Cardano Plutus VM Benchmark Results

**Date:** 2026-10-14

## Environment
```
date: 2026-10-14T16:05:48+00:00
kernel: 6.8.0-139-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
```

## Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc UPLC→native JIT (C++ / LLVM)** | C++ / LLVM | 166.18 us | 1.00x |
| **uplc-turbo Bytecode VM (Rust)** | Rust | 302.56 us | 1.82x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 359.88 us | 2.17x |
| **Plutigo CEK (Go)** | Go | 374.39 us | 2.25x |
| **uplc-turbo AST walker (Rust)** | Rust | 597.87 us | 3.60x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 632.66 us | 3.81x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 655.44 us | 3.94x |
| **Plutuz CEK (Zig)** | Zig | 671.76 us | 4.04x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 674.68 us | 4.06x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 721.93 us | 4.34x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 765.82 us | 4.61x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.35 ms | 14.13x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.38 ms | 14.34x |
| **opshin CEK (Python / CPython)** | Python / CPython | 55.45 ms | 333.70x |

### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| llvm-uplc UPLC→native JIT (C++ / LLVM) | 89 | 0 | 0 | 89 |
| uplc-turbo Bytecode VM (Rust) | 89 | 0 | 0 | 89 |
| plutus-core CEK (Haskell / GHC) | 89 | 0 | 0 | 89 |
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
| uplc-turbo AST walker (Rust) | 89 | 0 | 0 | 89 |
| Scalus UPLC→JVM JIT (Scala / JVM) | 89 | 0 | 0 | 89 |
| Julc CEK (Java / GraalVM) | 78 | 11 | 0 | 89 |
| Plutuz CEK (Zig) | 89 | 0 | 0 | 89 |
| Scalus CEK (Scala / JVM) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET AOT) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

## Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc UPLC→native JIT (C++ / LLVM) | uplc-turbo Bytecode VM (Rust) | uplc-turbo AST walker (Rust) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 166.96 us | 325.90 us | 299.37 us | 270.82 us | **69.13 us** | 138.43 us | 307.60 us | 336.66 us | 337.17 us | 351.70 us | 181.06 us | 1.18 ms | 1.21 ms | 119.75 ms |
| auction_1-2 | 577.39 us | 2.23 ms | 1.18 ms | 842.19 us | **280.97 us** | 506.81 us | 907.15 us | 1.08 ms | 1.20 ms | 1.30 ms | 622.81 us | 3.17 ms | 3.19 ms | 431.28 ms |
| auction_1-3 | 574.38 us | 1.85 ms | 1.18 ms | 859.27 us | **272.49 us** | 487.34 us | 914.57 us | 1.06 ms | 1.22 ms | 1.31 ms | 607.91 us | 3.18 ms | 3.20 ms | 434.41 ms |
| auction_1-4 | 213.62 us | 170.13 us | 379.77 us | 331.90 us | **89.00 us** | 183.04 us | 383.24 us | 402.34 us | 396.15 us | 424.53 us | 211.38 us | 1.36 ms | 1.37 ms | 143.63 ms |
| auction_2-1 | 167.51 us | 308.31 us | 298.94 us | 268.14 us | **72.82 us** | 140.28 us | 306.98 us | 339.18 us | 333.83 us | 350.91 us | 180.06 us | 1.02 ms | 1.05 ms | 120.49 ms |
| auction_2-2 | 586.41 us | 2.09 ms | 1.17 ms | 845.57 us | **278.09 us** | 488.48 us | 904.17 us | 1.07 ms | 1.21 ms | 1.30 ms | 617.09 us | 3.13 ms | 3.16 ms | 431.69 ms |
| auction_2-3 | 740.94 us | 2.19 ms | 1.52 ms | 1.06 ms | **349.21 us** | 632.52 us | 1.16 ms | 1.30 ms | 1.53 ms | 1.66 ms | 750.02 us | 4.35 ms | 4.22 ms | 543.19 ms |
| auction_2-4 | 567.67 us | 1.85 ms | 1.15 ms | 849.24 us | **270.66 us** | 486.57 us | 916.82 us | 1.04 ms | 1.21 ms | 1.28 ms | 608.34 us | 3.35 ms | 3.35 ms | 433.42 ms |
| auction_2-5 | 216.43 us | 171.29 us | 380.84 us | 335.32 us | **88.86 us** | 180.32 us | 385.05 us | 403.60 us | 413.84 us | 432.93 us | 211.00 us | 1.27 ms | 1.28 ms | 142.44 ms |
| coop-1 | 221.75 us | 98.88 us | 382.47 us | FAIL | **93.31 us** | 174.60 us | 344.54 us | 335.99 us | 346.63 us | 391.40 us | 195.89 us | 1.48 ms | 1.49 ms | FAIL |
| coop-2 | 709.12 us | 443.08 us | 1.25 ms | FAIL | **296.18 us** | 545.66 us | 1.11 ms | 1.01 ms | 1.20 ms | 1.21 ms | 628.81 us | 4.70 ms | 4.74 ms | FAIL |
| coop-3 | 2.06 ms | 1.65 ms | 4.22 ms | FAIL | **947.63 us** | 1.81 ms | 2.68 ms | 2.62 ms | 3.97 ms | 3.89 ms | 1.71 ms | 10.96 ms | 11.02 ms | FAIL |
| coop-4 | 934.20 us | 1.08 ms | 1.61 ms | FAIL | **393.06 us** | 703.97 us | 1.25 ms | 1.21 ms | 1.45 ms | 1.56 ms | 748.77 us | 5.35 ms | 5.38 ms | FAIL |
| coop-5 | 397.01 us | 307.81 us | 674.96 us | FAIL | **172.32 us** | 306.90 us | 615.73 us | 623.10 us | 701.63 us | 745.53 us | 386.91 us | 2.64 ms | 2.75 ms | FAIL |
| coop-6 | 661.15 us | 344.44 us | 1.16 ms | FAIL | **270.91 us** | 506.83 us | 1.01 ms | 878.51 us | 1.01 ms | 1.06 ms | 546.06 us | 3.88 ms | 3.95 ms | FAIL |
| coop-7 | 316.54 us | 133.67 us | 539.24 us | FAIL | **130.26 us** | 240.94 us | 489.37 us | 455.90 us | 497.42 us | 517.47 us | 273.23 us | 1.96 ms | 1.98 ms | FAIL |
| crowdfunding-success-1 | 200.02 us | 170.37 us | 347.51 us | 301.69 us | **87.81 us** | 162.96 us | 349.48 us | 393.26 us | 395.92 us | 406.98 us | 214.69 us | 1.34 ms | 1.35 ms | 142.32 ms |
| crowdfunding-success-2 | 202.48 us | 142.11 us | 351.53 us | 296.06 us | **86.83 us** | 161.29 us | 345.07 us | 393.03 us | 396.16 us | 410.95 us | 214.61 us | 1.24 ms | 1.29 ms | 143.11 ms |
| crowdfunding-success-3 | 202.36 us | 184.98 us | 350.12 us | 296.26 us | **87.17 us** | 161.12 us | 348.50 us | 394.49 us | 393.49 us | 415.04 us | 213.83 us | 1.23 ms | 1.26 ms | 141.75 ms |
| currency-1 | 227.65 us | 445.59 us | 459.88 us | 351.03 us | **109.98 us** | 196.49 us | 376.44 us | 435.64 us | 494.92 us | 522.75 us | 252.50 us | 1.43 ms | 1.48 ms | 175.07 ms |
| escrow-redeem_1-1 | 323.32 us | 501.05 us | 612.06 us | 476.43 us | **151.00 us** | 280.12 us | 517.58 us | 594.94 us | 663.49 us | 708.01 us | 342.38 us | 2.00 ms | 2.06 ms | 236.07 ms |
| escrow-redeem_1-2 | 326.48 us | 469.46 us | 620.31 us | 468.12 us | **149.63 us** | 275.62 us | 513.95 us | 587.01 us | 649.80 us | 703.62 us | 341.87 us | 1.88 ms | 1.91 ms | 234.98 ms |
| escrow-redeem_2-1 | 375.05 us | 480.48 us | 713.90 us | 539.71 us | **172.49 us** | 314.91 us | 586.83 us | 656.69 us | 743.22 us | 828.95 us | 379.79 us | 2.21 ms | 2.22 ms | 268.66 ms |
| escrow-redeem_2-2 | 374.13 us | 500.05 us | 721.29 us | 543.14 us | **173.44 us** | 315.21 us | 582.72 us | 651.47 us | 754.03 us | 823.00 us | 381.05 us | 2.28 ms | 2.34 ms | 268.04 ms |
| escrow-redeem_2-3 | 377.16 us | 529.82 us | 725.19 us | 529.34 us | **172.90 us** | 317.49 us | 585.37 us | 662.65 us | 735.29 us | 803.62 us | 379.47 us | 2.14 ms | 2.17 ms | 272.02 ms |
| escrow-refund-1 | 149.75 us | 379.65 us | 258.70 us | 254.03 us | **67.69 us** | 121.12 us | 296.97 us | 375.57 us | 351.63 us | 365.86 us | 203.25 us | 1.07 ms | 1.07 ms | 129.25 ms |
| future-increase-margin-1 | 229.34 us | 372.04 us | 458.37 us | 349.42 us | **109.18 us** | 194.80 us | 378.50 us | 437.80 us | 498.40 us | 519.56 us | 251.94 us | 1.49 ms | 1.47 ms | 176.02 ms |
| future-increase-margin-2 | 485.19 us | 780.28 us | 973.20 us | 684.98 us | **225.41 us** | 422.68 us | 754.14 us | 800.11 us | 1.00 ms | 1.04 ms | 470.93 us | 2.73 ms | 2.78 ms | 345.94 ms |
| future-increase-margin-3 | 482.62 us | 682.35 us | 970.53 us | 696.99 us | **224.81 us** | 434.67 us | 747.54 us | 816.82 us | 949.04 us | 1.02 ms | 471.69 us | 2.85 ms | 2.75 ms | 348.09 ms |
| future-increase-margin-4 | 450.17 us | 1.98 ms | 890.54 us | 719.53 us | **216.72 us** | 380.90 us | 789.71 us | 981.75 us | 1.05 ms | 1.12 ms | 548.98 us | 2.98 ms | 2.94 ms | FAIL |
| future-increase-margin-5 | 748.17 us | 3.09 ms | 1.49 ms | 1.14 ms | **388.53 us** | 648.02 us | 1.18 ms | 1.56 ms | 1.58 ms | 1.73 ms | 734.76 us | 6.70 ms | 6.83 ms | FAIL |
| future-pay-out-1 | 226.70 us | 347.76 us | 458.01 us | 351.54 us | **110.31 us** | 196.05 us | 376.86 us | 436.56 us | 491.45 us | 528.85 us | 253.75 us | 1.37 ms | 1.38 ms | 175.13 ms |
| future-pay-out-2 | 483.16 us | 655.51 us | 962.77 us | 696.77 us | **230.45 us** | 417.27 us | 753.31 us | 809.58 us | 992.30 us | 1.05 ms | 471.67 us | 2.91 ms | 2.91 ms | 343.91 ms |
| future-pay-out-3 | 488.51 us | 689.07 us | 972.27 us | 703.91 us | **228.25 us** | 419.00 us | 750.27 us | 802.63 us | 966.91 us | 1.03 ms | 471.80 us | 2.84 ms | 2.97 ms | 345.08 ms |
| future-pay-out-4 | 754.53 us | 3.12 ms | 1.49 ms | 1.14 ms | **393.73 us** | 649.54 us | 1.18 ms | 1.54 ms | 1.61 ms | 1.76 ms | 732.75 us | 6.50 ms | 6.48 ms | FAIL |
| future-settle-early-1 | 228.56 us | 449.49 us | 450.88 us | 352.04 us | **111.27 us** | 195.93 us | 376.63 us | 436.29 us | 492.88 us | 528.99 us | 252.51 us | 1.46 ms | 1.42 ms | 175.54 ms |
| future-settle-early-2 | 490.79 us | 648.35 us | 961.39 us | 685.52 us | **228.43 us** | 415.67 us | 752.43 us | 800.89 us | 968.31 us | 1.04 ms | 474.40 us | 2.91 ms | 3.08 ms | 346.99 ms |
| future-settle-early-3 | 486.77 us | 774.08 us | 964.60 us | 689.45 us | **226.98 us** | 416.33 us | 752.14 us | 812.39 us | 969.15 us | 1.05 ms | 469.35 us | 2.73 ms | 2.77 ms | 347.52 ms |
| future-settle-early-4 | 573.88 us | 2.87 ms | 1.11 ms | 894.26 us | **305.54 us** | 484.74 us | 936.62 us | 1.22 ms | 1.26 ms | 1.32 ms | 595.18 us | 5.59 ms | 5.55 ms | FAIL |
| game-sm-success_1-1 | 365.62 us | 1.67 ms | 679.30 us | 560.66 us | **173.30 us** | 297.69 us | 629.10 us | 772.59 us | 771.94 us | 828.17 us | 432.11 us | 2.54 ms | 2.55 ms | 282.02 ms |
| game-sm-success_1-2 | 185.76 us | 122.73 us | 332.36 us | 280.30 us | **79.47 us** | 158.04 us | 328.13 us | 347.56 us | 341.96 us | 355.50 us | 182.79 us | 1.14 ms | 1.16 ms | 127.65 ms |
| game-sm-success_1-3 | 587.21 us | 1.79 ms | 1.16 ms | 839.38 us | **278.94 us** | 511.87 us | 908.84 us | 1.06 ms | 1.18 ms | 1.26 ms | 606.65 us | 3.43 ms | 3.47 ms | 428.16 ms |
| game-sm-success_1-4 | 216.37 us | 120.81 us | 391.09 us | 327.44 us | **91.33 us** | 181.45 us | 374.23 us | 387.92 us | 379.95 us | 402.95 us | 203.64 us | 1.41 ms | 1.42 ms | 140.93 ms |
| game-sm-success_2-1 | 365.76 us | 1.56 ms | 677.22 us | 565.08 us | **173.29 us** | 300.76 us | 618.39 us | 773.06 us | 772.25 us | 831.06 us | 431.39 us | 2.33 ms | 2.44 ms | 281.00 ms |
| game-sm-success_2-2 | 188.96 us | 107.60 us | 329.28 us | 286.53 us | **78.72 us** | 156.41 us | 330.28 us | 349.20 us | 351.34 us | 352.68 us | 182.58 us | 1.14 ms | 1.16 ms | 126.09 ms |
| game-sm-success_2-3 | 585.27 us | 1.84 ms | 1.15 ms | 848.39 us | **278.48 us** | 490.78 us | 921.69 us | 1.07 ms | 1.17 ms | 1.26 ms | 604.91 us | 3.69 ms | 3.64 ms | 427.37 ms |
| game-sm-success_2-4 | 216.36 us | 112.56 us | 387.74 us | 327.77 us | **91.87 us** | 183.94 us | 375.51 us | 388.46 us | 388.66 us | 403.08 us | 203.08 us | 1.40 ms | 1.50 ms | 139.79 ms |
| game-sm-success_2-5 | 578.76 us | 1.77 ms | 1.16 ms | 852.02 us | **278.19 us** | 489.74 us | 911.27 us | 1.05 ms | 1.18 ms | 1.25 ms | 608.54 us | 3.39 ms | 3.46 ms | 427.73 ms |
| game-sm-success_2-6 | 214.40 us | 142.57 us | 386.40 us | 327.33 us | **90.76 us** | 182.39 us | 375.20 us | 388.85 us | 385.23 us | 401.65 us | 203.02 us | 1.35 ms | 1.35 ms | 142.54 ms |
| guardrail-sorted-large | 420.46 us | 450.27 us | 793.93 us | FAIL | **309.76 us** | 377.29 us | 654.32 us | 582.76 us | 730.83 us | 793.00 us | 453.63 us | 2.89 ms | 2.95 ms | FAIL |
| guardrail-sorted-small | 68.45 us | 120.75 us | 120.17 us | FAIL | **27.07 us** | 66.79 us | 137.66 us | 161.37 us | 166.81 us | 177.88 us | 91.93 us | 533.60 us | 537.90 us | FAIL |
| guardrail-unsorted-large | 571.12 us | 558.77 us | 1.13 ms | FAIL | **375.29 us** | 498.38 us | 822.12 us | 758.58 us | 973.72 us | 1.06 ms | 593.13 us | 3.39 ms | 3.56 ms | FAIL |
| guardrail-unsorted-small | 67.07 us | 121.93 us | 120.42 us | FAIL | **26.01 us** | 65.00 us | 135.00 us | 160.41 us | 163.41 us | 172.44 us | 90.51 us | 570.10 us | 597.60 us | FAIL |
| multisig-sm-01 | 373.94 us | 1.91 ms | 728.41 us | 598.29 us | **178.20 us** | 308.46 us | 654.04 us | 821.21 us | 836.73 us | 885.48 us | 459.48 us | 2.40 ms | 2.57 ms | FAIL |
| multisig-sm-02 | 366.92 us | 1.86 ms | 698.21 us | 574.52 us | **178.66 us** | 297.10 us | 642.92 us | 811.86 us | 813.87 us | 851.00 us | 453.60 us | 2.33 ms | 2.37 ms | FAIL |
| multisig-sm-03 | 372.40 us | 1.90 ms | 694.49 us | 587.87 us | **179.88 us** | 302.44 us | 651.89 us | 804.32 us | 813.58 us | 852.74 us | 456.57 us | 2.50 ms | 2.57 ms | FAIL |
| multisig-sm-04 | 370.40 us | 1.98 ms | 709.94 us | 578.30 us | **180.51 us** | 304.70 us | 653.00 us | 827.89 us | 828.81 us | 870.17 us | 463.47 us | 2.47 ms | 2.60 ms | FAIL |
| multisig-sm-05 | 513.59 us | 2.26 ms | 1.02 ms | 782.46 us | **248.87 us** | 431.06 us | 835.39 us | 1.00 ms | 1.14 ms | 1.21 ms | 572.01 us | 3.09 ms | 3.16 ms | FAIL |
| multisig-sm-06 | 377.85 us | 1.94 ms | 732.26 us | 598.19 us | **182.46 us** | 315.87 us | 658.58 us | 822.88 us | 830.79 us | 882.27 us | 461.98 us | 2.49 ms | 2.49 ms | FAIL |
| multisig-sm-07 | 374.36 us | 1.86 ms | 698.70 us | 578.34 us | **179.84 us** | 298.87 us | 642.14 us | 802.48 us | 792.58 us | 853.84 us | 455.12 us | 2.47 ms | 2.58 ms | FAIL |
| multisig-sm-08 | 369.79 us | 1.87 ms | 696.10 us | 579.83 us | **179.31 us** | 315.91 us | 646.48 us | 817.27 us | 825.95 us | 853.25 us | 456.43 us | 2.35 ms | 2.38 ms | FAIL |
| multisig-sm-09 | 370.18 us | 1.96 ms | 698.63 us | 583.72 us | **182.50 us** | 303.01 us | 660.13 us | 817.01 us | 844.71 us | 875.63 us | 461.49 us | 2.40 ms | 2.41 ms | FAIL |
| multisig-sm-10 | 512.38 us | 2.23 ms | 1.02 ms | 785.47 us | **251.74 us** | 432.58 us | 840.65 us | 1.01 ms | 1.11 ms | 1.19 ms | 572.13 us | 3.50 ms | 3.51 ms | FAIL |
| ping-pong-1 | 313.84 us | 1.48 ms | 585.72 us | 482.84 us | **150.32 us** | 252.19 us | 539.01 us | 684.26 us | 682.29 us | 728.56 us | 385.55 us | 1.97 ms | 2.01 ms | 250.17 ms |
| ping-pong-2 | 314.50 us | 1.48 ms | 586.86 us | 485.90 us | **151.03 us** | 254.07 us | 549.52 us | 688.98 us | 690.76 us | 741.10 us | 384.57 us | 1.97 ms | 2.01 ms | 249.38 ms |
| ping-pong_2-1 | 193.94 us | 1.01 ms | 354.50 us | 333.48 us | **95.34 us** | 157.41 us | 387.01 us | 514.99 us | 485.16 us | 520.26 us | 289.08 us | 1.49 ms | 1.51 ms | 185.10 ms |
| prism-1 | 156.56 us | 98.58 us | 273.62 us | 238.58 us | **66.20 us** | 131.13 us | 279.86 us | 306.52 us | 299.88 us | 308.28 us | 157.72 us | 993.00 us | 1.04 ms | 109.25 ms |
| prism-2 | 393.85 us | 1.46 ms | 723.42 us | 599.43 us | **184.23 us** | 316.46 us | 663.61 us | 802.46 us | 858.45 us | 896.89 us | 448.19 us | 2.35 ms | 2.38 ms | 295.75 ms |
| prism-3 | 343.80 us | 459.64 us | 653.83 us | 508.46 us | **156.08 us** | 307.55 us | 550.45 us | 592.94 us | 683.55 us | 713.13 us | 331.69 us | 2.10 ms | 2.04 ms | 234.83 ms |
| pubkey-1 | 134.70 us | 81.08 us | 231.65 us | 212.13 us | **57.97 us** | 110.30 us | 244.19 us | 273.67 us | 256.10 us | 268.55 us | 143.78 us | 893.70 us | 936.50 us | 96.77 ms |
| stablecoin_1-1 | 876.87 us | 4.85 ms | 1.59 ms | 1.44 ms | **444.82 us** | 731.26 us | 1.50 ms | 1.81 ms | 1.83 ms | 1.95 ms | 823.14 us | 9.65 ms | 9.73 ms | FAIL |
| stablecoin_1-2 | 183.74 us | 108.39 us | 323.68 us | 281.32 us | **80.14 us** | 174.23 us | 328.99 us | 341.58 us | 335.09 us | 344.04 us | 180.06 us | 1.15 ms | 1.16 ms | 122.71 ms |
| stablecoin_1-3 | 1.01 ms | 4.89 ms | 1.82 ms | 1.66 ms | **484.96 us** | 841.43 us | 1.67 ms | 2.01 ms | 2.18 ms | 2.22 ms | 912.58 us | 11.33 ms | 12.13 ms | FAIL |
| stablecoin_1-4 | 195.34 us | 111.71 us | 348.71 us | 293.56 us | **83.90 us** | 164.12 us | 344.69 us | 359.27 us | 350.44 us | 382.08 us | 188.25 us | 1.18 ms | 1.21 ms | 132.33 ms |
| stablecoin_1-5 | 1.26 ms | 4.94 ms | 2.26 ms | 2.11 ms | **562.79 us** | 1.07 ms | 2.22 ms | 2.48 ms | 2.63 ms | 2.76 ms | 1.10 ms | 12.51 ms | 12.44 ms | FAIL |
| stablecoin_1-6 | 240.12 us | 138.53 us | 428.09 us | 364.95 us | **102.52 us** | 205.20 us | 412.42 us | 417.26 us | 411.12 us | 449.22 us | 218.34 us | 1.55 ms | 1.66 ms | 151.83 ms |
| stablecoin_2-1 | 884.90 us | 4.76 ms | 1.58 ms | 1.43 ms | **445.02 us** | 731.59 us | 1.48 ms | 1.81 ms | 1.92 ms | 1.93 ms | 824.83 us | 9.59 ms | 9.78 ms | FAIL |
| stablecoin_2-2 | 183.92 us | 91.00 us | 331.22 us | 278.17 us | **80.05 us** | 153.56 us | 327.66 us | 343.44 us | 342.89 us | 346.63 us | 179.62 us | 1.12 ms | 1.15 ms | 122.15 ms |
| stablecoin_2-3 | 1.01 ms | 5.07 ms | 1.84 ms | 1.63 ms | **483.34 us** | 841.82 us | 1.67 ms | 2.00 ms | 2.08 ms | 2.21 ms | 909.46 us | 11.63 ms | 11.30 ms | FAIL |
| stablecoin_2-4 | 190.96 us | 103.84 us | 346.14 us | 296.89 us | **83.97 us** | 161.90 us | 346.41 us | 360.56 us | 349.44 us | 382.02 us | 187.81 us | 1.20 ms | 1.24 ms | 131.16 ms |
| token-account-1 | 174.49 us | 435.98 us | 338.75 us | 285.60 us | **85.55 us** | 148.53 us | 313.79 us | 373.57 us | 388.09 us | 419.10 us | 207.68 us | 1.11 ms | 1.12 ms | 137.68 ms |
| token-account-2 | 308.45 us | 202.27 us | 602.32 us | 451.06 us | **145.17 us** | 263.22 us | 469.80 us | 518.25 us | 600.16 us | 646.69 us | 303.13 us | 1.81 ms | 1.79 ms | 219.03 ms |
| uniswap-1 | 360.39 us | 455.26 us | 798.73 us | 511.06 us | **173.88 us** | 323.01 us | 553.25 us | 619.71 us | 759.54 us | 830.51 us | 367.81 us | 2.16 ms | 2.20 ms | 281.29 ms |
| uniswap-2 | 208.66 us | 494.76 us | 394.98 us | 331.31 us | **98.48 us** | 177.19 us | 364.71 us | 413.25 us | 430.23 us | 472.63 us | 231.49 us | 1.29 ms | 1.31 ms | 155.67 ms |
| uniswap-3 | 1.58 ms | 2.27 ms | 2.95 ms | 2.15 ms | **625.32 us** | 1.29 ms | 2.33 ms | 2.54 ms | 2.83 ms | 3.22 ms | 1.42 ms | 9.40 ms | 9.30 ms | 967.73 ms |
| uniswap-4 | 304.69 us | 160.56 us | 556.12 us | 463.07 us | **131.97 us** | 269.96 us | 526.86 us | 522.97 us | 558.20 us | 574.84 us | 278.81 us | 1.96 ms | 2.04 ms | 193.39 ms |
| uniswap-5 | 1.06 ms | 2.32 ms | 1.93 ms | 1.47 ms | **431.58 us** | 858.78 us | 1.61 ms | 1.71 ms | 2.02 ms | 2.14 ms | 1.01 ms | 6.35 ms | 6.27 ms | 660.46 ms |
| uniswap-6 | 294.20 us | 168.26 us | 533.25 us | 443.22 us | **127.50 us** | 247.97 us | 502.36 us | 504.93 us | 536.92 us | 558.35 us | 264.55 us | 1.77 ms | 1.77 ms | 187.99 ms |
| vesting-1 | 329.06 us | 1.05 ms | 628.64 us | 467.78 us | **159.80 us** | 269.63 us | 508.97 us | 585.50 us | 670.88 us | 705.59 us | 351.81 us | 2.03 ms | 2.05 ms | 241.09 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/saib-inc/cardano-plutus-vm-benchmark)*