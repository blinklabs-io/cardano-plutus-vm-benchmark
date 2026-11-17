# Cardano Plutus VM Benchmark Results

**Date:** 2026-11-15

**Corpus:** Mainnet validators (`mainnet_recent`): 100 of 1360 programs, selected with seed 1. The per-script tables list every program measured.

## Environment
```
date: 2026-11-15T20:23:08+00:00
kernel: 6.8.0-147-generic
cpu: Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (x86_64)
cores: 8
memory: 15Gi
corpus: mainnet_recent (100 of 1360 programs, sample 100, seed 1; list in corpus.txt)
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

### Per transaction (geometric mean of 7 transaction totals)

*Each VM's time for a transaction is the sum of its times for every script the transaction runs. A VM that fails any script fails the transaction, which is assigned the slowest competitor's total.*

| VM | Language | Geo Mean | vs Fastest | Failed transactions |
|---|---|---|---|---|
| **Amaru UPLC CEK (Rust)** | Rust | 41.07 us | 1.00x | 0 |
| **Plutigo CEK (Go)** | Go | 44.09 us | 1.07x | 0 |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 50.56 us | 1.23x | 0 |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 62.51 us | 1.52x | 0 |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 63.26 us | 1.54x | 0 |
| **Plutuz CEK (Zig)** | Zig | 100.05 us | 2.44x | 0 |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 121.30 us | 2.95x | 0 |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 208.52 us | 5.08x | 0 |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 258.90 us | 6.30x | 0 |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 3.03 ms | 73.81x | 0 |
| **opshin CEK (Python / CPython)** | Python / CPython | 10.22 ms | 248.80x | 1 |

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Amaru UPLC CEK (Rust)** | Rust | 164.66 us | 1.00x |
| **Plutigo CEK (Go)** | Go | 173.21 us | 1.05x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 207.31 us | 1.26x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 252.38 us | 1.53x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 256.26 us | 1.56x |
| **Plutuz CEK (Zig)** | Zig | 348.65 us | 2.12x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 591.95 us | 3.59x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 781.21 us | 4.74x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 873.05 us | 5.30x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 7.19 ms | 43.66x |
| **opshin CEK (Python / CPython)** | Python / CPython | 45.36 ms | 275.46x |

#### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| Amaru UPLC CEK (Rust) | 100 | 0 | 0 | 100 |
| Plutigo CEK (Go) | 100 | 0 | 0 | 100 |
| Scalus CEK (Scala / JVM) | 100 | 0 | 0 | 100 |
| Chrysalis CEK (C# / .NET) | 100 | 0 | 0 | 100 |
| Chrysalis CEK (C# / .NET AOT) | 100 | 0 | 0 | 100 |
| Plutuz CEK (Zig) | 100 | 0 | 0 | 100 |
| plutus-core CEK (Haskell / GHC) | 100 | 0 | 0 | 100 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 100 | 0 | 0 | 100 |
| blaze-plutus CEK (TypeScript / Node V8) | 100 | 0 | 0 | 100 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | 99 | 1 | 0 | 100 |
| opshin CEK (Python / CPython) | 81 | 19 | 0 | 100 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus CEK (Scala / JVM) | Amaru UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 047e5557ea893da60b93eacdae74d968f02c7a9999b826ae2eb6c32978b1b345-withdraw-1 | 1.81 ms | 1.24 ms | **808.14 us** | 45.37 ms | 1.33 ms | 1.26 ms | 1.28 ms | 1.01 ms | 5.56 ms | 6.06 ms | 267.59 ms |
| 06f57a9565ecadf00e2266ee8731a6378bbb07f9a4712a84809cd8a3bba3c969-spend-1 | 971.68 us | 280.04 us | 209.92 us | 5.98 ms | 440.36 us | 334.88 us | 331.71 us | **195.69 us** | 874.60 us | 955.60 us | 102.31 ms |
| 06f57a9565ecadf00e2266ee8731a6378bbb07f9a4712a84809cd8a3bba3c969-withdraw-0 | 2.27 ms | 1.70 ms | **1.06 ms** | 66.55 ms | 1.73 ms | 1.85 ms | 1.94 ms | 1.35 ms | 7.66 ms | 8.14 ms | 362.07 ms |
| 072c3053e18a3836dc90c3102c4e873a0c0048b5858ec6562f224c4aa4c8f564-spend-1 | 35.52 us | 14.39 us | **12.28 us** | 588.93 us | 30.16 us | 16.23 us | 14.96 us | 13.98 us | 48.60 us | 56.20 us | 3.47 ms |
| 07344c69689c3605f1f3982fb4b7a4506b468575b9dabf7efff7d9c9e082825c-withdraw-0 | 94.65 us | 41.16 us | **31.58 us** | 2.45 ms | 37.83 us | 46.45 us | 48.56 us | 39.98 us | 151.90 us | 171.70 us | 11.39 ms |
| 079e30993837608b034924c42cc4694d711695478824120c2b507885e0f3b79a-spend-3 | 767.26 us | 403.83 us | 325.75 us | 22.15 ms | 570.66 us | 567.09 us | 654.34 us | **321.38 us** | 2.09 ms | 2.24 ms | 205.38 ms |
| 0ce281ddc2701e852214823cf7f04ff8f49af9924e69034e8bfe371765c7f3ff-spend-0 | 1.44 ms | 614.67 us | **494.65 us** | 23.09 ms | 1.59 ms | 924.05 us | 932.93 us | 567.30 us | 3.07 ms | 3.20 ms | FAIL |
| 0e73f4aa816cfce02db01ee04f2017230752556a0e54ac6501945ac0e9dd4080-spend-2 | 500.00 us | 164.02 us | **114.92 us** | 3.99 ms | 208.02 us | 164.02 us | 165.14 us | 115.91 us | 485.70 us | 492.40 us | 50.00 ms |
| 0e73f4aa816cfce02db01ee04f2017230752556a0e54ac6501945ac0e9dd4080-withdraw-0 | 3.24 ms | 1.04 ms | **953.70 us** | 44.13 ms | 2.96 ms | 1.51 ms | 1.56 ms | 1.08 ms | 5.46 ms | 6.02 ms | FAIL |
| 0fc112573cf010b19921588bbc2b86a62e66b980e891ef482fd3e310c6d4ace8-spend-0 | 35.15 us | 14.14 us | **11.50 us** | 574.91 us | 32.22 us | 15.52 us | 15.87 us | 13.12 us | 46.50 us | 56.60 us | 3.40 ms |
| 1034704a8ddfc80084f53865c8c18aaaec96c81c6ce99002cb09934ad154d540-spend-2 | 2.99 ms | 885.06 us | **753.14 us** | 28.75 ms | 1.95 ms | 1.15 ms | 1.15 ms | 877.50 us | 3.75 ms | 4.24 ms | FAIL |
| 10ac955d64a7d3c096abb2dcc35062c3db04313b146086d996949f6c1c3eb47a-spend-0 | 1.01 ms | 263.98 us | 207.96 us | 5.41 ms | 440.05 us | 353.40 us | 322.01 us | **191.20 us** | 838.40 us | 902.90 us | 89.72 ms |
| 10ac955d64a7d3c096abb2dcc35062c3db04313b146086d996949f6c1c3eb47a-spend-1 | 952.70 us | 244.15 us | 206.35 us | 5.05 ms | 432.00 us | 325.24 us | 351.66 us | **190.97 us** | 821.90 us | 881.10 us | 93.30 ms |
| 1159c40949b99180499b71e05d29832955bafcdbb771c5dce4362c524ef501e8-withdraw-0 | 1.43 ms | 735.39 us | **488.96 us** | 24.53 ms | 831.52 us | 887.74 us | 810.16 us | 587.60 us | 2.83 ms | 3.31 ms | 180.98 ms |
| 15150e241b9f8a6d66750f5ab484069cb38becd38d1676f3cb3afae0c20a102b-spend-3 | 2.34 ms | 851.17 us | **731.86 us** | 24.85 ms | 2.77 ms | 1.23 ms | 1.17 ms | 743.11 us | 3.89 ms | 4.58 ms | FAIL |
| 1848fc0540637f76d0817f6669f53814bfe9148393f6bae94353f352a9cd9789-spend-1 | 253.97 us | 91.01 us | 92.64 us | 4.96 ms | 159.60 us | 132.46 us | 141.69 us | **90.66 us** | 471.10 us | 547.90 us | 41.10 ms |
| 1c2421ab522d18477812623c61a8e2d0f091c12e90435d783b99f8a707254e2b-spend-1 | 2.79 ms | 1.13 ms | 1.07 ms | 28.04 ms | 1.85 ms | 2.16 ms | 2.13 ms | **885.12 us** | 5.58 ms | 6.96 ms | FAIL |
| 1dd2a4ec66cbe49f57f742a34343288a1b2d9820341398008dff1727d47babe2-spend-1 | 1.88 ms | 591.86 us | 489.30 us | 15.33 ms | 1.75 ms | 848.98 us | 844.28 us | **472.38 us** | 2.48 ms | 3.19 ms | FAIL |
| 230b7b9efeeb173c4781b0d06ae5b07b934ad35e54382b40b3bbb8d951418119-spend-0 | 488.65 us | 162.97 us | **111.01 us** | 3.95 ms | 215.45 us | 166.11 us | 161.81 us | 111.99 us | 502.20 us | 551.10 us | 57.13 ms |
| 230b7b9efeeb173c4781b0d06ae5b07b934ad35e54382b40b3bbb8d951418119-spend-1 | 322.42 us | 91.30 us | **80.11 us** | 2.93 ms | 153.19 us | 105.39 us | 110.59 us | 88.91 us | 306.50 us | 369.30 us | 36.42 ms |
| 2752d5588fea3ad912fdcf2bb2fd6d208af2f168d3350656025788ff4fca7980-withdraw-0 | 101.72 us | 40.81 us | **31.41 us** | 2.29 ms | 42.28 us | 43.54 us | 44.03 us | 40.98 us | 142.00 us | 188.60 us | 11.41 ms |
| 2907afb1be082bc589464799734a4a052fcf756e4b04f1c181143c40550c1492-spend-0 | 487.61 us | 152.16 us | **111.72 us** | 3.67 ms | 225.85 us | 169.90 us | 187.71 us | 113.30 us | 471.50 us | 549.90 us | 52.50 ms |
| 2dffd33731beaa8ef42626a0ff6bb7bfd1bdb48fea25866ac12c887c074a5846-spend-1 | 251.90 us | 95.76 us | **89.20 us** | 4.90 ms | 164.84 us | 128.24 us | 149.86 us | 91.70 us | 464.70 us | 552.30 us | 38.39 ms |
| 2dffd33731beaa8ef42626a0ff6bb7bfd1bdb48fea25866ac12c887c074a5846-spend-2 | 420.37 us | 168.09 us | **155.52 us** | 9.82 ms | 358.90 us | 242.95 us | 232.72 us | 166.40 us | 814.50 us | 923.80 us | 67.57 ms |
| 2e0a7798f4a69ae3254bd19b4d21d4764e27b28bc179976c3940ad0bc7b98a95-withdraw-0 | 1.81 ms | 1.24 ms | **770.32 us** | 46.08 ms | 1.25 ms | 1.41 ms | 1.38 ms | 995.73 us | 5.40 ms | 6.34 ms | 279.48 ms |
| 2e17be2eb5967cc2b6f6d2773f27b78bd3edf0d30be26324a27ffbed408d5a41-spend-1 | 500.39 us | 188.21 us | **143.07 us** | 7.32 ms | 564.72 us | 214.83 us | 224.67 us | 149.76 us | 660.20 us | 720.70 us | 67.96 ms |
| 3a542d9004cd5c3d4d3c3f4408272e3331c87e158215ddb88ce9e5b6486babe3-spend-2 | 287.72 us | 82.78 us | **68.15 us** | 2.08 ms | 109.81 us | 93.87 us | 101.03 us | 68.83 us | 269.90 us | 295.40 us | 30.09 ms |
| 3b2f7288f98004fdfdf6389310d2bb54b81b56cd94616cde00121e50aab96e97-spend-0 | 749.88 us | 283.08 us | **220.50 us** | 9.63 ms | 434.61 us | 425.71 us | 441.03 us | 233.16 us | 1.41 ms | 1.53 ms | FAIL |
| 471b6c63a1b1bfb8312bb6fd9be4e254d575388ecd136879a3b60e23592d42fa-spend-3 | 682.37 us | 313.88 us | 260.14 us | 21.84 ms | 583.66 us | 479.47 us | 449.07 us | **257.73 us** | 1.48 ms | 1.65 ms | 114.61 ms |
| 497181b5f3b60e0c61ecd13e6502fe6ca298a68964e8f3944f603e127c469950-spend-0 | 322.67 us | 88.28 us | 76.44 us | 2.25 ms | 142.05 us | 93.43 us | 105.25 us | **74.70 us** | 280.70 us | 306.90 us | 30.83 ms |
| 4a450a9411b8a231de6ebec5ecfa2fcce57c1baac2ab5fd35e1fc5126341cc38-withdraw-0 | 2.85 ms | 791.16 us | **666.59 us** | 27.57 ms | 1.91 ms | 1.04 ms | 1.16 ms | 823.60 us | 3.39 ms | 4.06 ms | FAIL |
| 4bcb056620920316cb3c5cdb29e2530ae4c386eef466031ec18dec6c5ed1af6f-spend-1 | 475.34 us | 154.95 us | 111.44 us | 3.80 ms | 203.36 us | 160.58 us | 153.94 us | **109.18 us** | 500.20 us | 490.50 us | 48.58 ms |
| 4c553752cc3e282666db7cb2f1a8438d16dc60f23610f37e8da101a24f4521da-spend-3 | 1.00 ms | 256.73 us | 203.97 us | 4.47 ms | 418.50 us | 333.95 us | 367.69 us | **200.53 us** | 823.90 us | 857.40 us | 89.35 ms |
| 4d23634065b3fecb5c74891a75e57fbf5947338bd105687619c4b45855aa0f53-spend-1 | 501.64 us | 140.25 us | 105.87 us | 3.33 ms | 220.36 us | 147.17 us | 156.22 us | **104.33 us** | 458.90 us | 485.10 us | 48.70 ms |
| 4dacfe58b35ba66eaf2de7430e1ca1c4a0ef39c03a7f8ec2db6b6b60a6731ea3-spend-1 | 34.77 us | 14.38 us | **11.80 us** | 599.09 us | 30.85 us | 16.66 us | 15.60 us | 13.37 us | 43.00 us | 58.40 us | 3.67 ms |
| 54a2d1a5ab31f91974caee9eae3176ac0cf9daba5b8353bad694d085912b2772-spend-1 | 1.05 ms | 266.40 us | 217.40 us | 5.03 ms | 443.43 us | 341.04 us | 328.08 us | **194.30 us** | 852.60 us | 899.60 us | 97.00 ms |
| 560701f9620127953f66111eb5a43ccc711f7b8f87c826de4d0f12580f2c48e9-spend-0 | 307.99 us | 84.56 us | **71.75 us** | 2.27 ms | 143.30 us | 93.84 us | 96.98 us | 74.45 us | 289.30 us | 314.90 us | 32.58 ms |
| 5845e6241e910e18ecae0c23027081dba0edd2847b3732a4ff0bad9fd23e6af2-spend-0 | 311.48 us | 86.24 us | **72.05 us** | 2.27 ms | 141.88 us | 95.93 us | 98.17 us | 75.34 us | 274.10 us | 313.80 us | 32.13 ms |
| 62a11be50630f9c16da5aee0fae00b26dfdb450f6bdb0edf5fe249cb9b7374ae-withdraw-0 | 97.71 us | 41.51 us | **32.16 us** | 2.40 ms | 38.22 us | 44.53 us | 47.73 us | 38.19 us | 145.90 us | 189.90 us | 10.33 ms |
| 68a7ddeaa226d87325597b4f34d811f855a232178c98681d06e2b809937fa1c5-withdraw-0 | 1.44 ms | 757.27 us | **548.37 us** | 26.23 ms | 851.34 us | 869.62 us | 933.99 us | 609.30 us | 2.99 ms | 3.36 ms | 179.56 ms |
| 690a110a059712200fd3b71780c0d3dcbf58115f7602e82e488f6edf156ce9cc-spend-1 | 477.28 us | 152.95 us | 113.86 us | 3.71 ms | 218.71 us | 155.22 us | 164.24 us | **110.06 us** | 479.70 us | 540.50 us | 52.22 ms |
| 6963136c3eaf099e6103aa509053976631f8fb4d13be9f2da9e8c700f9b3a8ed-spend-2 | 317.69 us | 85.12 us | 74.14 us | 2.48 ms | 142.56 us | 100.58 us | 101.23 us | **73.74 us** | 278.30 us | 318.90 us | 33.62 ms |
| 69cb271e66fba6d994954678f84a8d3d8f55ce704cea1a8a2ed799d3272d9274-spend-0 | 505.39 us | 158.34 us | 121.32 us | 4.60 ms | 219.11 us | 168.83 us | 181.13 us | **115.23 us** | 494.40 us | 566.10 us | 54.30 ms |
| 69cb271e66fba6d994954678f84a8d3d8f55ce704cea1a8a2ed799d3272d9274-withdraw-0 | 3.73 ms | 1.31 ms | **1.14 ms** | 63.10 ms | 4.15 ms | 1.92 ms | 1.97 ms | 1.35 ms | 6.68 ms | 8.39 ms | FAIL |
| 6d9a5b869c864ed6aa21dad15406bbdbedb7711cab091ddf441a3312a4861b8c-spend-1 | 436.15 us | 179.40 us | **137.03 us** | 8.73 ms | 239.90 us | 239.99 us | 238.32 us | 139.93 us | 735.50 us | 851.60 us | 80.55 ms |
| 6d9a5b869c864ed6aa21dad15406bbdbedb7711cab091ddf441a3312a4861b8c-spend-3 | 422.07 us | 173.18 us | 133.34 us | 8.22 ms | 226.91 us | 233.81 us | 249.07 us | **131.49 us** | 687.00 us | 772.00 us | 76.15 ms |
| 6ed6dcefd6e92655097bf8fb2347e8c47214c72f6b4faf0327fd7626faf1d1c4-spend-2 | 2.90 ms | 881.17 us | **771.44 us** | 28.91 ms | 1.77 ms | 1.23 ms | 1.12 ms | 874.93 us | 3.46 ms | 4.14 ms | FAIL |
| 72d37d64464ade67a7e9ebfde460ace13ab334ead86cb7af42f9090fa5fbad95-spend-0 | 1.99 ms | 617.03 us | 495.50 us | 15.52 ms | 1.82 ms | 774.45 us | 866.82 us | **486.43 us** | 2.48 ms | 3.04 ms | FAIL |
| 75d066eeed445cc5000cadfaad96c28e0ba1fc8672ab592b193004ef7d5c8dcc-withdraw-0 | 3.31 ms | 1.09 ms | **895.48 us** | 44.35 ms | 3.12 ms | 1.65 ms | 1.63 ms | 1.09 ms | 5.16 ms | 5.79 ms | FAIL |
| 7683618ee491a7777a311974e047fa4b230d4ad3c5b83e07ede5a1ae91b9e568-withdraw-0 | 3.77 ms | 1.34 ms | **1.15 ms** | 61.15 ms | 4.16 ms | 2.08 ms | 2.00 ms | 1.30 ms | 6.61 ms | 8.05 ms | FAIL |
| 79ac5cc3cf75ece0b184373a68de4f2d716a1fe7c281e903514227964d7c9bdc-spend-4 | 513.81 us | 160.80 us | 118.94 us | 4.15 ms | 210.89 us | 198.82 us | 184.19 us | **116.63 us** | 499.70 us | 557.20 us | 50.79 ms |
| 809c08cf6c9252fd23e2066083c4036e44b4590a6794cda47055d7d2cd48fbe2-mint-0 | 624.15 us | 300.37 us | **233.05 us** | 14.17 ms | 1.99 ms | 421.62 us | 467.10 us | 276.03 us | 1.43 ms | 1.60 ms | 118.92 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-2 | 307.05 us | 85.95 us | **72.29 us** | 2.25 ms | 141.02 us | 100.05 us | 99.43 us | 73.12 us | 275.60 us | 313.60 us | 32.91 ms |
| 88aa412ef12341d0409925f1cb2310b7e59747b3ef3976424b30827d804e0652-withdraw-0 | 3.07 ms | 1.07 ms | **936.64 us** | 44.77 ms | 3.09 ms | 1.46 ms | 1.49 ms | 1.06 ms | 5.01 ms | 5.57 ms | FAIL |
| 8c308609194bf1928b5efa6622877653052cdd956fee57d34f787f370a2190db-spend-2 | 1.04 ms | 256.20 us | 226.63 us | 4.33 ms | 416.49 us | 324.25 us | 318.68 us | **192.37 us** | 794.60 us | 802.10 us | 97.83 ms |
| 8e1e87b906ef58aa1a19d19d53af2dccbf50830a14a799e56db7b113faa6651f-spend-4 | 511.67 us | 161.53 us | **113.15 us** | 4.47 ms | 209.52 us | 176.15 us | 173.63 us | 117.38 us | 495.50 us | 531.80 us | 55.56 ms |
| 8e4034e230b1771a025fb19c04d9b1df9478695c8049b8398e2ad07df02d5b00-spend-0 | 430.74 us | 176.89 us | **140.34 us** | 10.49 ms | 317.32 us | 242.64 us | 263.11 us | 153.42 us | 771.50 us | 871.50 us | 73.46 ms |
| 922edd6dbcd8d576893c0727e4c9ca0e96fda0b4fd52fcad88eafdfd91fb257c-spend-3 | 427.03 us | 163.19 us | 129.57 us | 7.94 ms | 249.18 us | 256.36 us | 230.00 us | **124.02 us** | 670.60 us | 742.00 us | 81.20 ms |
| 9896cb365fe3d1dd2e9a5cdc96bbccc51222d95e2d410793d68d6268f0466ad4-spend-4 | 325.18 us | 97.48 us | **82.13 us** | 2.85 ms | 159.69 us | 114.53 us | 118.54 us | 89.72 us | 298.90 us | 340.50 us | 36.47 ms |
| 9aa13e8788545578baaa2791bc71f649ed21ce38f325d7c5fea2b49f97166fa7-spend-1 | 580.03 us | 298.82 us | **236.53 us** | 13.67 ms | 1.92 ms | 395.81 us | 409.92 us | 264.07 us | 1.41 ms | 1.76 ms | 119.04 ms |
| 9b8c6b62b2d447b5ed835a735d2799c71f4f86e01ded7ab516df9424f85fa5c5-spend-0 | 531.70 us | 161.18 us | **114.46 us** | 4.31 ms | 225.71 us | 169.97 us | 171.02 us | 119.17 us | 487.50 us | 542.30 us | 53.32 ms |
| 9b8c6b62b2d447b5ed835a735d2799c71f4f86e01ded7ab516df9424f85fa5c5-spend-2 | 495.83 us | 158.28 us | 120.65 us | 4.41 ms | 226.78 us | 183.21 us | 172.68 us | **117.79 us** | 476.00 us | 528.90 us | 53.26 ms |
| 9d98eef7dbdbba6806c447cd2a67e71e6e0db4ae865084bc67773747c91994a2-spend-1 | 506.31 us | 163.22 us | 124.84 us | 4.47 ms | 223.01 us | 171.03 us | 168.48 us | **118.02 us** | 537.90 us | 532.00 us | 55.61 ms |
| 9f32ed141264497b49cb6b0d8439d6f1796d4230617635b70fdebcf4b527fa29-spend-2 | 307.44 us | 85.49 us | **72.61 us** | 2.28 ms | 137.54 us | 105.60 us | 95.93 us | 73.66 us | 279.30 us | 294.50 us | 34.28 ms |
| a65bbdb06c3b71ae94d40fd6dc96e8514deff4b9f466c2aa0f7e44664cfd2aa1-spend-0 | 431.93 us | 165.07 us | 129.05 us | 8.31 ms | 226.87 us | 224.16 us | 234.45 us | **121.52 us** | 730.90 us | 754.90 us | 82.44 ms |
| a6658babea9de7ebec38b42508123fa6a3843ce2d8fcdb9d7f5c2cb0ee4dcf86-spend-1 | 960.11 us | 250.87 us | 219.86 us | 4.16 ms | 415.69 us | 320.89 us | 325.17 us | **189.03 us** | 811.20 us | 770.10 us | 97.49 ms |
| a8db0a9dcc191b286c4239a02d57d3da8f91275bfa4f63a371746544cf6ed468-spend-2 | 324.21 us | 84.50 us | **73.60 us** | 2.20 ms | 143.13 us | 108.15 us | 98.48 us | 75.96 us | 309.50 us | 304.90 us | 31.97 ms |
| ad58ac07171001d52d275804de74c2690ab8bb9897234c90621a2e60f4d557b4-spend-0 | 501.51 us | 268.82 us | 179.60 us | 145.01 ms | 444.76 us | 352.55 us | 400.69 us | **159.58 us** | 2.10 ms | 3.26 ms | 73.54 ms |
| af93bf199959ef3a1b8f895f260ad44c71d7bcfe01505908f5e965444d6516c1-withdraw-0 | 1.36 ms | 695.18 us | **473.84 us** | 21.47 ms | 751.31 us | 737.93 us | 764.97 us | 556.36 us | 2.86 ms | 2.91 ms | 169.51 ms |
| b38ebc7a31238291e5910091d9cc22ae289aedcd1fe66d78b21f2947d4a4e8ec-spend-1 | 337.31 us | 97.40 us | **83.81 us** | 2.83 ms | 157.67 us | 101.97 us | 106.68 us | 85.93 us | 315.10 us | 341.90 us | 32.50 ms |
| b3a00c89128d5c56d0b17a220dc9666eaaa5e9314d4d662edabace8b246f1e48-spend-3 | 474.16 us | 156.56 us | **109.17 us** | 4.00 ms | 211.37 us | 160.24 us | 156.12 us | 109.44 us | 506.10 us | 496.70 us | 50.08 ms |
| b757904e72bd72e242e07a5e90ee0a58ae8f13277a569ec3e915b43f0373e7db-spend-2 | 201.73 us | 63.58 us | **53.94 us** | 3.00 ms | 112.48 us | 70.97 us | 68.97 us | 57.48 us | 223.60 us | 224.90 us | 18.71 ms |
| b8bfc4091553667248cd4fd998f49252d92f8af25d91a435e513edb07501b77e-mint-1 | 735.64 us | 354.20 us | **276.22 us** | 19.34 ms | 596.16 us | 436.56 us | 490.31 us | 290.74 us | 1.60 ms | 1.81 ms | 130.35 ms |
| b9d42b4b35e08f02aeba3cdcd4ca030c9a72a3ce6d07bb0d2816ecf38d905f9a-spend-0 | 2.33 ms | 756.92 us | **644.65 us** | 23.65 ms | 1.29 ms | 1.07 ms | 1.10 ms | 785.11 us | 3.09 ms | 3.58 ms | FAIL |
| b9d42b4b35e08f02aeba3cdcd4ca030c9a72a3ce6d07bb0d2816ecf38d905f9a-withdraw-0 | 98.35 us | 45.70 us | **32.09 us** | 2.62 ms | 39.35 us | 46.55 us | 48.58 us | 41.19 us | 159.40 us | 199.50 us | 11.70 ms |
| bc1918acaa783a69e12a7b047f1f29931460d6a28287eab5daa60500c345ddd7-spend-2 | 494.18 us | 153.20 us | **108.42 us** | 4.02 ms | 204.32 us | 150.21 us | 156.59 us | 112.70 us | 476.90 us | 581.50 us | 52.90 ms |
| be367eee297b5777e927ad74663c851a1f7d0e403de2d2480a11a47292e7a908-spend-2 | 512.18 us | 159.28 us | 124.91 us | 4.53 ms | 208.58 us | 162.70 us | 167.62 us | **114.47 us** | 507.40 us | 581.80 us | 52.15 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-withdraw-0 | 3.14 ms | 1.00 ms | **927.65 us** | 40.45 ms | 2.57 ms | 1.55 ms | 1.43 ms | 987.48 us | 4.63 ms | 5.50 ms | FAIL |
| c1188f93e914427fd3969efdab1160f1bdb991ed8394c79f127422347fbc1d37-spend-1 | 2.75 ms | 789.22 us | **606.41 us** | 22.00 ms | 1.49 ms | 918.45 us | 986.54 us | 724.05 us | 2.89 ms | 3.54 ms | FAIL |
| c6a1d6630c9c487df70be2ebd8d12b58162e3361b5efda6e6479a4db0f438751-spend-0 | 426.27 us | 167.50 us | 133.31 us | 7.97 ms | 231.51 us | 234.67 us | 212.38 us | **124.18 us** | 720.10 us | 793.00 us | 74.91 ms |
| c8959fc0f2ed80a9e3ef5cd9cc8b65853d6b98e6828fc4128a2c4b9baf917cc3-spend-4 | 300.64 us | 91.47 us | **75.90 us** | 2.52 ms | 114.78 us | 105.77 us | 102.72 us | 79.86 us | 284.60 us | 346.20 us | 30.97 ms |
| ca385cdf7753a005abb51173e66b13727ed635085bdd317f2fa789529e5754da-spend-2 | 437.50 us | 175.71 us | 136.77 us | 8.06 ms | 238.23 us | 242.05 us | 247.48 us | **135.74 us** | 759.60 us | 864.10 us | 84.59 ms |
| d1492333495135ab87d4034d7f3e56bac21928a71184ba79f61d1c4133f298a8-spend-1 | 486.35 us | 157.18 us | 111.25 us | 3.88 ms | 204.87 us | 151.56 us | 162.20 us | **107.94 us** | 471.80 us | 500.20 us | 53.76 ms |
| d37c44fb509c06b85216974bd213fb50f9301cc5b102d1506a723becf8bdacc5-spend-1 | 293.36 us | 82.44 us | 70.85 us | 2.11 ms | 109.08 us | 96.23 us | 95.06 us | **67.83 us** | 263.30 us | 296.30 us | 30.96 ms |
| d5017a6865dd289ec514cde490cfdfcd4862b812cc7562c44e50aa6adc194132-spend-0 | 449.33 us | 166.96 us | **152.79 us** | 8.96 ms | 310.04 us | 230.34 us | 245.13 us | 164.23 us | 898.00 us | 872.50 us | 66.13 ms |
| d6247cf553324b42cd302baae91f44fbcd9342f1d6988ba5214bb01358d63d50-withdraw-0 | 95.59 us | 41.67 us | **30.92 us** | 2.52 ms | 41.12 us | 46.45 us | 44.31 us | 40.73 us | 149.60 us | 186.80 us | 10.37 ms |
| d62df55b9d15e7ede962934a652d465cb21fbfd7419c28c8c025065fb49a95c7-withdraw-3 | 640.34 us | 312.98 us | **231.29 us** | FAIL | 532.29 us | 396.16 us | 413.48 us | 266.39 us | 1.33 ms | 1.41 ms | 94.15 ms |
| d829b5969ae5e397d13c7610a14834af24204d147c02d86b101de3406d231399-spend-4 | 498.30 us | 178.94 us | **144.93 us** | 7.47 ms | 583.01 us | 206.94 us | 219.53 us | 155.18 us | 628.50 us | 706.20 us | 63.21 ms |
| db7cc24da3b8bbfc5444bc85d883695e64cfd6966389db30eb5dc2a21076ee34-spend-0 | 2.88 ms | 775.42 us | **633.28 us** | 21.07 ms | 1.43 ms | 910.10 us | 943.22 us | 756.79 us | 2.92 ms | 3.42 ms | FAIL |
| dbe943750b032ce13040794ee67cb72d1c6e7a4c9f96cf804d6d13ab7f4f4cb9-withdraw-0 | 250.00 us | 72.43 us | **64.86 us** | 2.78 ms | 183.84 us | 105.35 us | 100.23 us | 70.98 us | 314.40 us | 326.00 us | 25.80 ms |
| dd64226d4315c5cbe19e2dd00557f0dff8ca7d492ddbe471f2d718067f421e2c-spend-2 | 462.83 us | 142.40 us | 103.37 us | 3.22 ms | 207.08 us | 148.64 us | 154.84 us | **100.43 us** | 478.50 us | 492.00 us | 53.04 ms |
| debe3afe9219b37e6f9580a4fc5354eeca5e60aa615e65fb8d9f0f2db1a9717d-spend-2 | 323.62 us | 95.36 us | 84.37 us | 3.01 ms | 159.08 us | 106.48 us | 102.17 us | **83.60 us** | 318.80 us | 336.90 us | 33.98 ms |
| e01b1d0b6c246b2897b1b75f422129518b0ade56cbf6b16a242e8932807b3ae1-spend-0 | 35.21 us | 14.38 us | **12.20 us** | 564.08 us | 33.06 us | 15.96 us | 16.17 us | 13.75 us | 46.70 us | 56.80 us | 3.58 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-2 | 465.96 us | 141.71 us | 102.97 us | 3.30 ms | 212.59 us | 150.09 us | 149.85 us | **102.04 us** | 507.50 us | 462.80 us | 54.00 ms |
| e0f2686ab18a9b21e8f04ea34df1bafe5dedea2150f6d27451f7bd52e5cde9c7-spend-1 | 980.63 us | 271.63 us | 211.88 us | 5.22 ms | 432.28 us | 313.83 us | 323.09 us | **201.47 us** | 896.20 us | 857.00 us | 102.07 ms |
| e102429d660fc75b02be2a16d00b83a70e94a79da562d65f0f9175f76709d74c-spend-1 | 471.39 us | 153.00 us | 115.68 us | 3.78 ms | 206.20 us | 166.14 us | 175.67 us | **107.48 us** | 491.70 us | 498.10 us | 58.58 ms |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-2 | 2.72 ms | 789.07 us | **630.69 us** | 20.89 ms | 1.39 ms | 893.49 us | 913.60 us | 758.34 us | 3.09 ms | 3.33 ms | FAIL |
| f5f8b246565f9b4d39ddd176183b6f1f1de70ca681495670acc0d6ce48d9b5d4-withdraw-0 | 1.86 ms | 1.27 ms | **765.58 us** | 45.10 ms | 1.34 ms | 1.26 ms | 1.29 ms | 1.02 ms | 5.32 ms | 5.71 ms | 260.56 ms |
| f625e0b7217e6507ccf4805c8325318b4f1c0d0dc2b763aa35b79535f03f25c7-spend-2 | 314.97 us | 85.92 us | **72.67 us** | 2.28 ms | 143.70 us | 100.59 us | 98.53 us | 75.96 us | 298.40 us | 299.50 us | 32.32 ms |
| fa6305a65a8667ccd09eb2553dc280c9def8be2abb1a392515b81bfb5d2261d8-spend-4 | 975.28 us | 275.91 us | 234.81 us | 5.86 ms | 421.56 us | 362.00 us | 375.91 us | **213.66 us** | 876.00 us | 895.10 us | 98.41 ms |

## Eval tier: evaluate a decoded program

The program is decoded before timing; each iteration evaluates it. JIT VMs compile before timing too.

### Per transaction (geometric mean of 7 transaction totals)

*Each VM's time for a transaction is the sum of its times for every script the transaction runs. A VM that fails any script fails the transaction, which is assigned the slowest competitor's total.*

| VM | Language | Geo Mean | vs Fastest | Failed transactions |
|---|---|---|---|---|
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 3.55 us | 1.00x | 0 |
| **Plutigo CEK (Go)** | Go | 13.05 us | 3.68x | 0 |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 14.58 us | 4.11x | 0 |
| **Amaru UPLC CEK (Rust)** | Rust | 15.56 us | 4.39x | 0 |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 18.43 us | 5.19x | 0 |
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 23.99 us | 6.77x | 0 |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 30.07 us | 8.48x | 0 |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 30.34 us | 8.55x | 0 |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 54.10 us | 15.25x | 0 |
| **Plutuz CEK (Zig)** | Zig | 70.87 us | 19.98x | 0 |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 91.00 us | 25.66x | 0 |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 113.75 us | 32.07x | 0 |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 2.02 ms | 569.30x | 0 |
| **opshin CEK (Python / CPython)** | Python / CPython | 6.99 ms | 1971.33x | 1 |

### Summary (geometric mean across all scripts)

*Note: VMs that fail or skip a script are assigned the slowest competitor's time for that script.*

| VM | Language | Geo Mean | vs Fastest |
|---|---|---|---|
| **Scalus UPLC→JVM JIT (Scala / JVM)** | Scala / JVM | 16.39 us | 1.00x |
| **Plutigo CEK (Go)** | Go | 39.02 us | 2.38x |
| **Amaru UPLC CEK (Rust)** | Rust | 39.27 us | 2.40x |
| **Scalus CEK (Scala / JVM)** | Scala / JVM | 41.45 us | 2.53x |
| **plutus-core CEK (Haskell / GHC)** | Haskell / GHC | 47.66 us | 2.91x |
| **Chrysalis CEK (C# / .NET)** | C# / .NET | 71.09 us | 4.34x |
| **llvm-uplc post-JIT execution (C++ / LLVM)** | C++ / LLVM | 71.33 us | 4.35x |
| **Chrysalis CEK (C# / .NET AOT)** | C# / .NET AOT | 73.49 us | 4.48x |
| **Plutuz CEK (Zig)** | Zig | 133.50 us | 8.14x |
| **Julc CEK (Java / GraalVM)** | Java / GraalVM | 154.59 us | 9.43x |
| **blaze-plutus CEK (TypeScript / Bun JSC)** | TypeScript / Bun JSC | 248.14 us | 15.14x |
| **blaze-plutus CEK (TypeScript / Node V8)** | TypeScript / Node V8 | 288.07 us | 17.57x |
| **Harmonic Labs plutus-machine CEK (TypeScript / Node.js)** | TypeScript / Node.js | 4.76 ms | 290.33x |
| **opshin CEK (Python / CPython)** | Python / CPython | 27.71 ms | 1690.58x |

#### Script Coverage

| VM | Passed | Failed | Missing | Total |
|---|---|---|---|---|
| Scalus UPLC→JVM JIT (Scala / JVM) | 100 | 0 | 0 | 100 |
| Plutigo CEK (Go) | 100 | 0 | 0 | 100 |
| Amaru UPLC CEK (Rust) | 100 | 0 | 0 | 100 |
| Scalus CEK (Scala / JVM) | 100 | 0 | 0 | 100 |
| plutus-core CEK (Haskell / GHC) | 100 | 0 | 0 | 100 |
| Chrysalis CEK (C# / .NET) | 100 | 0 | 0 | 100 |
| llvm-uplc post-JIT execution (C++ / LLVM) | 100 | 0 | 0 | 100 |
| Chrysalis CEK (C# / .NET AOT) | 100 | 0 | 0 | 100 |
| Plutuz CEK (Zig) | 100 | 0 | 0 | 100 |
| Julc CEK (Java / GraalVM) | 100 | 0 | 0 | 100 |
| blaze-plutus CEK (TypeScript / Bun JSC) | 100 | 0 | 0 | 100 |
| blaze-plutus CEK (TypeScript / Node V8) | 100 | 0 | 0 | 100 |
| Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | 99 | 1 | 0 | 100 |
| opshin CEK (Python / CPython) | 81 | 19 | 0 | 100 |

### Per-Script Results

| Script | plutus-core CEK (Haskell / GHC) | Scalus UPLC→JVM JIT (Scala / JVM) | Scalus CEK (Scala / JVM) | Julc CEK (Java / GraalVM) | llvm-uplc post-JIT execution (C++ / LLVM) | Amaru UPLC CEK (Rust) | Harmonic Labs plutus-machine CEK (TypeScript / Node.js) | Plutuz CEK (Zig) | Chrysalis CEK (C# / .NET) | Chrysalis CEK (C# / .NET AOT) | Plutigo CEK (Go) | blaze-plutus CEK (TypeScript / Bun JSC) | blaze-plutus CEK (TypeScript / Node V8) | opshin CEK (Python / CPython) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 047e5557ea893da60b93eacdae74d968f02c7a9999b826ae2eb6c32978b1b345-withdraw-1 | 698.08 us | 784.34 us | 951.72 us | 1.26 ms | **472.80 us** | 594.83 us | 40.02 ms | 985.47 us | 951.54 us | 991.62 us | 765.99 us | 4.19 ms | 4.73 ms | 210.88 ms |
| 06f57a9565ecadf00e2266ee8731a6378bbb07f9a4712a84809cd8a3bba3c969-spend-1 | 26.89 us | **12.28 us** | 23.65 us | 149.01 us | 54.87 us | 17.84 us | 3.85 ms | 116.03 us | 32.94 us | 33.92 us | 19.97 us | 126.40 us | 152.70 us | 42.10 ms |
| 06f57a9565ecadf00e2266ee8731a6378bbb07f9a4712a84809cd8a3bba3c969-withdraw-0 | 1.04 ms | 1.18 ms | 1.45 ms | 1.84 ms | **723.01 us** | 872.83 us | 64.80 ms | 1.53 ms | 1.30 ms | 1.40 ms | 1.13 ms | 6.27 ms | 7.19 ms | 305.05 ms |
| 072c3053e18a3836dc90c3102c4e873a0c0048b5858ec6562f224c4aa4c8f564-spend-1 | 3.31 us | **422 ns** | 2.54 us | 13.01 us | 8.59 us | 3.46 us | 321.67 us | 23.40 us | 6.20 us | 6.16 us | 2.37 us | 13.20 us | 16.60 us | 2.13 ms |
| 07344c69689c3605f1f3982fb4b7a4506b468575b9dabf7efff7d9c9e082825c-withdraw-0 | 10.10 us | **2.59 us** | 8.91 us | 31.86 us | 24.51 us | 8.22 us | 1.58 ms | 14.41 us | 17.70 us | 17.53 us | 8.91 us | 53.90 us | 66.70 us | 7.45 ms |
| 079e30993837608b034924c42cc4694d711695478824120c2b507885e0f3b79a-spend-3 | 359.64 us | **85.08 us** | 289.37 us | 536.98 us | 173.91 us | 226.82 us | 22.50 ms | 418.19 us | 454.37 us | 474.62 us | 242.98 us | 1.64 ms | 1.99 ms | 183.99 ms |
| 0ce281ddc2701e852214823cf7f04ff8f49af9924e69034e8bfe371765c7f3ff-spend-0 | 446.45 us | 266.10 us | 380.36 us | 699.93 us | **248.36 us** | 344.35 us | 19.88 ms | 1.24 ms | 579.62 us | 660.92 us | 367.27 us | 2.13 ms | 2.58 ms | FAIL |
| 0e73f4aa816cfce02db01ee04f2017230752556a0e54ac6501945ac0e9dd4080-spend-2 | 17.26 us | **3.56 us** | 15.07 us | 73.44 us | 48.35 us | 14.85 us | 2.05 ms | 46.84 us | 25.15 us | 27.96 us | 13.47 us | 95.10 us | 105.20 us | 24.64 ms |
| 0e73f4aa816cfce02db01ee04f2017230752556a0e54ac6501945ac0e9dd4080-withdraw-0 | 701.85 us | **345.17 us** | 577.45 us | 1.30 ms | 418.88 us | 591.17 us | 37.11 ms | 2.64 ms | 1.11 ms | 1.02 ms | 642.54 us | 3.57 ms | 4.13 ms | FAIL |
| 0fc112573cf010b19921588bbc2b86a62e66b980e891ef482fd3e310c6d4ace8-spend-0 | 3.26 us | **403 ns** | 2.51 us | 13.36 us | 7.45 us | 3.22 us | 318.07 us | 23.56 us | 6.57 us | 6.50 us | 2.54 us | 14.60 us | 16.20 us | 2.03 ms |
| 1034704a8ddfc80084f53865c8c18aaaec96c81c6ce99002cb09934ad154d540-spend-2 | 452.56 us | 372.21 us | 417.70 us | 1.00 ms | **326.34 us** | 445.32 us | 22.43 ms | 1.31 ms | 631.95 us | 740.61 us | 420.60 us | 2.26 ms | 3.17 ms | FAIL |
| 10ac955d64a7d3c096abb2dcc35062c3db04313b146086d996949f6c1c3eb47a-spend-0 | 23.94 us | **11.18 us** | 22.20 us | 137.34 us | 45.10 us | 17.18 us | 2.66 ms | 94.35 us | 31.71 us | 29.75 us | 18.75 us | 119.10 us | 135.30 us | 43.91 ms |
| 10ac955d64a7d3c096abb2dcc35062c3db04313b146086d996949f6c1c3eb47a-spend-1 | 24.67 us | **11.63 us** | 20.89 us | 141.05 us | 42.82 us | 16.37 us | 2.61 ms | 100.10 us | 28.68 us | 30.86 us | 18.15 us | 113.00 us | 133.10 us | 43.75 ms |
| 1159c40949b99180499b71e05d29832955bafcdbb771c5dce4362c524ef501e8-withdraw-0 | 367.93 us | 445.02 us | 487.17 us | 700.33 us | **268.35 us** | 295.54 us | 21.43 ms | 496.50 us | 458.53 us | 507.78 us | 383.80 us | 2.18 ms | 2.54 ms | 133.51 ms |
| 15150e241b9f8a6d66750f5ab484069cb38becd38d1676f3cb3afae0c20a102b-spend-3 | 513.41 us | 441.72 us | 437.04 us | 983.51 us | **323.70 us** | 477.27 us | 20.57 ms | 2.06 ms | 728.36 us | 774.24 us | 393.16 us | 2.92 ms | 3.16 ms | FAIL |
| 1848fc0540637f76d0817f6669f53814bfe9148393f6bae94353f352a9cd9789-spend-1 | 54.86 us | **15.13 us** | 42.63 us | 109.34 us | 52.27 us | 42.01 us | 4.02 ms | 95.51 us | 78.08 us | 79.73 us | 41.77 us | 298.50 us | 342.40 us | 29.29 ms |
| 1c2421ab522d18477812623c61a8e2d0f091c12e90435d783b99f8a707254e2b-spend-1 | 960.41 us | 1.57 ms | 758.39 us | 1.60 ms | **466.52 us** | 834.82 us | 25.29 ms | 1.45 ms | 1.44 ms | 1.71 ms | 662.32 us | 4.71 ms | 5.13 ms | FAIL |
| 1dd2a4ec66cbe49f57f742a34343288a1b2d9820341398008dff1727d47babe2-spend-1 | 288.37 us | 301.83 us | 257.02 us | 581.02 us | **184.38 us** | 240.00 us | 12.53 ms | 1.22 ms | 430.38 us | 417.83 us | 245.73 us | 1.51 ms | 1.77 ms | FAIL |
| 230b7b9efeeb173c4781b0d06ae5b07b934ad35e54382b40b3bbb8d951418119-spend-0 | 18.03 us | **3.42 us** | 14.05 us | 69.63 us | 47.63 us | 14.51 us | 2.14 ms | 43.34 us | 26.71 us | 27.05 us | 13.11 us | 102.80 us | 111.90 us | 26.39 ms |
| 230b7b9efeeb173c4781b0d06ae5b07b934ad35e54382b40b3bbb8d951418119-spend-1 | 5.47 us | **1.19 us** | 4.56 us | 40.99 us | 32.74 us | 5.21 us | 1.37 ms | 25.98 us | 10.61 us | 10.27 us | 4.99 us | 32.70 us | 33.50 us | 15.53 ms |
| 2752d5588fea3ad912fdcf2bb2fd6d208af2f168d3350656025788ff4fca7980-withdraw-0 | 9.37 us | **2.57 us** | 8.87 us | 32.32 us | 25.29 us | 8.24 us | 1.63 ms | 14.44 us | 16.43 us | 17.71 us | 8.69 us | 57.20 us | 66.80 us | 7.45 ms |
| 2907afb1be082bc589464799734a4a052fcf756e4b04f1c181143c40550c1492-spend-0 | 17.25 us | **3.57 us** | 14.27 us | 73.25 us | 45.80 us | 14.14 us | 2.09 ms | 46.36 us | 26.45 us | 28.97 us | 13.67 us | 99.60 us | 109.00 us | 25.48 ms |
| 2dffd33731beaa8ef42626a0ff6bb7bfd1bdb48fea25866ac12c887c074a5846-spend-1 | 53.95 us | **15.52 us** | 43.35 us | 103.88 us | 52.16 us | 42.77 us | 3.84 ms | 93.75 us | 78.35 us | 80.56 us | 43.81 us | 315.40 us | 341.30 us | 29.16 ms |
| 2dffd33731beaa8ef42626a0ff6bb7bfd1bdb48fea25866ac12c887c074a5846-spend-2 | 107.69 us | **33.59 us** | 84.13 us | 212.12 us | 78.48 us | 80.01 us | 8.52 ms | 253.38 us | 129.91 us | 153.87 us | 91.47 us | 572.00 us | 604.30 us | 53.71 ms |
| 2e0a7798f4a69ae3254bd19b4d21d4764e27b28bc179976c3940ad0bc7b98a95-withdraw-0 | 707.02 us | 877.37 us | 994.33 us | 1.27 ms | **507.62 us** | 594.08 us | 41.92 ms | 966.69 us | 919.07 us | 935.58 us | 768.20 us | 4.65 ms | 4.58 ms | 239.71 ms |
| 2e17be2eb5967cc2b6f6d2773f27b78bd3edf0d30be26324a27ffbed408d5a41-spend-1 | 49.93 us | **17.69 us** | 39.66 us | 143.41 us | 67.03 us | 40.92 us | 5.45 ms | 414.43 us | 79.96 us | 81.83 us | 49.34 us | 282.40 us | 295.90 us | 44.91 ms |
| 3a542d9004cd5c3d4d3c3f4408272e3331c87e158215ddb88ce9e5b6486babe3-spend-2 | 6.36 us | **1.35 us** | 5.36 us | 40.70 us | 25.66 us | 6.31 us | 951.64 us | 11.44 us | 11.22 us | 12.81 us | 5.24 us | 38.60 us | 39.80 us | 13.32 ms |
| 3b2f7288f98004fdfdf6389310d2bb54b81b56cd94616cde00121e50aab96e97-spend-0 | 216.32 us | **48.64 us** | 170.76 us | 332.06 us | 94.59 us | 119.30 us | 7.71 ms | 270.95 us | 237.89 us | 269.75 us | 136.41 us | 997.30 us | 1.04 ms | FAIL |
| 471b6c63a1b1bfb8312bb6fd9be4e254d575388ecd136879a3b60e23592d42fa-spend-3 | 172.49 us | **77.78 us** | 195.90 us | 434.68 us | 155.06 us | 158.63 us | 18.62 ms | 426.86 us | 241.66 us | 252.04 us | 147.32 us | 1.03 ms | 1.10 ms | 87.53 ms |
| 497181b5f3b60e0c61ecd13e6502fe6ca298a68964e8f3944f603e127c469950-spend-0 | 5.99 us | **1.20 us** | 4.63 us | 37.39 us | 26.17 us | 5.20 us | 1.11 ms | 27.57 us | 10.65 us | 10.25 us | 5.00 us | 29.10 us | 35.00 us | 13.95 ms |
| 4a450a9411b8a231de6ebec5ecfa2fcce57c1baac2ab5fd35e1fc5126341cc38-withdraw-0 | 429.49 us | **224.82 us** | 342.50 us | 814.76 us | 259.81 us | 376.26 us | 22.29 ms | 1.35 ms | 540.73 us | 609.30 us | 379.80 us | 2.04 ms | 2.56 ms | FAIL |
| 4bcb056620920316cb3c5cdb29e2530ae4c386eef466031ec18dec6c5ed1af6f-spend-1 | 17.12 us | **3.53 us** | 13.80 us | 71.55 us | 39.27 us | 14.50 us | 2.02 ms | 46.61 us | 26.41 us | 26.88 us | 12.95 us | 95.20 us | 114.50 us | 26.14 ms |
| 4c553752cc3e282666db7cb2f1a8438d16dc60f23610f37e8da101a24f4521da-spend-3 | 24.98 us | **12.00 us** | 22.28 us | 140.76 us | 38.59 us | 16.50 us | 2.40 ms | 83.26 us | 31.16 us | 30.54 us | 18.38 us | 108.00 us | 133.40 us | 41.95 ms |
| 4d23634065b3fecb5c74891a75e57fbf5947338bd105687619c4b45855aa0f53-spend-1 | 17.43 us | **3.48 us** | 13.91 us | 69.23 us | 32.66 us | 13.68 us | 1.77 ms | 44.53 us | 30.98 us | 29.21 us | 13.28 us | 91.90 us | 107.20 us | 25.25 ms |
| 4dacfe58b35ba66eaf2de7430e1ca1c4a0ef39c03a7f8ec2db6b6b60a6731ea3-spend-1 | 3.12 us | **406 ns** | 2.46 us | 13.47 us | 7.19 us | 3.44 us | 302.08 us | 22.15 us | 6.23 us | 5.83 us | 2.48 us | 13.20 us | 17.50 us | 2.16 ms |
| 54a2d1a5ab31f91974caee9eae3176ac0cf9daba5b8353bad694d085912b2772-spend-1 | 26.45 us | **12.20 us** | 23.13 us | 141.79 us | 47.95 us | 17.99 us | 2.90 ms | 99.53 us | 31.97 us | 32.74 us | 19.88 us | 116.70 us | 137.50 us | 41.36 ms |
| 560701f9620127953f66111eb5a43ccc711f7b8f87c826de4d0f12580f2c48e9-spend-0 | 5.75 us | **1.27 us** | 4.74 us | 38.77 us | 25.30 us | 5.27 us | 1.10 ms | 25.80 us | 11.59 us | 11.03 us | 5.06 us | 28.30 us | 34.70 us | 13.74 ms |
| 5845e6241e910e18ecae0c23027081dba0edd2847b3732a4ff0bad9fd23e6af2-spend-0 | 5.52 us | **1.17 us** | 4.49 us | 38.26 us | 25.13 us | 5.44 us | 1.06 ms | 26.06 us | 9.94 us | 10.61 us | 4.91 us | 28.10 us | 34.60 us | 13.66 ms |
| 62a11be50630f9c16da5aee0fae00b26dfdb450f6bdb0edf5fe249cb9b7374ae-withdraw-0 | 9.21 us | **2.46 us** | 8.83 us | 34.47 us | 26.39 us | 8.38 us | 1.65 ms | 14.26 us | 16.58 us | 17.56 us | 8.93 us | 51.40 us | 69.30 us | 6.88 ms |
| 68a7ddeaa226d87325597b4f34d811f855a232178c98681d06e2b809937fa1c5-withdraw-0 | 376.54 us | 418.70 us | 515.86 us | 711.66 us | **291.57 us** | 325.98 us | 22.52 ms | 511.91 us | 488.87 us | 513.75 us | 397.42 us | 2.14 ms | 2.57 ms | 128.13 ms |
| 690a110a059712200fd3b71780c0d3dcbf58115f7602e82e488f6edf156ce9cc-spend-1 | 17.30 us | **3.94 us** | 14.26 us | 70.61 us | 43.15 us | 13.78 us | 2.03 ms | 44.95 us | 26.14 us | 26.79 us | 12.80 us | 91.00 us | 113.80 us | 24.93 ms |
| 6963136c3eaf099e6103aa509053976631f8fb4d13be9f2da9e8c700f9b3a8ed-spend-2 | 5.77 us | **1.16 us** | 4.52 us | 38.30 us | 27.55 us | 5.17 us | 1.03 ms | 25.88 us | 9.95 us | 10.29 us | 4.77 us | 27.90 us | 33.60 us | 14.45 ms |
| 69cb271e66fba6d994954678f84a8d3d8f55ce704cea1a8a2ed799d3272d9274-spend-0 | 17.57 us | **3.52 us** | 13.88 us | 73.75 us | 50.47 us | 14.22 us | 2.41 ms | 43.43 us | 27.53 us | 26.83 us | 12.97 us | 91.60 us | 110.40 us | 26.57 ms |
| 69cb271e66fba6d994954678f84a8d3d8f55ce704cea1a8a2ed799d3272d9274-withdraw-0 | 1.01 ms | **521.64 us** | 835.97 us | 1.75 ms | 641.72 us | 828.38 us | 53.95 ms | 3.50 ms | 1.55 ms | 1.45 ms | 894.86 us | 4.87 ms | 5.97 ms | FAIL |
| 6d9a5b869c864ed6aa21dad15406bbdbedb7711cab091ddf441a3312a4861b8c-spend-1 | 105.45 us | **21.71 us** | 79.47 us | 199.75 us | 55.34 us | 69.03 us | 7.83 ms | 134.82 us | 134.52 us | 139.07 us | 66.31 us | 460.80 us | 570.70 us | 65.67 ms |
| 6d9a5b869c864ed6aa21dad15406bbdbedb7711cab091ddf441a3312a4861b8c-spend-3 | 93.77 us | **16.88 us** | 71.39 us | 184.61 us | 47.57 us | 61.82 us | 7.17 ms | 118.30 us | 122.14 us | 125.67 us | 61.69 us | 416.60 us | 490.20 us | 58.60 ms |
| 6ed6dcefd6e92655097bf8fb2347e8c47214c72f6b4faf0327fd7626faf1d1c4-spend-2 | 451.45 us | 388.48 us | 393.99 us | 978.47 us | **328.94 us** | 418.43 us | 24.01 ms | 1.19 ms | 644.25 us | 622.19 us | 395.01 us | 2.24 ms | 2.79 ms | FAIL |
| 72d37d64464ade67a7e9ebfde460ace13ab334ead86cb7af42f9090fa5fbad95-spend-0 | 287.57 us | 308.14 us | 262.67 us | 588.07 us | **205.69 us** | 255.12 us | 12.71 ms | 1.29 ms | 402.29 us | 410.76 us | 242.24 us | 1.42 ms | 1.77 ms | FAIL |
| 75d066eeed445cc5000cadfaad96c28e0ba1fc8672ab592b193004ef7d5c8dcc-withdraw-0 | 728.65 us | **338.74 us** | 598.71 us | 1.28 ms | 432.73 us | 599.74 us | 37.61 ms | 2.70 ms | 936.27 us | 1.00 ms | 653.02 us | 3.60 ms | 4.38 ms | FAIL |
| 7683618ee491a7777a311974e047fa4b230d4ad3c5b83e07ede5a1ae91b9e568-withdraw-0 | 966.09 us | **482.93 us** | 810.72 us | 1.78 ms | 571.15 us | 797.85 us | 51.72 ms | 3.59 ms | 1.38 ms | 1.48 ms | 921.01 us | 5.45 ms | 6.15 ms | FAIL |
| 79ac5cc3cf75ece0b184373a68de4f2d716a1fe7c281e903514227964d7c9bdc-spend-4 | 17.36 us | **3.45 us** | 15.27 us | 75.31 us | 53.49 us | 14.33 us | 2.49 ms | 44.17 us | 25.74 us | 28.59 us | 13.65 us | 99.80 us | 113.50 us | 25.03 ms |
| 809c08cf6c9252fd23e2066083c4036e44b4590a6794cda47055d7d2cd48fbe2-mint-0 | 215.81 us | **82.15 us** | 171.82 us | 350.23 us | 148.86 us | 153.80 us | 13.24 ms | 1.77 ms | 298.72 us | 308.50 us | 188.74 us | 1.15 ms | 1.28 ms | 108.66 ms |
| 8524a1608a92eeb70d670b153789a0344de435bf46ffa21720cae67355d70c08-spend-2 | 5.60 us | **1.21 us** | 4.73 us | 38.35 us | 26.08 us | 5.35 us | 1.02 ms | 26.98 us | 10.88 us | 10.98 us | 4.86 us | 30.70 us | 32.70 us | 13.81 ms |
| 88aa412ef12341d0409925f1cb2310b7e59747b3ef3976424b30827d804e0652-withdraw-0 | 700.59 us | **338.72 us** | 580.97 us | 1.32 ms | 420.01 us | 603.53 us | 37.01 ms | 2.40 ms | 938.91 us | 1.03 ms | 605.84 us | 3.78 ms | 4.25 ms | FAIL |
| 8c308609194bf1928b5efa6622877653052cdd956fee57d34f787f370a2190db-spend-2 | 26.34 us | **11.51 us** | 23.41 us | 139.14 us | 36.44 us | 17.97 us | 2.37 ms | 98.17 us | 30.88 us | 30.56 us | 18.89 us | 125.00 us | 138.00 us | 44.05 ms |
| 8e1e87b906ef58aa1a19d19d53af2dccbf50830a14a799e56db7b113faa6651f-spend-4 | 17.43 us | **3.38 us** | 13.73 us | 73.42 us | 58.91 us | 14.38 us | 2.41 ms | 43.17 us | 28.97 us | 28.39 us | 12.88 us | 105.40 us | 115.80 us | 26.35 ms |
| 8e4034e230b1771a025fb19c04d9b1df9478695c8049b8398e2ad07df02d5b00-spend-0 | 102.49 us | **32.86 us** | 80.27 us | 207.23 us | 82.35 us | 75.42 us | 7.65 ms | 200.91 us | 126.91 us | 134.49 us | 86.83 us | 525.50 us | 687.30 us | 52.98 ms |
| 922edd6dbcd8d576893c0727e4c9ca0e96fda0b4fd52fcad88eafdfd91fb257c-spend-3 | 93.06 us | **17.52 us** | 69.54 us | 184.15 us | 45.75 us | 58.52 us | 6.52 ms | 117.38 us | 114.86 us | 128.89 us | 59.33 us | 418.20 us | 489.50 us | 57.16 ms |
| 9896cb365fe3d1dd2e9a5cdc96bbccc51222d95e2d410793d68d6268f0466ad4-spend-4 | 5.65 us | **1.12 us** | 4.65 us | 41.81 us | 33.31 us | 5.14 us | 1.39 ms | 26.52 us | 10.11 us | 10.91 us | 5.01 us | 31.00 us | 34.30 us | 14.26 ms |
| 9aa13e8788545578baaa2791bc71f649ed21ce38f325d7c5fea2b49f97166fa7-spend-1 | 200.98 us | **55.44 us** | 167.37 us | 341.23 us | 153.78 us | 164.77 us | 11.99 ms | 1.69 ms | 293.97 us | 308.28 us | 167.46 us | 1.06 ms | 1.21 ms | 96.22 ms |
| 9b8c6b62b2d447b5ed835a735d2799c71f4f86e01ded7ab516df9424f85fa5c5-spend-0 | 17.32 us | **3.72 us** | 13.98 us | 76.81 us | 49.43 us | 14.69 us | 2.56 ms | 43.64 us | 28.26 us | 28.35 us | 13.38 us | 107.50 us | 106.40 us | 25.59 ms |
| 9b8c6b62b2d447b5ed835a735d2799c71f4f86e01ded7ab516df9424f85fa5c5-spend-2 | 16.91 us | **3.44 us** | 15.24 us | 73.64 us | 49.48 us | 13.77 us | 2.59 ms | 42.96 us | 25.57 us | 28.66 us | 13.47 us | 103.60 us | 105.80 us | 25.92 ms |
| 9d98eef7dbdbba6806c447cd2a67e71e6e0db4ae865084bc67773747c91994a2-spend-1 | 16.66 us | **3.58 us** | 14.13 us | 73.97 us | 51.05 us | 14.34 us | 2.52 ms | 43.12 us | 27.46 us | 29.93 us | 13.53 us | 96.60 us | 105.60 us | 26.94 ms |
| 9f32ed141264497b49cb6b0d8439d6f1796d4230617635b70fdebcf4b527fa29-spend-2 | 5.67 us | **1.18 us** | 4.50 us | 38.74 us | 28.37 us | 5.17 us | 1.05 ms | 25.87 us | 10.25 us | 10.19 us | 4.91 us | 29.60 us | 32.70 us | 15.22 ms |
| a65bbdb06c3b71ae94d40fd6dc96e8514deff4b9f466c2aa0f7e44664cfd2aa1-spend-0 | 89.74 us | **17.08 us** | 71.22 us | 185.38 us | 48.49 us | 60.07 us | 6.88 ms | 120.54 us | 125.22 us | 123.25 us | 59.72 us | 430.30 us | 506.10 us | 64.79 ms |
| a6658babea9de7ebec38b42508123fa6a3843ce2d8fcdb9d7f5c2cb0ee4dcf86-spend-1 | 24.42 us | **10.59 us** | 21.24 us | 133.73 us | 35.96 us | 15.54 us | 2.11 ms | 83.87 us | 29.45 us | 30.23 us | 17.22 us | 106.60 us | 127.20 us | 43.90 ms |
| a8db0a9dcc191b286c4239a02d57d3da8f91275bfa4f63a371746544cf6ed468-spend-2 | 5.90 us | **1.16 us** | 4.59 us | 39.13 us | 28.65 us | 5.49 us | 1.11 ms | 27.32 us | 10.36 us | 10.97 us | 4.83 us | 29.90 us | 35.50 us | 15.40 ms |
| ad58ac07171001d52d275804de74c2690ab8bb9897234c90621a2e60f4d557b4-spend-0 | 197.11 us | 97.98 us | 163.64 us | 409.64 us | 114.95 us | 120.66 us | 141.68 ms | 336.37 us | 280.40 us | 257.18 us | **93.75 us** | 1.66 ms | 3.20 ms | 63.70 ms |
| af93bf199959ef3a1b8f895f260ad44c71d7bcfe01505908f5e965444d6516c1-withdraw-0 | 346.54 us | 373.46 us | 426.03 us | 659.44 us | **250.93 us** | 270.62 us | 17.86 ms | 439.00 us | 461.95 us | 437.71 us | 346.63 us | 1.86 ms | 2.11 ms | 118.68 ms |
| b38ebc7a31238291e5910091d9cc22ae289aedcd1fe66d78b21f2947d4a4e8ec-spend-1 | 5.79 us | **1.13 us** | 4.63 us | 40.87 us | 36.27 us | 5.16 us | 1.33 ms | 28.12 us | 11.27 us | 10.89 us | 4.96 us | 30.30 us | 35.40 us | 14.25 ms |
| b3a00c89128d5c56d0b17a220dc9666eaaa5e9314d4d662edabace8b246f1e48-spend-3 | 16.70 us | **3.50 us** | 13.92 us | 72.96 us | 41.28 us | 13.92 us | 2.11 ms | 48.11 us | 27.36 us | 26.69 us | 13.38 us | 96.90 us | 118.60 us | 26.57 ms |
| b757904e72bd72e242e07a5e90ee0a58ae8f13277a569ec3e915b43f0373e7db-spend-2 | 4.60 us | **1.08 us** | 3.76 us | 30.76 us | 29.94 us | 4.94 us | 1.57 ms | 46.10 us | 9.28 us | 9.49 us | 4.34 us | 23.80 us | 26.40 us | 9.57 ms |
| b8bfc4091553667248cd4fd998f49252d92f8af25d91a435e513edb07501b77e-mint-1 | 200.76 us | **103.74 us** | 218.88 us | 488.98 us | 160.94 us | 164.92 us | 17.44 ms | 438.30 us | 286.71 us | 310.01 us | 170.22 us | 1.09 ms | 1.21 ms | 101.04 ms |
| b9d42b4b35e08f02aeba3cdcd4ca030c9a72a3ce6d07bb0d2816ecf38d905f9a-spend-0 | 358.94 us | 1.17 ms | 379.30 us | 882.97 us | **280.68 us** | 332.52 us | 19.47 ms | 779.43 us | 494.71 us | 481.51 us | 315.92 us | 1.80 ms | 2.13 ms | FAIL |
| b9d42b4b35e08f02aeba3cdcd4ca030c9a72a3ce6d07bb0d2816ecf38d905f9a-withdraw-0 | 9.95 us | **3.39 us** | 11.29 us | 38.20 us | 25.64 us | 8.80 us | 1.95 ms | 16.13 us | 16.10 us | 16.08 us | 9.62 us | 57.50 us | 65.80 us | 7.41 ms |
| bc1918acaa783a69e12a7b047f1f29931460d6a28287eab5daa60500c345ddd7-spend-2 | 17.12 us | **3.63 us** | 14.06 us | 74.21 us | 47.06 us | 14.41 us | 2.34 ms | 45.80 us | 26.46 us | 28.48 us | 13.66 us | 91.30 us | 105.00 us | 24.79 ms |
| be367eee297b5777e927ad74663c851a1f7d0e403de2d2480a11a47292e7a908-spend-2 | 16.64 us | **3.80 us** | 14.33 us | 73.74 us | 56.61 us | 14.18 us | 2.60 ms | 45.53 us | 30.18 us | 28.61 us | 12.86 us | 90.80 us | 105.60 us | 25.57 ms |
| c0e22f7175c8d0cb4e309ecfb533bd6bf47461016dfd16667ac640be355565de-withdraw-0 | 658.83 us | **306.05 us** | 526.36 us | 1.21 ms | 403.98 us | 565.24 us | 34.62 ms | 1.93 ms | 821.90 us | 926.49 us | 546.26 us | 2.98 ms | 3.63 ms | FAIL |
| c1188f93e914427fd3969efdab1160f1bdb991ed8394c79f127422347fbc1d37-spend-1 | 341.90 us | 311.89 us | 289.00 us | 739.94 us | **280.42 us** | 336.18 us | 17.64 ms | 805.31 us | 444.24 us | 476.13 us | 292.75 us | 1.69 ms | 1.93 ms | FAIL |
| c6a1d6630c9c487df70be2ebd8d12b58162e3361b5efda6e6479a4db0f438751-spend-0 | 92.86 us | **16.07 us** | 70.00 us | 180.30 us | 48.98 us | 59.12 us | 6.57 ms | 110.49 us | 118.02 us | 137.98 us | 57.76 us | 421.40 us | 466.00 us | 58.39 ms |
| c8959fc0f2ed80a9e3ef5cd9cc8b65853d6b98e6828fc4128a2c4b9baf917cc3-spend-4 | 6.32 us | **1.43 us** | 5.47 us | 42.17 us | 32.79 us | 6.04 us | 1.21 ms | 10.69 us | 11.79 us | 11.58 us | 4.95 us | 33.90 us | 39.80 us | 13.93 ms |
| ca385cdf7753a005abb51173e66b13727ed635085bdd317f2fa789529e5754da-spend-2 | 115.65 us | **20.82 us** | 79.77 us | 199.08 us | 52.43 us | 71.07 us | 7.32 ms | 135.43 us | 135.74 us | 135.84 us | 66.89 us | 471.80 us | 525.90 us | 63.08 ms |
| d1492333495135ab87d4034d7f3e56bac21928a71184ba79f61d1c4133f298a8-spend-1 | 16.43 us | **3.46 us** | 13.86 us | 72.75 us | 41.57 us | 14.39 us | 2.12 ms | 45.46 us | 26.20 us | 29.14 us | 13.20 us | 94.90 us | 105.00 us | 27.38 ms |
| d37c44fb509c06b85216974bd213fb50f9301cc5b102d1506a723becf8bdacc5-spend-1 | 6.32 us | **1.40 us** | 5.53 us | 40.91 us | 26.93 us | 6.32 us | 959.85 us | 10.66 us | 11.80 us | 12.02 us | 5.00 us | 34.70 us | 39.60 us | 14.33 ms |
| d5017a6865dd289ec514cde490cfdfcd4862b812cc7562c44e50aa6adc194132-spend-0 | 107.63 us | **34.59 us** | 84.72 us | 212.09 us | 79.43 us | 76.69 us | 8.15 ms | 207.14 us | 129.03 us | 140.13 us | 86.46 us | 530.30 us | 574.40 us | 55.13 ms |
| d6247cf553324b42cd302baae91f44fbcd9342f1d6988ba5214bb01358d63d50-withdraw-0 | 9.36 us | **2.63 us** | 8.76 us | 31.63 us | 26.01 us | 8.57 us | 1.57 ms | 14.44 us | 16.79 us | 19.06 us | 8.98 us | 56.30 us | 61.00 us | 7.17 ms |
| d62df55b9d15e7ede962934a652d465cb21fbfd7419c28c8c025065fb49a95c7-withdraw-3 | 138.17 us | **54.83 us** | 147.72 us | 336.98 us | 145.91 us | 121.38 us | FAIL | 329.00 us | 223.11 us | 196.33 us | 122.07 us | 733.00 us | 803.30 us | 71.44 ms |
| d829b5969ae5e397d13c7610a14834af24204d147c02d86b101de3406d231399-spend-4 | 47.14 us | **17.52 us** | 38.30 us | 142.50 us | 64.76 us | 38.99 us | 5.29 ms | 396.38 us | 72.26 us | 78.51 us | 47.50 us | 268.00 us | 279.90 us | 40.69 ms |
| db7cc24da3b8bbfc5444bc85d883695e64cfd6966389db30eb5dc2a21076ee34-spend-0 | 338.87 us | 371.15 us | 289.75 us | 761.70 us | **249.72 us** | 300.41 us | 15.91 ms | 795.29 us | 455.62 us | 465.51 us | 291.71 us | 1.60 ms | 1.88 ms | FAIL |
| dbe943750b032ce13040794ee67cb72d1c6e7a4c9f96cf804d6d13ab7f4f4cb9-withdraw-0 | 18.32 us | **8.49 us** | 16.94 us | 58.72 us | 29.70 us | 13.58 us | 1.89 ms | 104.67 us | 23.97 us | 26.92 us | 17.72 us | 92.30 us | 98.00 us | 13.93 ms |
| dd64226d4315c5cbe19e2dd00557f0dff8ca7d492ddbe471f2d718067f421e2c-spend-2 | 17.99 us | **3.39 us** | 13.84 us | 71.87 us | 33.76 us | 14.45 us | 1.75 ms | 45.95 us | 27.23 us | 29.35 us | 13.57 us | 95.90 us | 117.70 us | 24.65 ms |
| debe3afe9219b37e6f9580a4fc5354eeca5e60aa615e65fb8d9f0f2db1a9717d-spend-2 | 5.67 us | **1.18 us** | 4.78 us | 39.30 us | 34.26 us | 5.60 us | 1.36 ms | 27.02 us | 10.74 us | 10.30 us | 4.94 us | 28.80 us | 35.80 us | 14.66 ms |
| e01b1d0b6c246b2897b1b75f422129518b0ade56cbf6b16a242e8932807b3ae1-spend-0 | 3.11 us | **437 ns** | 2.51 us | 13.48 us | 7.01 us | 3.28 us | 328.14 us | 23.24 us | 6.71 us | 5.84 us | 2.50 us | 13.80 us | 16.60 us | 2.15 ms |
| e03d515e7ff1e5754c4545babdecf3ef754e1b787db0f03cfede7e3dc2d6b826-spend-2 | 17.66 us | **3.48 us** | 13.85 us | 70.84 us | 36.96 us | 14.88 us | 1.84 ms | 45.80 us | 27.70 us | 28.66 us | 12.98 us | 92.80 us | 109.00 us | 26.01 ms |
| e0f2686ab18a9b21e8f04ea34df1bafe5dedea2150f6d27451f7bd52e5cde9c7-spend-1 | 27.46 us | **11.78 us** | 23.42 us | 144.39 us | 44.05 us | 18.12 us | 2.92 ms | 105.65 us | 30.66 us | 33.90 us | 20.05 us | 117.30 us | 142.20 us | 44.36 ms |
| e102429d660fc75b02be2a16d00b83a70e94a79da562d65f0f9175f76709d74c-spend-1 | 17.01 us | **3.55 us** | 14.27 us | 72.74 us | 40.70 us | 13.71 us | 2.05 ms | 46.19 us | 27.60 us | 26.70 us | 12.85 us | 93.70 us | 109.90 us | 25.39 ms |
| f401f24221c086d2b5cac02a40dc568b40cdec2acc38326c0204db4958c1e57e-spend-2 | 329.15 us | 381.94 us | 292.14 us | 744.10 us | **242.74 us** | 305.82 us | 17.25 ms | 853.63 us | 501.90 us | 470.89 us | 295.01 us | 1.61 ms | 2.11 ms | FAIL |
| f5f8b246565f9b4d39ddd176183b6f1f1de70ca681495670acc0d6ce48d9b5d4-withdraw-0 | 752.37 us | 863.51 us | 978.95 us | 1.24 ms | **552.17 us** | 601.46 us | 43.41 ms | 997.70 us | 853.09 us | 956.56 us | 769.14 us | 4.18 ms | 4.72 ms | 210.45 ms |
| f625e0b7217e6507ccf4805c8325318b4f1c0d0dc2b763aa35b79535f03f25c7-spend-2 | 5.49 us | **1.14 us** | 4.94 us | 39.31 us | 26.41 us | 5.57 us | 1.03 ms | 27.13 us | 10.05 us | 10.23 us | 5.02 us | 28.80 us | 33.90 us | 14.19 ms |
| fa6305a65a8667ccd09eb2553dc280c9def8be2abb1a392515b81bfb5d2261d8-spend-4 | 25.60 us | **11.69 us** | 23.10 us | 144.19 us | 48.79 us | 17.67 us | 3.08 ms | 84.56 us | 29.49 us | 32.55 us | 19.14 us | 118.00 us | 131.40 us | 44.13 ms |

---
*Generated by [cardano-plutus-vm-benchmark](https://github.com/blinklabs-io/cardano-plutus-vm-benchmark)*