# Cardano Plutus VM Benchmark Results

**Date:** 2026-10-13

## Environment
```
date: 2026-10-13T21:34:53+00:00
kernel: 6.8.0-139-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
```

## Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc UPLC→native JIT (C++ / LLVM)** | C++ / LLVM | 166.44 us | 1.00x |
| **uplc-turbo Bytecode VM (Rust)** | Rust | 300.99 us | 1.81x |
| **Plutigo CEK (Go)** | Go | 371.70 us | 2.23x |
| **uplc-turbo AST walker (Rust)** | Rust | 600.50 us | 3.61x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 654.84 us | 3.93x |
| **Plutuz CEK (Zig)** | Zig | 668.12 us | 4.01x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 673.68 us | 4.05x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 725.66 us | 4.36x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 764.24 us | 4.59x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 905.83 us | 5.44x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.34 ms | 14.06x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.36 ms | 14.15x |
| **opshin CEK (Python / CPython)** | Python / CPython | 56.25 ms | 337.95x |

### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| llvm-uplc UPLC→native JIT (C++ / LLVM) | 89 | 0 | 0 | 89 |
| uplc-turbo Bytecode VM (Rust) | 89 | 0 | 0 | 89 |
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
| uplc-turbo AST walker (Rust) | 89 | 0 | 0 | 89 |
| Julc CEK (Java / GraalVM) | 78 | 11 | 0 | 89 |
| Plutuz CEK (Zig) | 89 | 0 | 0 | 89 |
| Scalus CEK (Scala / JVM) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET AOT) | 89 | 0 | 0 | 89 |
| Scalus UPLC→JVM JIT (Scala / JVM) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

## Per-Script Results

| Script | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc UPLC→native JIT (C++ / LLVM) | uplc-turbo Bytecode VM (Rust) | uplc-turbo AST walker (Rust) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 429.53 us | 302.02 us | 266.38 us | **72.33 us** | 137.95 us | 312.97 us | 335.86 us | 338.91 us | 347.19 us | 180.44 us | 1.14 ms | 1.22 ms | 123.86 ms |
| auction_1-2 | 2.48 ms | 1.16 ms | 839.69 us | **281.70 us** | 496.84 us | 911.33 us | 1.07 ms | 1.23 ms | 1.30 ms | 612.44 us | 3.17 ms | 3.18 ms | 440.50 ms |
| auction_1-3 | 2.21 ms | 1.18 ms | 844.74 us | **273.93 us** | 487.28 us | 915.88 us | 1.03 ms | 1.23 ms | 1.30 ms | 606.06 us | 3.23 ms | 3.19 ms | 443.70 ms |
| auction_1-4 | 235.91 us | 379.90 us | 331.19 us | **89.69 us** | 174.84 us | 388.60 us | 402.09 us | 406.77 us | 427.00 us | 210.18 us | 1.37 ms | 1.42 ms | 146.44 ms |
| auction_2-1 | 431.85 us | 304.99 us | 267.35 us | **73.10 us** | 143.82 us | 309.61 us | 338.81 us | 332.48 us | 348.56 us | 182.03 us | 1.02 ms | 1.02 ms | 126.39 ms |
| auction_2-2 | 2.49 ms | 1.17 ms | 866.60 us | **280.73 us** | 483.44 us | 903.93 us | 1.07 ms | 1.20 ms | 1.30 ms | 615.84 us | 3.15 ms | 3.15 ms | 444.62 ms |
| auction_2-3 | 2.45 ms | 1.55 ms | 1.07 ms | **349.88 us** | 625.59 us | 1.15 ms | 1.29 ms | 1.52 ms | 1.68 ms | 739.62 us | 4.26 ms | 4.18 ms | 557.24 ms |
| auction_2-4 | 2.33 ms | 1.16 ms | 860.82 us | **273.78 us** | 484.94 us | 914.08 us | 1.04 ms | 1.21 ms | 1.28 ms | 601.16 us | 3.21 ms | 3.28 ms | 446.44 ms |
| auction_2-5 | 220.99 us | 379.11 us | 334.24 us | **90.33 us** | 175.43 us | 389.70 us | 401.11 us | 403.09 us | 433.09 us | 209.49 us | 1.26 ms | 1.27 ms | 148.25 ms |
| coop-1 | 108.94 us | 383.65 us | FAIL | **93.61 us** | 170.38 us | 342.43 us | 333.87 us | 344.86 us | 385.56 us | 193.98 us | 1.49 ms | 1.46 ms | FAIL |
| coop-2 | 701.64 us | 1.22 ms | FAIL | **295.25 us** | 538.19 us | 1.10 ms | 1.00 ms | 1.20 ms | 1.22 ms | 610.44 us | 4.64 ms | 4.72 ms | FAIL |
| coop-3 | 2.49 ms | 4.20 ms | FAIL | **947.14 us** | 1.79 ms | 2.70 ms | 2.60 ms | 3.91 ms | 3.86 ms | 1.69 ms | 10.92 ms | 10.99 ms | FAIL |
| coop-4 | 2.07 ms | 1.59 ms | FAIL | **395.51 us** | 682.10 us | 1.22 ms | 1.21 ms | 1.47 ms | 1.53 ms | 746.10 us | 5.36 ms | 5.41 ms | FAIL |
| coop-5 | 434.82 us | 684.09 us | FAIL | **172.05 us** | 300.18 us | 618.93 us | 620.47 us | 707.62 us | 737.09 us | 383.29 us | 2.79 ms | 2.69 ms | FAIL |
| coop-6 | 357.07 us | 1.13 ms | FAIL | **268.77 us** | 497.03 us | 1.00 ms | 881.06 us | 1.01 ms | 1.02 ms | 542.39 us | 3.90 ms | 3.93 ms | FAIL |
| coop-7 | 140.52 us | 529.28 us | FAIL | **129.47 us** | 237.13 us | 487.15 us | 456.97 us | 493.07 us | 520.30 us | 272.40 us | 1.95 ms | 1.96 ms | FAIL |
| crowdfunding-success-1 | 367.56 us | 350.39 us | 304.07 us | **87.58 us** | 158.71 us | 350.62 us | 391.46 us | 387.14 us | 419.11 us | 212.64 us | 1.33 ms | 1.36 ms | 145.68 ms |
| crowdfunding-success-2 | 350.92 us | 348.24 us | 303.68 us | **87.43 us** | 157.14 us | 349.10 us | 391.96 us | 386.04 us | 407.16 us | 212.34 us | 1.23 ms | 1.26 ms | 143.37 ms |
| crowdfunding-success-3 | 322.47 us | 345.88 us | 299.09 us | **86.82 us** | 159.31 us | 350.97 us | 390.24 us | 396.71 us | 405.72 us | 213.05 us | 1.23 ms | 1.25 ms | 145.36 ms |
| currency-1 | 802.48 us | 460.25 us | 342.89 us | **110.28 us** | 199.50 us | 381.92 us | 432.77 us | 496.61 us | 526.58 us | 250.44 us | 1.44 ms | 1.47 ms | 179.93 ms |
| escrow-redeem_1-1 | 1.00 ms | 618.82 us | 475.70 us | **151.91 us** | 288.65 us | 528.81 us | 589.87 us | 670.59 us | 699.77 us | 341.88 us | 1.93 ms | 1.99 ms | 239.46 ms |
| escrow-redeem_1-2 | 1.00 ms | 620.60 us | 464.56 us | **151.88 us** | 267.35 us | 520.23 us | 587.30 us | 660.90 us | 705.81 us | 340.69 us | 1.89 ms | 1.90 ms | 240.50 ms |
| escrow-redeem_2-1 | 960.38 us | 713.15 us | 535.41 us | **173.77 us** | 310.26 us | 592.94 us | 656.27 us | 753.30 us | 796.61 us | 376.91 us | 2.22 ms | 2.23 ms | 273.79 ms |
| escrow-redeem_2-2 | 877.66 us | 724.29 us | 532.73 us | **173.05 us** | 318.52 us | 593.11 us | 647.87 us | 763.05 us | 800.88 us | 376.85 us | 2.24 ms | 2.30 ms | 272.91 ms |
| escrow-redeem_2-3 | 943.48 us | 725.38 us | 544.83 us | **173.75 us** | 309.80 us | 596.55 us | 656.48 us | 760.90 us | 803.84 us | 378.20 us | 2.14 ms | 2.15 ms | 276.37 ms |
| escrow-refund-1 | 774.66 us | 257.26 us | 252.07 us | **68.18 us** | 117.83 us | 299.12 us | 371.84 us | 351.42 us | 363.47 us | 200.87 us | 1.08 ms | 1.09 ms | 132.36 ms |
| future-increase-margin-1 | 743.85 us | 449.96 us | 354.89 us | **108.90 us** | 217.54 us | 380.08 us | 435.87 us | 500.97 us | 532.84 us | 250.44 us | 1.48 ms | 1.46 ms | 180.18 ms |
| future-increase-margin-2 | 1.19 ms | 963.14 us | 697.50 us | **226.44 us** | 413.05 us | 759.46 us | 796.51 us | 963.72 us | 1.02 ms | 469.05 us | 2.73 ms | 2.75 ms | 353.62 ms |
| future-increase-margin-3 | 1.02 ms | 956.22 us | 688.20 us | **225.07 us** | 418.00 us | 750.01 us | 806.35 us | 965.78 us | 1.04 ms | 470.97 us | 2.73 ms | 2.74 ms | 356.85 ms |
| future-increase-margin-4 | 2.38 ms | 913.29 us | 703.86 us | **218.21 us** | 379.65 us | 794.68 us | 974.85 us | 1.05 ms | 1.11 ms | 538.34 us | 3.24 ms | 2.93 ms | FAIL |
| future-increase-margin-5 | 3.83 ms | 1.46 ms | 1.15 ms | **393.13 us** | 645.36 us | 1.21 ms | 1.55 ms | 1.60 ms | 1.73 ms | 727.68 us | 6.63 ms | 6.89 ms | FAIL |
| future-pay-out-1 | 709.05 us | 452.92 us | 356.06 us | **109.96 us** | 195.24 us | 387.05 us | 432.94 us | 480.88 us | 525.94 us | 253.42 us | 1.37 ms | 1.35 ms | 177.34 ms |
| future-pay-out-2 | 1.08 ms | 985.53 us | 694.01 us | **226.79 us** | 414.80 us | 757.78 us | 797.51 us | 996.50 us | 1.03 ms | 469.72 us | 2.92 ms | 2.83 ms | 352.06 ms |
| future-pay-out-3 | 1.02 ms | 984.61 us | 686.53 us | **226.72 us** | 448.02 us | 753.60 us | 805.10 us | 980.30 us | 1.05 ms | 471.71 us | 2.85 ms | 2.84 ms | 354.11 ms |
| future-pay-out-4 | 3.78 ms | 1.47 ms | 1.16 ms | **391.60 us** | 637.40 us | 1.19 ms | 1.54 ms | 1.63 ms | 1.73 ms | 730.46 us | 6.45 ms | 6.41 ms | FAIL |
| future-settle-early-1 | 759.77 us | 455.24 us | 342.32 us | **109.39 us** | 199.95 us | 378.18 us | 435.32 us | 475.51 us | 529.07 us | 250.65 us | 1.42 ms | 1.38 ms | 180.41 ms |
| future-settle-early-2 | 1.06 ms | 966.08 us | 695.58 us | **226.74 us** | 411.11 us | 760.43 us | 797.77 us | 967.06 us | 1.05 ms | 469.70 us | 2.85 ms | 2.95 ms | 352.06 ms |
| future-settle-early-3 | 1.07 ms | 967.73 us | 690.25 us | **228.49 us** | 413.23 us | 751.85 us | 801.61 us | 986.26 us | 1.04 ms | 469.68 us | 2.71 ms | 2.70 ms | 352.12 ms |
| future-settle-early-4 | 3.09 ms | 1.11 ms | 909.12 us | **310.36 us** | 481.64 us | 938.19 us | 1.21 ms | 1.26 ms | 1.34 ms | 588.81 us | 5.75 ms | 5.47 ms | FAIL |
| game-sm-success_1-1 | 1.94 ms | 669.70 us | 570.53 us | **174.83 us** | 297.82 us | 630.72 us | 773.26 us | 792.63 us | 843.86 us | 428.08 us | 2.57 ms | 2.57 ms | 286.96 ms |
| game-sm-success_1-2 | 179.67 us | 336.69 us | 280.53 us | **78.56 us** | 155.73 us | 330.15 us | 346.93 us | 352.17 us | 352.67 us | 180.77 us | 1.14 ms | 1.14 ms | 128.73 ms |
| game-sm-success_1-3 | 2.08 ms | 1.15 ms | 848.97 us | **280.92 us** | 493.91 us | 906.36 us | 1.06 ms | 1.19 ms | 1.26 ms | 603.02 us | 3.46 ms | 3.42 ms | 437.50 ms |
| game-sm-success_1-4 | 248.94 us | 380.50 us | 317.84 us | **90.74 us** | 178.85 us | 376.95 us | 386.05 us | 383.69 us | 409.51 us | 202.06 us | 1.48 ms | 1.39 ms | 142.58 ms |
| game-sm-success_2-1 | 1.90 ms | 673.92 us | 565.46 us | **173.42 us** | 294.30 us | 621.71 us | 768.07 us | 795.57 us | 835.98 us | 430.31 us | 2.31 ms | 2.39 ms | 285.39 ms |
| game-sm-success_2-2 | 181.64 us | 332.96 us | 285.97 us | **78.54 us** | 153.15 us | 332.09 us | 348.07 us | 347.37 us | 350.82 us | 180.12 us | 1.14 ms | 1.12 ms | 128.31 ms |
| game-sm-success_2-3 | 2.00 ms | 1.16 ms | 855.16 us | **279.69 us** | 495.31 us | 910.69 us | 1.05 ms | 1.19 ms | 1.27 ms | 600.13 us | 3.67 ms | 3.55 ms | 436.43 ms |
| game-sm-success_2-4 | 170.81 us | 391.87 us | 322.00 us | **91.33 us** | 204.75 us | 378.15 us | 384.90 us | 391.51 us | 403.85 us | 201.47 us | 1.42 ms | 1.37 ms | 142.49 ms |
| game-sm-success_2-5 | 2.28 ms | 1.14 ms | 850.85 us | **280.63 us** | 493.63 us | 920.68 us | 1.06 ms | 1.18 ms | 1.26 ms | 608.32 us | 3.39 ms | 3.39 ms | 436.22 ms |
| game-sm-success_2-6 | 213.45 us | 387.68 us | 323.75 us | **91.07 us** | 178.15 us | 378.77 us | 386.92 us | 399.57 us | 403.34 us | 201.19 us | 1.34 ms | 1.31 ms | 143.67 ms |
| guardrail-sorted-large | 459.38 us | 783.95 us | FAIL | **309.66 us** | 376.56 us | 664.38 us | 572.89 us | 718.57 us | 778.22 us | 456.86 us | 2.85 ms | 2.93 ms | FAIL |
| guardrail-sorted-small | 135.56 us | 123.44 us | FAIL | **27.28 us** | 65.61 us | 136.44 us | 161.64 us | 167.81 us | 178.34 us | 92.42 us | 534.10 us | 527.70 us | FAIL |
| guardrail-unsorted-large | 623.82 us | 1.12 ms | FAIL | **375.79 us** | 496.17 us | 820.87 us | 751.06 us | 961.79 us | 1.05 ms | 571.62 us | 3.54 ms | 3.55 ms | FAIL |
| guardrail-unsorted-small | 120.99 us | 120.50 us | FAIL | **26.09 us** | 64.05 us | 135.09 us | 157.55 us | 166.71 us | 172.99 us | 89.96 us | 576.90 us | 555.40 us | FAIL |
| multisig-sm-01 | 2.23 ms | 718.49 us | 599.89 us | **183.59 us** | 308.18 us | 663.66 us | 819.26 us | 835.64 us | 896.88 us | 455.22 us | 2.42 ms | 2.42 ms | FAIL |
| multisig-sm-02 | 2.29 ms | 715.23 us | 570.87 us | **178.42 us** | 300.74 us | 647.10 us | 805.95 us | 821.59 us | 859.98 us | 449.89 us | 2.35 ms | 2.34 ms | FAIL |
| multisig-sm-03 | 2.24 ms | 692.04 us | 576.32 us | **182.16 us** | 304.96 us | 654.67 us | 805.97 us | 824.93 us | 862.99 us | 451.05 us | 2.51 ms | 2.45 ms | FAIL |
| multisig-sm-04 | 2.27 ms | 693.96 us | 583.29 us | **185.25 us** | 311.74 us | 658.40 us | 821.85 us | 848.38 us | 890.27 us | 460.44 us | 2.45 ms | 2.48 ms | FAIL |
| multisig-sm-05 | 2.68 ms | 1.04 ms | 795.38 us | **251.85 us** | 428.54 us | 848.86 us | 1.00 ms | 1.09 ms | 1.20 ms | 567.90 us | 3.09 ms | 3.09 ms | FAIL |
| multisig-sm-06 | 2.19 ms | 729.39 us | 601.10 us | **181.63 us** | 312.98 us | 655.17 us | 820.87 us | 836.92 us | 896.80 us | 455.25 us | 2.52 ms | 2.43 ms | FAIL |
| multisig-sm-07 | 2.36 ms | 679.99 us | 578.77 us | **182.35 us** | 301.21 us | 641.34 us | 805.36 us | 821.52 us | 866.29 us | 452.38 us | 2.51 ms | 2.58 ms | FAIL |
| multisig-sm-08 | 2.24 ms | 708.46 us | 587.10 us | **181.23 us** | 303.79 us | 661.36 us | 807.53 us | 835.45 us | 866.14 us | 454.67 us | 2.37 ms | 2.34 ms | FAIL |
| multisig-sm-09 | 2.23 ms | 711.15 us | 594.89 us | **182.23 us** | 306.70 us | 655.49 us | 811.21 us | 836.25 us | 879.29 us | 455.12 us | 2.43 ms | 2.36 ms | FAIL |
| multisig-sm-10 | 2.67 ms | 1.01 ms | 786.22 us | **251.53 us** | 433.72 us | 833.69 us | 1.01 ms | 1.11 ms | 1.20 ms | 569.74 us | 3.47 ms | 3.32 ms | FAIL |
| ping-pong-1 | 1.91 ms | 582.32 us | 490.45 us | **150.10 us** | 251.01 us | 537.47 us | 680.01 us | 678.05 us | 732.76 us | 381.81 us | 1.98 ms | 1.96 ms | 256.57 ms |
| ping-pong-2 | 1.82 ms | 574.41 us | 489.01 us | **150.31 us** | 254.77 us | 539.89 us | 693.44 us | 697.34 us | 727.90 us | 381.95 us | 1.97 ms | 1.97 ms | 255.25 ms |
| ping-pong_2-1 | 1.30 ms | 350.54 us | 332.98 us | **94.48 us** | 154.16 us | 395.03 us | 514.92 us | 486.84 us | 511.25 us | 284.31 us | 1.50 ms | 1.47 ms | 185.29 ms |
| prism-1 | 198.17 us | 272.07 us | 240.43 us | **66.02 us** | 128.62 us | 281.37 us | 307.87 us | 297.14 us | 306.16 us | 156.59 us | 980.50 us | 1.02 ms | 111.06 ms |
| prism-2 | 1.78 ms | 722.97 us | 596.64 us | **182.89 us** | 317.13 us | 666.41 us | 796.46 us | 823.52 us | 862.10 us | 446.12 us | 2.34 ms | 2.34 ms | 301.04 ms |
| prism-3 | 784.96 us | 675.89 us | 502.06 us | **157.72 us** | 310.16 us | 557.89 us | 587.62 us | 679.07 us | 724.21 us | 331.20 us | 2.06 ms | 2.01 ms | 242.09 ms |
| pubkey-1 | 207.84 us | 233.55 us | 207.00 us | **57.72 us** | 111.57 us | 243.36 us | 273.76 us | 264.70 us | 266.49 us | 143.71 us | 902.80 us | 900.00 us | 96.93 ms |
| stablecoin_1-1 | 5.28 ms | 1.56 ms | 1.43 ms | **444.87 us** | 733.33 us | 1.48 ms | 1.79 ms | 2.11 ms | 1.94 ms | 815.07 us | 9.66 ms | 9.55 ms | FAIL |
| stablecoin_1-2 | 202.34 us | 331.95 us | 280.82 us | **79.10 us** | 157.94 us | 331.29 us | 340.33 us | 341.54 us | 346.55 us | 179.74 us | 1.17 ms | 1.14 ms | 126.11 ms |
| stablecoin_1-3 | 5.55 ms | 1.80 ms | 1.65 ms | **482.41 us** | 839.75 us | 1.68 ms | 2.00 ms | 2.12 ms | 2.18 ms | 906.76 us | 11.69 ms | 11.21 ms | FAIL |
| stablecoin_1-4 | 175.53 us | 345.09 us | 298.28 us | **83.06 us** | 158.69 us | 347.99 us | 356.42 us | 356.88 us | 376.79 us | 185.81 us | 1.18 ms | 1.18 ms | 133.75 ms |
| stablecoin_1-5 | 5.48 ms | 2.30 ms | 2.10 ms | **565.88 us** | 1.06 ms | 2.17 ms | 2.48 ms | 2.62 ms | 2.75 ms | 1.09 ms | 12.58 ms | 12.28 ms | FAIL |
| stablecoin_1-6 | 230.26 us | 423.77 us | 360.31 us | **102.04 us** | 195.82 us | 415.04 us | 413.24 us | 425.00 us | 440.59 us | 218.41 us | 1.63 ms | 1.52 ms | 155.06 ms |
| stablecoin_2-1 | 5.44 ms | 1.61 ms | 1.44 ms | **444.75 us** | 728.15 us | 1.48 ms | 1.80 ms | 1.87 ms | 2.01 ms | 816.23 us | 9.67 ms | 9.59 ms | FAIL |
| stablecoin_2-2 | 175.01 us | 326.07 us | 279.64 us | **80.46 us** | 171.88 us | 331.76 us | 338.50 us | 330.86 us | 344.13 us | 178.62 us | 1.13 ms | 1.12 ms | 126.79 ms |
| stablecoin_2-3 | 5.74 ms | 1.81 ms | 1.66 ms | **485.06 us** | 840.39 us | 1.66 ms | 2.00 ms | 2.07 ms | 2.21 ms | 906.05 us | 14.34 ms | 11.44 ms | FAIL |
| stablecoin_2-4 | 199.23 us | 343.06 us | 291.73 us | **83.49 us** | 157.11 us | 347.49 us | 356.79 us | 353.75 us | 381.09 us | 186.70 us | 1.19 ms | 1.21 ms | 132.36 ms |
| token-account-1 | 844.29 us | 336.65 us | 285.29 us | **84.77 us** | 148.51 us | 315.67 us | 367.27 us | 393.75 us | 412.89 us | 207.99 us | 1.12 ms | 1.10 ms | 142.43 ms |
| token-account-2 | 408.26 us | 609.71 us | 437.20 us | **144.89 us** | 261.65 us | 476.80 us | 518.99 us | 596.82 us | 635.54 us | 300.33 us | 1.81 ms | 1.75 ms | 224.79 ms |
| uniswap-1 | 705.08 us | 797.32 us | 520.63 us | **172.78 us** | 319.40 us | 542.88 us | 609.97 us | 761.83 us | 826.94 us | 362.42 us | 2.13 ms | 2.24 ms | 283.66 ms |
| uniswap-2 | 808.64 us | 387.35 us | 335.96 us | **98.63 us** | 173.53 us | 370.12 us | 412.24 us | 453.81 us | 471.13 us | 228.99 us | 1.29 ms | 1.28 ms | 159.71 ms |
| uniswap-3 | 2.93 ms | 2.97 ms | 2.13 ms | **622.27 us** | 1.36 ms | 2.32 ms | 2.54 ms | 2.97 ms | 3.18 ms | 1.41 ms | 9.44 ms | 9.21 ms | 984.26 ms |
| uniswap-4 | 298.48 us | 553.39 us | 464.86 us | **130.09 us** | 263.12 us | 541.04 us | 520.58 us | 548.04 us | 581.72 us | 278.01 us | 1.92 ms | 1.97 ms | 198.39 ms |
| uniswap-5 | 2.93 ms | 1.88 ms | 1.43 ms | **433.63 us** | 860.59 us | 1.58 ms | 1.71 ms | 2.02 ms | 2.13 ms | 1.00 ms | 6.20 ms | 6.24 ms | 670.76 ms |
| uniswap-6 | 271.29 us | 535.08 us | 442.56 us | **125.83 us** | 243.39 us | 515.90 us | 501.73 us | 542.64 us | 558.73 us | 263.34 us | 1.75 ms | 1.74 ms | 191.06 ms |
| vesting-1 | 1.45 ms | 625.25 us | 460.20 us | **158.87 us** | 268.79 us | 507.60 us | 583.74 us | 673.87 us | 709.16 us | 350.03 us | 1.99 ms | 2.00 ms | 244.52 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/saib-inc/cardano-plutus-vm-benchmark)*