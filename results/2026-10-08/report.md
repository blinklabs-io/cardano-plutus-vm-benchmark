# Cardano Plutus VM Benchmark Results

**Date:** run

## Environment
```
date: 2026-10-08T01:59:44+00:00
kernel: 6.17.0-41-generic
cpu: 11th Gen Intel(R) Core(TM) i9-11900 @ 2.50GHz (x86_64)
cores: 16
memory: 61Gi
```

## Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc UPLC→native JIT (C++ / LLVM)** | C++ / LLVM | 111.79 us | 1.00x |
| **uplc-turbo Bytecode VM (Rust)** | Rust | 190.62 us | 1.71x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 220.21 us | 1.97x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 244.67 us | 2.19x |
| **Plutigo CEK (Go)** | Go | 250.59 us | 2.24x |
| **Plutuz CEK (Zig)** | Zig | 385.38 us | 3.45x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 398.95 us | 3.57x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 405.33 us | 3.63x |
| **uplc-turbo AST walker (Rust)** | Rust | 407.65 us | 3.65x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 453.58 us | 4.06x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 510.00 us | 4.56x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.41 ms | 12.57x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.46 ms | 13.03x |
| **opshin CEK (Python / CPython)** | Python / CPython | 36.46 ms | 326.14x |

### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| llvm-uplc UPLC→native JIT (C++ / LLVM) | 89 | 0 | 0 | 89 |
| uplc-turbo Bytecode VM (Rust) | 89 | 0 | 0 | 89 |
| plutus-core CEK (Haskell / GHC) | 89 | 0 | 0 | 89 |
| Scalus UPLC→JVM JIT (Scala / JVM) | 89 | 0 | 0 | 89 |
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
| Plutuz CEK (Zig) | 89 | 0 | 0 | 89 |
| Julc CEK (Java / GraalVM) | 78 | 11 | 0 | 89 |
| Scalus CEK (Scala / JVM) | 89 | 0 | 0 | 89 |
| uplc-turbo AST walker (Rust) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET AOT) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

## Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc UPLC→native JIT (C++ / LLVM) | uplc-turbo Bytecode VM (Rust) | uplc-turbo AST walker (Rust) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 102.14 us | 52.92 us | 176.20 us | 157.98 us | **45.03 us** | 84.41 us | 207.34 us | 252.28 us | 205.93 us | 232.87 us | 119.15 us | 654.90 us | 636.60 us | 79.46 ms |
| auction_1-2 | 347.79 us | 1.26 ms | 740.25 us | 514.64 us | **206.11 us** | 300.90 us | 622.60 us | 602.59 us | 823.23 us | 862.03 us | 414.31 us | 2.00 ms | 1.97 ms | 290.62 ms |
| auction_1-3 | 341.65 us | 1.01 ms | 726.84 us | 570.15 us | **179.86 us** | 311.84 us | 614.92 us | 598.47 us | 755.56 us | 874.80 us | 405.92 us | 2.00 ms | 1.99 ms | 303.80 ms |
| auction_1-4 | 132.87 us | 58.19 us | 219.26 us | 195.55 us | **55.57 us** | 113.62 us | 270.09 us | 224.68 us | 243.69 us | 276.97 us | 155.33 us | 801.60 us | 787.00 us | 110.07 ms |
| auction_2-1 | 105.28 us | 48.00 us | 198.53 us | 157.78 us | **46.18 us** | 88.52 us | 207.83 us | 191.36 us | 203.69 us | 231.56 us | 119.67 us | 639.90 us | 634.00 us | 79.53 ms |
| auction_2-2 | 346.37 us | 1.31 ms | 719.95 us | 516.52 us | **182.53 us** | 297.26 us | 619.20 us | 603.11 us | 769.88 us | 854.83 us | 414.38 us | 1.99 ms | 1.96 ms | 288.75 ms |
| auction_2-3 | 443.81 us | 1.19 ms | 949.34 us | 653.35 us | **229.50 us** | 404.72 us | 763.39 us | 730.57 us | 948.74 us | 1.10 ms | 499.45 us | 2.49 ms | 2.47 ms | 365.73 ms |
| auction_2-4 | 345.73 us | 1.00 ms | 718.78 us | 518.74 us | **199.49 us** | 297.31 us | 639.36 us | 595.43 us | 759.51 us | 875.28 us | 446.64 us | 2.00 ms | 1.99 ms | 291.19 ms |
| auction_2-5 | 135.17 us | 58.43 us | 214.59 us | 222.23 us | **54.60 us** | 111.57 us | 269.85 us | 224.57 us | 247.07 us | 278.02 us | 139.65 us | 800.80 us | 785.80 us | 96.05 ms |
| coop-1 | 140.93 us | 73.42 us | 219.12 us | FAIL | **58.66 us** | 110.22 us | 244.24 us | 227.14 us | 203.06 us | 271.61 us | 129.76 us | 887.60 us | 865.90 us | FAIL |
| coop-2 | 461.51 us | 264.34 us | 753.00 us | FAIL | **193.52 us** | 357.00 us | 726.71 us | 574.77 us | 651.14 us | 729.67 us | 399.05 us | 2.72 ms | 2.68 ms | FAIL |
| coop-3 | 1.26 ms | 813.98 us | 2.52 ms | FAIL | **679.04 us** | 1.13 ms | 1.75 ms | 1.41 ms | 1.99 ms | 2.32 ms | 1.15 ms | 6.76 ms | 6.63 ms | FAIL |
| coop-4 | 563.33 us | 404.15 us | 935.68 us | FAIL | **260.64 us** | 449.08 us | 839.02 us | 657.30 us | 829.56 us | 942.36 us | 484.05 us | 3.39 ms | 3.22 ms | FAIL |
| coop-5 | 260.90 us | 154.86 us | 443.50 us | FAIL | **113.51 us** | 201.79 us | 411.77 us | 344.24 us | 475.89 us | 460.23 us | 270.92 us | 1.54 ms | 1.53 ms | FAIL |
| coop-6 | 418.98 us | 219.54 us | 656.26 us | FAIL | **184.88 us** | 335.08 us | 690.83 us | 476.58 us | 539.85 us | 710.00 us | 350.23 us | 2.40 ms | 2.34 ms | FAIL |
| coop-7 | 196.23 us | 99.37 us | 292.26 us | FAIL | **81.66 us** | 152.61 us | 335.13 us | 320.61 us | 273.12 us | 318.91 us | 177.82 us | 1.20 ms | 1.18 ms | FAIL |
| crowdfunding-success-1 | 136.54 us | **41.52 us** | 199.97 us | 175.19 us | 56.85 us | 102.78 us | 241.66 us | 218.66 us | 241.63 us | 273.99 us | 143.16 us | 775.90 us | 761.40 us | 94.90 ms |
| crowdfunding-success-2 | 127.32 us | **39.34 us** | 201.31 us | 174.87 us | 57.09 us | 102.56 us | 239.08 us | 218.16 us | 236.27 us | 265.96 us | 156.13 us | 774.70 us | 762.30 us | 97.19 ms |
| crowdfunding-success-3 | 123.96 us | **38.21 us** | 203.07 us | 171.21 us | 56.99 us | 106.06 us | 246.59 us | 218.91 us | 238.05 us | 266.41 us | 141.51 us | 776.30 us | 762.10 us | 115.15 ms |
| currency-1 | 135.82 us | **65.64 us** | 260.37 us | 196.63 us | 73.25 us | 122.56 us | 256.02 us | 244.72 us | 299.64 us | 340.92 us | 162.39 us | 849.50 us | 830.00 us | 117.55 ms |
| escrow-redeem_1-1 | 208.75 us | **79.74 us** | 357.83 us | 302.76 us | 102.38 us | 166.03 us | 354.69 us | 334.32 us | 395.69 us | 453.87 us | 224.41 us | 1.18 ms | 1.16 ms | 157.33 ms |
| escrow-redeem_1-2 | 196.85 us | **84.81 us** | 408.95 us | 272.72 us | 102.03 us | 169.00 us | 351.59 us | 336.32 us | 465.31 us | 454.59 us | 222.96 us | 1.18 ms | 1.16 ms | 155.98 ms |
| escrow-redeem_2-1 | 223.55 us | 121.77 us | 418.13 us | 307.78 us | **116.86 us** | 200.04 us | 407.48 us | 370.27 us | 462.16 us | 515.54 us | 250.51 us | 1.34 ms | 1.31 ms | 177.62 ms |
| escrow-redeem_2-2 | 230.52 us | **87.75 us** | 418.57 us | 342.50 us | 116.77 us | 193.29 us | 397.00 us | 368.88 us | 451.33 us | 513.31 us | 283.06 us | 1.34 ms | 1.31 ms | 179.13 ms |
| escrow-redeem_2-3 | 225.24 us | 166.32 us | 416.86 us | 316.36 us | **116.68 us** | 208.62 us | 433.52 us | 372.66 us | 445.76 us | 583.82 us | 251.01 us | 1.34 ms | 1.31 ms | 213.41 ms |
| escrow-refund-1 | 91.96 us | **32.49 us** | 149.64 us | 143.22 us | 43.82 us | 75.22 us | 204.10 us | 209.05 us | 256.90 us | 244.40 us | 136.57 us | 663.80 us | 652.00 us | 84.97 ms |
| future-increase-margin-1 | 135.35 us | **60.19 us** | 258.50 us | 196.13 us | 80.78 us | 125.83 us | 261.32 us | 245.25 us | 295.34 us | 340.09 us | 162.99 us | 849.00 us | 828.90 us | 117.71 ms |
| future-increase-margin-2 | 289.36 us | 215.87 us | 644.61 us | 405.61 us | **150.84 us** | 261.48 us | 505.35 us | 511.51 us | 610.08 us | 667.29 us | 348.43 us | 1.68 ms | 1.65 ms | 229.16 ms |
| future-increase-margin-3 | 288.81 us | 159.53 us | 571.30 us | 404.89 us | **150.38 us** | 263.74 us | 526.05 us | 451.80 us | 583.19 us | 666.27 us | 312.42 us | 1.68 ms | 1.65 ms | 231.23 ms |
| future-increase-margin-4 | 265.82 us | 1.16 ms | 534.40 us | 487.45 us | **149.08 us** | 235.01 us | 546.29 us | 556.23 us | 783.89 us | 750.97 us | 356.64 us | 1.70 ms | 1.66 ms | FAIL |
| future-increase-margin-5 | 455.93 us | 2.28 ms | 964.25 us | 713.03 us | **264.82 us** | 413.88 us | 813.05 us | 884.40 us | 1.04 ms | 1.15 ms | 491.51 us | 3.93 ms | 3.87 ms | FAIL |
| future-pay-out-1 | 136.79 us | **64.65 us** | 259.85 us | 197.74 us | 72.92 us | 120.17 us | 255.12 us | 245.45 us | 295.12 us | 341.58 us | 162.40 us | 860.60 us | 832.00 us | 117.77 ms |
| future-pay-out-2 | 284.85 us | **134.42 us** | 573.39 us | 401.38 us | 152.38 us | 281.77 us | 527.02 us | 482.67 us | 585.55 us | 664.41 us | 313.47 us | 1.70 ms | 1.65 ms | 230.47 ms |
| future-pay-out-3 | 290.93 us | 210.06 us | 572.78 us | 408.05 us | **169.91 us** | 257.63 us | 502.10 us | 482.52 us | 566.76 us | 760.07 us | 350.66 us | 1.70 ms | 1.65 ms | 230.84 ms |
| future-pay-out-4 | 457.43 us | 2.28 ms | 919.19 us | 715.57 us | **262.85 us** | 414.60 us | 816.45 us | 884.66 us | 1.02 ms | 1.15 ms | 496.41 us | 3.88 ms | 3.83 ms | FAIL |
| future-settle-early-1 | 135.76 us | **52.84 us** | 268.01 us | 220.57 us | 73.11 us | 125.78 us | 254.93 us | 245.67 us | 314.17 us | 340.68 us | 162.19 us | 859.70 us | 833.60 us | 117.85 ms |
| future-settle-early-2 | 291.30 us | 271.03 us | 648.21 us | 397.60 us | **152.06 us** | 273.04 us | 545.45 us | 452.11 us | 574.62 us | 666.20 us | 311.19 us | 1.70 ms | 1.65 ms | 250.32 ms |
| future-settle-early-3 | 288.13 us | 169.54 us | 573.89 us | 406.00 us | **152.51 us** | 253.69 us | 503.50 us | 452.39 us | 574.91 us | 719.24 us | 350.58 us | 1.70 ms | 1.64 ms | 231.09 ms |
| future-settle-early-4 | 343.86 us | 2.09 ms | 676.86 us | 555.70 us | **209.84 us** | 312.47 us | 647.38 us | 711.14 us | 802.86 us | 911.22 us | 394.68 us | 3.32 ms | 3.28 ms | FAIL |
| game-sm-success_1-1 | 220.37 us | 731.05 us | 402.72 us | 335.86 us | **120.38 us** | 184.55 us | 420.39 us | 432.69 us | 567.84 us | 572.49 us | 277.44 us | 1.46 ms | 1.43 ms | 188.18 ms |
| game-sm-success_1-2 | 116.94 us | **37.91 us** | 192.65 us | 169.21 us | 50.56 us | 102.45 us | 222.68 us | 193.78 us | 209.62 us | 239.15 us | 121.59 us | 1.02 ms | 678.10 us | 83.92 ms |
| game-sm-success_1-3 | 339.79 us | 954.41 us | 691.24 us | 544.90 us | **188.55 us** | 301.39 us | 612.01 us | 674.46 us | 736.28 us | 856.25 us | 399.02 us | 2.88 ms | 2.10 ms | 290.79 ms |
| game-sm-success_1-4 | 136.00 us | **51.45 us** | 234.63 us | 192.38 us | 61.49 us | 113.69 us | 274.61 us | 214.94 us | 235.89 us | 279.46 us | 134.78 us | 1.19 ms | 793.50 us | 113.88 ms |
| game-sm-success_2-1 | 219.39 us | 682.48 us | 409.76 us | 349.78 us | **119.65 us** | 183.30 us | 427.00 us | 432.56 us | 503.25 us | 561.32 us | 303.82 us | 1.60 ms | 1.43 ms | 186.92 ms |
| game-sm-success_2-2 | 115.40 us | **38.72 us** | 220.31 us | 166.39 us | 55.08 us | 102.39 us | 220.27 us | 193.88 us | 246.56 us | 238.16 us | 121.39 us | 702.30 us | 676.90 us | 82.84 ms |
| game-sm-success_2-3 | 349.08 us | 871.20 us | 681.34 us | 502.96 us | **188.81 us** | 306.07 us | 608.59 us | 595.03 us | 739.99 us | 919.57 us | 397.69 us | 2.14 ms | 2.08 ms | 285.73 ms |
| game-sm-success_2-4 | 135.13 us | **54.36 us** | 226.72 us | 187.25 us | 58.24 us | 117.71 us | 261.37 us | 215.83 us | 237.61 us | 268.52 us | 134.83 us | 819.40 us | 792.60 us | 94.77 ms |
| game-sm-success_2-5 | 339.60 us | 937.90 us | 691.51 us | 505.62 us | **188.71 us** | 304.65 us | 629.77 us | 594.24 us | 825.92 us | 877.72 us | 443.86 us | 2.14 ms | 2.08 ms | 286.04 ms |
| game-sm-success_2-6 | 138.59 us | **52.12 us** | 224.59 us | 191.75 us | 58.02 us | 119.75 us | 258.58 us | 280.08 us | 234.31 us | 268.70 us | 134.54 us | 820.20 us | 807.90 us | 94.55 ms |
| guardrail-sorted-large | 267.60 us | 336.95 us | 437.02 us | FAIL | **227.45 us** | 242.99 us | 420.39 us | 317.71 us | 419.09 us | 500.29 us | 273.70 us | 1.65 ms | 2.33 ms | FAIL |
| guardrail-sorted-small | 45.33 us | 104.62 us | 74.09 us | FAIL | **16.84 us** | 42.72 us | 88.73 us | 91.16 us | 102.16 us | 112.98 us | 59.72 us | 334.60 us | 466.60 us | FAIL |
| guardrail-unsorted-large | 389.47 us | 394.38 us | 643.89 us | FAIL | **248.15 us** | 312.52 us | 530.15 us | 411.98 us | 570.69 us | 665.64 us | 348.73 us | 2.21 ms | 3.08 ms | FAIL |
| guardrail-unsorted-small | 45.23 us | 101.30 us | 68.35 us | FAIL | **15.95 us** | 44.16 us | 88.05 us | 89.52 us | 98.84 us | 110.42 us | 58.09 us | 335.60 us | 351.70 us | FAIL |
| multisig-sm-01 | 218.92 us | 1.06 ms | 478.21 us | 359.42 us | **138.80 us** | 191.70 us | 442.25 us | 463.77 us | 542.50 us | 611.22 us | 327.10 us | 1.53 ms | 1.51 ms | FAIL |
| multisig-sm-02 | 225.70 us | 1.03 ms | 406.13 us | 347.81 us | **123.69 us** | 191.14 us | 441.58 us | 457.97 us | 537.93 us | 594.95 us | 294.36 us | 1.50 ms | 1.45 ms | FAIL |
| multisig-sm-03 | 221.20 us | 1.11 ms | 407.87 us | 391.38 us | **125.05 us** | 188.65 us | 448.11 us | 457.48 us | 541.61 us | 610.98 us | 296.99 us | 1.51 ms | 1.47 ms | FAIL |
| multisig-sm-04 | 216.19 us | 1.04 ms | 418.67 us | 346.60 us | **125.80 us** | 196.41 us | 441.60 us | 462.91 us | 534.47 us | 617.00 us | 297.54 us | 1.52 ms | 1.49 ms | FAIL |
| multisig-sm-05 | 299.36 us | 1.36 ms | 618.10 us | 474.33 us | **171.76 us** | 271.46 us | 578.65 us | 576.24 us | 704.70 us | 806.33 us | 416.48 us | 1.96 ms | 1.92 ms | FAIL |
| multisig-sm-06 | 231.78 us | 1.12 ms | 422.93 us | 362.23 us | **125.29 us** | 195.78 us | 441.94 us | 526.10 us | 535.41 us | 607.49 us | 295.89 us | 1.52 ms | 1.49 ms | FAIL |
| multisig-sm-07 | 217.25 us | 996.89 us | 467.35 us | 342.98 us | **123.87 us** | 190.82 us | 453.97 us | 457.98 us | 536.12 us | 597.91 us | 294.13 us | 1.50 ms | 1.46 ms | FAIL |
| multisig-sm-08 | 219.18 us | 1.05 ms | 418.89 us | 350.34 us | **124.97 us** | 196.55 us | 441.45 us | 458.20 us | 532.51 us | 599.70 us | 304.40 us | 1.51 ms | 1.47 ms | FAIL |
| multisig-sm-09 | 234.99 us | 1.07 ms | 420.01 us | 390.34 us | **134.32 us** | 189.88 us | 457.85 us | 461.40 us | 532.92 us | 604.26 us | 298.13 us | 1.52 ms | 1.49 ms | FAIL |
| multisig-sm-10 | 302.49 us | 1.42 ms | 620.97 us | 481.58 us | **170.89 us** | 274.42 us | 569.23 us | 575.72 us | 787.41 us | 798.62 us | 377.95 us | 1.95 ms | 1.91 ms | FAIL |
| ping-pong-1 | 180.68 us | 519.14 us | 354.16 us | 287.23 us | **103.99 us** | 158.44 us | 366.91 us | 443.44 us | 435.11 us | 527.36 us | 275.83 us | 1.27 ms | 1.23 ms | 165.43 ms |
| ping-pong-2 | 198.62 us | 555.82 us | 357.52 us | 284.18 us | **104.13 us** | 163.99 us | 365.78 us | 384.46 us | 516.83 us | 495.92 us | 244.65 us | 1.26 ms | 1.23 ms | 200.57 ms |
| ping-pong_2-1 | 115.89 us | 267.48 us | 208.87 us | 188.16 us | **70.94 us** | 96.49 us | 281.82 us | 291.00 us | 314.84 us | 351.91 us | 186.78 us | 909.70 us | 884.80 us | 119.44 ms |
| prism-1 | 96.53 us | **20.28 us** | 160.28 us | 148.27 us | 41.80 us | 81.44 us | 188.75 us | 169.94 us | 183.65 us | 204.92 us | 105.95 us | 606.90 us | 585.80 us | 71.90 ms |
| prism-2 | 223.73 us | 609.22 us | 498.22 us | 377.19 us | **125.49 us** | 197.21 us | 447.83 us | 451.45 us | 528.24 us | 591.40 us | 322.70 us | 1.49 ms | 1.44 ms | 195.91 ms |
| prism-3 | 203.75 us | 140.80 us | 387.60 us | 292.62 us | **117.77 us** | 192.22 us | 371.94 us | 333.92 us | 412.56 us | 471.62 us | 213.67 us | 1.22 ms | 1.19 ms | 157.51 ms |
| pubkey-1 | 84.34 us | **18.14 us** | 135.97 us | 122.75 us | 36.18 us | 67.54 us | 179.71 us | 153.88 us | 162.08 us | 181.67 us | 97.53 us | 525.20 us | 505.70 us | 63.65 ms |
| stablecoin_1-1 | 548.63 us | 4.09 ms | 1.03 ms | 981.00 us | **299.57 us** | 484.60 us | 993.89 us | 1.06 ms | 1.21 ms | 1.33 ms | 554.08 us | 5.72 ms | 5.68 ms | FAIL |
| stablecoin_1-2 | 114.72 us | **43.26 us** | 194.39 us | 163.58 us | 51.42 us | 94.84 us | 221.72 us | 191.20 us | 204.80 us | 234.21 us | 119.61 us | 696.90 us | 677.90 us | 81.66 ms |
| stablecoin_1-3 | 630.56 us | 4.04 ms | 1.17 ms | 1.03 ms | **342.39 us** | 574.95 us | 1.12 ms | 1.19 ms | 1.39 ms | 1.50 ms | 614.73 us | 6.24 ms | 6.15 ms | FAIL |
| stablecoin_1-4 | 120.29 us | **41.66 us** | 200.37 us | 172.84 us | 53.47 us | 100.68 us | 232.78 us | 199.04 us | 223.37 us | 283.83 us | 137.17 us | 744.80 us | 718.40 us | 85.59 ms |
| stablecoin_1-5 | 799.63 us | 3.69 ms | 1.44 ms | 1.34 ms | **377.17 us** | 721.46 us | 1.44 ms | 1.64 ms | 1.87 ms | 1.87 ms | 733.82 us | 7.39 ms | 7.25 ms | FAIL |
| stablecoin_1-6 | 149.84 us | **59.63 us** | 249.73 us | 212.40 us | 65.99 us | 123.66 us | 276.80 us | 230.30 us | 256.50 us | 291.12 us | 144.25 us | 887.40 us | 859.20 us | 137.42 ms |
| stablecoin_2-1 | 548.57 us | 3.77 ms | 1.13 ms | 1.00 ms | **299.61 us** | 492.51 us | 999.16 us | 1.06 ms | 1.22 ms | 1.33 ms | 553.08 us | 5.75 ms | 5.65 ms | FAIL |
| stablecoin_2-2 | 115.66 us | **44.66 us** | 190.13 us | 163.15 us | 51.12 us | 95.33 us | 222.00 us | 190.77 us | 207.76 us | 232.92 us | 132.16 us | 696.70 us | 676.00 us | 82.61 ms |
| stablecoin_2-3 | 633.77 us | 3.89 ms | 1.17 ms | 1.03 ms | **325.94 us** | 562.46 us | 1.12 ms | 1.19 ms | 1.38 ms | 1.76 ms | 617.93 us | 6.22 ms | 6.17 ms | FAIL |
| stablecoin_2-4 | 119.87 us | **40.84 us** | 198.68 us | 173.82 us | 53.74 us | 99.64 us | 234.17 us | 198.75 us | 255.75 us | 248.16 us | 124.60 us | 739.70 us | 715.50 us | 86.57 ms |
| token-account-1 | 107.59 us | 61.58 us | 194.75 us | 157.42 us | **56.54 us** | 95.81 us | 225.12 us | 207.69 us | 242.50 us | 272.88 us | 134.76 us | 700.00 us | 677.60 us | 92.18 ms |
| token-account-2 | 181.35 us | **55.13 us** | 340.70 us | 251.65 us | 94.59 us | 161.88 us | 325.75 us | 300.07 us | 356.04 us | 416.39 us | 198.79 us | 1.43 ms | 1.04 ms | 147.37 ms |
| uniswap-1 | 209.56 us | **78.62 us** | 472.06 us | 334.91 us | 114.89 us | 203.15 us | 364.54 us | 395.93 us | 516.65 us | 556.49 us | 239.08 us | 1.81 ms | 1.23 ms | 188.00 ms |
| uniswap-2 | 128.51 us | **66.69 us** | 231.12 us | 186.75 us | 73.19 us | 107.35 us | 247.51 us | 231.86 us | 273.39 us | 308.31 us | 164.12 us | 1.16 ms | 798.10 us | 103.34 ms |
| uniswap-3 | 968.04 us | 1.14 ms | 1.98 ms | 1.27 ms | **417.25 us** | 837.24 us | 1.48 ms | 1.39 ms | 1.75 ms | 2.06 ms | 918.77 us | 7.05 ms | 5.52 ms | 672.49 ms |
| uniswap-4 | 188.72 us | **68.02 us** | 325.38 us | 275.50 us | 85.57 us | 160.69 us | 381.67 us | 288.83 us | 328.27 us | 371.94 us | 183.43 us | 1.13 ms | 1.11 ms | 129.65 ms |
| uniswap-5 | 669.10 us | 1.19 ms | 1.16 ms | 842.17 us | **289.96 us** | 560.82 us | 1.02 ms | 953.05 us | 1.20 ms | 1.38 ms | 654.50 us | 3.94 ms | 3.84 ms | 441.15 ms |
| uniswap-6 | 183.00 us | **69.65 us** | 305.93 us | 269.32 us | 82.36 us | 154.43 us | 352.78 us | 278.33 us | 388.14 us | 364.52 us | 196.14 us | 1.08 ms | 1.06 ms | 126.77 ms |
| vesting-1 | 190.33 us | 314.14 us | 371.26 us | 298.33 us | **110.38 us** | 162.61 us | 344.39 us | 334.17 us | 407.42 us | 469.70 us | 225.03 us | 1.16 ms | 1.15 ms | 161.50 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/saib-inc/cardano-plutus-vm-benchmark)*