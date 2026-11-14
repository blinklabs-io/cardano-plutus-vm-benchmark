# Cardano Plutus VM Benchmark Results

**Date:** 2026-11-13

## Environment
```
date: 2026-11-13T20:39:15+00:00
kernel: 6.8.0-147-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
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
| **Plutigo CEK (Go)** | Go | 351.12 us | 1.00x |
| **Amaru UPLC CEK (Rust)** | Rust | 375.51 us | 1.07x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 459.99 us | 1.31x |
| **Plutuz CEK (Zig)** | Zig | 686.84 us | 1.96x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 727.85 us | 2.07x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 759.30 us | 2.16x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 1.05 ms | 2.98x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.31 ms | 6.58x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.37 ms | 6.76x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 14.89 ms | 42.42x |
| **opshin CEK (Python / CPython)** | Python / CPython | 106.80 ms | 304.17x |

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
| auction_1-1 | 534.98 us | 219.66 us | 188.25 us | 7.25 ms | 364.39 us | 330.16 us | 334.19 us | **167.58 us** | 998.60 us | 1.08 ms | 109.90 ms |
| auction_1-2 | 1.81 ms | 717.64 us | 597.06 us | 12.81 ms | 1.13 ms | 1.17 ms | 1.33 ms | **581.61 us** | 3.02 ms | 3.22 ms | 388.34 ms |
| auction_1-3 | 1.69 ms | 727.94 us | 623.62 us | 13.05 ms | 1.06 ms | 1.15 ms | 1.22 ms | **577.51 us** | 2.97 ms | 3.48 ms | 444.45 ms |
| auction_1-4 | 591.53 us | 256.99 us | 221.65 us | 9.37 ms | 402.76 us | 437.21 us | 417.70 us | **209.55 us** | 1.21 ms | 1.51 ms | 139.83 ms |
| auction_2-1 | 531.52 us | 227.60 us | 190.11 us | 6.98 ms | 337.90 us | 324.46 us | 333.88 us | **172.53 us** | 1.01 ms | 1.14 ms | 115.65 ms |
| auction_2-2 | 1.68 ms | 704.92 us | 592.40 us | 12.85 ms | 1.11 ms | 1.23 ms | 1.27 ms | **569.44 us** | 2.97 ms | 3.16 ms | 385.01 ms |
| auction_2-3 | 1.95 ms | 907.57 us | 782.41 us | 17.12 ms | 1.34 ms | 1.44 ms | 1.60 ms | **668.31 us** | 3.77 ms | 3.99 ms | 496.77 ms |
| auction_2-4 | 1.70 ms | 709.76 us | 595.38 us | 13.90 ms | 1.05 ms | 1.21 ms | 1.23 ms | **543.12 us** | 3.05 ms | 3.18 ms | 424.13 ms |
| auction_2-5 | 608.38 us | 262.80 us | 213.02 us | 9.40 ms | 423.07 us | 428.51 us | 416.89 us | **191.28 us** | 1.17 ms | 1.28 ms | 132.48 ms |
| coop-1 | 467.19 us | 248.28 us | **172.53 us** | 11.08 ms | 391.20 us | 341.38 us | 370.14 us | 189.24 us | 1.69 ms | 1.42 ms | FAIL |
| coop-2 | 1.41 ms | 851.81 us | **530.41 us** | 34.00 ms | 1.04 ms | 1.20 ms | 1.18 ms | 635.68 us | 5.26 ms | 4.34 ms | FAIL |
| coop-3 | 2.97 ms | 2.10 ms | **1.34 ms** | 37.43 ms | 2.54 ms | 4.08 ms | 3.83 ms | 1.64 ms | 16.02 ms | 10.97 ms | FAIL |
| coop-4 | 1.78 ms | 967.29 us | **636.95 us** | 29.07 ms | 1.16 ms | 1.50 ms | 1.64 ms | 698.59 us | 6.67 ms | 5.46 ms | FAIL |
| coop-5 | 835.31 us | 486.20 us | 355.35 us | 16.33 ms | 613.57 us | 687.27 us | 708.47 us | **354.17 us** | 3.49 ms | 2.40 ms | FAIL |
| coop-6 | 1.06 ms | 701.96 us | **423.59 us** | 32.99 ms | 905.76 us | 1.03 ms | 998.10 us | 533.57 us | 4.53 ms | 3.84 ms | FAIL |
| coop-7 | 610.15 us | 337.05 us | **230.11 us** | 15.38 ms | 496.25 us | 516.01 us | 521.26 us | 264.99 us | 2.29 ms | 2.02 ms | FAIL |
| crowdfunding-success-1 | 644.30 us | 267.29 us | 206.54 us | 8.88 ms | 400.02 us | 399.81 us | 396.89 us | **204.98 us** | 1.27 ms | 1.23 ms | 129.23 ms |
| crowdfunding-success-2 | 628.92 us | 261.50 us | 213.75 us | 8.89 ms | 419.67 us | 377.93 us | 393.78 us | **204.63 us** | 1.30 ms | 1.23 ms | 129.28 ms |
| crowdfunding-success-3 | 639.10 us | 260.51 us | 223.28 us | 9.00 ms | 421.10 us | 402.14 us | 401.97 us | **198.35 us** | 1.29 ms | 1.23 ms | 129.59 ms |
| currency-1 | 688.04 us | 297.94 us | 262.89 us | 6.78 ms | 432.20 us | 507.66 us | 552.15 us | **226.17 us** | 1.54 ms | 1.39 ms | 158.95 ms |
| escrow-redeem_1-1 | 953.89 us | 422.11 us | 320.02 us | 10.46 ms | 579.78 us | 666.98 us | 669.29 us | **316.55 us** | 2.11 ms | 1.93 ms | 215.79 ms |
| escrow-redeem_1-2 | 934.86 us | 427.17 us | 347.54 us | 11.44 ms | 593.46 us | 649.53 us | 699.26 us | **310.70 us** | 2.07 ms | 1.92 ms | 213.48 ms |
| escrow-redeem_2-1 | 1.01 ms | 461.73 us | 354.17 us | 12.36 ms | 699.94 us | 796.19 us | 765.81 us | **344.96 us** | 2.34 ms | 2.30 ms | 273.74 ms |
| escrow-redeem_2-2 | 1.03 ms | 446.17 us | **354.98 us** | 11.50 ms | 689.15 us | 766.89 us | 843.26 us | 368.37 us | 2.42 ms | 2.15 ms | 259.94 ms |
| escrow-redeem_2-3 | 1.01 ms | 461.56 us | 374.76 us | 12.03 ms | 668.63 us | 805.27 us | 794.50 us | **365.56 us** | 2.36 ms | 2.09 ms | 243.39 ms |
| escrow-refund-1 | 698.08 us | 264.76 us | 216.89 us | 6.81 ms | 395.38 us | 345.22 us | 378.71 us | **181.90 us** | 1.13 ms | 1.03 ms | 121.62 ms |
| future-increase-margin-1 | 709.04 us | 296.57 us | 259.71 us | 6.92 ms | 459.61 us | 535.23 us | 504.34 us | **237.20 us** | 1.38 ms | 1.33 ms | 161.98 ms |
| future-increase-margin-2 | 1.17 ms | 566.79 us | 452.94 us | 14.23 ms | 805.66 us | 989.26 us | 1.12 ms | **438.85 us** | 2.66 ms | 2.65 ms | 308.58 ms |
| future-increase-margin-3 | 1.25 ms | 554.74 us | **436.49 us** | 14.60 ms | 810.12 us | 1.00 ms | 997.86 us | 445.53 us | 2.56 ms | 2.65 ms | 313.61 ms |
| future-increase-margin-4 | 1.77 ms | 678.46 us | 587.90 us | 13.31 ms | 966.65 us | 1.03 ms | 1.08 ms | **520.02 us** | 2.76 ms | 2.69 ms | FAIL |
| future-increase-margin-5 | 2.14 ms | 904.58 us | 806.06 us | 151.09 ms | 1.51 ms | 1.61 ms | 1.67 ms | **721.36 us** | 5.29 ms | 6.50 ms | FAIL |
| future-pay-out-1 | 667.83 us | 308.19 us | 239.01 us | 6.76 ms | 434.73 us | 501.20 us | 518.51 us | **237.42 us** | 1.45 ms | 1.34 ms | 176.72 ms |
| future-pay-out-2 | 1.14 ms | 560.09 us | 440.11 us | 14.26 ms | 808.69 us | 932.76 us | 1.03 ms | **429.54 us** | 2.86 ms | 2.71 ms | 321.38 ms |
| future-pay-out-3 | 1.18 ms | 571.97 us | 486.00 us | 13.90 ms | 826.19 us | 957.41 us | 998.86 us | **425.01 us** | 2.80 ms | 2.68 ms | 317.57 ms |
| future-pay-out-4 | 2.09 ms | 914.85 us | 809.45 us | 149.78 ms | 1.59 ms | 1.58 ms | 1.83 ms | **667.25 us** | 5.28 ms | 6.35 ms | FAIL |
| future-settle-early-1 | 685.78 us | 308.31 us | 239.13 us | 7.33 ms | 457.08 us | 491.05 us | 504.06 us | **230.01 us** | 1.48 ms | 1.34 ms | 162.71 ms |
| future-settle-early-2 | 1.15 ms | 550.29 us | 474.09 us | 14.58 ms | 800.88 us | 985.63 us | 1.07 ms | **458.16 us** | 2.92 ms | 2.68 ms | 317.97 ms |
| future-settle-early-3 | 1.21 ms | 563.79 us | 457.58 us | 13.90 ms | 805.46 us | 1.07 ms | 989.57 us | **454.12 us** | 2.95 ms | 2.68 ms | 340.86 ms |
| future-settle-early-4 | 1.97 ms | 772.19 us | 636.24 us | 151.49 ms | 1.25 ms | 1.21 ms | 1.34 ms | **539.87 us** | 4.41 ms | 5.45 ms | FAIL |
| game-sm-success_1-1 | 1.53 ms | 543.79 us | 419.57 us | 10.96 ms | 786.29 us | 827.07 us | 800.48 us | **397.79 us** | 2.34 ms | 2.27 ms | 285.51 ms |
| game-sm-success_1-2 | 489.61 us | 218.99 us | 203.65 us | 8.26 ms | 361.24 us | 350.34 us | 347.96 us | **173.63 us** | 1.17 ms | 1.13 ms | 119.64 ms |
| game-sm-success_1-3 | 1.88 ms | 687.40 us | 615.44 us | 13.94 ms | 1.04 ms | 1.23 ms | 1.29 ms | **582.84 us** | 3.76 ms | 3.38 ms | 382.94 ms |
| game-sm-success_1-4 | 540.21 us | 244.63 us | 209.94 us | 10.61 ms | 412.96 us | 374.97 us | 387.74 us | **193.37 us** | 1.40 ms | 1.29 ms | 127.87 ms |
| game-sm-success_2-1 | 1.40 ms | 546.32 us | **417.01 us** | 11.57 ms | 825.24 us | 764.65 us | 834.99 us | 421.16 us | 2.26 ms | 2.30 ms | 254.21 ms |
| game-sm-success_2-2 | 494.70 us | 222.96 us | 197.39 us | 8.26 ms | 358.93 us | 357.01 us | 354.63 us | **169.95 us** | 1.17 ms | 1.14 ms | 115.31 ms |
| game-sm-success_2-3 | 1.74 ms | 698.18 us | 588.68 us | 13.63 ms | 1.04 ms | 1.17 ms | 1.30 ms | **563.17 us** | 3.46 ms | 3.53 ms | 412.46 ms |
| game-sm-success_2-4 | 536.71 us | 246.44 us | 203.79 us | 9.40 ms | 377.60 us | 381.66 us | 385.97 us | **188.89 us** | 1.35 ms | 1.35 ms | 137.52 ms |
| game-sm-success_2-5 | 1.64 ms | 708.26 us | 588.45 us | 13.76 ms | 1.05 ms | 1.17 ms | 1.21 ms | **545.78 us** | 3.43 ms | 3.71 ms | 392.85 ms |
| game-sm-success_2-6 | 547.98 us | 245.76 us | 242.82 us | 9.43 ms | 379.58 us | 410.99 us | 392.54 us | **183.56 us** | 1.37 ms | 1.37 ms | 128.29 ms |
| guardrail-sorted-large | 767.13 us | 492.20 us | **367.09 us** | 56.65 ms | 588.63 us | 702.82 us | 803.97 us | 415.57 us | 3.58 ms | 2.89 ms | FAIL |
| guardrail-sorted-small | 270.76 us | 131.85 us | 99.41 us | 1.50 ms | 159.53 us | 175.34 us | 178.89 us | **96.28 us** | 733.50 us | 579.10 us | FAIL |
| guardrail-unsorted-large | 936.27 us | 660.24 us | **436.98 us** | 61.78 ms | 768.13 us | 937.74 us | 1.02 ms | 521.33 us | 5.79 ms | 4.09 ms | FAIL |
| guardrail-unsorted-small | 289.69 us | 127.43 us | 96.65 us | 1.38 ms | 172.59 us | 164.99 us | 180.70 us | **92.73 us** | 880.50 us | 571.70 us | FAIL |
| multisig-sm-01 | 1.45 ms | 551.01 us | 462.57 us | 11.15 ms | 859.02 us | 825.89 us | 893.94 us | **439.39 us** | 2.69 ms | 2.59 ms | FAIL |
| multisig-sm-02 | 1.60 ms | 572.34 us | 446.23 us | 11.66 ms | 802.32 us | 799.47 us | 866.99 us | **433.21 us** | 2.56 ms | 2.48 ms | FAIL |
| multisig-sm-03 | 1.47 ms | 575.41 us | 443.77 us | 10.58 ms | 844.93 us | 800.39 us | 819.99 us | **427.33 us** | 2.62 ms | 2.48 ms | FAIL |
| multisig-sm-04 | 1.61 ms | 582.35 us | 511.10 us | 10.53 ms | 835.10 us | 885.71 us | 910.31 us | **460.40 us** | 2.64 ms | 2.69 ms | FAIL |
| multisig-sm-05 | 1.68 ms | 663.28 us | 572.67 us | 12.31 ms | 1.05 ms | 1.08 ms | 1.19 ms | **540.53 us** | 3.42 ms | 3.13 ms | FAIL |
| multisig-sm-06 | 1.55 ms | 590.16 us | 451.21 us | 11.58 ms | 820.80 us | 874.15 us | 913.72 us | **416.81 us** | 2.62 ms | 2.46 ms | FAIL |
| multisig-sm-07 | 1.49 ms | 544.68 us | 449.54 us | 11.14 ms | 825.70 us | 796.75 us | 816.09 us | **411.29 us** | 2.64 ms | 2.55 ms | FAIL |
| multisig-sm-08 | 1.53 ms | 580.01 us | 482.72 us | 10.45 ms | 872.40 us | 906.12 us | 845.35 us | **415.84 us** | 2.58 ms | 2.43 ms | FAIL |
| multisig-sm-09 | 1.49 ms | 555.17 us | 443.61 us | 10.50 ms | 856.87 us | 809.46 us | 916.50 us | **418.62 us** | 2.60 ms | 2.48 ms | FAIL |
| multisig-sm-10 | 1.65 ms | 719.74 us | 578.82 us | 11.85 ms | 984.23 us | 1.17 ms | 1.15 ms | **536.67 us** | 3.58 ms | 3.30 ms | FAIL |
| ping-pong-1 | 1.30 ms | 465.43 us | 391.38 us | 8.64 ms | 685.53 us | 758.10 us | 704.03 us | **373.51 us** | 2.19 ms | 2.02 ms | 242.48 ms |
| ping-pong-2 | 1.21 ms | 487.82 us | 402.60 us | 8.59 ms | 819.48 us | 700.90 us | 765.43 us | **354.06 us** | 2.19 ms | 2.07 ms | 242.72 ms |
| ping-pong_2-1 | 1.08 ms | 379.93 us | 288.69 us | 7.31 ms | 516.89 us | 480.48 us | 548.24 us | **263.65 us** | 1.51 ms | 1.39 ms | 171.22 ms |
| prism-1 | 453.35 us | 204.81 us | 162.60 us | 7.79 ms | 297.39 us | 304.81 us | 298.21 us | **156.76 us** | 1.05 ms | 1.06 ms | 106.48 ms |
| prism-2 | 1.49 ms | 540.85 us | 434.10 us | 12.65 ms | 804.28 us | 816.73 us | 894.47 us | **422.01 us** | 2.57 ms | 2.37 ms | 288.12 ms |
| prism-3 | 783.59 us | 393.61 us | 346.61 us | 11.26 ms | 621.79 us | 723.55 us | 702.15 us | **300.77 us** | 2.16 ms | 2.01 ms | 209.96 ms |
| pubkey-1 | 475.83 us | 174.63 us | 146.91 us | 6.31 ms | 299.14 us | 247.20 us | 253.34 us | **138.59 us** | 894.50 us | 856.20 us | 88.72 ms |
| stablecoin_1-1 | 2.85 ms | 1.14 ms | 999.64 us | 287.47 ms | 1.84 ms | 1.91 ms | 2.43 ms | **799.73 us** | 7.15 ms | 9.60 ms | FAIL |
| stablecoin_1-2 | 516.74 us | 221.27 us | 218.94 us | 9.73 ms | 345.75 us | 328.13 us | 334.36 us | **162.10 us** | 1.18 ms | 1.13 ms | 112.31 ms |
| stablecoin_1-3 | 3.03 ms | 1.22 ms | 1.15 ms | 289.77 ms | 2.09 ms | 2.18 ms | 2.30 ms | **841.14 us** | 7.76 ms | 10.45 ms | FAIL |
| stablecoin_1-4 | 536.16 us | 239.49 us | 188.71 us | 9.46 ms | 366.95 us | 351.86 us | 364.21 us | **174.29 us** | 1.24 ms | 1.17 ms | 117.53 ms |
| stablecoin_1-5 | 3.60 ms | 1.42 ms | 1.36 ms | 294.20 ms | 2.65 ms | 2.57 ms | 3.04 ms | **1.01 ms** | 8.95 ms | 12.20 ms | FAIL |
| stablecoin_1-6 | 553.52 us | 266.88 us | 233.83 us | 13.08 ms | 406.86 us | 403.14 us | 441.23 us | **205.24 us** | 1.48 ms | 1.40 ms | 144.10 ms |
| stablecoin_2-1 | 2.88 ms | 1.13 ms | 982.95 us | 299.52 ms | 1.79 ms | 1.78 ms | 1.95 ms | **827.04 us** | 6.63 ms | 9.59 ms | FAIL |
| stablecoin_2-2 | 489.00 us | 233.09 us | 194.36 us | 8.74 ms | 369.88 us | 352.03 us | 329.28 us | **170.21 us** | 1.19 ms | 1.12 ms | 114.03 ms |
| stablecoin_2-3 | 3.20 ms | 1.22 ms | 1.21 ms | 296.29 ms | 2.14 ms | 2.03 ms | 2.19 ms | **858.66 us** | 7.28 ms | 10.40 ms | FAIL |
| stablecoin_2-4 | 497.12 us | 225.80 us | 197.53 us | 10.14 ms | 363.08 us | 339.48 us | 373.08 us | **178.13 us** | 1.22 ms | 1.18 ms | 120.37 ms |
| token-account-1 | 591.50 us | 255.33 us | 201.47 us | 5.98 ms | 362.14 us | 391.83 us | 397.23 us | **193.22 us** | 1.14 ms | 1.10 ms | 126.08 ms |
| token-account-2 | 737.59 us | 351.21 us | 284.75 us | 9.35 ms | 523.09 us | 652.89 us | 671.14 us | **272.15 us** | 1.84 ms | 1.70 ms | 206.97 ms |
| uniswap-1 | 833.82 us | 418.55 us | **341.16 us** | 9.25 ms | 610.43 us | 747.06 us | 845.57 us | 351.17 us | 2.22 ms | 2.03 ms | 279.51 ms |
| uniswap-2 | 627.38 us | 279.92 us | 235.05 us | 8.25 ms | 414.20 us | 471.16 us | 515.55 us | **224.41 us** | 1.30 ms | 1.28 ms | 141.87 ms |
| uniswap-3 | 3.73 ms | 1.66 ms | 1.36 ms | 31.28 ms | 2.52 ms | 2.84 ms | 3.02 ms | **1.31 ms** | 9.25 ms | 9.04 ms | 915.36 ms |
| uniswap-4 | 704.23 us | 321.54 us | 285.45 us | 15.89 ms | 510.00 us | 576.34 us | 546.13 us | **251.50 us** | 1.93 ms | 1.80 ms | 184.14 ms |
| uniswap-5 | 2.75 ms | 1.20 ms | 1.03 ms | 30.29 ms | 1.92 ms | 1.94 ms | 2.06 ms | **916.80 us** | 6.01 ms | 6.23 ms | 623.93 ms |
| uniswap-6 | 652.70 us | 319.06 us | 272.52 us | 15.46 ms | 530.75 us | 558.39 us | 556.80 us | **253.71 us** | 1.70 ms | 1.74 ms | 171.59 ms |
| vesting-1 | 1.01 ms | 440.34 us | 328.27 us | 9.14 ms | 599.92 us | 647.67 us | 718.82 us | **322.63 us** | 1.82 ms | 1.83 ms | 219.94 ms |

## Eval tier: evaluate a decoded program

The program is decoded before timing; each iteration evaluates it. JIT VMs compile before timing too.

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 168.95 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 186.40 us | 1.10x |
| **Plutigo CEK (Go)** | Go | 244.43 us | 1.45x |
| **Amaru UPLC CEK (Rust)** | Rust | 253.88 us | 1.50x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 284.47 us | 1.68x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 362.85 us | 2.15x |
| **Plutuz CEK (Zig)** | Zig | 467.44 us | 2.77x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 525.01 us | 3.11x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 547.94 us | 3.24x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 823.80 us | 4.88x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.87 ms | 11.05x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.88 ms | 11.12x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 12.84 ms | 76.01x |
| **opshin CEK (Python / CPython)** | Python / CPython | 91.76 ms | 543.12x |

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
| blaze-plutus CEK (TypeScript / Node V8) | 89 | 0 | 0 | 89 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 89 | 0 | 0 | 89 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | 89 | 0 | 0 | 89 |
| opshin CEK (Python / CPython) | 59 | 30 | 0 | 89 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc post-JIT execution (C++ / LLVM) | Amaru UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| auction_1-1 | 165.67 us | **42.71 us** | 118.47 us | 276.81 us | 70.54 us | 114.42 us | 6.59 ms | 222.65 us | 226.51 us | 224.57 us | 110.92 us | 765.90 us | 909.40 us | 97.35 ms |
| auction_1-2 | 628.85 us | 1.17 ms | 450.99 us | 840.60 us | **311.54 us** | 467.55 us | 10.82 ms | 772.33 us | 917.31 us | 977.40 us | 438.11 us | 2.79 ms | 2.73 ms | 346.76 ms |
| auction_1-3 | 563.99 us | 763.34 us | 462.67 us | 883.10 us | **275.00 us** | 422.78 us | 11.62 ms | 717.35 us | 944.42 us | 1.01 ms | 424.49 us | 2.78 ms | 2.66 ms | 362.44 ms |
| auction_1-4 | 230.88 us | **47.60 us** | 152.56 us | 326.31 us | 88.79 us | 147.66 us | 8.82 ms | 272.55 us | 296.56 us | 305.69 us | 133.70 us | 1.02 ms | 1.21 ms | 112.57 ms |
| auction_2-1 | 164.61 us | **42.77 us** | 122.96 us | 274.65 us | 76.06 us | 121.03 us | 6.82 ms | 236.70 us | 221.39 us | 225.29 us | 104.69 us | 868.10 us | 891.50 us | 92.96 ms |
| auction_2-2 | 580.94 us | 1.18 ms | 447.76 us | 823.24 us | **277.06 us** | 468.93 us | 11.35 ms | 793.81 us | 952.12 us | 1.02 ms | 427.15 us | 2.64 ms | 2.75 ms | 350.91 ms |
| auction_2-3 | 736.29 us | 1.11 ms | 634.06 us | 1.13 ms | **349.21 us** | 547.28 us | 13.72 ms | 943.07 us | 1.14 ms | 1.36 ms | 544.12 us | 3.80 ms | 3.55 ms | 434.91 ms |
| auction_2-4 | 590.64 us | 691.81 us | 438.17 us | 831.52 us | **273.49 us** | 433.15 us | 11.31 ms | 715.12 us | 957.97 us | 1.08 ms | 443.59 us | 2.89 ms | 2.70 ms | 371.34 ms |
| auction_2-5 | 213.39 us | **45.72 us** | 160.17 us | 329.31 us | 94.11 us | 147.75 us | 8.66 ms | 286.54 us | 277.28 us | 283.30 us | 133.07 us | 1.14 ms | 1.24 ms | 116.07 ms |
| coop-1 | 216.45 us | **45.78 us** | 188.84 us | FAIL | 98.45 us | 126.76 us | 9.40 ms | 272.49 us | 281.93 us | 302.93 us | 137.28 us | 1.49 ms | 1.42 ms | FAIL |
| coop-2 | 727.03 us | **159.38 us** | 662.82 us | FAIL | 295.51 us | 376.84 us | 29.22 ms | 804.33 us | 853.29 us | 930.81 us | 441.96 us | 4.37 ms | 4.17 ms | FAIL |
| coop-3 | 1.98 ms | **670.60 us** | 2.00 ms | FAIL | 968.05 us | 1.24 ms | 35.04 ms | 2.62 ms | 3.26 ms | 3.18 ms | 1.47 ms | 16.01 ms | 10.19 ms | FAIL |
| coop-4 | 941.21 us | **263.35 us** | 780.34 us | FAIL | 422.39 us | 508.17 us | 29.47 ms | 1.09 ms | 1.12 ms | 1.14 ms | 562.31 us | 6.43 ms | 4.91 ms | FAIL |
| coop-5 | 386.30 us | **90.56 us** | 337.54 us | FAIL | 169.68 us | 226.75 us | 14.97 ms | 449.59 us | 487.48 us | 497.08 us | 247.85 us | 2.54 ms | 2.11 ms | FAIL |
| coop-6 | 732.22 us | **142.32 us** | 589.51 us | FAIL | 265.24 us | 339.21 us | 29.77 ms | 859.70 us | 817.20 us | 915.45 us | 448.54 us | 4.08 ms | 3.77 ms | FAIL |
| coop-7 | 304.66 us | **57.82 us** | 275.84 us | FAIL | 133.28 us | 167.16 us | 13.95 ms | 419.17 us | 402.20 us | 383.72 us | 201.07 us | 2.06 ms | 1.74 ms | FAIL |
| crowdfunding-success-1 | 215.43 us | **41.74 us** | 138.01 us | 298.59 us | 92.58 us | 133.34 us | 8.13 ms | 242.38 us | 261.25 us | 275.13 us | 127.16 us | 1.07 ms | 988.80 us | 105.80 ms |
| crowdfunding-success-2 | 199.24 us | **42.28 us** | 149.61 us | 318.67 us | 90.70 us | 132.16 us | 7.82 ms | 237.66 us | 270.26 us | 273.17 us | 123.65 us | 1.08 ms | 1.02 ms | 110.57 ms |
| crowdfunding-success-3 | 204.71 us | **41.42 us** | 138.88 us | 301.19 us | 85.84 us | 124.89 us | 7.82 ms | 238.32 us | 266.81 us | 290.33 us | 123.01 us | 1.11 ms | 959.50 us | 103.60 ms |
| currency-1 | 229.43 us | **67.52 us** | 184.77 us | 363.71 us | 111.90 us | 171.70 us | 6.10 ms | 318.42 us | 382.75 us | 375.00 us | 164.99 us | 1.31 ms | 1.21 ms | 134.46 ms |
| escrow-redeem_1-1 | 317.17 us | **91.04 us** | 247.41 us | 467.16 us | 155.64 us | 229.90 us | 9.70 ms | 406.46 us | 461.52 us | 486.43 us | 236.95 us | 1.80 ms | 1.64 ms | 178.68 ms |
| escrow-redeem_1-2 | 329.62 us | **85.73 us** | 259.78 us | 506.21 us | 149.02 us | 218.41 us | 8.79 ms | 397.91 us | 480.80 us | 476.40 us | 230.13 us | 1.78 ms | 1.70 ms | 191.77 ms |
| escrow-redeem_2-1 | 367.19 us | **93.31 us** | 287.84 us | 535.60 us | 186.26 us | 250.74 us | 10.15 ms | 449.06 us | 569.96 us | 565.91 us | 251.92 us | 2.09 ms | 1.93 ms | 207.55 ms |
| escrow-redeem_2-2 | 375.13 us | **107.94 us** | 287.30 us | 553.55 us | 176.90 us | 250.86 us | 10.02 ms | 448.47 us | 541.47 us | 583.22 us | 250.49 us | 1.99 ms | 1.91 ms | 222.04 ms |
| escrow-redeem_2-3 | 366.15 us | **99.32 us** | 292.59 us | 534.01 us | 170.15 us | 263.62 us | 10.02 ms | 452.94 us | 546.56 us | 557.74 us | 250.83 us | 1.97 ms | 1.81 ms | 224.93 ms |
| escrow-refund-1 | 161.08 us | **33.61 us** | 103.73 us | 261.94 us | 69.14 us | 97.49 us | 5.54 ms | 185.78 us | 188.48 us | 190.36 us | 91.58 us | 682.50 us | 819.40 us | 91.99 ms |
| future-increase-margin-1 | 221.30 us | **63.16 us** | 184.79 us | 346.12 us | 109.81 us | 167.59 us | 5.85 ms | 321.19 us | 373.96 us | 366.83 us | 166.62 us | 1.03 ms | 1.19 ms | 142.15 ms |
| future-increase-margin-2 | 511.46 us | **159.93 us** | 365.75 us | 677.61 us | 221.30 us | 347.49 us | 13.86 ms | 607.38 us | 739.89 us | 793.61 us | 362.06 us | 2.18 ms | 2.50 ms | 288.54 ms |
| future-increase-margin-3 | 482.05 us | **157.77 us** | 408.64 us | 693.82 us | 235.29 us | 354.77 us | 13.55 ms | 613.40 us | 764.48 us | 765.36 us | 354.29 us | 2.17 ms | 2.45 ms | 286.93 ms |
| future-increase-margin-4 | 476.48 us | 659.36 us | 338.62 us | 720.36 us | **215.30 us** | 353.60 us | 10.01 ms | 620.00 us | 680.41 us | 778.30 us | 336.00 us | 1.98 ms | 2.30 ms | FAIL |
| future-increase-margin-5 | 734.66 us | 1.58 ms | 622.06 us | 1.31 ms | **384.41 us** | 581.16 us | 147.77 ms | 1.16 ms | 1.26 ms | 1.35 ms | 502.06 us | 4.24 ms | 6.16 ms | FAIL |
| future-pay-out-1 | 225.18 us | **64.16 us** | 174.75 us | 342.68 us | 108.62 us | 161.78 us | 5.67 ms | 298.69 us | 375.36 us | 423.56 us | 157.23 us | 1.07 ms | 1.14 ms | 133.85 ms |
| future-pay-out-2 | 496.69 us | **176.75 us** | 402.06 us | 705.09 us | 234.42 us | 350.81 us | 12.37 ms | 650.55 us | 784.84 us | 763.09 us | 331.51 us | 2.26 ms | 2.50 ms | 297.15 ms |
| future-pay-out-3 | 476.63 us | **163.40 us** | 366.29 us | 666.32 us | 229.66 us | 334.41 us | 12.32 ms | 595.79 us | 707.23 us | 766.25 us | 348.52 us | 2.25 ms | 2.31 ms | 301.24 ms |
| future-pay-out-4 | 743.35 us | 1.55 ms | 604.18 us | 1.32 ms | **386.28 us** | 599.37 us | 156.46 ms | 1.17 ms | 1.29 ms | 1.27 ms | 525.55 us | 4.08 ms | 5.70 ms | FAIL |
| future-settle-early-1 | 223.16 us | **60.33 us** | 179.70 us | 348.54 us | 109.12 us | 178.73 us | 5.70 ms | 286.68 us | 366.07 us | 363.97 us | 159.78 us | 983.00 us | 1.12 ms | 140.39 ms |
| future-settle-early-2 | 510.29 us | **176.49 us** | 380.34 us | 718.99 us | 233.89 us | 333.90 us | 12.54 ms | 602.38 us | 729.12 us | 848.30 us | 335.15 us | 2.15 ms | 2.26 ms | 279.79 ms |
| future-settle-early-3 | 478.50 us | **179.13 us** | 383.46 us | 658.35 us | 227.19 us | 337.17 us | 12.21 ms | 590.96 us | 734.00 us | 767.01 us | 334.94 us | 2.21 ms | 2.36 ms | 275.99 ms |
| future-settle-early-4 | 580.48 us | 1.45 ms | 456.08 us | 1.05 ms | **309.30 us** | 436.81 us | 145.45 ms | 894.63 us | 931.27 us | 984.56 us | 369.61 us | 3.04 ms | 4.67 ms | FAIL |
| game-sm-success_1-1 | 359.77 us | 312.20 us | 297.62 us | 548.26 us | **170.16 us** | 272.18 us | 8.77 ms | 477.80 us | 526.71 us | 538.68 us | 250.93 us | 1.60 ms | 1.66 ms | 205.90 ms |
| game-sm-success_1-2 | 206.09 us | **37.32 us** | 131.50 us | 295.02 us | 78.20 us | 128.05 us | 7.83 ms | 244.32 us | 246.47 us | 267.37 us | 125.05 us | 865.80 us | 963.10 us | 96.74 ms |
| game-sm-success_1-3 | 566.61 us | 654.96 us | 464.58 us | 839.00 us | **276.45 us** | 430.71 us | 13.17 ms | 789.84 us | 966.88 us | 942.35 us | 441.77 us | 2.67 ms | 2.65 ms | 346.16 ms |
| game-sm-success_1-4 | 224.46 us | **44.01 us** | 153.54 us | 334.62 us | 89.28 us | 146.51 us | 9.04 ms | 277.17 us | 287.93 us | 290.31 us | 135.10 us | 1.04 ms | 1.08 ms | 124.69 ms |
| game-sm-success_2-1 | 368.12 us | 411.85 us | 294.55 us | 551.87 us | **183.60 us** | 273.62 us | 8.88 ms | 457.69 us | 559.82 us | 556.11 us | 256.36 us | 1.64 ms | 1.62 ms | 220.59 ms |
| game-sm-success_2-2 | 184.15 us | **36.71 us** | 131.97 us | 295.01 us | 77.83 us | 122.93 us | 7.28 ms | 244.97 us | 252.69 us | 255.49 us | 110.67 us | 895.10 us | 926.30 us | 102.46 ms |
| game-sm-success_2-3 | 579.36 us | 711.76 us | 448.89 us | 816.66 us | **292.02 us** | 424.51 us | 11.45 ms | 811.26 us | 1.01 ms | 1.01 ms | 407.54 us | 2.67 ms | 2.61 ms | 353.79 ms |
| game-sm-success_2-4 | 216.79 us | **46.98 us** | 159.12 us | 334.25 us | 93.85 us | 154.54 us | 8.38 ms | 276.73 us | 279.63 us | 285.43 us | 134.34 us | 1.02 ms | 1.08 ms | 110.39 ms |
| game-sm-success_2-5 | 602.40 us | 579.98 us | 452.25 us | 872.58 us | **274.79 us** | 428.00 us | 11.73 ms | 732.32 us | 934.06 us | 1.00 ms | 448.27 us | 2.59 ms | 2.61 ms | 331.04 ms |
| game-sm-success_2-6 | 211.92 us | **43.94 us** | 159.71 us | 330.57 us | 98.71 us | 150.04 us | 8.82 ms | 277.92 us | 299.64 us | 300.19 us | 135.84 us | 1.03 ms | 1.07 ms | 112.93 ms |
| guardrail-sorted-large | 423.35 us | **239.05 us** | 386.44 us | FAIL | 310.67 us | 239.74 us | 57.90 ms | 444.09 us | 591.85 us | 628.42 us | 271.61 us | 2.58 ms | 2.10 ms | FAIL |
| guardrail-sorted-small | 67.73 us | 85.62 us | 85.31 us | FAIL | **27.11 us** | 49.46 us | 874.18 us | 78.92 us | 84.93 us | 94.69 us | 46.16 us | 585.70 us | 364.10 us | FAIL |
| guardrail-unsorted-large | 626.39 us | **311.75 us** | 528.69 us | FAIL | 370.14 us | 320.82 us | 55.00 ms | 616.51 us | 890.86 us | 912.01 us | 394.55 us | 4.24 ms | 2.90 ms | FAIL |
| guardrail-unsorted-small | 65.32 us | 87.98 us | 79.60 us | FAIL | **25.93 us** | 44.97 us | 788.61 us | 76.72 us | 85.65 us | 97.04 us | 45.09 us | 530.00 us | 353.40 us | FAIL |
| multisig-sm-01 | 373.36 us | 414.97 us | 283.54 us | 587.88 us | **177.37 us** | 272.13 us | 8.57 ms | 529.83 us | 560.28 us | 607.74 us | 284.11 us | 1.95 ms | 1.67 ms | FAIL |
| multisig-sm-02 | 365.85 us | 583.50 us | 291.43 us | 570.57 us | **191.66 us** | 290.08 us | 8.62 ms | 489.16 us | 514.64 us | 597.16 us | 289.06 us | 1.87 ms | 1.87 ms | FAIL |
| multisig-sm-03 | 385.45 us | 511.22 us | 285.02 us | 598.04 us | **181.71 us** | 272.19 us | 8.99 ms | 495.87 us | 522.83 us | 582.15 us | 274.94 us | 1.95 ms | 1.80 ms | FAIL |
| multisig-sm-04 | 364.01 us | 681.52 us | 291.83 us | 597.35 us | **180.22 us** | 279.11 us | 10.02 ms | 486.94 us | 583.79 us | 597.93 us | 271.22 us | 1.97 ms | 1.72 ms | FAIL |
| multisig-sm-05 | 537.27 us | 939.38 us | 398.30 us | 774.83 us | **245.41 us** | 396.35 us | 10.88 ms | 684.14 us | 769.09 us | 844.39 us | 375.52 us | 2.81 ms | 2.56 ms | FAIL |
| multisig-sm-06 | 382.28 us | 441.99 us | 287.38 us | 581.70 us | **185.69 us** | 292.08 us | 8.38 ms | 510.87 us | 572.40 us | 598.41 us | 271.04 us | 1.99 ms | 1.68 ms | FAIL |
| multisig-sm-07 | 370.52 us | 505.90 us | 282.83 us | 599.95 us | **200.19 us** | 263.91 us | 8.54 ms | 462.42 us | 500.25 us | 557.02 us | 260.18 us | 1.91 ms | 1.62 ms | FAIL |
| multisig-sm-08 | 359.02 us | 481.75 us | 289.83 us | 564.25 us | **177.44 us** | 267.26 us | 8.39 ms | 468.81 us | 576.82 us | 614.99 us | 286.82 us | 1.96 ms | 1.78 ms | FAIL |
| multisig-sm-09 | 385.98 us | 555.70 us | 296.40 us | 591.43 us | **179.58 us** | 274.09 us | 8.53 ms | 483.98 us | 543.16 us | 589.53 us | 284.33 us | 1.86 ms | 1.70 ms | FAIL |
| multisig-sm-10 | 521.26 us | 952.36 us | 399.01 us | 788.58 us | **261.80 us** | 415.12 us | 9.99 ms | 678.83 us | 806.98 us | 900.88 us | 367.04 us | 2.72 ms | 2.29 ms | FAIL |
| ping-pong-1 | 327.18 us | 246.87 us | 250.83 us | 501.79 us | **150.03 us** | 223.53 us | 7.42 ms | 432.82 us | 457.42 us | 459.95 us | 215.93 us | 1.65 ms | 1.45 ms | 206.17 ms |
| ping-pong-2 | 302.85 us | 196.65 us | 235.15 us | 477.21 us | **160.55 us** | 225.29 us | 7.62 ms | 418.48 us | 441.66 us | 477.49 us | 214.96 us | 1.57 ms | 1.41 ms | 193.59 ms |
| ping-pong_2-1 | 204.87 us | **79.81 us** | 147.71 us | 344.37 us | 93.67 us | 138.43 us | 5.65 ms | 242.46 us | 267.79 us | 266.55 us | 126.91 us | 975.50 us | 874.30 us | 122.42 ms |
| prism-1 | 156.71 us | **31.97 us** | 122.93 us | 240.83 us | 67.00 us | 108.90 us | 5.99 ms | 201.33 us | 213.19 us | 221.91 us | 101.02 us | 745.20 us | 777.80 us | 82.37 ms |
| prism-2 | 402.46 us | 317.67 us | 299.20 us | 606.32 us | **180.59 us** | 270.68 us | 9.66 ms | 490.27 us | 587.87 us | 578.48 us | 298.85 us | 1.75 ms | 1.74 ms | 220.36 ms |
| prism-3 | 332.21 us | **101.05 us** | 269.58 us | 495.41 us | 154.25 us | 246.51 us | 9.61 ms | 439.30 us | 496.03 us | 526.00 us | 247.44 us | 1.66 ms | 1.61 ms | 185.98 ms |
| pubkey-1 | 141.31 us | **25.20 us** | 101.05 us | 214.30 us | 59.19 us | 93.25 us | 5.16 ms | 185.10 us | 169.96 us | 189.60 us | 78.83 us | 643.80 us | 654.40 us | 70.64 ms |
| stablecoin_1-1 | 875.02 us | 2.60 ms | 787.97 us | 1.72 ms | **459.46 us** | 755.67 us | 307.63 ms | 1.38 ms | 1.37 ms | 1.40 ms | 542.45 us | 5.46 ms | 8.22 ms | FAIL |
| stablecoin_1-2 | 182.21 us | **39.03 us** | 129.02 us | 290.44 us | 88.25 us | 125.85 us | 7.89 ms | 241.68 us | 250.23 us | 238.34 us | 108.84 us | 953.60 us | 905.20 us | 94.76 ms |
| stablecoin_1-3 | 1.00 ms | 2.59 ms | 861.98 us | 1.90 ms | **475.34 us** | 872.59 us | 284.63 ms | 1.47 ms | 1.68 ms | 1.64 ms | 640.23 us | 6.78 ms | 8.94 ms | FAIL |
| stablecoin_1-4 | 200.35 us | **43.12 us** | 135.29 us | 299.69 us | 91.78 us | 138.89 us | 8.26 ms | 245.19 us | 262.02 us | 257.46 us | 125.92 us | 1.02 ms | 959.10 us | 102.36 ms |
| stablecoin_1-5 | 1.26 ms | 2.62 ms | 1.08 ms | 2.42 ms | **575.22 us** | 1.14 ms | 297.85 ms | 1.93 ms | 2.20 ms | 2.26 ms | 818.06 us | 7.81 ms | 10.42 ms | FAIL |
| stablecoin_1-6 | 237.40 us | **48.73 us** | 166.55 us | 352.69 us | 114.71 us | 157.45 us | 10.12 ms | 321.79 us | 310.08 us | 313.62 us | 140.63 us | 1.15 ms | 1.17 ms | 125.22 ms |
| stablecoin_2-1 | 889.92 us | 2.59 ms | 761.09 us | 1.70 ms | **444.48 us** | 738.65 us | 284.85 ms | 1.32 ms | 1.59 ms | 1.50 ms | 538.84 us | 6.26 ms | 8.14 ms | FAIL |
| stablecoin_2-2 | 189.09 us | **38.48 us** | 130.33 us | 282.47 us | 82.70 us | 126.89 us | 8.12 ms | 256.57 us | 237.77 us | 248.90 us | 109.52 us | 926.90 us | 898.10 us | 95.57 ms |
| stablecoin_2-3 | 1.03 ms | 2.71 ms | 848.01 us | 1.97 ms | **517.75 us** | 883.32 us | 306.00 ms | 1.63 ms | 1.72 ms | 1.86 ms | 654.87 us | 6.71 ms | 8.93 ms | FAIL |
| stablecoin_2-4 | 188.69 us | **40.29 us** | 138.88 us | 295.42 us | 82.36 us | 133.79 us | 8.19 ms | 256.14 us | 253.96 us | 258.59 us | 126.92 us | 1.00 ms | 959.40 us | 110.42 ms |
| token-account-1 | 190.41 us | **56.78 us** | 135.68 us | 290.69 us | 84.23 us | 137.79 us | 4.86 ms | 234.75 us | 268.05 us | 269.03 us | 132.03 us | 912.00 us | 829.70 us | 115.61 ms |
| token-account-2 | 308.25 us | **72.82 us** | 251.91 us | 440.52 us | 142.09 us | 206.52 us | 8.12 ms | 377.06 us | 483.89 us | 488.55 us | 220.15 us | 1.46 ms | 1.43 ms | 203.54 ms |
| uniswap-1 | 367.45 us | **98.24 us** | 285.27 us | 530.29 us | 177.49 us | 249.52 us | 8.04 ms | 464.61 us | 573.28 us | 681.96 us | 267.52 us | 1.77 ms | 1.72 ms | 240.35 ms |
| uniswap-2 | 205.92 us | **62.44 us** | 169.25 us | 330.29 us | 98.09 us | 148.63 us | 7.16 ms | 264.86 us | 292.17 us | 316.66 us | 136.74 us | 966.70 us | 998.40 us | 123.67 ms |
| uniswap-3 | 1.64 ms | 926.39 us | 1.22 ms | 2.17 ms | **712.25 us** | 1.22 ms | 29.13 ms | 2.26 ms | 2.27 ms | 2.53 ms | 1.10 ms | 7.21 ms | 7.44 ms | 804.87 ms |
| uniswap-4 | 303.24 us | **62.54 us** | 237.68 us | 472.26 us | 130.62 us | 205.25 us | 14.23 ms | 423.43 us | 469.35 us | 441.27 us | 189.74 us | 1.48 ms | 1.56 ms | 167.74 ms |
| uniswap-5 | 1.04 ms | 687.43 us | 795.16 us | 1.46 ms | **435.94 us** | 749.12 us | 23.37 ms | 1.31 ms | 1.42 ms | 1.65 ms | 774.57 us | 5.23 ms | 5.23 ms | 543.19 ms |
| uniswap-6 | 289.87 us | **58.57 us** | 231.43 us | 436.01 us | 126.22 us | 203.77 us | 12.97 ms | 389.49 us | 449.19 us | 409.08 us | 191.57 us | 1.43 ms | 1.52 ms | 156.17 ms |
| vesting-1 | 328.11 us | 219.72 us | 247.72 us | 488.66 us | **158.75 us** | 236.63 us | 7.64 ms | 382.92 us | 483.08 us | 496.88 us | 233.26 us | 1.49 ms | 1.58 ms | 185.25 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*