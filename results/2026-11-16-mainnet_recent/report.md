# Cardano Plutus VM Benchmark Results

**Date:** 2026-11-16

**Corpus:** Mainnet validators (`mainnet_recent`): every script of 40 of 522 transactions (102 of 1360 programs), selected with seed 1. The per-script tables list every program measured.

## Environment
```
date: 2026-11-16T20:09:25+00:00
kernel: 6.8.0-147-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
corpus: mainnet_recent (102 of 1360 programs from 40 of 522 transactions, sample 40, seed 1; list in corpus.txt)
```

## VM Versions

| VM | Source revision | Toolchain |
|---|---|---|
| plutus-core CEK (Haskell / GHC) | master@12ddaca ([12ddaca](https://github.com/IntersectMBO/plutus/commit/12ddacadae1ac78709c8fc7aa2eec252df60a41d)) | GHC 9.6.4 |
| Scalus UPLC→JVM JIT (Scala / JVM) | master@a3e3487 ([a3e3487](https://github.com/scalus3/scalus/commit/a3e348790452d614cf242f980380fc1246fc01f8)) | JDK 21 / Scala 3 |
| Scalus CEK (Scala / JVM) | master@a3e3487 ([a3e3487](https://github.com/scalus3/scalus/commit/a3e348790452d614cf242f980380fc1246fc01f8)) | JDK 21 / Scala 3 |
| Julc CEK (Java / GraalVM) | main@8724e2c ([8724e2c](https://github.com/bloxbean/julc/commit/8724e2ce2008db78a3f9679fc0160fc10bead83a)) | GraalVM 25.0.2-graal |
| llvm-uplc post-JIT execution (C++ / LLVM) | master@6bcef67 ([6bcef67](https://github.com/SeungheonOh/llvm-uplc/commit/6bcef67ce1995d232327f13d9080fe2f0261a55c)) | LLVM 22.1.0 |
| Amaru UPLC CEK (Rust) | [0.6.0](https://crates.io/crates/amaru-uplc/0.6.0) | rustc nightly-2026-09-04 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | [3.0.5](https://www.npmjs.com/package/@harmoniclabs/plutus-machine/v/3.0.5) | Node.js 22 |
| Plutuz CEK (Zig) | main@33b812d ([33b812d](https://github.com/utxo-company/plutuz/commit/33b812dbcf88f6851286e54cb93a4a443353f94c)) | Zig 0.15.2 |
| Chrysalis CEK (C# / .NET) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Chrysalis CEK (C# / .NET AOT) | v1.7.14-alpha ([7c45d47](https://github.com/SAIB-Inc/Chrysalis/commit/7c45d47c87c63520cea84212dbd01ecc8d372ac3)) | .NET SDK 10.0 |
| Plutigo CEK (Go) | main@ba8c219 ([ba8c219](https://github.com/blinklabs-io/plutigo/commit/ba8c21970a6e23356df46390371e456fec2ff9db)) | Go 1.27.3 |
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
| **Amaru UPLC CEK (Rust)** | Rust | 350.87 us | 1.00x | 0 |
| **Plutigo CEK (Go)** | Go | 388.74 us | 1.11x | 0 |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 436.27 us | 1.24x | 0 |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 547.33 us | 1.56x | 0 |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 565.61 us | 1.61x | 0 |
| **Plutuz CEK (Zig)** | Zig | 872.44 us | 2.49x | 0 |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 1.26 ms | 3.58x | 0 |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.80 ms | 5.14x | 0 |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.86 ms | 5.29x | 0 |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 14.35 ms | 40.89x | 0 |
| **opshin CEK (Python / CPython)** | Python / CPython | 33.51 ms | 95.51x | 24 |

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Amaru UPLC CEK (Rust)** | Rust | 143.15 us | 1.00x |
| **Plutigo CEK (Go)** | Go | 152.60 us | 1.07x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 177.90 us | 1.24x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 211.28 us | 1.48x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 218.33 us | 1.53x |
| **Plutuz CEK (Zig)** | Zig | 294.92 us | 2.06x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 534.87 us | 3.74x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 629.29 us | 4.40x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 687.99 us | 4.81x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 5.40 ms | 37.72x |
| **opshin CEK (Python / CPython)** | Python / CPython | 33.92 ms | 236.93x |

#### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| Amaru UPLC CEK (Rust) | 102 | 0 | 0 | 102 |
| Plutigo CEK (Go) | 102 | 0 | 0 | 102 |
| Scalus CEK (Scala / JVM) | 102 | 0 | 0 | 102 |
| Chrysalis CEK (C# / .NET) | 102 | 0 | 0 | 102 |
| Chrysalis CEK (C# / .NET AOT) | 102 | 0 | 0 | 102 |
| Plutuz CEK (Zig) | 102 | 0 | 0 | 102 |
| plutus-core CEK (Haskell / GHC) | 102 | 0 | 0 | 102 |
| blaze-plutus CEK (TypeScript / Node V8) | 102 | 0 | 0 | 102 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 102 | 0 | 0 | 102 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | 102 | 0 | 0 | 102 |
| opshin CEK (Python / CPython) | 78 | 24 | 0 | 102 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus CEK (Scala / JVM) | Amaru UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 04cb6786e24f2690d94e908b31b02213b0befe91ac58923ac57951726df25cc9-spend-1 | 34.70 us | 13.57 us | **11.59 us** | 459.38 us | 27.97 us | 16.55 us | 15.54 us | 14.03 us | 41.90 us | 41.00 us | 3.37 ms |
| 0fc112573cf010b19921588bbc2b86a62e66b980e891ef482fd3e310c6d4ace8-spend-0 | 34.07 us | 13.76 us | **11.59 us** | 475.89 us | 27.72 us | 15.32 us | 16.94 us | 13.46 us | 41.80 us | 39.60 us | 3.39 ms |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-0 | 2.24 ms | 761.27 us | 673.33 us | 21.26 ms | 1.99 ms | 1.00 ms | 1.05 ms | **540.11 us** | 3.16 ms | 3.75 ms | FAIL |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-2 | 98.03 us | 38.76 us | **34.16 us** | 1.57 ms | 37.85 us | 42.90 us | 42.19 us | 38.17 us | 135.00 us | 113.80 us | 9.43 ms |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-3 | 108.90 us | 40.73 us | **32.37 us** | 1.55 ms | 38.73 us | 41.85 us | 49.77 us | 37.54 us | 139.60 us | 117.90 us | 9.61 ms |
| 206ac25b32f1ff0becac4a4ca788f833910b0fc2ad0ed3507577f89ed40a1f3d-spend-0 | 1.55 ms | 734.49 us | **569.09 us** | 27.18 ms | 1.92 ms | 961.05 us | 1.09 ms | 673.67 us | 3.82 ms | 3.96 ms | FAIL |
| 206ac25b32f1ff0becac4a4ca788f833910b0fc2ad0ed3507577f89ed40a1f3d-spend-1 | 200.54 us | 63.95 us | **57.82 us** | 2.38 ms | 107.20 us | 69.82 us | 66.06 us | 58.63 us | 241.30 us | 175.50 us | 19.25 ms |
| 316b997bb14d86e3fa1af6dc4898b307f4ff182c1d511462cd3f455362836e47-spend-0 | 935.38 us | 268.71 us | 216.52 us | 4.82 ms | 424.92 us | 335.83 us | 361.57 us | **202.53 us** | 1.01 ms | 789.70 us | 91.21 ms |
| 316b997bb14d86e3fa1af6dc4898b307f4ff182c1d511462cd3f455362836e47-withdraw-0 | 1.45 ms | 818.15 us | **513.25 us** | 25.99 ms | 954.37 us | 872.74 us | 844.75 us | 603.94 us | 4.25 ms | 3.42 ms | 178.19 ms |
| 3598b54af22fda534e594138b0703ff7971c24c75a63190ec303a3ce497ab244-spend-0 | 34.32 us | 14.21 us | **11.43 us** | 623.59 us | 32.93 us | 15.84 us | 15.89 us | 12.90 us | 48.10 us | 41.70 us | 3.38 ms |
| 37a68e7227267dc3ee41b94949c45a84a5c2a8d01cb1dc646333618af9eaee63-spend-0 | 100.42 us | 35.13 us | **32.27 us** | 1.74 ms | 40.90 us | 39.44 us | 40.84 us | 34.15 us | 144.20 us | 115.20 us | 9.41 ms |
| 37a68e7227267dc3ee41b94949c45a84a5c2a8d01cb1dc646333618af9eaee63-spend-1 | 1.87 ms | 612.16 us | 487.70 us | 15.70 ms | 1.79 ms | 846.99 us | 824.01 us | **479.11 us** | 2.88 ms | 2.88 ms | FAIL |
| 3cff44e46e2d4712017a72cd2fe5272270af0f55745fec48b74442fd017df379-spend-0 | 607.38 us | 272.21 us | **199.54 us** | 10.37 ms | 647.04 us | 327.35 us | 359.47 us | 250.09 us | 1.21 ms | 1.30 ms | 110.60 ms |
| 3e3b0282bf031ff6fc34d7706ecba6c2dfb7676cf53d7d54f5fb9c1c5991753c-spend-1 | 2.07 ms | 615.21 us | 489.19 us | 14.80 ms | 1.71 ms | 793.59 us | 868.54 us | **475.51 us** | 2.51 ms | 2.85 ms | FAIL |
| 3e3b0282bf031ff6fc34d7706ecba6c2dfb7676cf53d7d54f5fb9c1c5991753c-spend-2 | 91.65 us | 34.98 us | **30.98 us** | 1.57 ms | 36.88 us | 42.06 us | 42.08 us | 34.13 us | 121.20 us | 114.60 us | 10.49 ms |
| 43dfbfbefaa184ed1010ecd05c2f5b96dd29bc062d08bc97f26187a1bd30738f-spend-0 | 92.67 us | 25.00 us | 24.98 us | 906.27 us | 34.93 us | 33.51 us | 34.39 us | **24.39 us** | 114.90 us | 96.70 us | 10.34 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-0 | 1.64 ms | 639.82 us | **514.87 us** | 33.07 ms | 1.02 ms | 945.51 us | 924.17 us | 519.56 us | 3.56 ms | 3.19 ms | 256.90 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-1 | 2.29 ms | 677.96 us | **557.01 us** | 39.04 ms | 1.12 ms | 938.88 us | 1.05 ms | 625.12 us | 3.76 ms | 2.87 ms | 276.41 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-3 | 664.37 us | 312.27 us | **278.80 us** | 18.76 ms | 593.76 us | 446.36 us | 424.20 us | 280.06 us | 1.72 ms | 1.61 ms | 118.24 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-0 | 490.68 us | 168.50 us | **114.39 us** | 3.85 ms | 228.07 us | 167.99 us | 168.61 us | 117.85 us | 521.30 us | 444.20 us | 52.69 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-1 | 482.46 us | 159.91 us | 118.67 us | 3.91 ms | 228.46 us | 157.46 us | 180.46 us | **113.61 us** | 531.10 us | 446.30 us | 50.55 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-2 | 518.82 us | 165.80 us | 115.80 us | 4.09 ms | 221.28 us | 170.66 us | 163.96 us | **114.88 us** | 529.90 us | 444.30 us | 50.72 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-4 | 331.01 us | 101.95 us | **82.82 us** | 3.02 ms | 145.18 us | 111.12 us | 116.19 us | 88.09 us | 354.00 us | 287.30 us | 33.34 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-withdraw-0 | 3.43 ms | 1.39 ms | **1.11 ms** | 58.83 ms | 4.06 ms | 1.95 ms | 2.13 ms | 1.34 ms | 7.63 ms | 7.62 ms | FAIL |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-spend-0 | 2.83 ms | 748.37 us | **584.45 us** | 22.74 ms | 1.33 ms | 887.01 us | 894.88 us | 757.42 us | 3.13 ms | 2.93 ms | FAIL |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-spend-1 | 284.48 us | 82.19 us | 76.03 us | 1.84 ms | 108.82 us | 87.73 us | 100.13 us | **72.95 us** | 264.30 us | 233.70 us | 28.67 ms |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-withdraw-0 | 99.67 us | 38.08 us | **31.97 us** | 2.09 ms | 35.51 us | 39.28 us | 40.53 us | 38.75 us | 133.30 us | 121.30 us | 9.62 ms |
| 56c90a79fb6c5d5fcdfa7306c93f458ce90b97a8d4109b271a0c2d21e987b345-spend-1 | 417.62 us | 172.69 us | **142.44 us** | 8.72 ms | 328.86 us | 249.76 us | 236.69 us | 156.34 us | 849.70 us | 824.70 us | 71.79 ms |
| 56c90a79fb6c5d5fcdfa7306c93f458ce90b97a8d4109b271a0c2d21e987b345-spend-3 | 235.78 us | 82.72 us | **77.32 us** | 3.70 ms | 135.44 us | 116.43 us | 112.39 us | 79.19 us | 400.50 us | 397.40 us | 37.94 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-spend-0 | 311.78 us | 85.30 us | 77.25 us | 1.95 ms | 136.29 us | 95.78 us | 95.58 us | **71.71 us** | 274.40 us | 239.70 us | 34.23 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-spend-2 | 481.14 us | 148.69 us | 103.20 us | 3.11 ms | 211.31 us | 149.50 us | 181.51 us | **100.95 us** | 446.80 us | 407.00 us | 53.66 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-withdraw-0 | 2.67 ms | 801.48 us | **643.36 us** | 26.75 ms | 1.99 ms | 1.01 ms | 1.11 ms | 897.03 us | 3.60 ms | 3.72 ms | FAIL |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-spend-0 | 497.52 us | 149.37 us | 107.22 us | 3.11 ms | 200.46 us | 157.03 us | 151.41 us | **104.19 us** | 432.70 us | 408.20 us | 49.27 ms |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-spend-1 | 310.79 us | 83.89 us | 75.88 us | 1.90 ms | 138.01 us | 92.30 us | 99.24 us | **73.48 us** | 270.40 us | 250.00 us | 31.50 ms |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-withdraw-0 | 2.93 ms | 875.63 us | **654.72 us** | 25.13 ms | 2.32 ms | 1.08 ms | 1.09 ms | 798.92 us | 3.33 ms | 3.83 ms | FAIL |
| 5e1d902963b3cef77bd9bff968f8f93229853319bc7e606302094a80ac4e8bbc-spend-1 | 35.66 us | 14.09 us | **11.36 us** | 463.44 us | 32.79 us | 16.49 us | 15.20 us | 12.93 us | 45.70 us | 41.80 us | 3.51 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-0 | 509.60 us | 163.65 us | 124.97 us | 3.83 ms | 234.07 us | 169.29 us | 201.02 us | **116.64 us** | 490.70 us | 445.10 us | 52.25 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-2 | 349.26 us | 99.18 us | **83.47 us** | 2.88 ms | 152.67 us | 106.25 us | 108.20 us | 95.64 us | 326.50 us | 290.10 us | 33.25 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-3 | 488.55 us | 163.96 us | **114.57 us** | 3.95 ms | 218.81 us | 167.12 us | 164.82 us | 126.72 us | 492.40 us | 467.50 us | 50.92 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-4 | 491.42 us | 164.10 us | **113.72 us** | 4.51 ms | 216.26 us | 174.30 us | 169.13 us | 123.60 us | 500.00 us | 452.00 us | 50.86 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-withdraw-0 | 3.43 ms | **1.27 ms** | 1.31 ms | 61.78 ms | 3.98 ms | 1.98 ms | 2.07 ms | 1.29 ms | 6.67 ms | 7.28 ms | FAIL |
| 81af9388c7fb7f1a557c802069ab2f8cae1b441dc46e3755d98e10c825a672f4-spend-0 | 963.63 us | 264.50 us | 203.07 us | 3.98 ms | 399.41 us | 318.83 us | 338.38 us | **179.81 us** | 800.10 us | 698.00 us | 86.99 ms |
| 81af9388c7fb7f1a557c802069ab2f8cae1b441dc46e3755d98e10c825a672f4-withdraw-0 | 1.39 ms | 755.50 us | **502.01 us** | 24.78 ms | 834.61 us | 805.49 us | 916.54 us | 584.78 us | 3.81 ms | 3.28 ms | 176.40 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-1 | 454.92 us | 145.13 us | 103.16 us | 2.97 ms | 201.23 us | 158.34 us | 152.63 us | **103.16 us** | 500.10 us | 441.40 us | 50.01 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-2 | 353.06 us | 84.25 us | 79.64 us | 2.01 ms | 135.99 us | 99.41 us | 105.92 us | **79.01 us** | 274.80 us | 268.10 us | 30.77 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-withdraw-0 | 2.80 ms | 843.12 us | **639.75 us** | 25.95 ms | 1.90 ms | 1.03 ms | 1.06 ms | 814.85 us | 3.32 ms | 4.20 ms | FAIL |
| 8864ea90e54f74150e7f58d4680e9b9a0959ace4d7048a942cd7a2adfb0a3e3d-spend-0 | 109.17 us | 34.45 us | **30.92 us** | 1.55 ms | 61.09 us | 45.29 us | 43.97 us | 35.51 us | 152.80 us | 137.20 us | 11.32 ms |
| 8864ea90e54f74150e7f58d4680e9b9a0959ace4d7048a942cd7a2adfb0a3e3d-withdraw-0 | 468.39 us | 188.79 us | **143.51 us** | 6.35 ms | 387.35 us | 246.09 us | 266.01 us | 158.94 us | 995.80 us | 847.90 us | 66.29 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-spend-0 | 308.98 us | 85.18 us | 77.28 us | 1.88 ms | 158.77 us | 101.53 us | 102.55 us | **76.74 us** | 301.90 us | 250.60 us | 33.74 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-spend-1 | 459.91 us | 142.50 us | 105.40 us | 2.84 ms | 220.18 us | 144.07 us | 161.47 us | **99.60 us** | 442.60 us | 450.00 us | 54.18 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-withdraw-0 | 2.92 ms | 813.81 us | **641.54 us** | 25.03 ms | 1.97 ms | 1.06 ms | 1.19 ms | 886.75 us | 3.51 ms | 4.21 ms | FAIL |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-spend-1 | 2.71 ms | 776.18 us | **646.83 us** | 20.41 ms | 1.40 ms | 896.44 us | 883.69 us | 788.43 us | 3.11 ms | 3.53 ms | FAIL |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-spend-2 | 278.71 us | 82.30 us | **70.72 us** | 1.68 ms | 109.58 us | 88.92 us | 91.69 us | 72.19 us | 261.60 us | 264.60 us | 31.91 ms |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-withdraw-0 | 95.91 us | 42.32 us | **30.75 us** | 2.14 ms | 37.37 us | 43.81 us | 46.85 us | 39.57 us | 147.00 us | 141.10 us | 11.39 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-0 | 505.44 us | 165.64 us | **113.69 us** | 4.48 ms | 209.30 us | 170.67 us | 167.88 us | 114.51 us | 496.50 us | 477.70 us | 52.97 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-1 | 497.78 us | 163.60 us | 133.31 us | 4.14 ms | 213.75 us | 168.20 us | 174.04 us | **114.55 us** | 494.30 us | 459.00 us | 55.29 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-2 | 351.86 us | 109.22 us | **86.45 us** | 3.01 ms | 145.33 us | 118.63 us | 119.72 us | 92.45 us | 331.00 us | 290.40 us | 37.24 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-3 | 478.79 us | 155.98 us | **121.13 us** | 3.80 ms | 214.44 us | 169.36 us | 165.99 us | 124.94 us | 510.10 us | 449.20 us | 53.67 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-withdraw-0 | 3.87 ms | 1.33 ms | **1.10 ms** | 55.99 ms | 3.94 ms | 1.92 ms | 1.99 ms | 1.30 ms | 6.87 ms | 7.30 ms | FAIL |
| 9821e1defa09d0e9407e4ce6622ead240125df3df75fba63539c55afd841d6f8-spend-1 | 35.07 us | 14.12 us | **12.62 us** | 540.73 us | 30.05 us | 16.04 us | 16.14 us | 12.99 us | 46.50 us | 40.10 us | 3.80 ms |
| 9b456b77cfc279bd3d80822b553952720e452fddc05c47cac387f1d4f6da6700-spend-1 | 35.75 us | 14.51 us | **11.46 us** | 542.35 us | 30.27 us | 16.36 us | 15.09 us | 13.17 us | 47.30 us | 43.00 us | 3.53 ms |
| 9d61863e3a770cc83ec05bccd87b25c28eba22f423a0a63acbeea17fa23e5499-spend-0 | 1.02 ms | 245.25 us | 197.74 us | 4.34 ms | 388.92 us | 317.18 us | 355.55 us | **179.34 us** | 776.50 us | 711.40 us | 90.47 ms |
| 9d61863e3a770cc83ec05bccd87b25c28eba22f423a0a63acbeea17fa23e5499-withdraw-0 | 1.31 ms | 703.94 us | **462.13 us** | 20.70 ms | 807.25 us | 819.20 us | 784.68 us | 526.77 us | 3.12 ms | 2.78 ms | 165.10 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-spend-0 | 459.20 us | 144.31 us | **110.53 us** | 3.02 ms | 235.56 us | 144.16 us | 152.37 us | 111.22 us | 474.30 us | 404.70 us | 47.21 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-spend-2 | 318.41 us | 83.73 us | **73.69 us** | 2.09 ms | 156.56 us | 96.24 us | 105.08 us | 79.46 us | 278.70 us | 237.20 us | 30.73 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-withdraw-0 | 2.86 ms | 837.82 us | **678.29 us** | 25.53 ms | 2.07 ms | 1.09 ms | 1.06 ms | 798.51 us | 3.55 ms | 3.71 ms | FAIL |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-0 | 312.71 us | 92.68 us | **74.66 us** | 2.18 ms | 139.57 us | 102.86 us | 103.45 us | 77.45 us | 329.10 us | 261.10 us | 33.13 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-1 | 486.85 us | 157.96 us | 115.22 us | 3.12 ms | 204.38 us | 149.42 us | 178.00 us | **104.96 us** | 522.80 us | 409.00 us | 48.80 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-3 | 325.83 us | 91.28 us | **74.76 us** | 2.25 ms | 139.71 us | 99.64 us | 102.87 us | 78.29 us | 324.50 us | 261.30 us | 33.54 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-withdraw-0 | 3.19 ms | 967.37 us | **761.43 us** | 36.95 ms | 2.21 ms | 1.20 ms | 1.37 ms | 912.04 us | 4.74 ms | 4.49 ms | FAIL |
| b045c8789a4d7d250c7971e12d4bd0a7e423015e18489e91b1d42967c0c1aea6-spend-0 | 705.39 us | 240.86 us | **186.30 us** | 8.02 ms | 357.54 us | 395.87 us | 381.41 us | 210.79 us | 1.45 ms | 1.18 ms | FAIL |
| beaa9d1683d7bdde24a920f2561b0b9dbe90b652c18b3e59154cfd222c5f696f-spend-1 | 242.20 us | 99.15 us | 92.35 us | 4.93 ms | 153.78 us | 131.39 us | 133.62 us | **90.67 us** | 532.60 us | 473.20 us | 42.59 ms |
| beaa9d1683d7bdde24a920f2561b0b9dbe90b652c18b3e59154cfd222c5f696f-spend-3 | 449.53 us | 169.95 us | **147.60 us** | 9.11 ms | 365.15 us | 225.88 us | 266.35 us | 157.29 us | 944.20 us | 887.50 us | 73.91 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-mint-0 | 763.03 us | 205.08 us | **166.79 us** | 4.04 ms | 271.82 us | 262.23 us | 270.66 us | 173.19 us | 754.30 us | 643.80 us | 85.38 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-mint-1 | 567.71 us | 228.65 us | 200.19 us | 9.95 ms | 333.61 us | 326.89 us | 314.69 us | **181.33 us** | 1.20 ms | 973.80 us | 84.49 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-0 | 2.99 ms | 1.07 ms | **898.36 us** | 49.16 ms | 1.93 ms | 1.59 ms | 1.62 ms | 1.02 ms | 6.49 ms | 4.62 ms | FAIL |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-2 | 2.74 ms | 998.60 us | **760.04 us** | 52.97 ms | 1.74 ms | 1.33 ms | 1.42 ms | 965.67 us | 6.21 ms | 4.57 ms | 339.12 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-3 | 601.87 us | 267.89 us | **222.00 us** | 15.70 ms | 459.25 us | 364.45 us | 352.93 us | 234.35 us | 1.37 ms | 1.14 ms | 97.96 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-0 | 341.23 us | 99.03 us | 85.76 us | 2.52 ms | 142.36 us | 104.43 us | 118.72 us | **84.20 us** | 334.70 us | 266.60 us | 32.56 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-1 | 344.09 us | 94.44 us | 82.85 us | 2.58 ms | 143.14 us | 121.99 us | 113.16 us | **82.48 us** | 315.60 us | 267.70 us | 32.14 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-2 | 487.16 us | 170.86 us | **110.03 us** | 3.51 ms | 208.20 us | 170.99 us | 163.94 us | 111.31 us | 489.60 us | 428.50 us | 49.69 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-4 | 352.10 us | 93.05 us | **79.11 us** | 2.49 ms | 143.19 us | 106.69 us | 124.70 us | 85.30 us | 307.10 us | 267.10 us | 31.95 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-withdraw-0 | 3.34 ms | 1.03 ms | **879.66 us** | 37.52 ms | 2.50 ms | 1.55 ms | 1.40 ms | 997.58 us | 4.60 ms | 5.19 ms | FAIL |
| c6aa9ec93c2e4fe6396240b1fae8ed4a1e5960403af40ae1d52d0753beced05c-spend-2 | 354.02 us | 143.94 us | **107.82 us** | 5.26 ms | 188.55 us | 193.25 us | 195.80 us | 117.81 us | 653.80 us | 601.40 us | 63.54 ms |
| c6aa9ec93c2e4fe6396240b1fae8ed4a1e5960403af40ae1d52d0753beced05c-spend-3 | 2.57 ms | 1.14 ms | 1.02 ms | 29.35 ms | 1.85 ms | 1.98 ms | 2.11 ms | **859.68 us** | 6.43 ms | 6.31 ms | FAIL |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-spend-2 | 1.04 ms | 251.62 us | 208.65 us | 4.25 ms | 430.67 us | 308.07 us | 318.18 us | **182.50 us** | 844.20 us | 800.70 us | 88.44 ms |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-withdraw-0 | 237.01 us | 76.70 us | **69.20 us** | 2.64 ms | 195.48 us | 99.80 us | 97.67 us | 71.66 us | 344.10 us | 288.80 us | 26.12 ms |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-withdraw-1 | 1.45 ms | 729.24 us | **493.76 us** | 21.47 ms | 869.08 us | 824.92 us | 858.26 us | 555.17 us | 3.32 ms | 3.03 ms | 191.48 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-spend-0 | 496.95 us | 144.89 us | **103.15 us** | 2.99 ms | 224.75 us | 144.12 us | 150.39 us | 104.61 us | 467.00 us | 405.80 us | 53.01 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-spend-1 | 321.87 us | 85.75 us | **73.01 us** | 2.07 ms | 152.01 us | 100.93 us | 105.74 us | 82.87 us | 285.20 us | 246.50 us | 35.69 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-withdraw-0 | 2.88 ms | 804.38 us | **645.23 us** | 25.43 ms | 2.07 ms | 1.01 ms | 1.07 ms | 836.00 us | 3.56 ms | 3.71 ms | FAIL |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-0 | 317.11 us | 86.30 us | **71.64 us** | 2.08 ms | 142.39 us | 99.65 us | 98.83 us | 71.67 us | 280.00 us | 238.80 us | 33.89 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-2 | 466.28 us | 143.63 us | 103.52 us | 3.06 ms | 208.14 us | 158.85 us | 163.10 us | **98.81 us** | 482.50 us | 403.90 us | 52.68 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-withdraw-0 | 2.82 ms | 835.09 us | **724.26 us** | 24.88 ms | 1.91 ms | 1.01 ms | 1.13 ms | 812.28 us | 3.77 ms | 3.76 ms | FAIL |
| e2fbfa2be7dc3f978d4131f60a99085b888b8b7a2123d41400dc4697d6a84df7-spend-0 | 93.02 us | 35.34 us | **30.16 us** | 1.52 ms | 36.03 us | 39.63 us | 38.48 us | 34.96 us | 131.90 us | 111.70 us | 10.06 ms |
| e2fbfa2be7dc3f978d4131f60a99085b888b8b7a2123d41400dc4697d6a84df7-spend-1 | 2.01 ms | 647.51 us | 482.88 us | 15.35 ms | 1.73 ms | 794.16 us | 921.52 us | **478.94 us** | 2.65 ms | 2.95 ms | FAIL |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-0 | 322.74 us | 79.54 us | **67.38 us** | 1.67 ms | 109.84 us | 89.60 us | 91.40 us | 70.61 us | 273.50 us | 256.50 us | 30.88 ms |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-2 | 3.03 ms | 809.36 us | **620.43 us** | 20.37 ms | 1.43 ms | 945.34 us | 892.76 us | 734.20 us | 2.89 ms | 3.20 ms | FAIL |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-withdraw-0 | 93.17 us | 41.56 us | **30.83 us** | 2.16 ms | 37.91 us | 44.93 us | 46.70 us | 38.48 us | 145.00 us | 130.50 us | 11.23 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-spend-1 | 508.28 us | 147.53 us | 103.73 us | 3.26 ms | 202.47 us | 143.59 us | 152.31 us | **100.26 us** | 454.60 us | 403.60 us | 49.06 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-spend-2 | 306.95 us | 82.97 us | 74.16 us | 2.00 ms | 136.77 us | 100.22 us | 97.13 us | **72.39 us** | 286.80 us | 238.60 us | 30.50 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-withdraw-0 | 2.86 ms | 834.42 us | **690.24 us** | 26.39 ms | 1.90 ms | 1.01 ms | 1.08 ms | 842.38 us | 3.56 ms | 3.76 ms | FAIL |

## Eval tier: evaluate a decoded program

The program is decoded before timing; each iteration evaluates it. JIT VMs compile before timing too.

### Per transaction (geometric mean of 40 transaction totals)

*Each VM's time for a transaction is the sum of its times for every script the transaction runs. A VM that fails any script fails the transaction, which is assigned the slowest competitor's total.*

| VM | Language | Geo Mean | vs Fastest | Failed transactions |
|---|---|---|---|---|
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 96.68 us | 1.00x | 0 |
| **Plutigo CEK (Go)** | Go | 152.87 us | 1.58x | 0 |
| **Amaru UPLC CEK (Rust)** | Rust | 155.24 us | 1.61x | 0 |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 160.48 us | 1.66x | 0 |
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 166.40 us | 1.72x | 0 |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 173.03 us | 1.79x | 0 |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 262.25 us | 2.71x | 0 |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 269.48 us | 2.79x | 0 |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 390.18 us | 4.04x | 0 |
| **Plutuz CEK (Zig)** | Zig | 540.39 us | 5.59x | 0 |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 1.03 ms | 10.68x | 0 |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 1.08 ms | 11.12x | 0 |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 11.24 ms | 116.23x | 0 |
| **opshin CEK (Python / CPython)** | Python / CPython | 24.45 ms | 252.91x | 24 |

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 13.00 us | 1.00x |
| **Plutigo CEK (Go)** | Go | 30.65 us | 2.36x |
| **Amaru UPLC CEK (Rust)** | Rust | 32.16 us | 2.47x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 32.29 us | 2.48x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 35.51 us | 2.73x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 57.34 us | 4.41x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 59.62 us | 4.59x |
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 65.73 us | 5.06x |
| **Plutuz CEK (Zig)** | Zig | 106.64 us | 8.20x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 113.06 us | 8.70x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 223.16 us | 17.16x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 224.62 us | 17.28x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 3.74 ms | 287.74x |
| **opshin CEK (Python / CPython)** | Python / CPython | 20.15 ms | 1549.75x |

#### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| Scalus UPLC→JVM JIT (Scala / JVM) | 102 | 0 | 0 | 102 |
| Plutigo CEK (Go) | 102 | 0 | 0 | 102 |
| Amaru UPLC CEK (Rust) | 102 | 0 | 0 | 102 |
| Scalus CEK (Scala / JVM) | 102 | 0 | 0 | 102 |
| plutus-core CEK (Haskell / GHC) | 102 | 0 | 0 | 102 |
| Chrysalis CEK (C# / .NET) | 102 | 0 | 0 | 102 |
| Chrysalis CEK (C# / .NET AOT) | 102 | 0 | 0 | 102 |
| llvm-uplc post-JIT execution (C++ / LLVM) | 102 | 0 | 0 | 102 |
| Plutuz CEK (Zig) | 102 | 0 | 0 | 102 |
| Julc CEK (Java / GraalVM) | 102 | 0 | 0 | 102 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 102 | 0 | 0 | 102 |
| blaze-plutus CEK (TypeScript / Node V8) | 102 | 0 | 0 | 102 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | 102 | 0 | 0 | 102 |
| opshin CEK (Python / CPython) | 78 | 24 | 0 | 102 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc post-JIT execution (C++ / LLVM) | Amaru UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 04cb6786e24f2690d94e908b31b02213b0befe91ac58923ac57951726df25cc9-spend-1 | 3.00 us | **417 ns** | 2.51 us | 11.04 us | 7.01 us | 3.42 us | 314.45 us | 18.92 us | 6.16 us | 6.22 us | 2.76 us | 14.00 us | 19.20 us | 2.01 ms |
| 0fc112573cf010b19921588bbc2b86a62e66b980e891ef482fd3e310c6d4ace8-spend-0 | 3.31 us | **422 ns** | 2.60 us | 11.89 us | 6.78 us | 3.19 us | 319.06 us | 18.98 us | 6.52 us | 6.03 us | 2.47 us | 12.70 us | 17.50 us | 2.04 ms |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-0 | 401.76 us | 780.33 us | 343.58 us | 730.84 us | **241.71 us** | 368.32 us | 16.51 ms | 1.78 ms | 642.80 us | 585.47 us | 318.37 us | 1.90 ms | 2.82 ms | FAIL |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-2 | 5.43 us | **1.59 us** | 4.83 us | 17.89 us | 28.76 us | 5.55 us | 1.12 ms | 9.47 us | 10.25 us | 10.57 us | 4.30 us | 29.20 us | 36.10 us | 5.07 ms |
| 1fa35fdb02def65d70348c4a0a1a3b749a93c8f267dc8b531347936388028a18-spend-3 | 5.46 us | **1.47 us** | 4.62 us | 17.54 us | 28.97 us | 5.39 us | 1.22 ms | 9.52 us | 10.92 us | 11.78 us | 4.27 us | 30.10 us | 38.50 us | 5.03 ms |
| 206ac25b32f1ff0becac4a4ca788f833910b0fc2ad0ed3507577f89ed40a1f3d-spend-0 | 525.38 us | **298.00 us** | 487.03 us | 830.55 us | 301.15 us | 383.75 us | 25.63 ms | 1.58 ms | 734.57 us | 756.47 us | 457.91 us | 2.58 ms | 3.39 ms | FAIL |
| 206ac25b32f1ff0becac4a4ca788f833910b0fc2ad0ed3507577f89ed40a1f3d-spend-1 | 4.50 us | **1.14 us** | 3.74 us | 22.86 us | 32.58 us | 5.39 us | 1.59 ms | 41.56 us | 8.99 us | 9.13 us | 4.30 us | 23.60 us | 27.10 us | 8.46 ms |
| 316b997bb14d86e3fa1af6dc4898b307f4ff182c1d511462cd3f455362836e47-spend-0 | 19.55 us | **10.26 us** | 18.66 us | 131.19 us | 57.05 us | 16.03 us | 2.73 ms | 75.71 us | 27.88 us | 27.84 us | 17.22 us | 149.90 us | 128.80 us | 40.03 ms |
| 316b997bb14d86e3fa1af6dc4898b307f4ff182c1d511462cd3f455362836e47-withdraw-0 | 371.66 us | 465.37 us | 496.13 us | 704.70 us | **293.02 us** | 305.04 us | 22.43 ms | 503.85 us | 470.98 us | 483.86 us | 388.95 us | 2.81 ms | 2.54 ms | 136.41 ms |
| 3598b54af22fda534e594138b0703ff7971c24c75a63190ec303a3ce497ab244-spend-0 | 3.22 us | **413 ns** | 2.62 us | 11.12 us | 6.91 us | 3.21 us | 305.02 us | 21.29 us | 6.18 us | 6.75 us | 2.37 us | 14.80 us | 18.30 us | 2.33 ms |
| 37a68e7227267dc3ee41b94949c45a84a5c2a8d01cb1dc646333618af9eaee63-spend-0 | 6.96 us | **1.95 us** | 5.67 us | 19.27 us | 23.70 us | 6.78 us | 1.01 ms | 10.59 us | 12.54 us | 12.19 us | 5.29 us | 38.80 us | 45.40 us | 5.65 ms |
| 37a68e7227267dc3ee41b94949c45a84a5c2a8d01cb1dc646333618af9eaee63-spend-1 | 285.32 us | 610.16 us | 254.09 us | 563.95 us | **182.63 us** | 241.35 us | 13.13 ms | 1.28 ms | 403.34 us | 429.02 us | 233.24 us | 1.46 ms | 2.11 ms | FAIL |
| 3cff44e46e2d4712017a72cd2fe5272270af0f55745fec48b74442fd017df379-spend-0 | 144.31 us | **39.31 us** | 127.87 us | 256.99 us | 115.19 us | 110.82 us | 10.42 ms | 506.62 us | 202.18 us | 202.34 us | 143.44 us | 748.10 us | 888.20 us | 80.14 ms |
| 3e3b0282bf031ff6fc34d7706ecba6c2dfb7676cf53d7d54f5fb9c1c5991753c-spend-1 | 284.97 us | 418.82 us | 252.51 us | 537.52 us | **182.97 us** | 244.49 us | 12.69 ms | 1.33 ms | 406.38 us | 411.85 us | 271.93 us | 1.38 ms | 1.84 ms | FAIL |
| 3e3b0282bf031ff6fc34d7706ecba6c2dfb7676cf53d7d54f5fb9c1c5991753c-spend-2 | 6.61 us | **1.94 us** | 5.66 us | 19.86 us | 23.59 us | 6.58 us | 1.05 ms | 9.95 us | 11.67 us | 14.10 us | 5.37 us | 34.50 us | 42.50 us | 5.57 ms |
| 43dfbfbefaa184ed1010ecd05c2f5b96dd29bc062d08bc97f26187a1bd30738f-spend-0 | 4.77 us | **1.76 us** | 5.54 us | 22.37 us | 10.98 us | 5.35 us | 592.35 us | 7.73 us | 10.02 us | 9.66 us | 4.20 us | 37.10 us | 35.40 us | 5.00 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-0 | 343.56 us | **181.55 us** | 408.61 us | 795.53 us | 248.77 us | 293.44 us | 29.06 ms | 644.51 us | 541.00 us | 489.90 us | 308.13 us | 3.08 ms | 2.30 ms | 178.66 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-1 | 263.91 us | **198.95 us** | 278.05 us | 657.74 us | 226.17 us | 245.94 us | 33.54 ms | 580.02 us | 376.97 us | 387.93 us | 214.76 us | 1.87 ms | 1.70 ms | 163.59 ms |
| 4d0688efbb6c86bed339d4e32c6d6bac32cd12f7b58a3f05ed6c1946c6abaa7f-spend-3 | 159.84 us | **70.39 us** | 195.02 us | 408.85 us | 153.30 us | 161.74 us | 16.92 ms | 402.96 us | 269.28 us | 246.46 us | 147.06 us | 1.34 ms | 1.15 ms | 90.10 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-0 | 16.12 us | **3.59 us** | 14.18 us | 62.91 us | 55.40 us | 13.68 us | 2.70 ms | 43.79 us | 26.78 us | 29.22 us | 13.80 us | 107.10 us | 110.30 us | 26.35 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-1 | 16.39 us | **3.62 us** | 15.78 us | 64.62 us | 49.60 us | 13.91 us | 2.57 ms | 45.97 us | 26.79 us | 27.81 us | 13.67 us | 109.20 us | 114.60 us | 24.70 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-2 | 16.48 us | **3.60 us** | 13.69 us | 63.50 us | 50.88 us | 13.96 us | 2.47 ms | 48.69 us | 28.92 us | 29.09 us | 13.39 us | 110.10 us | 112.80 us | 24.53 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-spend-4 | 5.47 us | **1.19 us** | 4.64 us | 33.12 us | 44.46 us | 5.47 us | 1.79 ms | 28.89 us | 10.39 us | 10.85 us | 4.90 us | 34.60 us | 34.10 us | 14.41 ms |
| 520e37a2777089921c50a8ff3d15f7742c58dfc5a548555ca1960f372206e602-withdraw-0 | 902.85 us | **420.30 us** | 829.79 us | 1.72 ms | 571.84 us | 828.49 us | 53.83 ms | 3.56 ms | 1.41 ms | 1.38 ms | 857.47 us | 6.46 ms | 6.15 ms | FAIL |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-spend-0 | 300.83 us | 331.18 us | 282.15 us | 641.33 us | **233.81 us** | 289.74 us | 15.63 ms | 750.65 us | 433.20 us | 471.02 us | 277.40 us | 2.05 ms | 1.90 ms | FAIL |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-spend-1 | 6.46 us | **1.46 us** | 5.57 us | 36.27 us | 23.82 us | 6.46 us | 911.37 us | 10.67 us | 11.09 us | 12.05 us | 5.31 us | 44.30 us | 40.10 us | 13.42 ms |
| 5580e04420083bd288188d7eef5c40398d334a4fba8b066a7f1b91e89c57e478-withdraw-0 | 8.18 us | **2.40 us** | 7.60 us | 20.08 us | 25.26 us | 8.08 us | 1.67 ms | 13.41 us | 15.29 us | 15.09 us | 9.03 us | 66.50 us | 57.00 us | 6.28 ms |
| 56c90a79fb6c5d5fcdfa7306c93f458ce90b97a8d4109b271a0c2d21e987b345-spend-1 | 101.10 us | **33.95 us** | 85.60 us | 183.48 us | 83.52 us | 77.51 us | 8.96 ms | 228.92 us | 131.32 us | 152.88 us | 85.64 us | 632.20 us | 615.90 us | 50.06 ms |
| 56c90a79fb6c5d5fcdfa7306c93f458ce90b97a8d4109b271a0c2d21e987b345-spend-3 | 42.68 us | **11.65 us** | 31.23 us | 76.34 us | 45.66 us | 30.59 us | 3.16 ms | 75.13 us | 54.98 us | 56.13 us | 32.32 us | 252.00 us | 245.00 us | 26.90 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-spend-0 | 5.64 us | **1.24 us** | 4.64 us | 35.06 us | 24.76 us | 5.11 us | 1.07 ms | 26.99 us | 10.75 us | 10.38 us | 4.78 us | 37.00 us | 34.90 us | 15.60 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-spend-2 | 16.30 us | **3.56 us** | 15.33 us | 63.85 us | 35.37 us | 15.75 us | 1.71 ms | 45.03 us | 26.22 us | 30.04 us | 12.85 us | 99.90 us | 114.90 us | 27.35 ms |
| 5c86af86bef9773d582ed641789add4c32df3dbd442a2d7a523239006e721928-withdraw-0 | 415.77 us | **272.19 us** | 363.00 us | 782.97 us | 276.21 us | 362.92 us | 20.55 ms | 1.38 ms | 555.08 us | 579.60 us | 359.21 us | 2.18 ms | 2.61 ms | FAIL |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-spend-0 | 16.15 us | **3.47 us** | 13.85 us | 64.38 us | 35.84 us | 14.15 us | 1.70 ms | 44.97 us | 27.44 us | 27.08 us | 13.85 us | 100.40 us | 106.90 us | 26.58 ms |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-spend-1 | 5.74 us | **1.20 us** | 4.75 us | 33.00 us | 25.42 us | 5.29 us | 1.04 ms | 29.37 us | 10.37 us | 11.49 us | 5.03 us | 32.90 us | 33.80 us | 14.41 ms |
| 5cf5f0fb43ef1f8664b037e06b8265b51b6857ab2e8c626fc2fa10a4157f9cdb-withdraw-0 | 398.71 us | **295.84 us** | 352.87 us | 776.75 us | 314.33 us | 375.98 us | 23.40 ms | 1.50 ms | 564.63 us | 595.38 us | 376.46 us | 2.25 ms | 2.57 ms | FAIL |
| 5e1d902963b3cef77bd9bff968f8f93229853319bc7e606302094a80ac4e8bbc-spend-1 | 2.96 us | **420 ns** | 2.63 us | 11.31 us | 7.34 us | 3.28 us | 324.03 us | 21.11 us | 6.61 us | 5.92 us | 2.46 us | 14.80 us | 17.60 us | 2.10 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-0 | 16.65 us | **3.59 us** | 13.63 us | 66.10 us | 49.67 us | 14.16 us | 2.45 ms | 43.03 us | 26.70 us | 28.36 us | 12.86 us | 95.40 us | 118.50 us | 25.64 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-2 | 5.27 us | **1.16 us** | 4.88 us | 32.44 us | 38.96 us | 5.37 us | 1.75 ms | 26.39 us | 10.49 us | 10.36 us | 4.86 us | 30.50 us | 35.30 us | 14.15 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-3 | 16.24 us | **3.50 us** | 14.98 us | 64.96 us | 58.81 us | 15.52 us | 2.44 ms | 44.44 us | 25.21 us | 29.72 us | 13.48 us | 97.60 us | 109.30 us | 24.70 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-spend-4 | 16.41 us | **3.60 us** | 13.81 us | 63.45 us | 51.55 us | 14.31 us | 2.45 ms | 42.87 us | 26.79 us | 27.82 us | 14.16 us | 105.00 us | 106.60 us | 25.02 ms |
| 7aad9d758bb8ba5a1a6db2c040863a6fb95a6d48e28f9d0013f00c3c0a9618f8-withdraw-0 | 934.99 us | **414.79 us** | 808.12 us | 1.71 ms | 603.81 us | 789.03 us | 52.19 ms | 3.35 ms | 1.40 ms | 1.37 ms | 846.29 us | 5.17 ms | 5.64 ms | FAIL |
| 81af9388c7fb7f1a557c802069ab2f8cae1b441dc46e3755d98e10c825a672f4-spend-0 | 19.48 us | **11.30 us** | 18.02 us | 125.58 us | 33.39 us | 15.43 us | 2.35 ms | 75.67 us | 25.53 us | 30.45 us | 15.56 us | 138.80 us | 107.20 us | 39.01 ms |
| 81af9388c7fb7f1a557c802069ab2f8cae1b441dc46e3755d98e10c825a672f4-withdraw-0 | 395.59 us | 467.50 us | 525.01 us | 729.22 us | 311.06 us | **305.17 us** | 24.90 ms | 505.88 us | 467.23 us | 527.64 us | 402.26 us | 3.51 ms | 2.44 ms | 131.11 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-1 | 18.05 us | **3.79 us** | 14.04 us | 64.00 us | 33.59 us | 13.66 us | 1.79 ms | 43.29 us | 27.41 us | 26.91 us | 12.73 us | 130.70 us | 106.10 us | 23.76 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-2 | 5.12 us | **1.15 us** | 4.96 us | 34.45 us | 25.75 us | 5.21 us | 1.03 ms | 28.00 us | 10.68 us | 10.70 us | 4.81 us | 31.50 us | 32.40 us | 13.53 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-withdraw-0 | 399.66 us | **257.09 us** | 341.26 us | 748.81 us | 270.06 us | 379.55 us | 20.33 ms | 1.47 ms | 588.25 us | 578.59 us | 380.21 us | 2.15 ms | 2.39 ms | FAIL |
| 8864ea90e54f74150e7f58d4680e9b9a0959ace4d7048a942cd7a2adfb0a3e3d-spend-0 | 7.20 us | **2.64 us** | 8.52 us | 27.49 us | 18.34 us | 7.23 us | 978.17 us | 29.28 us | 12.82 us | 13.02 us | 7.49 us | 57.00 us | 47.00 us | 6.37 ms |
| 8864ea90e54f74150e7f58d4680e9b9a0959ace4d7048a942cd7a2adfb0a3e3d-withdraw-0 | 92.82 us | **37.52 us** | 96.24 us | 206.21 us | 72.97 us | 76.40 us | 5.17 ms | 241.35 us | 118.88 us | 138.85 us | 78.99 us | 690.70 us | 539.90 us | 46.90 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-spend-0 | 5.34 us | **1.26 us** | 4.84 us | 32.97 us | 28.37 us | 5.15 us | 1.03 ms | 25.98 us | 10.74 us | 10.67 us | 4.76 us | 36.90 us | 32.40 us | 14.02 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-spend-1 | 16.99 us | **3.49 us** | 14.09 us | 62.92 us | 32.77 us | 14.55 us | 1.92 ms | 44.69 us | 26.83 us | 27.81 us | 13.04 us | 112.90 us | 106.70 us | 25.68 ms |
| 89553182a5487bd6705877584384095e764058416d9561ebd6ae9b7701ed9b01-withdraw-0 | 391.31 us | **252.07 us** | 357.89 us | 778.47 us | 276.57 us | 361.59 us | 21.87 ms | 1.38 ms | 553.26 us | 595.98 us | 371.64 us | 2.39 ms | 2.40 ms | FAIL |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-spend-1 | 309.71 us | 316.42 us | 298.55 us | 699.37 us | **264.95 us** | 307.99 us | 16.55 ms | 852.04 us | 471.22 us | 469.90 us | 300.73 us | 1.93 ms | 1.94 ms | FAIL |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-spend-2 | 6.41 us | **1.46 us** | 5.52 us | 34.93 us | 24.73 us | 6.31 us | 920.80 us | 10.24 us | 10.99 us | 13.46 us | 5.49 us | 39.10 us | 40.10 us | 14.66 ms |
| 8d8b269e8998bbc54b0a770089ee9f36bf5a48eff7c1cdc7c92872b928c0d7c8-withdraw-0 | 9.34 us | **2.79 us** | 8.84 us | 23.50 us | 24.27 us | 8.63 us | 1.58 ms | 14.36 us | 16.67 us | 17.66 us | 8.57 us | 59.10 us | 61.10 us | 7.82 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-0 | 16.42 us | **3.50 us** | 13.86 us | 65.78 us | 53.16 us | 14.26 us | 2.41 ms | 43.88 us | 27.43 us | 27.10 us | 13.13 us | 107.60 us | 106.50 us | 27.40 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-1 | 16.88 us | **3.50 us** | 14.83 us | 65.19 us | 56.24 us | 14.05 us | 2.39 ms | 45.39 us | 26.12 us | 30.03 us | 13.07 us | 105.60 us | 106.10 us | 24.66 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-2 | 5.13 us | **1.22 us** | 4.57 us | 32.75 us | 40.87 us | 5.04 us | 1.92 ms | 29.31 us | 10.55 us | 10.32 us | 4.81 us | 32.30 us | 32.50 us | 14.31 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-spend-3 | 17.59 us | **3.50 us** | 14.48 us | 65.43 us | 48.99 us | 14.49 us | 2.72 ms | 48.49 us | 25.46 us | 26.98 us | 12.86 us | 109.70 us | 106.30 us | 24.62 ms |
| 90cb5b2794405aa739fd72c7d9807423a74d5c83bb94c6d22df53b473d7b0f9f-withdraw-0 | 948.38 us | **494.05 us** | 798.39 us | 1.62 ms | 584.36 us | 781.69 us | 53.69 ms | 3.54 ms | 1.29 ms | 1.65 ms | 914.41 us | 5.46 ms | 5.61 ms | FAIL |
| 9821e1defa09d0e9407e4ce6622ead240125df3df75fba63539c55afd841d6f8-spend-1 | 2.99 us | **402 ns** | 2.47 us | 11.38 us | 7.35 us | 3.20 us | 309.07 us | 21.45 us | 6.84 us | 6.12 us | 2.44 us | 15.70 us | 16.30 us | 2.03 ms |
| 9b456b77cfc279bd3d80822b553952720e452fddc05c47cac387f1d4f6da6700-spend-1 | 3.48 us | **429 ns** | 2.47 us | 11.18 us | 7.38 us | 3.30 us | 310.37 us | 22.05 us | 6.66 us | 6.06 us | 2.38 us | 15.30 us | 16.30 us | 2.19 ms |
| 9d61863e3a770cc83ec05bccd87b25c28eba22f423a0a63acbeea17fa23e5499-spend-0 | 19.76 us | **10.79 us** | 18.51 us | 133.11 us | 39.16 us | 17.00 us | 2.03 ms | 75.87 us | 27.20 us | 26.89 us | 15.76 us | 131.40 us | 107.30 us | 41.62 ms |
| 9d61863e3a770cc83ec05bccd87b25c28eba22f423a0a63acbeea17fa23e5499-withdraw-0 | 331.53 us | 326.03 us | 437.59 us | 614.64 us | **254.61 us** | 268.44 us | 16.50 ms | 424.14 us | 393.38 us | 430.85 us | 359.37 us | 2.35 ms | 2.06 ms | 121.52 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-spend-0 | 17.06 us | **3.46 us** | 14.26 us | 63.62 us | 32.38 us | 14.87 us | 1.78 ms | 42.95 us | 25.50 us | 29.77 us | 13.33 us | 112.30 us | 121.50 us | 24.20 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-spend-2 | 5.16 us | **1.22 us** | 4.46 us | 32.16 us | 28.14 us | 5.05 us | 1.13 ms | 25.67 us | 11.74 us | 10.74 us | 5.19 us | 33.90 us | 36.20 us | 13.51 ms |
| a640b437d8b74eb832e1eb42b537419ef29ae4a7f027781817810ab3891217cf-withdraw-0 | 414.33 us | 305.60 us | 354.38 us | 792.05 us | **264.86 us** | 379.76 us | 21.35 ms | 1.36 ms | 574.68 us | 575.17 us | 376.03 us | 2.42 ms | 2.73 ms | FAIL |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-0 | 5.60 us | **1.17 us** | 4.67 us | 33.69 us | 32.62 us | 5.19 us | 1.28 ms | 25.64 us | 9.99 us | 11.82 us | 4.79 us | 32.10 us | 36.00 us | 13.81 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-1 | 15.98 us | **3.47 us** | 14.04 us | 63.56 us | 36.64 us | 13.93 us | 1.90 ms | 42.69 us | 29.01 us | 27.11 us | 12.95 us | 103.40 us | 120.80 us | 24.21 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-spend-3 | 5.82 us | **1.17 us** | 4.68 us | 33.63 us | 30.15 us | 5.17 us | 1.22 ms | 25.56 us | 10.03 us | 10.37 us | 4.74 us | 32.70 us | 34.50 us | 13.60 ms |
| a9a1c75415a0b94d888b9de41a54e1937dfdccb3be31edf48b776d4832aa28b4-withdraw-0 | 502.37 us | **301.07 us** | 445.86 us | 947.94 us | 351.85 us | 495.18 us | 26.90 ms | 1.80 ms | 703.90 us | 799.66 us | 447.13 us | 3.11 ms | 3.79 ms | FAIL |
| b045c8789a4d7d250c7971e12d4bd0a7e423015e18489e91b1d42967c0c1aea6-spend-0 | 158.66 us | **36.88 us** | 142.56 us | 266.56 us | 80.52 us | 95.03 us | 6.31 ms | 193.17 us | 253.38 us | 205.78 us | 107.55 us | 900.70 us | 916.50 us | FAIL |
| beaa9d1683d7bdde24a920f2561b0b9dbe90b652c18b3e59154cfd222c5f696f-spend-1 | 50.80 us | **15.06 us** | 41.76 us | 89.14 us | 55.40 us | 40.33 us | 4.37 ms | 89.16 us | 75.06 us | 76.91 us | 45.28 us | 286.70 us | 365.90 us | 28.33 ms |
| beaa9d1683d7bdde24a920f2561b0b9dbe90b652c18b3e59154cfd222c5f696f-spend-3 | 108.51 us | **32.67 us** | 89.11 us | 194.45 us | 92.49 us | 78.88 us | 9.17 ms | 258.84 us | 135.21 us | 148.15 us | 87.44 us | 534.00 us | 645.40 us | 57.43 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-mint-0 | 26.26 us | **12.44 us** | 27.23 us | 119.59 us | 52.25 us | 24.53 us | 2.65 ms | 38.37 us | 39.40 us | 38.16 us | 21.75 us | 187.90 us | 171.90 us | 43.81 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-mint-1 | 92.19 us | **44.48 us** | 108.38 us | 247.44 us | 97.40 us | 84.48 us | 8.78 ms | 188.30 us | 139.54 us | 145.30 us | 78.57 us | 916.50 us | 630.20 us | 67.11 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-0 | 592.20 us | 1.38 ms | 638.67 us | 1.33 ms | **419.70 us** | 545.64 us | 45.05 ms | 1.19 ms | 839.31 us | 964.65 us | 547.27 us | 5.04 ms | 3.65 ms | FAIL |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-2 | 473.00 us | 935.82 us | 575.12 us | 1.22 ms | **376.56 us** | 492.20 us | 43.13 ms | 1.03 ms | 821.52 us | 760.19 us | 424.21 us | 4.18 ms | 3.13 ms | 263.74 ms |
| c02bca582fd48df4c2fa59247fccb5af4ae236e6e843c8e0a65988e03de16e31-spend-3 | 123.67 us | **58.10 us** | 135.29 us | 283.48 us | 120.74 us | 112.50 us | 12.63 ms | 322.06 us | 181.75 us | 176.76 us | 112.83 us | 895.40 us | 770.40 us | 70.75 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-0 | 5.12 us | **1.13 us** | 4.59 us | 34.69 us | 40.92 us | 5.09 us | 1.40 ms | 28.15 us | 10.49 us | 10.53 us | 4.89 us | 30.10 us | 32.30 us | 13.99 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-1 | 5.19 us | **1.29 us** | 4.69 us | 33.27 us | 43.63 us | 5.17 us | 1.47 ms | 28.28 us | 10.15 us | 10.58 us | 4.69 us | 30.70 us | 32.50 us | 13.76 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-2 | 15.93 us | **3.66 us** | 13.76 us | 64.16 us | 51.13 us | 15.09 us | 2.10 ms | 45.08 us | 26.36 us | 30.69 us | 12.92 us | 100.90 us | 116.40 us | 24.33 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-spend-4 | 5.55 us | **1.19 us** | 4.83 us | 32.50 us | 39.86 us | 5.18 us | 1.34 ms | 26.20 us | 10.59 us | 10.78 us | 4.81 us | 30.00 us | 33.50 us | 14.04 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-withdraw-0 | 581.81 us | **306.43 us** | 512.09 us | 1.12 ms | 390.04 us | 557.82 us | 33.02 ms | 1.93 ms | 892.34 us | 878.06 us | 535.39 us | 3.27 ms | 3.66 ms | FAIL |
| c6aa9ec93c2e4fe6396240b1fae8ed4a1e5960403af40ae1d52d0753beced05c-spend-2 | 77.74 us | **18.25 us** | 65.49 us | 127.30 us | 51.38 us | 51.85 us | 4.35 ms | 101.87 us | 105.49 us | 129.81 us | 55.01 us | 409.20 us | 413.20 us | 47.00 ms |
| c6aa9ec93c2e4fe6396240b1fae8ed4a1e5960403af40ae1d52d0753beced05c-spend-3 | 874.77 us | 1.52 ms | 753.23 us | 1.48 ms | **466.69 us** | 903.42 us | 23.01 ms | 1.37 ms | 1.57 ms | 1.62 ms | 703.55 us | 5.05 ms | 5.01 ms | FAIL |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-spend-2 | 23.61 us | **11.69 us** | 24.02 us | 133.81 us | 50.35 us | 17.70 us | 2.12 ms | 101.63 us | 29.50 us | 32.25 us | 18.79 us | 177.40 us | 129.70 us | 39.42 ms |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-withdraw-0 | 21.40 us | **9.49 us** | 19.79 us | 58.20 us | 32.86 us | 14.55 us | 2.11 ms | 108.83 us | 28.68 us | 32.24 us | 20.20 us | 151.60 us | 113.20 us | 14.62 ms |
| d07abba71f61a3da474a8559df90d5403498c99d3bad640e4e413e97adbf5f45-withdraw-1 | 350.93 us | 380.15 us | 484.77 us | 694.25 us | **278.12 us** | 294.04 us | 21.26 ms | 483.00 us | 432.83 us | 456.89 us | 377.75 us | 3.57 ms | 2.38 ms | 129.74 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-spend-0 | 16.06 us | **3.46 us** | 13.67 us | 62.95 us | 44.87 us | 15.26 us | 1.83 ms | 49.46 us | 28.02 us | 27.64 us | 12.91 us | 188.60 us | 118.50 us | 24.21 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-spend-1 | 5.35 us | **1.21 us** | 4.60 us | 33.40 us | 32.64 us | 5.13 us | 1.06 ms | 29.84 us | 10.24 us | 11.29 us | 4.97 us | 34.40 us | 37.40 us | 13.20 ms |
| dfcf1fe2a0bca423b0e7260a24922c0437785c894ecb27fef5587c2d4d5f1227-withdraw-0 | 412.14 us | 332.45 us | 356.94 us | 808.94 us | **283.96 us** | 353.94 us | 22.36 ms | 1.37 ms | 534.67 us | 596.12 us | 391.38 us | 2.53 ms | 2.42 ms | FAIL |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-0 | 5.71 us | **1.22 us** | 4.63 us | 33.41 us | 31.68 us | 5.77 us | 1.03 ms | 27.00 us | 10.81 us | 10.30 us | 4.77 us | 34.60 us | 32.30 us | 14.77 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-2 | 16.81 us | **3.49 us** | 14.27 us | 62.50 us | 39.02 us | 14.81 us | 1.71 ms | 45.63 us | 27.14 us | 30.08 us | 12.77 us | 110.20 us | 106.30 us | 28.03 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-withdraw-0 | 419.69 us | **255.97 us** | 342.08 us | 814.89 us | 272.29 us | 356.14 us | 21.36 ms | 1.40 ms | 538.64 us | 601.45 us | 361.06 us | 2.63 ms | 2.40 ms | FAIL |
| e2fbfa2be7dc3f978d4131f60a99085b888b8b7a2123d41400dc4697d6a84df7-spend-0 | 7.02 us | **1.81 us** | 5.87 us | 19.22 us | 27.59 us | 6.08 us | 1.13 ms | 11.06 us | 11.91 us | 12.85 us | 5.17 us | 42.80 us | 40.30 us | 5.92 ms |
| e2fbfa2be7dc3f978d4131f60a99085b888b8b7a2123d41400dc4697d6a84df7-spend-1 | 271.41 us | 449.08 us | 246.07 us | 559.23 us | **192.87 us** | 267.03 us | 11.97 ms | 1.23 ms | 385.50 us | 439.78 us | 231.00 us | 1.74 ms | 1.69 ms | FAIL |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-0 | 5.97 us | **1.45 us** | 5.56 us | 34.49 us | 30.02 us | 6.09 us | 929.98 us | 10.33 us | 11.23 us | 11.56 us | 5.59 us | 39.50 us | 40.00 us | 15.12 ms |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-2 | 317.82 us | 368.44 us | 304.61 us | 707.02 us | **250.71 us** | 313.96 us | 16.75 ms | 878.88 us | 491.00 us | 499.56 us | 298.33 us | 1.92 ms | 1.94 ms | FAIL |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-withdraw-0 | 9.62 us | **2.52 us** | 9.02 us | 22.79 us | 30.77 us | 8.29 us | 1.57 ms | 15.48 us | 15.56 us | 17.41 us | 8.62 us | 58.70 us | 61.00 us | 6.82 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-spend-1 | 16.12 us | **3.52 us** | 13.84 us | 63.86 us | 40.74 us | 16.65 us | 1.76 ms | 48.14 us | 27.24 us | 27.80 us | 13.44 us | 105.00 us | 106.40 us | 23.90 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-spend-2 | 5.47 us | **1.18 us** | 4.58 us | 33.55 us | 33.62 us | 5.52 us | 1.00 ms | 28.16 us | 10.66 us | 11.77 us | 4.90 us | 33.50 us | 32.50 us | 13.59 ms |
| f72cc6d135256d2dcb98b13d5ea222ca234bdae2b3540e446e1331cc50660edd-withdraw-0 | 402.19 us | **280.67 us** | 359.46 us | 785.65 us | 297.67 us | 352.14 us | 23.64 ms | 1.34 ms | 543.96 us | 576.41 us | 356.10 us | 2.47 ms | 2.40 ms | FAIL |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*