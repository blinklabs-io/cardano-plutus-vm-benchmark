# Cardano Plutus VM Benchmark Results

**Date:** 2026-11-11

## Environment
```
date: 2026-11-11T13:54:20+00:00
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
| Plutigo CEK (Go) | v0.12.1 ([7bc0974](https://github.com/blinklabs-io/plutigo/commit/7bc0974b34074a0a12efc95ba9dfac58453173bf)) | Go 1.27.3 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 0.5.3 ([320fc36](https://github.com/butaneprotocol/blaze-cardano/commit/320fc3604cfeac640013fd8206efaecfe8a2360f)) | Bun 1.3.14 |
| blaze-plutus CEK (TypeScript / Node V8) | 0.5.3 ([320fc36](https://github.com/butaneprotocol/blaze-cardano/commit/320fc3604cfeac640013fd8206efaecfe8a2360f)) | Node.js 22 |
| opshin CEK (Python / CPython) | 1.3.3 ([eda2fba](https://github.com/OpShin/uplc/commit/eda2fbaa89c1a2db4ec6c6c1fa5eea2a8b2671d4)) | Python 3.14 |

## Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

*Measurement caveats: llvm-uplc reports steady-state execution after JIT compilation; its per-script compilation time is retained only in the raw JSON. Scalus JIT, Scalus CEK, Julc and Chrysalis use three measurement samples, and their raw framework output should be consulted for uncertainty.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 162.69 us | 1.00x |
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 174.84 us | 1.07x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 351.02 us | 2.16x |
| **Plutigo CEK (Go)** | Go | 352.55 us | 2.17x |
| **Amaru UPLC CEK (Rust)** | Rust | 370.44 us | 2.28x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 444.33 us | 2.73x |
| **Plutuz CEK (Zig)** | Zig | 655.00 us | 4.03x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 706.66 us | 4.34x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 748.33 us | 4.60x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 804.04 us | 4.94x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.29 ms | 14.05x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 2.30 ms | 14.13x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 14.45 ms | 88.82x |
| **opshin CEK (Python / CPython)** | Python / CPython | 104.09 ms | 639.84x |

### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| llvm-uplc post-JIT execution (C++ / LLVM) | 89 | 0 | 0 | 89 |
| Scalus UPLC→JVM JIT (Scala / JVM) | 89 | 0 | 0 | 89 |
| plutus-core CEK (Haskell / GHC) | 89 | 0 | 0 | 89 |
| Plutigo CEK (Go) | 89 | 0 | 0 | 89 |
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
| auction_1-1 | 162.91 us | **41.64 us** | 218.66 us | 263.12 us | 68.34 us | 185.40 us | 7.15 ms | 331.82 us | 329.46 us | 345.07 us | 174.21 us | 1.07 ms | 1.06 ms | 110.57 ms |
| auction_1-2 | 572.26 us | 897.55 us | 702.83 us | 837.62 us | **282.65 us** | 616.42 us | 12.84 ms | 1.07 ms | 1.16 ms | 1.28 ms | 573.91 us | 3.16 ms | 3.18 ms | 390.34 ms |
| auction_1-3 | 569.03 us | 621.36 us | 697.64 us | 821.50 us | **270.41 us** | 605.95 us | 13.17 ms | 1.01 ms | 1.19 ms | 1.26 ms | 564.28 us | 3.18 ms | 3.33 ms | 399.57 ms |
| auction_1-4 | 210.38 us | **47.50 us** | 247.78 us | 325.48 us | 87.69 us | 218.75 us | 9.70 ms | 395.19 us | 395.47 us | 431.77 us | 198.61 us | 1.26 ms | 1.27 ms | 131.25 ms |
| auction_2-1 | 162.54 us | **42.42 us** | 212.58 us | 266.00 us | 70.86 us | 186.64 us | 7.05 ms | 332.52 us | 335.63 us | 346.86 us | 171.50 us | 1.01 ms | 1.02 ms | 110.71 ms |
| auction_2-2 | 573.58 us | 906.96 us | 707.91 us | 816.32 us | **275.27 us** | 605.75 us | 12.70 ms | 1.05 ms | 1.19 ms | 1.27 ms | 575.60 us | 3.21 ms | 3.17 ms | 388.60 ms |
| auction_2-3 | 726.64 us | 966.19 us | 843.61 us | 1.04 ms | **344.46 us** | 734.93 us | 15.62 ms | 1.26 ms | 1.49 ms | 1.62 ms | 690.68 us | 3.96 ms | 3.98 ms | 492.31 ms |
| auction_2-4 | 559.01 us | 563.30 us | 698.06 us | 829.54 us | **269.40 us** | 607.49 us | 13.15 ms | 1.01 ms | 1.18 ms | 1.25 ms | 576.80 us | 3.20 ms | 3.19 ms | 391.24 ms |
| auction_2-5 | 213.11 us | **48.45 us** | 249.85 us | 321.26 us | 87.51 us | 217.78 us | 9.46 ms | 395.43 us | 419.75 us | 417.67 us | 199.04 us | 1.26 ms | 1.27 ms | 133.60 ms |
| coop-1 | 218.71 us | **40.31 us** | 245.19 us | FAIL | 91.34 us | 176.77 us | 10.40 ms | 331.91 us | 338.87 us | 369.16 us | 189.44 us | 1.42 ms | 1.57 ms | FAIL |
| coop-2 | 685.50 us | **158.15 us** | 765.93 us | FAIL | 287.00 us | 500.43 us | 31.63 ms | 962.58 us | 1.16 ms | 1.20 ms | 594.60 us | 4.40 ms | 4.51 ms | FAIL |
| coop-3 | 2.02 ms | **646.29 us** | 2.12 ms | FAIL | 929.75 us | 1.35 ms | 36.22 ms | 2.54 ms | 3.85 ms | 3.76 ms | 1.60 ms | 10.89 ms | 11.16 ms | FAIL |
| coop-4 | 902.91 us | **242.78 us** | 933.96 us | FAIL | 384.92 us | 637.85 us | 28.21 ms | 1.15 ms | 1.39 ms | 1.50 ms | 721.86 us | 5.17 ms | 5.33 ms | FAIL |
| coop-5 | 382.81 us | **84.74 us** | 472.28 us | FAIL | 168.02 us | 335.87 us | 15.40 ms | 608.05 us | 681.13 us | 724.38 us | 367.75 us | 2.44 ms | 2.64 ms | FAIL |
| coop-6 | 634.89 us | **142.44 us** | 688.44 us | FAIL | 263.52 us | 430.20 us | 30.85 ms | 872.82 us | 974.69 us | 1.01 ms | 512.67 us | 3.87 ms | 4.04 ms | FAIL |
| coop-7 | 303.69 us | **53.94 us** | 330.60 us | FAIL | 127.39 us | 231.45 us | 15.58 ms | 450.89 us | 482.85 us | 506.10 us | 259.70 us | 1.96 ms | 2.12 ms | FAIL |
| crowdfunding-success-1 | 197.48 us | **43.24 us** | 255.73 us | 301.99 us | 85.46 us | 209.94 us | 8.90 ms | 382.81 us | 383.83 us | 400.62 us | 202.18 us | 1.23 ms | 1.24 ms | 130.59 ms |
| crowdfunding-success-2 | 196.78 us | **43.11 us** | 257.02 us | 298.44 us | 84.03 us | 209.30 us | 8.95 ms | 384.96 us | 383.07 us | 397.71 us | 206.72 us | 1.23 ms | 1.24 ms | 130.46 ms |
| crowdfunding-success-3 | 197.85 us | **40.99 us** | 254.87 us | 295.11 us | 84.89 us | 209.85 us | 8.96 ms | 387.14 us | 380.81 us | 394.38 us | 201.55 us | 1.25 ms | 1.24 ms | 132.30 ms |
| currency-1 | 222.37 us | **63.46 us** | 293.40 us | 343.52 us | 106.82 us | 246.29 us | 6.71 ms | 425.15 us | 476.48 us | 513.80 us | 235.53 us | 1.45 ms | 1.37 ms | 160.65 ms |
| escrow-redeem_1-1 | 316.37 us | **86.73 us** | 405.71 us | 459.49 us | 148.21 us | 325.33 us | 10.17 ms | 576.31 us | 646.40 us | 680.80 us | 322.03 us | 1.90 ms | 1.90 ms | 223.38 ms |
| escrow-redeem_1-2 | 319.04 us | **82.26 us** | 403.63 us | 461.14 us | 149.20 us | 331.28 us | 10.26 ms | 574.00 us | 633.43 us | 726.31 us | 320.71 us | 1.89 ms | 1.89 ms | 214.57 ms |
| escrow-redeem_2-1 | 366.28 us | **93.48 us** | 447.79 us | 530.67 us | 169.94 us | 363.90 us | 11.60 ms | 639.43 us | 735.07 us | 780.55 us | 355.48 us | 2.15 ms | 2.15 ms | 244.69 ms |
| escrow-redeem_2-2 | 366.78 us | **92.03 us** | 446.46 us | 516.22 us | 168.70 us | 362.14 us | 11.62 ms | 638.44 us | 746.29 us | 785.70 us | 354.48 us | 2.15 ms | 2.15 ms | 241.27 ms |
| escrow-redeem_2-3 | 368.49 us | **99.82 us** | 442.38 us | 532.76 us | 168.51 us | 364.32 us | 11.60 ms | 636.97 us | 743.35 us | 791.83 us | 356.05 us | 2.15 ms | 2.15 ms | 246.72 ms |
| escrow-refund-1 | 144.05 us | **35.52 us** | 254.85 us | 248.26 us | 66.27 us | 200.93 us | 6.57 ms | 365.56 us | 339.26 us | 355.93 us | 190.39 us | 1.05 ms | 1.06 ms | 120.24 ms |
| future-increase-margin-1 | 221.34 us | **63.57 us** | 295.11 us | 344.77 us | 105.57 us | 245.79 us | 6.80 ms | 426.17 us | 480.66 us | 513.77 us | 235.12 us | 1.36 ms | 1.42 ms | 161.19 ms |
| future-increase-margin-2 | 479.08 us | **153.96 us** | 542.01 us | 662.44 us | 219.55 us | 448.88 us | 14.03 ms | 799.28 us | 947.98 us | 1.01 ms | 449.92 us | 2.73 ms | 2.80 ms | 308.43 ms |
| future-increase-margin-3 | 475.77 us | **142.06 us** | 538.36 us | 678.70 us | 219.16 us | 449.88 us | 14.01 ms | 781.42 us | 952.89 us | 1.01 ms | 439.15 us | 2.74 ms | 2.74 ms | 314.12 ms |
| future-increase-margin-4 | 439.10 us | 534.95 us | 658.48 us | 696.00 us | **212.25 us** | 556.41 us | 12.13 ms | 958.80 us | 1.03 ms | 1.09 ms | 511.93 us | 2.84 ms | 2.76 ms | FAIL |
| future-increase-margin-5 | 728.29 us | 1.50 ms | 898.70 us | 1.12 ms | **381.45 us** | 814.95 us | 147.30 ms | 1.50 ms | 1.53 ms | 1.70 ms | 685.56 us | 6.65 ms | 6.62 ms | FAIL |
| future-pay-out-1 | 223.08 us | **66.05 us** | 291.93 us | 338.18 us | 106.17 us | 247.85 us | 6.58 ms | 428.28 us | 474.19 us | 515.23 us | 236.69 us | 1.37 ms | 1.37 ms | 159.12 ms |
| future-pay-out-2 | 481.04 us | **162.01 us** | 540.37 us | 672.64 us | 228.22 us | 454.76 us | 14.05 ms | 779.60 us | 974.90 us | 1.01 ms | 440.04 us | 2.75 ms | 2.74 ms | 311.32 ms |
| future-pay-out-3 | 478.44 us | **145.60 us** | 532.18 us | 664.79 us | 224.00 us | 453.10 us | 14.00 ms | 780.31 us | 969.95 us | 1.03 ms | 439.49 us | 2.75 ms | 2.74 ms | 320.50 ms |
| future-pay-out-4 | 736.31 us | 1.52 ms | 900.78 us | 1.14 ms | **382.80 us** | 803.94 us | 147.15 ms | 1.49 ms | 1.57 ms | 1.70 ms | 680.95 us | 6.55 ms | 6.45 ms | FAIL |
| future-settle-early-1 | 221.69 us | **60.54 us** | 291.42 us | 341.03 us | 105.96 us | 247.20 us | 6.57 ms | 426.09 us | 478.38 us | 512.90 us | 235.64 us | 1.37 ms | 1.37 ms | 160.60 ms |
| future-settle-early-2 | 478.23 us | **153.72 us** | 538.07 us | 672.12 us | 221.57 us | 450.16 us | 13.95 ms | 780.48 us | 958.39 us | 1.01 ms | 440.12 us | 2.76 ms | 2.76 ms | 310.96 ms |
| future-settle-early-3 | 481.85 us | **163.51 us** | 538.34 us | 678.75 us | 221.09 us | 452.32 us | 14.39 ms | 781.20 us | 928.70 us | 1.00 ms | 449.31 us | 2.75 ms | 2.78 ms | 315.86 ms |
| future-settle-early-4 | 560.32 us | 1.27 ms | 773.27 us | 879.43 us | **302.75 us** | 645.46 us | 144.70 ms | 1.20 ms | 1.22 ms | 1.30 ms | 554.84 us | 5.54 ms | 5.52 ms | FAIL |
| game-sm-success_1-1 | 358.20 us | 310.54 us | 516.24 us | 543.65 us | **171.20 us** | 422.32 us | 10.59 ms | 771.36 us | 782.75 us | 816.05 us | 408.54 us | 2.31 ms | 2.31 ms | 256.09 ms |
| game-sm-success_1-2 | 183.42 us | **38.86 us** | 213.77 us | 276.14 us | 77.50 us | 188.84 us | 8.26 ms | 340.62 us | 339.05 us | 342.46 us | 172.43 us | 1.14 ms | 1.15 ms | 117.20 ms |
| game-sm-success_1-3 | 562.90 us | 578.58 us | 687.59 us | 828.01 us | **276.33 us** | 598.85 us | 13.75 ms | 1.03 ms | 1.14 ms | 1.30 ms | 563.97 us | 3.44 ms | 3.44 ms | 384.55 ms |
| game-sm-success_1-4 | 209.68 us | **43.55 us** | 233.04 us | 321.94 us | 88.37 us | 207.28 us | 9.44 ms | 378.02 us | 379.33 us | 389.04 us | 191.43 us | 1.32 ms | 1.31 ms | 129.66 ms |
| game-sm-success_2-1 | 360.52 us | 331.41 us | 520.25 us | 550.11 us | **170.90 us** | 427.68 us | 10.55 ms | 753.41 us | 748.89 us | 818.20 us | 406.08 us | 2.33 ms | 2.33 ms | 256.03 ms |
| game-sm-success_2-2 | 181.77 us | **39.17 us** | 211.33 us | 277.13 us | 76.73 us | 187.66 us | 8.14 ms | 344.30 us | 340.67 us | 347.08 us | 171.88 us | 1.15 ms | 1.14 ms | 116.62 ms |
| game-sm-success_2-3 | 564.18 us | 560.39 us | 688.46 us | 819.13 us | **273.71 us** | 593.62 us | 13.62 ms | 1.03 ms | 1.16 ms | 1.25 ms | 563.51 us | 3.44 ms | 3.44 ms | 389.92 ms |
| game-sm-success_2-4 | 213.73 us | **43.37 us** | 233.60 us | 322.99 us | 88.75 us | 206.38 us | 9.44 ms | 380.75 us | 371.39 us | 396.07 us | 191.79 us | 1.31 ms | 1.31 ms | 129.96 ms |
| game-sm-success_2-5 | 567.18 us | 569.76 us | 690.52 us | 822.06 us | **274.14 us** | 600.32 us | 13.69 ms | 1.03 ms | 1.25 ms | 1.23 ms | 569.78 us | 3.41 ms | 3.42 ms | 386.58 ms |
| game-sm-success_2-6 | 210.17 us | **42.58 us** | 233.28 us | 321.91 us | 88.91 us | 205.73 us | 9.60 ms | 378.87 us | 381.22 us | 402.82 us | 193.30 us | 1.32 ms | 1.31 ms | 128.86 ms |
| guardrail-sorted-large | 420.26 us | **226.69 us** | 486.10 us | FAIL | 304.70 us | 353.06 us | 56.95 ms | 560.97 us | 710.85 us | 761.88 us | 402.42 us | 2.74 ms | 2.77 ms | FAIL |
| guardrail-sorted-small | 66.91 us | 83.42 us | 122.99 us | FAIL | **26.37 us** | 95.78 us | 1.38 ms | 158.43 us | 165.78 us | 175.43 us | 95.70 us | 529.80 us | 628.70 us | FAIL |
| guardrail-unsorted-large | 560.13 us | **292.93 us** | 637.50 us | FAIL | 369.30 us | 446.60 us | 58.38 ms | 727.38 us | 934.83 us | 1.03 ms | 523.23 us | 3.57 ms | 3.53 ms | FAIL |
| guardrail-unsorted-small | 65.05 us | 83.16 us | 121.01 us | FAIL | **25.45 us** | 93.79 us | 1.35 ms | 156.23 us | 156.88 us | 172.43 us | 92.62 us | 524.70 us | 637.30 us | FAIL |
| multisig-sm-01 | 366.89 us | 364.65 us | 555.18 us | 579.18 us | **177.28 us** | 457.83 us | 10.57 ms | 802.97 us | 817.47 us | 868.56 us | 433.22 us | 2.42 ms | 2.40 ms | FAIL |
| multisig-sm-02 | 359.00 us | 500.41 us | 543.17 us | 558.41 us | **174.92 us** | 450.94 us | 10.48 ms | 808.47 us | 790.86 us | 839.79 us | 427.19 us | 2.36 ms | 2.35 ms | FAIL |
| multisig-sm-03 | 361.17 us | 454.07 us | 551.32 us | 571.61 us | **175.93 us** | 457.53 us | 10.56 ms | 789.65 us | 838.73 us | 838.45 us | 434.38 us | 2.38 ms | 2.36 ms | FAIL |
| multisig-sm-04 | 362.61 us | 485.24 us | 547.58 us | 569.91 us | **179.59 us** | 459.64 us | 10.66 ms | 803.02 us | 827.37 us | 853.19 us | 435.43 us | 2.41 ms | 2.38 ms | FAIL |
| multisig-sm-05 | 502.73 us | 855.20 us | 662.84 us | 757.65 us | **246.01 us** | 579.30 us | 12.18 ms | 982.12 us | 1.06 ms | 1.17 ms | 533.93 us | 3.20 ms | 3.10 ms | FAIL |
| multisig-sm-06 | 367.09 us | 359.11 us | 550.70 us | 583.33 us | **178.93 us** | 460.66 us | 10.55 ms | 809.50 us | 820.27 us | 881.91 us | 439.48 us | 2.40 ms | 2.40 ms | FAIL |
| multisig-sm-07 | 360.44 us | 454.59 us | 537.85 us | 557.53 us | **176.59 us** | 453.72 us | 10.52 ms | 790.68 us | 780.74 us | 837.02 us | 428.49 us | 2.36 ms | 2.34 ms | FAIL |
| multisig-sm-08 | 362.32 us | 503.82 us | 550.43 us | 573.70 us | **178.80 us** | 457.49 us | 10.82 ms | 791.45 us | 799.42 us | 847.52 us | 434.23 us | 2.36 ms | 2.35 ms | FAIL |
| multisig-sm-09 | 366.18 us | 493.87 us | 554.68 us | 567.92 us | **178.71 us** | 462.78 us | 10.70 ms | 799.00 us | 833.45 us | 863.30 us | 435.23 us | 2.40 ms | 2.42 ms | FAIL |
| multisig-sm-10 | 501.37 us | 833.30 us | 659.91 us | 760.01 us | **246.27 us** | 580.82 us | 12.12 ms | 982.36 us | 1.09 ms | 1.17 ms | 533.82 us | 3.13 ms | 3.10 ms | FAIL |
| ping-pong-1 | 303.14 us | 225.06 us | 467.96 us | 468.67 us | **147.88 us** | 378.30 us | 8.81 ms | 671.89 us | 663.79 us | 715.28 us | 357.52 us | 1.99 ms | 1.98 ms | 230.74 ms |
| ping-pong-2 | 299.39 us | 212.61 us | 469.10 us | 473.83 us | **147.31 us** | 378.25 us | 8.91 ms | 670.11 us | 664.31 us | 713.67 us | 358.44 us | 2.00 ms | 1.99 ms | 227.54 ms |
| ping-pong_2-1 | 187.51 us | **88.65 us** | 372.06 us | 326.32 us | 93.14 us | 288.49 us | 7.06 ms | 506.96 us | 486.30 us | 505.91 us | 269.11 us | 1.43 ms | 1.42 ms | 168.24 ms |
| prism-1 | 152.41 us | **30.04 us** | 184.56 us | 236.82 us | 64.94 us | 166.29 us | 6.91 ms | 300.59 us | 292.73 us | 297.53 us | 149.66 us | 987.50 us | 982.10 us | 100.34 ms |
| prism-2 | 378.21 us | 311.35 us | 541.60 us | 579.93 us | **180.84 us** | 445.21 us | 12.22 ms | 801.18 us | 804.66 us | 890.11 us | 421.70 us | 2.36 ms | 2.35 ms | 269.40 ms |
| prism-3 | 331.05 us | **92.90 us** | 380.69 us | 498.36 us | 154.81 us | 339.40 us | 11.14 ms | 575.06 us | 659.37 us | 710.06 us | 317.05 us | 1.98 ms | 1.96 ms | 212.95 ms |
| pubkey-1 | 130.06 us | **25.91 us** | 174.99 us | 203.72 us | 57.22 us | 146.22 us | 6.23 ms | 267.90 us | 253.23 us | 256.88 us | 135.34 us | 859.00 us | 855.00 us | 89.13 ms |
| stablecoin_1-1 | 862.78 us | 2.50 ms | 1.11 ms | 1.39 ms | **434.86 us** | 989.28 us | 285.62 ms | 1.74 ms | 1.81 ms | 1.90 ms | 779.91 us | 9.62 ms | 9.58 ms | FAIL |
| stablecoin_1-2 | 179.22 us | **37.50 us** | 208.37 us | 275.70 us | 78.00 us | 184.55 us | 8.74 ms | 338.33 us | 328.35 us | 337.42 us | 170.13 us | 1.14 ms | 1.12 ms | 113.93 ms |
| stablecoin_1-3 | 989.65 us | 2.55 ms | 1.20 ms | 1.64 ms | **475.53 us** | 1.12 ms | 286.30 ms | 1.93 ms | 2.20 ms | 2.15 ms | 859.48 us | 10.51 ms | 10.39 ms | FAIL |
| stablecoin_1-4 | 188.41 us | **40.70 us** | 217.43 us | 289.62 us | 81.78 us | 192.14 us | 9.32 ms | 350.59 us | 347.54 us | 372.12 us | 177.01 us | 1.19 ms | 1.18 ms | 118.77 ms |
| stablecoin_1-5 | 1.24 ms | 2.64 ms | 1.41 ms | 2.06 ms | **551.35 us** | 1.38 ms | 284.65 ms | 2.40 ms | 2.54 ms | 2.69 ms | 1.03 ms | 12.25 ms | 12.28 ms | FAIL |
| stablecoin_1-6 | 233.87 us | **48.37 us** | 252.93 us | 353.59 us | 99.96 us | 222.99 us | 11.33 ms | 404.86 us | 400.85 us | 435.73 us | 206.09 us | 1.46 ms | 1.41 ms | 146.70 ms |
| stablecoin_2-1 | 859.34 us | 2.45 ms | 1.12 ms | 1.39 ms | **435.50 us** | 1.02 ms | 286.22 ms | 1.75 ms | 1.79 ms | 1.92 ms | 782.08 us | 9.63 ms | 9.62 ms | FAIL |
| stablecoin_2-2 | 178.80 us | **38.03 us** | 207.87 us | 271.04 us | 77.53 us | 187.42 us | 8.75 ms | 335.16 us | 330.92 us | 337.82 us | 170.24 us | 1.14 ms | 1.13 ms | 114.85 ms |
| stablecoin_2-3 | 985.51 us | 2.52 ms | 1.22 ms | 1.61 ms | **476.38 us** | 1.13 ms | 286.47 ms | 1.94 ms | 2.04 ms | 2.15 ms | 873.64 us | 10.56 ms | 10.35 ms | FAIL |
| stablecoin_2-4 | 187.32 us | **42.15 us** | 218.12 us | 287.31 us | 82.00 us | 200.05 us | 9.30 ms | 350.59 us | 342.07 us | 370.43 us | 176.72 us | 1.20 ms | 1.19 ms | 119.60 ms |
| token-account-1 | 169.26 us | **48.88 us** | 247.93 us | 279.09 us | 82.93 us | 210.34 us | 5.84 ms | 361.92 us | 384.93 us | 404.10 us | 196.13 us | 1.12 ms | 1.11 ms | 126.98 ms |
| token-account-2 | 299.95 us | **67.86 us** | 345.28 us | 435.43 us | 141.33 us | 291.85 us | 9.24 ms | 517.01 us | 608.96 us | 624.06 us | 285.85 us | 1.73 ms | 1.73 ms | 197.79 ms |
| uniswap-1 | 348.80 us | **96.91 us** | 400.37 us | 501.07 us | 167.41 us | 340.69 us | 9.30 ms | 596.59 us | 757.44 us | 817.08 us | 337.76 us | 2.08 ms | 2.06 ms | 253.32 ms |
| uniswap-2 | 200.24 us | **62.04 us** | 275.07 us | 324.33 us | 95.94 us | 235.74 us | 8.26 ms | 405.48 us | 432.63 us | 460.13 us | 216.58 us | 1.29 ms | 1.28 ms | 142.08 ms |
| uniswap-3 | 1.58 ms | 908.99 us | 1.55 ms | 2.12 ms | **610.74 us** | 1.34 ms | 31.36 ms | 2.47 ms | 2.86 ms | 3.07 ms | 1.32 ms | 9.16 ms | 9.15 ms | 872.63 ms |
| uniswap-4 | 297.06 us | **60.12 us** | 314.00 us | 455.40 us | 127.89 us | 278.56 us | 15.31 ms | 511.98 us | 525.02 us | 577.67 us | 261.00 us | 1.84 ms | 1.81 ms | 177.66 ms |
| uniswap-5 | 1.04 ms | 658.73 us | 1.14 ms | 1.38 ms | **421.25 us** | 955.34 us | 26.57 ms | 1.65 ms | 1.95 ms | 2.07 ms | 938.74 us | 6.32 ms | 6.36 ms | 607.46 ms |
| uniswap-6 | 282.23 us | **58.58 us** | 317.37 us | 439.88 us | 122.89 us | 267.53 us | 14.34 ms | 491.09 us | 516.69 us | 536.06 us | 253.52 us | 1.79 ms | 1.76 ms | 173.14 ms |
| vesting-1 | 316.76 us | 161.67 us | 409.41 us | 458.60 us | **155.07 us** | 334.81 us | 8.76 ms | 572.17 us | 659.56 us | 705.19 us | 336.56 us | 1.86 ms | 1.84 ms | 219.14 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*