# Cardano Plutus VM Benchmark Results

**Date:** run

## Environment
```
date: 2026-10-07T19:32:54+00:00
kernel: 6.17.0-41-generic
cpu: 11th Gen Intel(R) Core(TM) i9-11900 @ 2.50GHz (x86_64)
cores: 16
memory: 61Gi
```

## Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc UPLC→native JIT (C++ / LLVM)** | C++ / LLVM | 120.09 us | 1.00x |
| **uplc-turbo Bytecode VM (Rust)** | Rust | 196.00 us | 1.63x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 219.04 us | 1.82x |
| **Plutigo CEK (Go)** | Go | 237.13 us | 1.97x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 251.19 us | 2.09x |
| **uplc-turbo AST walker (Rust)** | Rust | 256.52 us | 2.14x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 269.75 us | 2.25x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 333.06 us | 2.77x |
| **Plutuz CEK (Zig)** | Zig | 383.43 us | 3.19x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 442.03 us | 3.68x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 493.77 us | 4.11x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.44 ms | 12.00x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.46 ms | 12.15x |
| **opshin CEK (Python / CPython)** | Python / CPython | 37.41 ms | 311.50x |

### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| llvm-uplc UPLC→native JIT (C++ / LLVM) | 89 | 0 | 0 | 89 |
| uplc-turbo Bytecode VM (Rust) | 89 | 0 | 0 | 89 |
| plutus-core CEK (Haskell / GHC) | 89 | 0 | 0 | 89 |
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
| Scalus UPLC→JVM JIT (Scala / JVM) | 89 | 0 | 0 | 89 |
| uplc-turbo AST walker (Rust) | 89 | 0 | 0 | 89 |
| Julc CEK (Java / GraalVM) | 89 | 0 | 0 | 89 |
| Scalus CEK (Scala / JVM) | 89 | 0 | 0 | 89 |
| Plutuz CEK (Zig) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET) | 89 | 0 | 0 | 89 |
| Chrysalis CEK (C# / .NET AOT) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

## Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc UPLC→native JIT (C++ / LLVM) | uplc-turbo Bytecode VM (Rust) | uplc-turbo AST walker (Rust) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 101.59 us | 53.40 us | 142.34 us | 127.08 us | **50.69 us** | 96.10 us | 135.00 us | 189.76 us | 205.71 us | 248.37 us | 124.47 us | 631.60 us | 640.00 us | 80.15 ms |
| auction_1-2 | 347.07 us | 1.35 ms | 629.69 us | 422.83 us | **201.86 us** | 282.63 us | 384.32 us | 600.80 us | 737.49 us | 867.56 us | 386.43 us | 1.96 ms | 1.99 ms | 292.60 ms |
| auction_1-3 | 350.96 us | 995.18 us | 572.59 us | 441.94 us | **221.45 us** | 285.02 us | 385.04 us | 593.87 us | 749.00 us | 844.89 us | 380.56 us | 1.97 ms | 2.00 ms | 293.91 ms |
| auction_1-4 | 132.39 us | **60.12 us** | 181.39 us | 162.51 us | 62.86 us | 130.33 us | 162.31 us | 223.43 us | 238.54 us | 264.73 us | 131.25 us | 776.90 us | 788.60 us | 96.83 ms |
| auction_2-1 | 100.57 us | **50.41 us** | 140.54 us | 139.08 us | 50.72 us | 97.46 us | 134.40 us | 200.79 us | 205.84 us | 261.25 us | 112.59 us | 627.80 us | 631.60 us | 100.70 ms |
| auction_2-2 | 356.58 us | 1.37 ms | 572.26 us | 418.99 us | **217.95 us** | 318.32 us | 387.12 us | 666.14 us | 759.88 us | 895.68 us | 386.45 us | 1.95 ms | 1.97 ms | 293.26 ms |
| auction_2-3 | 455.73 us | 1.36 ms | 743.37 us | 551.81 us | **250.78 us** | 363.48 us | 468.45 us | 727.66 us | 934.97 us | 1.07 ms | 529.56 us | 2.43 ms | 2.47 ms | 369.85 ms |
| auction_2-4 | 340.91 us | 1.09 ms | 652.13 us | 418.78 us | **197.30 us** | 298.67 us | 398.38 us | 593.37 us | 886.47 us | 962.92 us | 381.12 us | 1.96 ms | 1.99 ms | 293.11 ms |
| auction_2-5 | 135.00 us | **55.68 us** | 176.31 us | 163.11 us | 62.53 us | 125.34 us | 166.03 us | 223.44 us | 239.22 us | 272.93 us | 131.20 us | 775.70 us | 786.80 us | 132.95 ms |
| coop-1 | 139.49 us | 72.48 us | 181.48 us | 174.71 us | **63.76 us** | 127.02 us | 143.81 us | 187.95 us | 198.90 us | 225.22 us | 119.41 us | 902.40 us | 941.40 us | FAIL |
| coop-2 | 425.25 us | 279.19 us | 617.46 us | 650.68 us | **209.59 us** | 423.96 us | 458.93 us | 545.20 us | 787.83 us | 707.13 us | 409.28 us | 3.88 ms | 2.73 ms | FAIL |
| coop-3 | 1.28 ms | 862.37 us | 2.10 ms | 1.57 ms | **721.38 us** | 1.06 ms | 911.48 us | 1.41 ms | 2.00 ms | 2.26 ms | 1.07 ms | 9.58 ms | 6.86 ms | FAIL |
| coop-4 | 571.60 us | 360.72 us | 798.72 us | 976.95 us | **282.14 us** | 462.63 us | 481.33 us | 665.07 us | 798.71 us | 968.92 us | 450.51 us | 4.85 ms | 3.35 ms | FAIL |
| coop-5 | 236.72 us | 166.28 us | 332.49 us | 295.38 us | **122.92 us** | 222.60 us | 256.41 us | 407.50 us | 395.49 us | 448.72 us | 227.17 us | 1.54 ms | 1.61 ms | FAIL |
| coop-6 | 449.05 us | **213.47 us** | 565.74 us | 524.83 us | 217.05 us | 407.61 us | 408.38 us | 477.13 us | 520.62 us | 594.42 us | 319.07 us | 2.35 ms | 2.46 ms | FAIL |
| coop-7 | 195.12 us | 98.02 us | 254.09 us | 243.41 us | **89.07 us** | 191.27 us | 211.81 us | 251.78 us | 268.66 us | 304.48 us | 160.92 us | 1.19 ms | 1.27 ms | FAIL |
| crowdfunding-success-1 | 121.77 us | **39.81 us** | 185.37 us | 149.32 us | 61.57 us | 110.40 us | 157.65 us | 218.02 us | 230.11 us | 290.67 us | 144.59 us | 767.80 us | 775.50 us | 94.45 ms |
| crowdfunding-success-2 | 121.23 us | **42.67 us** | 166.08 us | 136.35 us | 60.89 us | 115.70 us | 152.75 us | 217.98 us | 230.87 us | 257.10 us | 131.65 us | 767.80 us | 916.30 us | 95.95 ms |
| crowdfunding-success-3 | 130.77 us | **41.31 us** | 162.49 us | 136.30 us | 69.48 us | 111.19 us | 152.81 us | 217.40 us | 233.14 us | 258.03 us | 131.37 us | 768.80 us | 1.09 ms | 94.71 ms |
| currency-1 | 136.72 us | **59.32 us** | 212.30 us | 161.41 us | 77.96 us | 123.83 us | 161.21 us | 244.21 us | 292.83 us | 333.58 us | 155.10 us | 842.00 us | 1.21 ms | 118.82 ms |
| escrow-redeem_1-1 | 193.30 us | **75.67 us** | 294.80 us | 219.15 us | 111.38 us | 167.50 us | 223.31 us | 332.41 us | 395.97 us | 437.52 us | 230.67 us | 1.17 ms | 1.65 ms | 158.58 ms |
| escrow-redeem_1-2 | 206.57 us | **103.43 us** | 294.19 us | 218.94 us | 108.07 us | 178.07 us | 219.89 us | 357.46 us | 391.49 us | 438.34 us | 209.08 us | 1.17 ms | 1.19 ms | 158.94 ms |
| escrow-redeem_2-1 | 226.47 us | 136.28 us | 360.47 us | 273.08 us | **124.23 us** | 193.59 us | 251.45 us | 403.24 us | 447.25 us | 497.67 us | 233.57 us | 1.33 ms | 1.34 ms | 180.83 ms |
| escrow-redeem_2-2 | 223.05 us | 141.70 us | 346.52 us | 257.91 us | **126.18 us** | 198.87 us | 250.35 us | 367.90 us | 470.45 us | 499.85 us | 232.46 us | 1.32 ms | 1.34 ms | 179.51 ms |
| escrow-redeem_2-3 | 222.50 us | 125.61 us | 384.15 us | 255.64 us | **124.67 us** | 193.48 us | 256.63 us | 367.77 us | 445.18 us | 495.68 us | 232.28 us | 1.33 ms | 1.35 ms | 180.31 ms |
| escrow-refund-1 | 91.09 us | **45.87 us** | 119.75 us | 109.83 us | 47.97 us | 87.60 us | 133.78 us | 208.65 us | 219.85 us | 239.14 us | 127.48 us | 659.00 us | 667.60 us | 95.28 ms |
| future-increase-margin-1 | 137.10 us | **52.21 us** | 211.26 us | 159.38 us | 77.64 us | 121.27 us | 160.00 us | 245.64 us | 295.58 us | 331.17 us | 169.93 us | 840.70 us | 852.60 us | 132.47 ms |
| future-increase-margin-2 | 288.20 us | 211.10 us | 462.93 us | 334.60 us | **160.69 us** | 260.65 us | 320.65 us | 453.14 us | 561.81 us | 657.05 us | 291.63 us | 1.67 ms | 1.69 ms | 233.92 ms |
| future-increase-margin-3 | 293.24 us | 304.04 us | 459.02 us | 345.78 us | **160.76 us** | 252.55 us | 328.79 us | 450.30 us | 563.09 us | 644.35 us | 290.58 us | 1.67 ms | 1.69 ms | 232.88 ms |
| future-increase-margin-4 | 270.60 us | 1.13 ms | 435.91 us | 337.94 us | **157.12 us** | 246.54 us | 335.28 us | 553.66 us | 664.69 us | 734.97 us | 347.69 us | 1.69 ms | 1.71 ms | FAIL |
| future-increase-margin-5 | 453.25 us | 2.28 ms | 837.49 us | 600.20 us | **275.42 us** | 382.68 us | 495.14 us | 934.04 us | 1.02 ms | 1.12 ms | 532.22 us | 3.92 ms | 3.95 ms | FAIL |
| future-pay-out-1 | 137.34 us | **50.62 us** | 211.71 us | 179.72 us | 77.99 us | 124.14 us | 161.24 us | 275.23 us | 294.72 us | 335.49 us | 154.54 us | 853.50 us | 854.20 us | 118.57 ms |
| future-pay-out-2 | 292.32 us | 207.35 us | 464.40 us | 341.15 us | **161.23 us** | 253.69 us | 324.31 us | 451.15 us | 683.56 us | 644.78 us | 290.20 us | 1.69 ms | 1.69 ms | 231.95 ms |
| future-pay-out-3 | 289.63 us | **152.37 us** | 507.62 us | 335.28 us | 161.52 us | 276.93 us | 319.14 us | 450.27 us | 565.97 us | 642.75 us | 290.31 us | 1.69 ms | 1.69 ms | 265.61 ms |
| future-pay-out-4 | 461.88 us | 2.53 ms | 754.46 us | 609.22 us | **306.16 us** | 385.37 us | 505.55 us | 881.63 us | 1.02 ms | 1.11 ms | 475.97 us | 3.85 ms | 3.90 ms | FAIL |
| future-settle-early-1 | 137.26 us | **61.33 us** | 209.23 us | 158.85 us | 78.05 us | 128.79 us | 161.55 us | 244.17 us | 290.36 us | 333.25 us | 155.07 us | 853.90 us | 854.30 us | 118.76 ms |
| future-settle-early-2 | 287.47 us | 220.42 us | 465.62 us | 336.58 us | **161.57 us** | 253.02 us | 331.40 us | 461.10 us | 634.77 us | 639.65 us | 322.51 us | 1.69 ms | 1.69 ms | 233.03 ms |
| future-settle-early-3 | 294.31 us | 238.36 us | 466.01 us | 384.38 us | **177.25 us** | 267.61 us | 319.97 us | 499.72 us | 566.58 us | 640.61 us | 290.25 us | 1.69 ms | 1.69 ms | 231.56 ms |
| future-settle-early-4 | 352.29 us | 2.09 ms | 564.19 us | 458.86 us | **219.49 us** | 294.74 us | 422.06 us | 709.32 us | 805.48 us | 887.58 us | 379.24 us | 3.30 ms | 3.35 ms | FAIL |
| game-sm-success_1-1 | 216.63 us | 727.29 us | 364.86 us | 258.87 us | **126.85 us** | 191.03 us | 270.75 us | 431.62 us | 488.97 us | 547.96 us | 266.86 us | 1.47 ms | 1.47 ms | 188.67 ms |
| game-sm-success_1-2 | 116.10 us | **38.89 us** | 160.41 us | 136.65 us | 54.91 us | 108.65 us | 148.72 us | 192.65 us | 203.29 us | 230.08 us | 126.27 us | 692.00 us | 695.60 us | 83.70 ms |
| game-sm-success_1-3 | 351.32 us | 949.27 us | 614.26 us | 417.79 us | **224.21 us** | 305.98 us | 375.22 us | 594.72 us | 748.88 us | 837.31 us | 378.83 us | 2.12 ms | 2.14 ms | 287.73 ms |
| game-sm-success_1-4 | 130.01 us | **45.90 us** | 182.54 us | 157.59 us | 62.74 us | 126.13 us | 171.35 us | 214.32 us | 227.57 us | 261.08 us | 126.22 us | 811.20 us | 811.00 us | 101.43 ms |
| game-sm-success_2-1 | 224.74 us | 720.90 us | 325.94 us | 283.63 us | **136.40 us** | 192.14 us | 270.59 us | 431.68 us | 493.90 us | 547.48 us | 266.80 us | 1.46 ms | 1.45 ms | 198.93 ms |
| game-sm-success_2-2 | 114.87 us | **46.38 us** | 157.54 us | 136.84 us | 54.35 us | 108.36 us | 144.84 us | 192.92 us | 208.22 us | 229.87 us | 113.69 us | 691.80 us | 693.20 us | 84.52 ms |
| game-sm-success_2-3 | 346.35 us | 965.84 us | 559.72 us | 424.16 us | **198.78 us** | 307.99 us | 377.50 us | 593.27 us | 881.38 us | 829.94 us | 379.49 us | 2.12 ms | 2.13 ms | 287.78 ms |
| game-sm-success_2-4 | 138.52 us | **50.71 us** | 184.12 us | 158.59 us | 63.11 us | 126.51 us | 169.78 us | 273.81 us | 230.49 us | 258.03 us | 139.18 us | 810.00 us | 810.40 us | 94.31 ms |
| game-sm-success_2-5 | 351.38 us | 865.23 us | 636.22 us | 415.18 us | **198.95 us** | 302.43 us | 379.70 us | 599.79 us | 738.92 us | 829.19 us | 378.28 us | 2.13 ms | 2.12 ms | 288.55 ms |
| game-sm-success_2-6 | 130.20 us | **46.97 us** | 186.45 us | 159.30 us | 63.00 us | 125.94 us | 164.68 us | 214.26 us | 227.39 us | 258.86 us | 126.54 us | 814.80 us | 808.50 us | 127.86 ms |
| guardrail-sorted-large | 271.97 us | 371.10 us | 359.49 us | 447.99 us | **222.41 us** | 260.56 us | 286.11 us | 316.23 us | 406.11 us | 517.84 us | 258.19 us | 1.64 ms | 1.75 ms | FAIL |
| guardrail-sorted-small | 43.45 us | 103.14 us | 58.51 us | 48.63 us | **18.39 us** | 39.31 us | 63.89 us | 90.78 us | 97.77 us | 110.63 us | 63.98 us | 329.80 us | 383.90 us | FAIL |
| guardrail-unsorted-large | 349.61 us | 395.92 us | 540.27 us | 468.78 us | **262.55 us** | 306.84 us | 342.88 us | 411.81 us | 558.42 us | 643.62 us | 329.59 us | 2.19 ms | 2.18 ms | FAIL |
| guardrail-unsorted-small | 45.72 us | 109.31 us | 55.83 us | 47.79 us | **16.90 us** | 37.94 us | 57.79 us | 89.25 us | 98.30 us | 105.88 us | 56.48 us | 326.40 us | 377.10 us | FAIL |
| multisig-sm-01 | 231.48 us | 1.10 ms | 379.81 us | 271.48 us | **132.00 us** | 202.79 us | 280.97 us | 462.30 us | 644.38 us | 595.51 us | 288.70 us | 1.52 ms | 1.53 ms | FAIL |
| multisig-sm-02 | 218.31 us | 1.04 ms | 341.29 us | 263.07 us | **144.95 us** | 188.82 us | 281.84 us | 515.85 us | 512.03 us | 582.89 us | 284.68 us | 1.50 ms | 1.49 ms | FAIL |
| multisig-sm-03 | 217.71 us | 1.04 ms | 348.45 us | 264.58 us | **132.37 us** | 196.85 us | 286.98 us | 457.53 us | 535.33 us | 581.29 us | 287.96 us | 1.50 ms | 1.50 ms | FAIL |
| multisig-sm-04 | 229.77 us | 1.06 ms | 397.42 us | 265.69 us | **141.53 us** | 194.29 us | 285.04 us | 461.01 us | 529.91 us | 584.66 us | 318.30 us | 1.51 ms | 1.52 ms | FAIL |
| multisig-sm-05 | 308.14 us | 1.48 ms | 509.29 us | 429.41 us | **181.34 us** | 270.34 us | 357.62 us | 573.90 us | 707.53 us | 787.97 us | 359.37 us | 1.94 ms | 1.98 ms | FAIL |
| multisig-sm-06 | 222.03 us | 1.08 ms | 343.66 us | 270.19 us | **132.75 us** | 193.73 us | 282.84 us | 462.96 us | 535.22 us | 595.69 us | 288.98 us | 1.53 ms | 1.52 ms | FAIL |
| multisig-sm-07 | 238.34 us | 1.02 ms | 345.91 us | 266.02 us | **131.50 us** | 194.20 us | 289.32 us | 455.85 us | 527.95 us | 584.29 us | 286.95 us | 1.49 ms | 1.49 ms | FAIL |
| multisig-sm-08 | 220.57 us | 1.04 ms | 338.65 us | 265.12 us | **132.56 us** | 188.64 us | 280.60 us | 456.19 us | 521.96 us | 581.57 us | 312.72 us | 1.50 ms | 1.50 ms | FAIL |
| multisig-sm-09 | 221.14 us | 1.08 ms | 346.14 us | 268.57 us | **146.36 us** | 199.42 us | 291.24 us | 498.67 us | 539.91 us | 586.95 us | 288.18 us | 1.52 ms | 1.52 ms | FAIL |
| multisig-sm-10 | 304.99 us | 1.41 ms | 568.73 us | 381.43 us | **182.31 us** | 259.85 us | 352.91 us | 598.04 us | 705.00 us | 776.81 us | 360.57 us | 1.93 ms | 1.96 ms | FAIL |
| ping-pong-1 | 186.00 us | 586.12 us | 288.33 us | 245.35 us | **122.17 us** | 161.04 us | 263.71 us | 383.69 us | 433.17 us | 543.80 us | 234.75 us | 1.27 ms | 1.25 ms | 167.38 ms |
| ping-pong-2 | 185.78 us | 607.49 us | 306.74 us | 216.86 us | **111.53 us** | 156.22 us | 243.28 us | 383.31 us | 434.98 us | 480.66 us | 236.75 us | 1.25 ms | 1.26 ms | 166.80 ms |
| ping-pong_2-1 | 115.28 us | 300.50 us | 170.94 us | 132.08 us | **68.81 us** | 106.49 us | 189.22 us | 291.08 us | 308.88 us | 334.39 us | 179.91 us | 906.30 us | 901.60 us | 120.72 ms |
| prism-1 | 94.73 us | **20.94 us** | 129.44 us | 114.36 us | 45.48 us | 92.22 us | 126.14 us | 169.16 us | 177.87 us | 199.95 us | 111.65 us | 600.90 us | 595.90 us | 72.58 ms |
| prism-2 | 229.14 us | 690.27 us | 353.61 us | 279.10 us | **134.11 us** | 201.40 us | 298.75 us | 449.30 us | 508.57 us | 578.20 us | 276.76 us | 1.48 ms | 1.48 ms | 197.39 ms |
| prism-3 | 200.75 us | **107.50 us** | 318.66 us | 246.42 us | 113.06 us | 184.51 us | 229.45 us | 395.26 us | 396.71 us | 448.47 us | 205.70 us | 1.69 ms | 1.21 ms | 159.03 ms |
| pubkey-1 | 82.57 us | **17.96 us** | 109.83 us | 102.06 us | 39.66 us | 79.06 us | 112.34 us | 153.05 us | 163.06 us | 175.00 us | 91.12 us | 728.50 us | 519.00 us | 64.34 ms |
| stablecoin_1-1 | 550.54 us | 3.84 ms | 958.34 us | 786.59 us | **310.68 us** | 453.44 us | 589.36 us | 1.06 ms | 1.19 ms | 1.28 ms | 594.59 us | 8.14 ms | 5.69 ms | FAIL |
| stablecoin_1-2 | 110.53 us | **40.78 us** | 156.97 us | 135.84 us | 55.21 us | 109.46 us | 145.89 us | 190.30 us | 204.45 us | 226.15 us | 112.82 us | 757.10 us | 687.20 us | 83.43 ms |
| stablecoin_1-3 | 630.14 us | 3.85 ms | 983.67 us | 963.52 us | **339.28 us** | 517.94 us | 653.88 us | 1.20 ms | 1.48 ms | 1.70 ms | 604.81 us | 6.19 ms | 6.16 ms | FAIL |
| stablecoin_1-4 | 118.39 us | **48.09 us** | 170.13 us | 141.94 us | 58.23 us | 119.51 us | 151.32 us | 198.26 us | 212.35 us | 236.88 us | 117.04 us | 734.00 us | 730.50 us | 87.39 ms |
| stablecoin_1-5 | 782.75 us | 3.86 ms | 1.23 ms | 1.19 ms | **392.39 us** | 652.58 us | 803.97 us | 1.47 ms | 1.68 ms | 1.81 ms | 738.35 us | 7.30 ms | 7.33 ms | FAIL |
| stablecoin_1-6 | 145.48 us | **62.46 us** | 201.57 us | 180.57 us | 71.79 us | 145.46 us | 184.17 us | 228.88 us | 248.87 us | 281.01 us | 135.81 us | 876.10 us | 990.50 us | 102.82 ms |
| stablecoin_2-1 | 550.54 us | 3.82 ms | 851.33 us | 788.17 us | **310.56 us** | 451.97 us | 589.38 us | 1.06 ms | 1.18 ms | 1.28 ms | 592.33 us | 5.72 ms | 8.13 ms | FAIL |
| stablecoin_2-2 | 110.80 us | **42.43 us** | 154.76 us | 135.50 us | 55.24 us | 116.87 us | 146.74 us | 190.23 us | 205.13 us | 255.01 us | 112.97 us | 689.90 us | 976.00 us | 109.85 ms |
| stablecoin_2-3 | 631.23 us | 3.92 ms | 992.07 us | 1.00 ms | **343.27 us** | 519.90 us | 669.66 us | 1.28 ms | 1.37 ms | 1.46 ms | 609.34 us | 6.29 ms | 8.85 ms | FAIL |
| stablecoin_2-4 | 118.44 us | **41.60 us** | 185.27 us | 142.04 us | 58.88 us | 120.24 us | 154.58 us | 220.06 us | 217.64 us | 237.28 us | 117.13 us | 732.10 us | 731.50 us | 88.00 ms |
| token-account-1 | 103.56 us | **59.22 us** | 161.09 us | 125.60 us | 68.58 us | 95.61 us | 141.03 us | 207.81 us | 241.02 us | 265.03 us | 140.42 us | 693.50 us | 691.70 us | 92.81 ms |
| token-account-2 | 184.34 us | **65.32 us** | 274.49 us | 208.07 us | 101.15 us | 172.56 us | 209.36 us | 290.99 us | 354.49 us | 402.08 us | 187.10 us | 1.06 ms | 1.06 ms | 147.85 ms |
| uniswap-1 | 215.80 us | **83.41 us** | 355.51 us | 251.03 us | 121.17 us | 186.06 us | 230.84 us | 341.80 us | 446.54 us | 522.65 us | 226.90 us | 1.27 ms | 1.26 ms | 189.57 ms |
| uniswap-2 | 122.47 us | **56.03 us** | 186.83 us | 152.51 us | 70.14 us | 117.89 us | 155.73 us | 231.96 us | 264.69 us | 300.58 us | 141.74 us | 818.10 us | 812.80 us | 104.32 ms |
| uniswap-3 | 980.64 us | 1.25 ms | 1.43 ms | 1.21 ms | **438.52 us** | 747.97 us | 863.48 us | 1.39 ms | 1.70 ms | 1.96 ms | 899.61 us | 5.63 ms | 5.66 ms | 688.34 ms |
| uniswap-4 | 187.54 us | **65.87 us** | 273.46 us | 231.17 us | 93.62 us | 192.97 us | 236.11 us | 286.65 us | 344.53 us | 360.35 us | 169.95 us | 1.12 ms | 1.12 ms | 130.08 ms |
| uniswap-5 | 641.02 us | 1.17 ms | 932.34 us | 720.42 us | **306.02 us** | 516.26 us | 629.02 us | 1.08 ms | 1.17 ms | 1.34 ms | 685.65 us | 3.88 ms | 3.89 ms | 444.92 ms |
| uniswap-6 | 182.41 us | **72.98 us** | 289.23 us | 226.36 us | 102.44 us | 181.18 us | 222.64 us | 277.04 us | 312.13 us | 366.67 us | 165.52 us | 1.07 ms | 1.08 ms | 126.70 ms |
| vesting-1 | 196.96 us | 282.37 us | 308.25 us | 212.93 us | **116.76 us** | 160.19 us | 220.65 us | 334.32 us | 409.41 us | 459.00 us | 212.59 us | 1.16 ms | 1.17 ms | 163.14 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/saib-inc/cardano-plutus-vm-benchmark)*