# Cardano Plutus VM Benchmark Results

**Date:** 2026-11-22

**Corpus:** Mainnet validators (`mainnet_recent`): every script of 40 of 522 transactions (102 of 1360 programs), selected with seed 1. The per-script tables list every program measured.

## Environment
```
date: 2026-11-22T21:13:17+00:00
kernel: 6.8.0-147-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
corpus: mainnet_recent (102 of 1360 programs from 40 of 522 transactions, sample 40, seed 1; list in corpus.txt)
```

## VM Versions

| VM | Source revision | Toolchain |
|---|---|---|
| plutus-core CEK (Haskell / GHC) | master@ef2eb74 ([ef2eb74](https://github.com/IntersectMBO/plutus/commit/ef2eb74d836259d11b7f4cc4261851e707cfedb3)) | GHC 9.6.4 |
| Scalus UPLC→JVM JIT (Scala / JVM) | master@a3e3487 ([a3e3487](https://github.com/scalus3/scalus/commit/a3e348790452d614cf242f980380fc1246fc01f8)) | JDK 21 / Scala 3 |
| Scalus CEK (Scala / JVM) | master@a3e3487 ([a3e3487](https://github.com/scalus3/scalus/commit/a3e348790452d614cf242f980380fc1246fc01f8)) | JDK 21 / Scala 3 |
| Julc CEK (Java / GraalVM) | v0.1.0-pre22 ([b782bf4](https://github.com/bloxbean/julc/commit/b782bf4c1858a779c4d2e60ae5273c8c888edfc9)) | GraalVM 25.0.2-graal |
| llvm-uplc post-JIT execution (C++ / LLVM) | master@6bcef67 ([6bcef67](https://github.com/SeungheonOh/llvm-uplc/commit/6bcef67ce1995d232327f13d9080fe2f0261a55c)) | LLVM 22.1.0 |
| Amaru UPLC CEK (Rust) | [0.6.0](https://crates.io/crates/amaru-uplc/0.6.0) | rustc nightly-2026-09-04 |
| Aiken UPLC CEK (Rust) | main@b298f3f ([b298f3f](https://github.com/aiken-lang/aiken/commit/b298f3fe77a8f4704c79167294ab289f29c191fc)) | rustc 1.97 |
| Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | [3.1.0](https://www.npmjs.com/package/@harmoniclabs/plutus-machine/v/3.1.0) | Bun 1.3.14 |
| Plutuz CEK (Zig) | main@33b812d ([33b812d](https://github.com/utxo-company/plutuz/commit/33b812dbcf88f6851286e54cb93a4a443353f94c)) | Zig 0.15.2 |
| Chrysalis CEK (C# / .NET) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Chrysalis CEK (C# / .NET AOT) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Plutigo CEK (Go) | main@af1f997 ([af1f997](https://github.com/blinklabs-io/plutigo/commit/af1f9974d47624ad04241dda957670ad7421a6c1)) | Go 1.27.3 |
| blaze-plutus CEK (TypeScript / Bun JSC) | main@9936de1 ([9936de1](https://github.com/butaneprotocol/blaze-cardano/commit/9936de18a1c2a6999ae8a341703b1b0e32c5865d)) | Bun 1.3.14 |
| blaze-plutus CEK (TypeScript / Node V8) | main@9936de1 ([9936de1](https://github.com/butaneprotocol/blaze-cardano/commit/9936de18a1c2a6999ae8a341703b1b0e32c5865d)) | Node.js 22 |
| opshin CEK (Python / CPython) | 1.3.3 ([eda2fba](https://github.com/OpShin/uplc/commit/eda2fbaa89c1a2db4ec6c6c1fa5eea2a8b2671d4)) | Python 3.14 |

*Measurement caveats: llvm-uplc and Scalus JIT report execution after JIT compilation; llvm-uplc's per-script compilation time is retained only in the raw JSON. Scalus JIT, Scalus CEK, Julc and Chrysalis use three measurement samples, and their raw framework output should be consulted for uncertainty.*

## Full tier: decode and evaluate

Each iteration decodes the whole .flat file, including its Data arguments, and evaluates it.

### Per transaction (geometric mean of 40 transaction totals)

*Each VM's time for a transaction is the sum of its times for every script the transaction runs. A VM that fails any script fails the transaction, which is assigned the slowest competitor's total.*

| VM | Language | Geo Mean | vs Fastest | Failed transactions |
|---|---|---|---|---|
| **Plutigo CEK (Go)** | Go | 325.62 us | 1.00x | 0 |
| **Amaru UPLC CEK (Rust)** | Rust | 340.57 us | 1.05x | 0 |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 417.39 us | 1.28x | 0 |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 524.13 us | 1.61x | 0 |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 544.57 us | 1.67x | 0 |
| **Plutuz CEK (Zig)** | Zig | 846.87 us | 2.60x | 0 |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 1.18 ms | 3.63x | 0 |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.75 ms | 5.38x | 0 |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.80 ms | 5.53x | 0 |
| **Aiken UPLC CEK (Rust)** | Rust | 3.87 ms | 11.89x | 0 |
| **Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 9.14 ms | 28.07x | 0 |
| **opshin CEK (Python / CPython)** | Python / CPython | 25.59 ms | 78.59x | 24 |

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Plutigo CEK (Go)** | Go | 128.61 us | 1.00x |
| **Amaru UPLC CEK (Rust)** | Rust | 138.20 us | 1.07x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 170.28 us | 1.32x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 202.78 us | 1.58x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 210.29 us | 1.64x |
| **Plutuz CEK (Zig)** | Zig | 286.34 us | 2.23x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 505.90 us | 3.93x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 614.39 us | 4.78x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 664.92 us | 5.17x |
| **Aiken UPLC CEK (Rust)** | Rust | 1.88 ms | 14.58x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 3.71 ms | 28.83x |
| **opshin CEK (Python / CPython)** | Python / CPython | 29.82 ms | 231.87x |

#### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| Plutigo CEK (Go) | 102 | 0 | 0 | 102 |
| Amaru UPLC CEK (Rust) | 102 | 0 | 0 | 102 |
| Scalus CEK (Scala / JVM) | 102 | 0 | 0 | 102 |
| Chrysalis CEK (C# / .NET) | 102 | 0 | 0 | 102 |
| Chrysalis CEK (C# / .NET AOT) | 102 | 0 | 0 | 102 |
| Plutuz CEK (Zig) | 102 | 0 | 0 | 102 |
| plutus-core CEK (Haskell / GHC) | 102 | 0 | 0 | 102 |
| blaze-plutus CEK (TypeScript / Node V8) | 102 | 0 | 0 | 102 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 102 | 0 | 0 | 102 |
| Aiken UPLC CEK (Rust) | 102 | 0 | 0 | 102 |
| Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | 102 | 0 | 0 | 102 |
| opshin CEK (Python / CPython) | 78 | 24 | 0 | 102 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus CEK (Scala / JVM) | Amaru UPLC CEK (Rust) | Aiken UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 04cb6786e24f2690d94e908b31b02213b0befe91ac58923ac57951726df25cc9-spend-1 | 33.84 us | 13.41 us | 11.22 us | 194.01 us | 320.14 us | 27.77 us | 15.28 us | 15.14 us | **10.31 us** | 40.60 us | 39.40 us | 3.41 ms |
| 0fc112573cf010b19921588bbc2b86a62e66b980e891ef482fd3e310c6d4ace8-spend-0 | 33.88 us | 13.57 us | 11.21 us | 193.08 us | 324.85 us | 27.75 us | 15.31 us | 15.38 us | **10.30 us** | 40.30 us | 37.00 us | 3.42 ms |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-0 | 2.02 ms | 699.60 us | 590.82 us | 5.47 ms | 13.21 ms | 1.97 ms | 923.19 us | 1.01 ms | **528.32 us** | 3.16 ms | 3.55 ms | FAIL |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-2 | 96.56 us | 36.96 us | 32.26 us | 541.09 us | 1.14 ms | 37.74 us | 41.71 us | 41.92 us | **29.23 us** | 127.70 us | 105.20 us | 9.57 ms |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-3 | 96.49 us | 37.88 us | 31.82 us | 548.09 us | 1.29 ms | 38.10 us | 41.58 us | 42.02 us | **29.33 us** | 126.00 us | 106.10 us | 9.69 ms |
| 206ac25b32f1ff0becac4a4ca788f833910b0fc2ad0ed3507577f89ed40a1f3d-spend-0 | 1.49 ms | 722.41 us | **567.46 us** | 4.14 ms | 14.25 ms | 1.87 ms | 971.02 us | 1.04 ms | 627.00 us | 3.51 ms | 3.73 ms | FAIL |
| 206ac25b32f1ff0becac4a4ca788f833910b0fc2ad0ed3507577f89ed40a1f3d-spend-1 | 185.62 us | 59.46 us | 52.63 us | 939.66 us | 1.52 ms | 107.73 us | 63.22 us | 65.60 us | **46.37 us** | 207.30 us | 172.70 us | 18.54 ms |
| 316b997bb14d86e3fa1af6dc4898b307f4ff182c1d511462cd3f455362836e47-spend-0 | 906.11 us | 268.00 us | 213.09 us | 3.24 ms | 3.91 ms | 398.43 us | 332.82 us | 345.82 us | **189.48 us** | 902.60 us | 756.30 us | 92.16 ms |
| 316b997bb14d86e3fa1af6dc4898b307f4ff182c1d511462cd3f455362836e47-withdraw-0 | 1.38 ms | 765.21 us | **510.40 us** | 3.66 ms | 9.95 ms | 837.83 us | 849.50 us | 841.29 us | 589.62 us | 3.90 ms | 3.33 ms | 179.56 ms |
| 3598b54af22fda534e594138b0703ff7971c24c75a63190ec303a3ce497ab244-spend-0 | 33.89 us | 13.45 us | 11.37 us | 193.54 us | 401.32 us | 32.63 us | 15.65 us | 15.86 us | **10.33 us** | 47.00 us | 39.90 us | 3.43 ms |
| 37a68e7227267dc3ee41b94949c45a84a5c2a8d01cb1dc646333618af9eaee63-spend-0 | 89.93 us | 34.04 us | 29.15 us | 492.25 us | 979.74 us | 39.64 us | 39.51 us | 38.50 us | **26.22 us** | 123.60 us | 111.60 us | 9.53 ms |
| 37a68e7227267dc3ee41b94949c45a84a5c2a8d01cb1dc646333618af9eaee63-spend-1 | 1.83 ms | 599.42 us | 483.56 us | 5.20 ms | 10.47 ms | 1.71 ms | 762.57 us | 827.38 us | **440.74 us** | 2.70 ms | 2.77 ms | FAIL |
| 3cff44e46e2d4712017a72cd2fe5272270af0f55745fec48b74442fd017df379-spend-0 | 597.95 us | 261.33 us | **200.68 us** | 2.07 ms | 7.11 ms | 626.27 us | 322.44 us | 338.24 us | 208.17 us | 1.17 ms | 1.20 ms | 98.27 ms |
| 3e3b0282bf031ff6fc34d7706ecba6c2dfb7676cf53d7d54f5fb9c1c5991753c-spend-1 | 1.83 ms | 590.91 us | 478.50 us | 5.35 ms | 10.23 ms | 1.71 ms | 760.68 us | 827.35 us | **439.20 us** | 2.37 ms | 2.73 ms | FAIL |
| 3e3b0282bf031ff6fc34d7706ecba6c2dfb7676cf53d7d54f5fb9c1c5991753c-spend-2 | 90.03 us | 33.80 us | 29.69 us | 487.82 us | 996.39 us | 36.16 us | 39.67 us | 39.45 us | **27.01 us** | 121.10 us | 113.10 us | 9.51 ms |
| 43dfbfbefaa184ed1010ecd05c2f5b96dd29bc062d08bc97f26187a1bd30738f-spend-0 | 89.60 us | 24.20 us | 24.64 us | 372.75 us | 600.85 us | 35.06 us | 33.46 us | 32.72 us | **21.98 us** | 105.00 us | 90.60 us | 9.56 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-0 | 1.53 ms | 614.62 us | 501.82 us | 4.28 ms | 18.39 ms | 1.01 ms | 869.80 us | 900.38 us | **495.95 us** | 3.49 ms | 2.89 ms | 243.29 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-1 | 2.29 ms | 626.31 us | 549.31 us | 5.38 ms | 17.38 ms | 1.12 ms | 926.80 us | 954.84 us | **485.81 us** | 3.43 ms | 2.75 ms | 259.75 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-3 | 645.55 us | 312.40 us | 256.15 us | 2.11 ms | 10.29 ms | 559.78 us | 421.83 us | 424.62 us | **247.18 us** | 1.69 ms | 1.49 ms | 113.18 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-0 | 481.95 us | 153.76 us | 113.35 us | 2.11 ms | 2.98 ms | 209.18 us | 159.39 us | 164.46 us | **100.21 us** | 491.90 us | 444.80 us | 51.34 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-1 | 478.81 us | 158.11 us | 116.70 us | 2.07 ms | 2.97 ms | 209.16 us | 156.78 us | 164.13 us | **100.30 us** | 508.50 us | 444.90 us | 51.18 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-2 | 479.79 us | 155.57 us | 112.21 us | 2.07 ms | 2.94 ms | 208.90 us | 155.66 us | 164.09 us | **100.11 us** | 492.50 us | 445.40 us | 51.22 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-4 | 330.73 us | 97.74 us | 80.82 us | 1.57 ms | 2.18 ms | 145.08 us | 108.85 us | 107.38 us | **73.92 us** | 335.90 us | 288.30 us | 34.93 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-withdraw-0 | 3.26 ms | 1.26 ms | **1.12 ms** | 7.38 ms | 36.40 ms | 4.02 ms | 1.91 ms | 2.00 ms | 1.14 ms | 7.27 ms | 7.66 ms | FAIL |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-spend-0 | 2.56 ms | 745.59 us | 587.19 us | 6.18 ms | 14.20 ms | 1.31 ms | 854.22 us | 886.80 us | **536.57 us** | 3.06 ms | 2.94 ms | FAIL |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-spend-1 | 275.62 us | 77.46 us | 66.11 us | 1.28 ms | 1.41 ms | 108.96 us | 87.23 us | 90.60 us | **57.51 us** | 254.80 us | 236.40 us | 28.95 ms |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-withdraw-0 | 89.08 us | 38.70 us | 29.67 us | 467.84 us | 1.43 ms | 35.54 us | 40.18 us | 40.35 us | **29.07 us** | 130.00 us | 122.50 us | 9.69 ms |
| 56c90a79fb6c5d5fcdfa7306c93f458ce90b97a8d4109b271a0c2d21e987b345-spend-1 | 404.38 us | 165.72 us | **140.96 us** | 1.46 ms | 6.46 ms | 327.18 us | 219.56 us | 228.84 us | 145.50 us | 845.30 us | 832.50 us | 65.17 ms |
| 56c90a79fb6c5d5fcdfa7306c93f458ce90b97a8d4109b271a0c2d21e987b345-spend-3 | 225.85 us | 78.96 us | 74.32 us | 942.98 us | 2.82 ms | 134.47 us | 113.89 us | 111.03 us | **71.87 us** | 404.00 us | 388.80 us | 32.22 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-spend-0 | 298.91 us | 81.34 us | 70.27 us | 1.38 ms | 1.61 ms | 135.47 us | 91.78 us | 95.79 us | **62.97 us** | 272.30 us | 240.40 us | 30.94 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-spend-2 | 446.62 us | 139.06 us | 103.91 us | 1.92 ms | 2.31 ms | 200.89 us | 142.46 us | 152.10 us | **90.57 us** | 453.30 us | 405.00 us | 49.08 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-withdraw-0 | 2.67 ms | 788.69 us | 642.66 us | 6.36 ms | 16.68 ms | 1.94 ms | 1.01 ms | 1.07 ms | **623.10 us** | 3.40 ms | 3.77 ms | FAIL |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-spend-0 | 448.26 us | 140.01 us | 104.07 us | 1.91 ms | 2.34 ms | 201.93 us | 144.80 us | 151.57 us | **90.81 us** | 440.70 us | 409.60 us | 48.89 ms |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-spend-1 | 301.12 us | 82.65 us | 70.82 us | 1.39 ms | 1.64 ms | 136.62 us | 93.78 us | 93.41 us | **63.21 us** | 272.00 us | 250.70 us | 31.17 ms |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-withdraw-0 | 2.69 ms | 801.57 us | 650.12 us | 6.33 ms | 18.15 ms | 1.99 ms | 1.01 ms | 1.09 ms | **633.06 us** | 3.36 ms | 3.67 ms | FAIL |
| 5e1d902963b3cef77bd9bff968f8f93229853319bc7e606302094a80ac4e8bbc-spend-1 | 33.74 us | 13.66 us | 11.44 us | 193.65 us | 373.82 us | 30.03 us | 15.21 us | 15.36 us | **10.26 us** | 45.10 us | 40.20 us | 3.42 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-0 | 476.69 us | 154.79 us | 112.92 us | 2.08 ms | 3.10 ms | 209.85 us | 158.60 us | 166.64 us | **100.80 us** | 491.30 us | 445.40 us | 51.49 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-2 | 334.19 us | 98.53 us | 81.41 us | 1.58 ms | 2.24 ms | 146.84 us | 112.06 us | 107.77 us | **74.26 us** | 335.10 us | 290.80 us | 33.69 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-3 | 480.22 us | 157.94 us | 113.56 us | 2.08 ms | 3.03 ms | 209.63 us | 157.31 us | 164.31 us | **103.60 us** | 498.60 us | 446.70 us | 51.45 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-4 | 479.00 us | 157.98 us | 113.46 us | 2.07 ms | 3.03 ms | 209.70 us | 157.69 us | 164.60 us | **101.00 us** | 485.80 us | 446.10 us | 51.41 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-withdraw-0 | 3.40 ms | 1.27 ms | **1.09 ms** | 7.41 ms | 35.83 ms | 3.95 ms | 1.85 ms | 1.97 ms | 1.12 ms | 6.61 ms | 7.28 ms | FAIL |
| 81af9388c7fb7f1a557c802069ab2f8cae1b441dc46e3755d98e10c825a672f4-spend-0 | 930.23 us | 243.67 us | 198.48 us | 2.94 ms | 2.98 ms | 387.69 us | 310.59 us | 316.56 us | **173.09 us** | 796.50 us | 699.30 us | 88.41 ms |
| 81af9388c7fb7f1a557c802069ab2f8cae1b441dc46e3755d98e10c825a672f4-withdraw-0 | 1.33 ms | 749.65 us | **508.20 us** | 3.46 ms | 8.28 ms | 822.25 us | 806.71 us | 848.82 us | 561.41 us | 3.87 ms | 3.23 ms | 177.49 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-1 | 450.99 us | 137.15 us | 103.59 us | 1.89 ms | 2.32 ms | 200.73 us | 142.12 us | 151.61 us | **90.75 us** | 457.90 us | 404.20 us | 48.89 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-2 | 301.15 us | 81.04 us | 70.16 us | 1.38 ms | 1.60 ms | 135.70 us | 92.20 us | 96.59 us | **62.74 us** | 282.90 us | 239.60 us | 31.07 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-withdraw-0 | 2.66 ms | 790.01 us | 638.50 us | 6.33 ms | 17.30 ms | 1.90 ms | 1.02 ms | 1.06 ms | **622.73 us** | 3.40 ms | 3.72 ms | FAIL |
| 8864ea90e54f74150e7f58d4680e9b9a0959ace4d7048a942cd7a2adfb0a3e3d-spend-0 | 104.95 us | 34.30 us | 31.22 us | 464.59 us | 1.03 ms | 60.74 us | 43.52 us | 44.11 us | **29.85 us** | 147.20 us | 125.40 us | 11.44 ms |
| 8864ea90e54f74150e7f58d4680e9b9a0959ace4d7048a942cd7a2adfb0a3e3d-withdraw-0 | 415.55 us | 176.36 us | **142.94 us** | 1.40 ms | 4.42 ms | 356.21 us | 254.91 us | 237.56 us | 144.06 us | 951.30 us | 857.00 us | 64.76 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-spend-0 | 302.21 us | 80.94 us | 70.76 us | 1.39 ms | 1.59 ms | 136.53 us | 95.12 us | 98.96 us | **64.09 us** | 297.70 us | 258.50 us | 31.07 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-spend-1 | 448.65 us | 136.84 us | 103.39 us | 1.89 ms | 2.33 ms | 201.42 us | 142.33 us | 149.55 us | **90.67 us** | 435.50 us | 403.80 us | 48.67 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-withdraw-0 | 2.69 ms | 794.43 us | 637.01 us | 6.26 ms | 16.46 ms | 1.89 ms | 1.03 ms | 1.06 ms | **621.60 us** | 3.59 ms | 3.76 ms | FAIL |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-spend-1 | 2.55 ms | 751.73 us | 592.39 us | 6.28 ms | 14.89 ms | 1.39 ms | 854.90 us | 881.54 us | **552.49 us** | 3.06 ms | 3.19 ms | FAIL |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-spend-2 | 278.74 us | 79.54 us | 66.27 us | 1.32 ms | 1.44 ms | 117.60 us | 88.17 us | 96.02 us | **57.92 us** | 263.00 us | 236.20 us | 29.08 ms |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-withdraw-0 | 92.89 us | 39.08 us | 30.93 us | 472.73 us | 1.46 ms | 40.94 us | 42.64 us | 43.56 us | **30.39 us** | 143.70 us | 131.30 us | 10.37 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-0 | 480.00 us | 157.84 us | 115.56 us | 2.08 ms | 3.10 ms | 210.76 us | 158.60 us | 168.84 us | **100.51 us** | 496.80 us | 446.60 us | 50.75 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-1 | 480.26 us | 154.54 us | 114.56 us | 2.08 ms | 2.96 ms | 209.83 us | 160.48 us | 166.38 us | **100.75 us** | 504.60 us | 445.00 us | 51.60 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-2 | 331.39 us | 97.64 us | 81.46 us | 1.59 ms | 2.21 ms | 145.21 us | 109.84 us | 114.26 us | **74.13 us** | 332.20 us | 288.50 us | 34.28 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-3 | 479.70 us | 157.26 us | 114.08 us | 2.08 ms | 3.02 ms | 209.74 us | 158.12 us | 165.66 us | **100.73 us** | 501.10 us | 445.10 us | 53.57 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-withdraw-0 | 3.31 ms | 1.25 ms | **1.10 ms** | 7.52 ms | 35.47 ms | 3.92 ms | 1.85 ms | 1.95 ms | 1.13 ms | 7.12 ms | 7.30 ms | FAIL |
| 9821e1defa09d0e9407e4ce6622ead240125df3df75fba63539c55afd841d6f8-spend-1 | 33.87 us | 13.43 us | 11.24 us | 193.85 us | 405.84 us | 30.11 us | 15.28 us | 15.27 us | **10.24 us** | 50.20 us | 40.40 us | 3.41 ms |
| 9b456b77cfc279bd3d80822b553952720e452fddc05c47cac387f1d4f6da6700-spend-1 | 33.93 us | 13.80 us | 11.24 us | 194.42 us | 348.50 us | 30.20 us | 15.28 us | 15.31 us | **10.26 us** | 49.50 us | 40.50 us | 3.41 ms |
| 9d61863e3a770cc83ec05bccd87b25c28eba22f423a0a63acbeea17fa23e5499-spend-0 | 929.55 us | 244.72 us | 203.05 us | 2.97 ms | 3.05 ms | 388.40 us | 310.28 us | 328.37 us | **173.55 us** | 794.80 us | 695.10 us | 89.38 ms |
| 9d61863e3a770cc83ec05bccd87b25c28eba22f423a0a63acbeea17fa23e5499-withdraw-0 | 1.33 ms | 661.49 us | **449.37 us** | 3.48 ms | 8.06 ms | 738.35 us | 730.85 us | 769.24 us | 506.82 us | 3.22 ms | 2.79 ms | 165.62 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-spend-0 | 451.20 us | 136.52 us | 104.22 us | 1.90 ms | 2.36 ms | 200.34 us | 142.09 us | 150.50 us | **90.76 us** | 476.20 us | 404.60 us | 48.52 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-spend-2 | 299.27 us | 81.55 us | 69.62 us | 1.40 ms | 1.60 ms | 135.44 us | 95.67 us | 98.77 us | **62.76 us** | 278.20 us | 237.30 us | 31.01 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-withdraw-0 | 2.79 ms | 792.51 us | 640.24 us | 6.26 ms | 16.60 ms | 1.90 ms | 1.02 ms | 1.06 ms | **623.89 us** | 3.60 ms | 3.72 ms | FAIL |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-0 | 316.00 us | 87.96 us | 74.06 us | 1.45 ms | 1.79 ms | 139.47 us | 98.31 us | 103.63 us | **67.25 us** | 302.50 us | 260.20 us | 31.36 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-1 | 459.28 us | 146.57 us | 108.76 us | 1.96 ms | 2.54 ms | 203.47 us | 146.90 us | 158.51 us | **94.71 us** | 464.40 us | 410.60 us | 49.79 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-3 | 313.25 us | 89.86 us | 74.35 us | 1.46 ms | 1.79 ms | 138.91 us | 99.55 us | 102.32 us | **67.73 us** | 303.60 us | 260.10 us | 31.81 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-withdraw-0 | 2.88 ms | 889.66 us | 748.04 us | 6.71 ms | 21.50 ms | 2.21 ms | 1.16 ms | 1.23 ms | **720.90 us** | 4.35 ms | 4.52 ms | FAIL |
| b045c8789a4d7d250c7971e12d4bd0a7e423015e18489e91b1d42967c0c1aea6-spend-0 | 637.15 us | 234.85 us | **184.94 us** | 1.85 ms | 4.60 ms | 346.76 us | 347.47 us | 372.01 us | 187.88 us | 1.32 ms | 1.20 ms | FAIL |
| beaa9d1683d7bdde24a920f2561b0b9dbe90b652c18b3e59154cfd222c5f696f-spend-1 | 237.33 us | 89.82 us | 83.52 us | 966.68 us | 3.26 ms | 152.35 us | 127.80 us | 133.41 us | **82.37 us** | 503.10 us | 477.70 us | 37.44 ms |
| beaa9d1683d7bdde24a920f2561b0b9dbe90b652c18b3e59154cfd222c5f696f-spend-3 | 408.35 us | 167.02 us | **146.63 us** | 1.47 ms | 6.73 ms | 365.08 us | 222.17 us | 238.41 us | 148.33 us | 864.10 us | 848.90 us | 66.28 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-mint-0 | 724.85 us | 193.68 us | 165.45 us | 2.48 ms | 3.26 ms | 271.73 us | 258.50 us | 274.00 us | **152.33 us** | 704.60 us | 629.50 us | 77.44 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-mint-1 | 546.66 us | 222.36 us | 186.39 us | 1.92 ms | 7.10 ms | 332.17 us | 304.66 us | 316.34 us | **169.96 us** | 1.12 ms | 976.90 us | 84.93 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-0 | 2.86 ms | 1.06 ms | 874.00 us | 6.17 ms | 31.47 ms | 1.75 ms | 1.52 ms | 1.55 ms | **816.97 us** | 6.36 ms | 4.64 ms | FAIL |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-2 | 2.51 ms | 947.15 us | 756.22 us | 5.65 ms | 27.42 ms | 1.55 ms | 1.32 ms | 1.34 ms | **699.40 us** | 5.12 ms | 4.63 ms | 334.30 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-3 | 583.30 us | 260.27 us | 208.50 us | 1.95 ms | 9.65 ms | 458.58 us | 344.49 us | 352.69 us | **200.25 us** | 1.25 ms | 1.16 ms | 96.39 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-0 | 322.99 us | 94.28 us | 77.66 us | 1.50 ms | 2.00 ms | 142.57 us | 103.86 us | 105.82 us | **72.08 us** | 310.10 us | 267.80 us | 32.14 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-1 | 322.61 us | 92.92 us | 77.58 us | 1.51 ms | 1.99 ms | 142.45 us | 106.46 us | 116.62 us | **71.07 us** | 305.20 us | 267.60 us | 32.06 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-2 | 471.83 us | 149.09 us | 110.03 us | 2.04 ms | 2.70 ms | 208.23 us | 159.16 us | 163.78 us | **98.91 us** | 479.20 us | 430.10 us | 50.33 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-4 | 321.57 us | 92.95 us | 77.53 us | 1.50 ms | 1.97 ms | 142.61 us | 107.28 us | 112.54 us | **70.77 us** | 300.50 us | 266.50 us | 32.55 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-withdraw-0 | 2.99 ms | 978.65 us | 839.90 us | 6.74 ms | 25.92 ms | 2.50 ms | 1.37 ms | 1.39 ms | **794.96 us** | 4.57 ms | 5.20 ms | FAIL |
| c6aa9ec93c2e4fe6396240b1fae8ed4a1e5960403af40ae1d52d0753beced05c-spend-2 | 330.25 us | 139.33 us | 107.99 us | 1.27 ms | 3.44 ms | 187.57 us | 180.49 us | 200.25 us | **100.07 us** | 623.70 us | 604.80 us | 62.13 ms |
| c6aa9ec93c2e4fe6396240b1fae8ed4a1e5960403af40ae1d52d0753beced05c-spend-3 | 2.35 ms | 1.07 ms | 1.02 ms | 5.76 ms | 17.67 ms | 1.78 ms | 1.91 ms | 2.04 ms | **850.04 us** | 6.03 ms | 6.37 ms | FAIL |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-spend-2 | 931.39 us | 252.15 us | 201.08 us | 3.03 ms | 3.05 ms | 410.43 us | 306.16 us | 315.54 us | **176.45 us** | 811.70 us | 734.30 us | 89.40 ms |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-withdraw-0 | 233.40 us | 71.68 us | **64.82 us** | 932.05 us | 1.71 ms | 185.74 us | 98.10 us | 95.17 us | 65.25 us | 321.90 us | 283.20 us | 26.97 ms |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-withdraw-1 | 1.30 ms | 702.94 us | **479.09 us** | 3.43 ms | 8.24 ms | 793.17 us | 748.48 us | 818.08 us | 539.41 us | 3.09 ms | 3.04 ms | 174.50 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-spend-0 | 445.92 us | 141.56 us | 103.50 us | 1.89 ms | 2.35 ms | 202.16 us | 145.46 us | 150.10 us | **90.70 us** | 450.70 us | 405.30 us | 48.98 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-spend-1 | 301.92 us | 81.62 us | 70.78 us | 1.38 ms | 1.63 ms | 136.55 us | 92.49 us | 97.54 us | **64.76 us** | 269.40 us | 246.60 us | 31.20 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-withdraw-0 | 2.68 ms | 791.03 us | 644.78 us | 6.31 ms | 17.13 ms | 1.91 ms | 1.01 ms | 1.07 ms | **624.99 us** | 3.47 ms | 3.71 ms | FAIL |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-0 | 299.02 us | 81.75 us | 70.82 us | 1.39 ms | 1.59 ms | 135.93 us | 96.18 us | 99.43 us | **63.36 us** | 280.90 us | 237.70 us | 31.11 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-2 | 445.71 us | 136.79 us | 105.87 us | 1.89 ms | 2.32 ms | 200.69 us | 142.41 us | 161.06 us | **90.84 us** | 452.00 us | 405.50 us | 48.94 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-withdraw-0 | 2.68 ms | 786.91 us | 642.89 us | 6.32 ms | 16.73 ms | 1.91 ms | 999.56 us | 1.07 ms | **622.21 us** | 3.41 ms | 3.75 ms | FAIL |
| e2fbfa2be7dc3f978d4131f60a99085b888b8b7a2123d41400dc4697d6a84df7-spend-0 | 90.27 us | 33.36 us | 29.20 us | 492.15 us | 1.01 ms | 36.09 us | 39.44 us | 38.87 us | **26.18 us** | 131.40 us | 111.80 us | 9.46 ms |
| e2fbfa2be7dc3f978d4131f60a99085b888b8b7a2123d41400dc4697d6a84df7-spend-1 | 1.82 ms | 592.74 us | 481.23 us | 5.18 ms | 10.41 ms | 1.76 ms | 767.28 us | 828.90 us | **440.35 us** | 2.52 ms | 2.69 ms | FAIL |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-0 | 277.19 us | 80.07 us | 67.42 us | 1.30 ms | 1.42 ms | 109.75 us | 87.80 us | 91.78 us | **58.09 us** | 272.40 us | 236.80 us | 29.67 ms |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-2 | 2.58 ms | 755.27 us | 604.99 us | 6.22 ms | 15.17 ms | 1.40 ms | 860.58 us | 893.20 us | **552.59 us** | 2.95 ms | 3.20 ms | FAIL |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-withdraw-0 | 91.38 us | 39.94 us | 30.88 us | 472.28 us | 1.45 ms | 37.47 us | 43.48 us | 42.87 us | **30.66 us** | 144.30 us | 131.20 us | 10.39 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-spend-1 | 447.44 us | 137.05 us | 102.87 us | 1.88 ms | 2.47 ms | 199.19 us | 143.01 us | 151.31 us | **91.92 us** | 442.20 us | 404.50 us | 48.81 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-spend-2 | 298.48 us | 82.02 us | 70.06 us | 1.37 ms | 1.60 ms | 134.94 us | 92.88 us | 96.25 us | **62.99 us** | 271.80 us | 240.20 us | 31.34 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-withdraw-0 | 2.68 ms | 792.51 us | 637.85 us | 6.34 ms | 16.56 ms | 1.91 ms | 1.02 ms | 1.05 ms | **626.49 us** | 3.38 ms | 3.76 ms | FAIL |

## Eval tier: evaluate a decoded program

The program is decoded before timing; each iteration evaluates it. JIT VMs compile before timing too.

### Per transaction (geometric mean of 40 transaction totals)

*Each VM's time for a transaction is the sum of its times for every script the transaction runs. A VM that fails any script fails the transaction, which is assigned the slowest competitor's total.*

| VM | Language | Geo Mean | vs Fastest | Failed transactions |
|---|---|---|---|---|
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 88.31 us | 1.00x | 0 |
| **Plutigo CEK (Go)** | Go | 146.68 us | 1.66x | 0 |
| **Amaru UPLC CEK (Rust)** | Rust | 150.54 us | 1.70x | 0 |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 153.64 us | 1.74x | 0 |
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 161.10 us | 1.82x | 0 |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 164.06 us | 1.86x | 0 |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 250.23 us | 2.83x | 0 |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 261.21 us | 2.96x | 0 |
| **Aiken UPLC CEK (Rust)** | Rust | 357.08 us | 4.04x | 0 |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 373.70 us | 4.23x | 0 |
| **Plutuz CEK (Zig)** | Zig | 521.93 us | 5.91x | 0 |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 993.59 us | 11.25x | 0 |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.01 ms | 11.48x | 0 |
| **Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 6.54 ms | 74.04x | 0 |
| **opshin CEK (Python / CPython)** | Python / CPython | 17.82 ms | 201.83x | 24 |

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 12.25 us | 1.00x |
| **Plutigo CEK (Go)** | Go | 29.62 us | 2.42x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 30.86 us | 2.52x |
| **Amaru UPLC CEK (Rust)** | Rust | 30.90 us | 2.52x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 33.47 us | 2.73x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 54.84 us | 4.48x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 57.32 us | 4.68x |
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 63.05 us | 5.14x |
| **Aiken UPLC CEK (Rust)** | Rust | 89.18 us | 7.28x |
| **Plutuz CEK (Zig)** | Zig | 102.38 us | 8.35x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 108.40 us | 8.85x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 211.98 us | 17.30x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 212.62 us | 17.35x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 2.22 ms | 181.35x |
| **opshin CEK (Python / CPython)** | Python / CPython | 17.61 ms | 1437.13x |

#### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| Scalus UPLC→JVM JIT (Scala / JVM) | 102 | 0 | 0 | 102 |
| Plutigo CEK (Go) | 102 | 0 | 0 | 102 |
| Scalus CEK (Scala / JVM) | 102 | 0 | 0 | 102 |
| Amaru UPLC CEK (Rust) | 102 | 0 | 0 | 102 |
| plutus-core CEK (Haskell / GHC) | 102 | 0 | 0 | 102 |
| Chrysalis CEK (C# / .NET) | 102 | 0 | 0 | 102 |
| Chrysalis CEK (C# / .NET AOT) | 102 | 0 | 0 | 102 |
| llvm-uplc post-JIT execution (C++ / LLVM) | 102 | 0 | 0 | 102 |
| Aiken UPLC CEK (Rust) | 102 | 0 | 0 | 102 |
| Plutuz CEK (Zig) | 102 | 0 | 0 | 102 |
| Julc CEK (Java / GraalVM) | 102 | 0 | 0 | 102 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 102 | 0 | 0 | 102 |
| blaze-plutus CEK (TypeScript / Node V8) | 102 | 0 | 0 | 102 |
| Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | 102 | 0 | 0 | 102 |
| opshin CEK (Python / CPython) | 78 | 24 | 0 | 102 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc post-JIT execution (C++ / LLVM) | Amaru UPLC CEK (Rust) | Aiken UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 04cb6786e24f2690d94e908b31b02213b0befe91ac58923ac57951726df25cc9-spend-1 | 2.87 us | **404 ns** | 2.43 us | 10.77 us | 6.83 us | 3.27 us | 14.74 us | 218.85 us | 19.04 us | 6.18 us | 5.98 us | 2.40 us | 14.00 us | 16.20 us | 2.06 ms |
| 0fc112573cf010b19921588bbc2b86a62e66b980e891ef482fd3e310c6d4ace8-spend-0 | 2.85 us | **395 ns** | 2.42 us | 10.72 us | 6.61 us | 3.22 us | 14.47 us | 213.97 us | 18.57 us | 6.16 us | 5.91 us | 2.39 us | 12.70 us | 16.00 us | 2.05 ms |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-0 | 372.66 us | 816.85 us | 336.78 us | 713.52 us | **242.15 us** | 344.50 us | 680.09 us | 9.28 ms | 1.62 ms | 553.40 us | 586.03 us | 311.77 us | 1.91 ms | 2.41 ms | FAIL |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-2 | 5.10 us | **1.50 us** | 4.51 us | 17.14 us | 28.38 us | 5.29 us | 21.83 us | 635.73 us | 8.37 us | 10.28 us | 10.71 us | 4.37 us | 27.80 us | 32.60 us | 5.10 ms |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-3 | 5.10 us | **1.46 us** | 4.49 us | 17.16 us | 28.92 us | 5.20 us | 22.11 us | 655.31 us | 8.40 us | 10.28 us | 10.49 us | 4.36 us | 27.40 us | 33.00 us | 5.10 ms |
| 206ac25b32f1ff0becac4a4ca788f833910b0fc2ad0ed3507577f89ed40a1f3d-spend-0 | 491.30 us | **286.39 us** | 453.09 us | 762.75 us | 295.50 us | 380.74 us | 889.29 us | 10.80 ms | 1.51 ms | 672.16 us | 758.83 us | 455.64 us | 2.51 ms | 2.89 ms | FAIL |
| 206ac25b32f1ff0becac4a4ca788f833910b0fc2ad0ed3507577f89ed40a1f3d-spend-1 | 4.10 us | **1.02 us** | 3.66 us | 22.73 us | 35.33 us | 4.80 us | 21.44 us | 690.11 us | 40.24 us | 8.97 us | 9.14 us | 4.00 us | 22.10 us | 25.00 us | 8.62 ms |
| 316b997bb14d86e3fa1af6dc4898b307f4ff182c1d511462cd3f455362836e47-spend-0 | 19.47 us | **9.38 us** | 17.24 us | 123.46 us | 56.47 us | 14.74 us | 44.20 us | 1.39 ms | 75.59 us | 25.54 us | 26.82 us | 15.73 us | 151.70 us | 107.60 us | 40.41 ms |
| 316b997bb14d86e3fa1af6dc4898b307f4ff182c1d511462cd3f455362836e47-withdraw-0 | 348.98 us | 426.50 us | 494.88 us | 688.15 us | **291.39 us** | 299.88 us | 569.03 us | 6.58 ms | 497.73 us | 451.12 us | 482.61 us | 378.19 us | 2.85 ms | 2.39 ms | 129.38 ms |
| 3598b54af22fda534e594138b0703ff7971c24c75a63190ec303a3ce497ab244-spend-0 | 2.87 us | **403 ns** | 2.38 us | 10.99 us | 8.62 us | 3.19 us | 14.80 us | 224.63 us | 21.04 us | 6.11 us | 6.15 us | 2.41 us | 14.90 us | 16.10 us | 2.06 ms |
| 37a68e7227267dc3ee41b94949c45a84a5c2a8d01cb1dc646333618af9eaee63-spend-0 | 6.23 us | **1.80 us** | 5.43 us | 18.38 us | 24.21 us | 6.03 us | 23.56 us | 572.92 us | 9.82 us | 11.74 us | 12.21 us | 5.17 us | 39.20 us | 41.00 us | 5.46 ms |
| 37a68e7227267dc3ee41b94949c45a84a5c2a8d01cb1dc646333618af9eaee63-spend-1 | 268.65 us | 317.96 us | 246.33 us | 534.82 us | **180.08 us** | 240.42 us | 503.40 us | 6.94 ms | 1.22 ms | 396.11 us | 414.46 us | 230.03 us | 1.47 ms | 1.70 ms | FAIL |
| 3cff44e46e2d4712017a72cd2fe5272270af0f55745fec48b74442fd017df379-spend-0 | 139.88 us | **38.13 us** | 120.87 us | 246.22 us | 107.41 us | 113.69 us | 270.13 us | 5.63 ms | 465.37 us | 195.02 us | 199.65 us | 126.92 us | 761.10 us | 833.50 us | 74.01 ms |
| 3e3b0282bf031ff6fc34d7706ecba6c2dfb7676cf53d7d54f5fb9c1c5991753c-spend-1 | 273.49 us | 364.31 us | 243.37 us | 527.50 us | **181.99 us** | 238.19 us | 499.86 us | 7.01 ms | 1.24 ms | 396.16 us | 412.33 us | 227.72 us | 1.42 ms | 1.67 ms | FAIL |
| 3e3b0282bf031ff6fc34d7706ecba6c2dfb7676cf53d7d54f5fb9c1c5991753c-spend-2 | 6.28 us | **1.87 us** | 5.50 us | 17.68 us | 24.63 us | 6.03 us | 23.55 us | 593.19 us | 9.85 us | 11.75 us | 12.17 us | 5.23 us | 34.20 us | 39.90 us | 5.46 ms |
| 43dfbfbefaa184ed1010ecd05c2f5b96dd29bc062d08bc97f26187a1bd30738f-spend-0 | 4.55 us | **1.69 us** | 5.35 us | 21.52 us | 11.89 us | 5.10 us | 19.38 us | 337.31 us | 7.83 us | 9.77 us | 9.53 us | 4.23 us | 37.30 us | 32.10 us | 5.06 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-0 | 328.02 us | **177.06 us** | 375.36 us | 742.56 us | 251.66 us | 286.76 us | 661.67 us | 15.13 ms | 642.07 us | 477.50 us | 483.56 us | 296.52 us | 3.12 ms | 2.14 ms | 181.02 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-1 | 245.07 us | **179.72 us** | 272.36 us | 653.32 us | 223.58 us | 242.62 us | 464.16 us | 13.02 ms | 585.10 us | 368.99 us | 382.25 us | 220.20 us | 1.88 ms | 1.60 ms | 168.52 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-3 | 158.77 us | **73.55 us** | 183.06 us | 378.64 us | 151.44 us | 155.09 us | 300.88 us | 8.36 ms | 395.73 us | 240.72 us | 245.87 us | 143.03 us | 1.32 ms | 1.06 ms | 86.73 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-0 | 15.65 us | **3.38 us** | 13.48 us | 61.53 us | 53.66 us | 13.85 us | 43.03 us | 1.41 ms | 42.97 us | 25.56 us | 27.06 us | 12.96 us | 106.50 us | 104.60 us | 25.11 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-1 | 16.35 us | **3.42 us** | 13.47 us | 61.73 us | 53.90 us | 13.74 us | 43.07 us | 1.41 ms | 43.09 us | 26.15 us | 27.17 us | 12.81 us | 103.70 us | 105.00 us | 25.10 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-2 | 15.60 us | **3.46 us** | 14.52 us | 62.24 us | 53.72 us | 13.73 us | 43.22 us | 1.44 ms | 43.18 us | 25.52 us | 28.54 us | 12.84 us | 105.20 us | 105.00 us | 25.13 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-4 | 5.00 us | **1.10 us** | 4.47 us | 31.76 us | 44.46 us | 5.01 us | 20.61 us | 982.07 us | 25.81 us | 10.01 us | 10.34 us | 4.80 us | 32.10 us | 32.00 us | 14.45 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-withdraw-0 | 903.63 us | **417.85 us** | 793.99 us | 1.61 ms | 557.93 us | 796.27 us | 1.48 ms | 30.54 ms | 3.39 ms | 1.29 ms | 1.37 ms | 854.71 us | 5.62 ms | 5.70 ms | FAIL |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-spend-0 | 291.11 us | 290.66 us | 270.04 us | 650.19 us | **237.14 us** | 296.68 us | 510.47 us | 11.10 ms | 741.38 us | 414.77 us | 434.06 us | 266.37 us | 1.77 ms | 1.81 ms | FAIL |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-spend-1 | 5.79 us | **1.41 us** | 5.35 us | 33.31 us | 23.18 us | 6.21 us | 22.60 us | 645.05 us | 10.33 us | 11.49 us | 11.57 us | 4.92 us | 38.70 us | 39.50 us | 13.39 ms |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-withdraw-0 | 7.93 us | **2.22 us** | 7.29 us | 19.53 us | 22.85 us | 7.48 us | 25.54 us | 1.02 ms | 13.08 us | 14.32 us | 14.97 us | 7.75 us | 53.40 us | 54.10 us | 6.47 ms |
| 56c90a79fb6c5d5fcdfa7306c93f458ce90b97a8d4109b271a0c2d21e987b345-spend-1 | 97.57 us | **33.22 us** | 81.74 us | 172.53 us | 81.54 us | 78.17 us | 184.02 us | 5.41 ms | 219.59 us | 130.70 us | 137.36 us | 85.71 us | 563.80 us | 579.20 us | 50.77 ms |
| 56c90a79fb6c5d5fcdfa7306c93f458ce90b97a8d4109b271a0c2d21e987b345-spend-3 | 38.44 us | **11.18 us** | 30.95 us | 75.10 us | 44.98 us | 30.36 us | 83.87 us | 2.23 ms | 71.55 us | 51.15 us | 56.74 us | 31.47 us | 227.00 us | 234.70 us | 22.72 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-spend-0 | 5.23 us | **1.10 us** | 4.42 us | 32.18 us | 28.91 us | 5.02 us | 20.45 us | 685.19 us | 25.64 us | 9.88 us | 10.43 us | 4.76 us | 28.10 us | 31.90 us | 13.63 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-spend-2 | 15.46 us | **3.45 us** | 13.46 us | 60.95 us | 36.47 us | 13.70 us | 43.52 us | 1.17 ms | 45.34 us | 25.71 us | 27.15 us | 12.89 us | 92.20 us | 104.60 us | 24.34 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-withdraw-0 | 384.83 us | **225.65 us** | 336.96 us | 740.82 us | 258.40 us | 349.14 us | 662.54 us | 13.27 ms | 1.31 ms | 548.65 us | 580.87 us | 354.40 us | 2.00 ms | 2.38 ms | FAIL |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-spend-0 | 15.67 us | **3.47 us** | 13.47 us | 61.66 us | 33.43 us | 13.72 us | 43.14 us | 1.20 ms | 42.86 us | 26.12 us | 27.01 us | 12.97 us | 92.20 us | 104.70 us | 24.34 ms |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-spend-1 | 5.00 us | **1.12 us** | 4.39 us | 32.37 us | 25.52 us | 5.13 us | 20.44 us | 711.52 us | 25.50 us | 9.79 us | 10.39 us | 4.78 us | 28.60 us | 32.10 us | 13.63 ms |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-withdraw-0 | 397.35 us | **243.81 us** | 349.93 us | 759.81 us | 264.32 us | 351.77 us | 678.04 us | 13.80 ms | 1.39 ms | 544.91 us | 618.67 us | 361.84 us | 2.09 ms | 2.43 ms | FAIL |
| 5e1d902963b3cef77bd9bff968f8f93229853319bc7e606302094a80ac4e8bbc-spend-1 | 2.87 us | **398 ns** | 2.32 us | 10.95 us | 6.98 us | 3.22 us | 14.28 us | 255.97 us | 20.98 us | 6.25 us | 5.92 us | 2.38 us | 13.70 us | 16.10 us | 2.05 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-0 | 15.60 us | **3.45 us** | 13.42 us | 62.52 us | 50.42 us | 13.78 us | 43.45 us | 1.55 ms | 42.90 us | 25.98 us | 27.02 us | 12.76 us | 92.20 us | 105.80 us | 25.18 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-2 | 4.98 us | **1.17 us** | 4.42 us | 32.36 us | 39.65 us | 5.05 us | 20.40 us | 1.00 ms | 25.67 us | 9.70 us | 10.35 us | 4.85 us | 28.50 us | 32.10 us | 14.71 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-3 | 15.54 us | **3.47 us** | 13.52 us | 61.36 us | 53.25 us | 13.69 us | 44.28 us | 1.44 ms | 42.71 us | 25.66 us | 27.35 us | 12.87 us | 95.10 us | 105.20 us | 25.57 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-4 | 15.55 us | **3.49 us** | 13.50 us | 61.41 us | 51.80 us | 13.73 us | 44.20 us | 1.44 ms | 42.99 us | 25.36 us | 26.84 us | 13.02 us | 94.60 us | 108.10 us | 25.13 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-withdraw-0 | 889.27 us | **402.65 us** | 786.21 us | 1.58 ms | 560.85 us | 782.04 us | 1.46 ms | 30.25 ms | 3.31 ms | 1.26 ms | 1.37 ms | 832.63 us | 4.84 ms | 6.34 ms | FAIL |
| 81af9388c7fb7f1a557c802069ab2f8cae1b441dc46e3755d98e10c825a672f4-spend-0 | 19.06 us | **9.92 us** | 18.14 us | 122.26 us | 38.49 us | 14.90 us | 44.77 us | 1.02 ms | 75.63 us | 26.44 us | 27.20 us | 15.35 us | 126.60 us | 118.60 us | 39.37 ms |
| 81af9388c7fb7f1a557c802069ab2f8cae1b441dc46e3755d98e10c825a672f4-withdraw-0 | 348.95 us | 420.76 us | 500.93 us | 694.87 us | **281.92 us** | 309.69 us | 546.84 us | 6.31 ms | 503.05 us | 448.01 us | 488.95 us | 377.86 us | 3.26 ms | 2.43 ms | 127.89 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-1 | 15.58 us | **3.44 us** | 13.51 us | 60.71 us | 32.38 us | 13.59 us | 42.96 us | 1.14 ms | 43.05 us | 25.26 us | 27.04 us | 12.85 us | 111.30 us | 104.90 us | 24.86 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-2 | 5.02 us | **1.16 us** | 4.46 us | 32.37 us | 24.78 us | 5.16 us | 20.12 us | 667.18 us | 25.94 us | 9.76 us | 10.36 us | 4.79 us | 29.80 us | 32.00 us | 13.83 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-withdraw-0 | 388.09 us | **247.42 us** | 335.85 us | 744.61 us | 260.88 us | 341.49 us | 660.34 us | 13.19 ms | 1.31 ms | 570.07 us | 584.60 us | 353.18 us | 2.11 ms | 2.37 ms | FAIL |
| 8864ea90e54f74150e7f58d4680e9b9a0959ace4d7048a942cd7a2adfb0a3e3d-spend-0 | 6.80 us | **2.58 us** | 7.90 us | 26.07 us | 18.02 us | 6.89 us | 23.55 us | 664.76 us | 28.39 us | 12.88 us | 13.12 us | 7.13 us | 53.30 us | 46.70 us | 6.43 ms |
| 8864ea90e54f74150e7f58d4680e9b9a0959ace4d7048a942cd7a2adfb0a3e3d-withdraw-0 | 89.67 us | **36.76 us** | 93.94 us | 201.24 us | 71.25 us | 74.07 us | 185.00 us | 3.61 ms | 249.03 us | 118.57 us | 128.51 us | 79.88 us | 721.80 us | 532.70 us | 46.28 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-spend-0 | 4.94 us | **1.15 us** | 4.46 us | 31.98 us | 25.08 us | 5.07 us | 20.67 us | 684.73 us | 25.80 us | 9.82 us | 10.32 us | 4.79 us | 33.50 us | 32.00 us | 13.82 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-spend-1 | 15.65 us | **3.45 us** | 13.64 us | 60.80 us | 32.71 us | 13.62 us | 43.23 us | 1.16 ms | 42.89 us | 26.07 us | 27.41 us | 12.91 us | 107.60 us | 104.60 us | 23.89 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-withdraw-0 | 388.69 us | **260.37 us** | 338.81 us | 741.66 us | 261.21 us | 349.17 us | 655.98 us | 13.54 ms | 1.31 ms | 547.80 us | 578.26 us | 355.27 us | 2.31 ms | 2.36 ms | FAIL |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-spend-1 | 304.08 us | 313.69 us | 286.10 us | 670.31 us | **244.01 us** | 305.31 us | 553.39 us | 11.11 ms | 807.42 us | 446.10 us | 461.10 us | 281.57 us | 1.89 ms | 1.91 ms | FAIL |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-spend-2 | 5.81 us | **1.35 us** | 5.24 us | 34.71 us | 24.30 us | 6.09 us | 22.36 us | 660.74 us | 10.20 us | 11.11 us | 11.53 us | 4.94 us | 43.60 us | 39.40 us | 13.44 ms |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-withdraw-0 | 8.94 us | **2.50 us** | 8.66 us | 20.66 us | 24.55 us | 7.94 us | 27.57 us | 1.05 ms | 14.17 us | 15.95 us | 16.68 us | 8.54 us | 62.20 us | 61.10 us | 7.46 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-0 | 15.71 us | **3.52 us** | 13.52 us | 60.77 us | 50.98 us | 13.85 us | 43.69 us | 1.45 ms | 42.83 us | 26.13 us | 26.99 us | 12.84 us | 106.90 us | 105.30 us | 25.65 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-1 | 15.75 us | **3.45 us** | 14.75 us | 60.88 us | 51.28 us | 13.77 us | 43.37 us | 1.44 ms | 42.97 us | 25.52 us | 26.95 us | 12.84 us | 104.40 us | 104.20 us | 25.33 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-2 | 4.96 us | **1.15 us** | 4.46 us | 31.62 us | 38.32 us | 5.01 us | 20.98 us | 988.60 us | 25.64 us | 9.92 us | 10.51 us | 4.79 us | 31.70 us | 31.90 us | 14.48 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-3 | 15.56 us | **3.42 us** | 13.58 us | 61.37 us | 49.20 us | 13.85 us | 43.24 us | 1.44 ms | 43.08 us | 25.93 us | 26.89 us | 13.12 us | 105.00 us | 104.50 us | 25.69 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-withdraw-0 | 890.82 us | **442.73 us** | 765.44 us | 1.55 ms | 559.65 us | 781.48 us | 1.44 ms | 30.21 ms | 3.30 ms | 1.26 ms | 1.36 ms | 829.20 us | 5.53 ms | 5.55 ms | FAIL |
| 9821e1defa09d0e9407e4ce6622ead240125df3df75fba63539c55afd841d6f8-spend-1 | 2.88 us | **406 ns** | 2.45 us | 10.87 us | 7.02 us | 3.31 us | 14.82 us | 247.00 us | 21.03 us | 6.19 us | 5.94 us | 2.39 us | 15.10 us | 16.10 us | 2.05 ms |
| 9b456b77cfc279bd3d80822b553952720e452fddc05c47cac387f1d4f6da6700-spend-1 | 2.86 us | **406 ns** | 2.44 us | 10.44 us | 7.02 us | 3.25 us | 14.66 us | 248.15 us | 21.07 us | 6.19 us | 5.95 us | 2.40 us | 15.30 us | 17.50 us | 2.05 ms |
| 9d61863e3a770cc83ec05bccd87b25c28eba22f423a0a63acbeea17fa23e5499-spend-0 | 18.95 us | **9.35 us** | 17.18 us | 121.77 us | 39.11 us | 15.00 us | 44.93 us | 1.08 ms | 75.26 us | 26.12 us | 26.15 us | 15.43 us | 130.40 us | 107.10 us | 39.63 ms |
| 9d61863e3a770cc83ec05bccd87b25c28eba22f423a0a63acbeea17fa23e5499-withdraw-0 | 312.32 us | 325.88 us | 407.25 us | 614.44 us | **243.88 us** | 258.85 us | 531.54 us | 6.20 ms | 422.95 us | 393.79 us | 415.22 us | 325.08 us | 2.29 ms | 2.03 ms | 118.00 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-spend-0 | 15.54 us | **3.50 us** | 13.47 us | 61.85 us | 33.27 us | 13.59 us | 42.96 us | 1.17 ms | 42.70 us | 25.48 us | 26.87 us | 12.94 us | 108.90 us | 104.50 us | 24.39 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-spend-2 | 4.98 us | **1.19 us** | 4.38 us | 31.87 us | 25.24 us | 5.03 us | 20.20 us | 717.55 us | 25.44 us | 9.78 us | 10.41 us | 4.77 us | 32.60 us | 31.90 us | 13.63 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-withdraw-0 | 388.42 us | **241.10 us** | 335.98 us | 745.45 us | 262.19 us | 342.97 us | 652.08 us | 13.65 ms | 1.31 ms | 550.40 us | 601.44 us | 354.86 us | 2.39 ms | 2.36 ms | FAIL |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-0 | 4.97 us | **1.14 us** | 4.43 us | 32.63 us | 29.71 us | 5.14 us | 20.25 us | 821.82 us | 25.89 us | 9.67 us | 10.40 us | 4.77 us | 33.10 us | 32.20 us | 13.98 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-1 | 15.58 us | **3.45 us** | 14.43 us | 61.80 us | 37.81 us | 13.58 us | 43.73 us | 1.30 ms | 45.86 us | 25.93 us | 26.89 us | 13.07 us | 108.50 us | 104.70 us | 25.02 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-3 | 4.98 us | **1.19 us** | 4.36 us | 32.32 us | 29.84 us | 5.15 us | 20.14 us | 737.40 us | 25.75 us | 9.77 us | 10.32 us | 4.76 us | 32.50 us | 32.20 us | 13.90 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-withdraw-0 | 491.87 us | **267.48 us** | 432.22 us | 936.68 us | 327.29 us | 456.46 us | 818.31 us | 16.40 ms | 1.61 ms | 705.03 us | 736.65 us | 440.35 us | 3.13 ms | 3.01 ms | FAIL |
| b045c8789a4d7d250c7971e12d4bd0a7e423015e18489e91b1d42967c0c1aea6-spend-0 | 155.23 us | **34.74 us** | 134.43 us | 255.65 us | 80.08 us | 90.79 us | 302.34 us | 3.65 ms | 186.61 us | 192.38 us | 206.62 us | 102.58 us | 904.60 us | 839.40 us | FAIL |
| beaa9d1683d7bdde24a920f2561b0b9dbe90b652c18b3e59154cfd222c5f696f-spend-1 | 50.17 us | **15.07 us** | 41.65 us | 91.15 us | 52.41 us | 39.52 us | 104.50 us | 2.69 ms | 89.19 us | 70.18 us | 75.30 us | 41.85 us | 297.50 us | 315.80 us | 28.45 ms |
| beaa9d1683d7bdde24a920f2561b0b9dbe90b652c18b3e59154cfd222c5f696f-spend-3 | 100.65 us | **33.11 us** | 83.34 us | 176.03 us | 83.50 us | 77.82 us | 184.54 us | 5.58 ms | 256.24 us | 134.99 us | 142.13 us | 86.08 us | 579.50 us | 596.60 us | 51.98 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-mint-0 | 24.48 us | **11.71 us** | 26.01 us | 120.35 us | 48.49 us | 22.12 us | 62.85 us | 1.58 ms | 37.88 us | 36.90 us | 38.40 us | 21.57 us | 190.40 us | 156.30 us | 38.17 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-mint-1 | 86.38 us | **40.86 us** | 101.17 us | 237.84 us | 94.56 us | 84.50 us | 181.73 us | 5.59 ms | 174.19 us | 137.69 us | 140.79 us | 74.60 us | 883.50 us | 601.30 us | 58.87 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-0 | 544.59 us | 1.42 ms | 626.92 us | 1.33 ms | **418.68 us** | 533.82 us | 1.04 ms | 27.31 ms | 1.13 ms | 832.32 us | 847.71 us | 506.62 us | 5.15 ms | 3.51 ms | FAIL |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-2 | 478.07 us | 801.62 us | 539.91 us | 1.12 ms | **365.68 us** | 456.53 us | 846.69 us | 25.71 ms | 1.02 ms | 709.00 us | 711.09 us | 416.65 us | 4.40 ms | 3.05 ms | 247.68 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-3 | 115.44 us | **58.11 us** | 132.30 us | 281.17 us | 115.72 us | 106.99 us | 226.77 us | 8.32 ms | 295.95 us | 170.27 us | 174.47 us | 102.28 us | 879.90 us | 759.10 us | 71.77 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-0 | 5.00 us | **1.09 us** | 4.41 us | 32.00 us | 34.73 us | 4.99 us | 19.82 us | 900.18 us | 26.00 us | 9.95 us | 10.36 us | 4.83 us | 29.30 us | 31.80 us | 14.32 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-1 | 4.97 us | **1.15 us** | 4.41 us | 31.64 us | 34.79 us | 5.21 us | 21.11 us | 898.15 us | 26.09 us | 10.12 us | 10.33 us | 4.83 us | 28.90 us | 32.10 us | 14.41 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-2 | 15.70 us | **3.40 us** | 13.50 us | 61.24 us | 49.10 us | 13.73 us | 42.98 us | 1.37 ms | 43.22 us | 27.09 us | 27.09 us | 12.90 us | 92.70 us | 104.20 us | 24.40 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-4 | 4.99 us | **1.18 us** | 4.44 us | 32.11 us | 34.53 us | 5.25 us | 20.75 us | 907.15 us | 26.01 us | 9.92 us | 10.34 us | 4.77 us | 28.30 us | 31.90 us | 14.12 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-withdraw-0 | 574.60 us | **326.82 us** | 503.48 us | 1.08 ms | 382.32 us | 540.76 us | 961.08 us | 20.40 ms | 1.91 ms | 821.89 us | 879.68 us | 520.16 us | 3.10 ms | 3.62 ms | FAIL |
| c6aa9ec93c2e4fe6396240b1fae8ed4a1e5960403af40ae1d52d0753beced05c-spend-2 | 73.02 us | **18.97 us** | 59.49 us | 117.77 us | 49.51 us | 52.41 us | 160.75 us | 2.82 ms | 99.98 us | 104.74 us | 115.02 us | 49.59 us | 370.40 us | 407.10 us | 48.40 ms |
| c6aa9ec93c2e4fe6396240b1fae8ed4a1e5960403af40ae1d52d0753beced05c-spend-3 | 844.45 us | 1.49 ms | 736.16 us | 1.43 ms | **438.55 us** | 794.20 us | 1.82 ms | 15.96 ms | 1.39 ms | 1.48 ms | 1.58 ms | 653.71 us | 4.50 ms | 5.00 ms | FAIL |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-spend-2 | 23.03 us | **12.53 us** | 22.24 us | 129.90 us | 43.26 us | 17.11 us | 50.88 us | 1.18 ms | 95.89 us | 29.89 us | 31.06 us | 18.52 us | 149.90 us | 128.30 us | 42.94 ms |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-withdraw-0 | 20.57 us | **8.96 us** | 18.68 us | 56.42 us | 28.35 us | 14.36 us | 46.02 us | 1.10 ms | 107.78 us | 26.33 us | 28.09 us | 19.72 us | 134.60 us | 112.30 us | 14.76 ms |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-withdraw-1 | 330.17 us | 370.34 us | 454.80 us | 654.37 us | **272.12 us** | 284.65 us | 546.89 us | 6.66 ms | 474.50 us | 420.85 us | 454.23 us | 360.74 us | 3.14 ms | 2.23 ms | 123.25 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-spend-0 | 15.65 us | **3.48 us** | 13.48 us | 60.53 us | 34.47 us | 13.63 us | 43.42 us | 1.18 ms | 43.14 us | 25.40 us | 26.89 us | 12.97 us | 121.00 us | 105.10 us | 24.27 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-spend-1 | 4.99 us | **1.28 us** | 4.49 us | 32.34 us | 27.25 us | 5.12 us | 20.48 us | 699.88 us | 25.93 us | 10.07 us | 10.50 us | 4.77 us | 30.40 us | 32.10 us | 13.72 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-withdraw-0 | 390.50 us | **238.59 us** | 338.79 us | 748.67 us | 269.91 us | 350.23 us | 669.33 us | 13.96 ms | 1.33 ms | 547.72 us | 578.80 us | 358.71 us | 2.29 ms | 2.40 ms | FAIL |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-0 | 4.98 us | **1.16 us** | 4.49 us | 31.76 us | 26.86 us | 5.27 us | 20.26 us | 698.66 us | 25.59 us | 9.98 us | 10.40 us | 4.77 us | 31.50 us | 31.90 us | 13.81 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-2 | 15.53 us | **3.41 us** | 13.65 us | 61.36 us | 34.96 us | 13.63 us | 43.20 us | 1.16 ms | 42.79 us | 25.77 us | 27.01 us | 12.87 us | 102.00 us | 105.40 us | 24.67 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-withdraw-0 | 386.51 us | **242.29 us** | 337.47 us | 754.77 us | 264.67 us | 344.14 us | 650.26 us | 12.75 ms | 1.31 ms | 544.26 us | 575.85 us | 354.37 us | 2.28 ms | 2.37 ms | FAIL |
| e2fbfa2be7dc3f978d4131f60a99085b888b8b7a2123d41400dc4697d6a84df7-spend-0 | 6.26 us | **1.82 us** | 5.62 us | 18.68 us | 23.43 us | 6.09 us | 24.39 us | 595.37 us | 9.87 us | 11.56 us | 12.24 us | 5.20 us | 37.90 us | 39.80 us | 5.41 ms |
| e2fbfa2be7dc3f978d4131f60a99085b888b8b7a2123d41400dc4697d6a84df7-spend-1 | 267.55 us | 315.45 us | 244.23 us | 536.75 us | **186.31 us** | 240.33 us | 497.96 us | 7.49 ms | 1.22 ms | 385.49 us | 413.24 us | 229.98 us | 1.62 ms | 1.67 ms | FAIL |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-0 | 5.76 us | **1.47 us** | 5.37 us | 34.06 us | 25.95 us | 5.94 us | 22.01 us | 666.00 us | 10.33 us | 11.38 us | 11.90 us | 4.94 us | 37.80 us | 39.60 us | 13.38 ms |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-2 | 303.90 us | 286.89 us | 285.28 us | 667.31 us | **254.41 us** | 308.00 us | 537.00 us | 11.39 ms | 829.01 us | 444.25 us | 458.45 us | 281.95 us | 1.82 ms | 1.93 ms | FAIL |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-withdraw-0 | 9.00 us | **2.42 us** | 8.57 us | 22.80 us | 26.19 us | 8.11 us | 26.77 us | 1.08 ms | 14.23 us | 15.86 us | 16.58 us | 8.75 us | 56.30 us | 60.70 us | 6.97 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-spend-1 | 15.62 us | **3.46 us** | 13.48 us | 61.53 us | 34.97 us | 13.63 us | 43.42 us | 1.15 ms | 44.08 us | 25.64 us | 26.91 us | 12.91 us | 101.20 us | 104.90 us | 24.67 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-spend-2 | 4.99 us | **1.13 us** | 4.45 us | 32.08 us | 27.27 us | 5.08 us | 20.61 us | 669.32 us | 26.63 us | 9.93 us | 10.35 us | 4.76 us | 30.00 us | 32.10 us | 13.70 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-withdraw-0 | 388.41 us | **232.84 us** | 337.83 us | 766.78 us | 264.64 us | 347.19 us | 657.12 us | 13.02 ms | 1.31 ms | 544.14 us | 579.70 us | 354.25 us | 2.17 ms | 2.37 ms | FAIL |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*