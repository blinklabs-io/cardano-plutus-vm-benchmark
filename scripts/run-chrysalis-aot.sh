#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="/bench/data/plutus_use_cases"
PROJECT_DIR="/bench/chrysalis"

echo "Chrysalis AOT (.NET / NativeAOT)"

# Symlink canonical flat files into expected location
rm -rf "$PROJECT_DIR/benchmarks/data/plutus_use_cases"
ln -sf "$DATA_DIR" "$PROJECT_DIR/benchmarks/data/plutus_use_cases"

# Clean previous BDN artifacts to avoid mixing JIT and AOT results
rm -rf "$PROJECT_DIR/BenchmarkDotNet.Artifacts"

cd "$PROJECT_DIR"
dotnet run -c Release --project benchmarks/PlutusBench -- \
    --job short \
    --runtimes nativeaot10.0 \
    --exporters json \
    2>&1 | tee "$RUN_DIR/chrysalis-aot-raw.log"

# BDN names reports after the benchmark class, not the runtime, so copying
# into RUN_DIR itself would overwrite the JIT run's reports.
mkdir -p "$RUN_DIR/chrysalis-aot"
cp -r BenchmarkDotNet.Artifacts/results/* "$RUN_DIR/chrysalis-aot/" 2>/dev/null || true

# Parse this run's own artifacts, not every report under RUN_DIR
python3 /bench/parsers/parse_benchmarkdotnet.py chrysalis-aot BenchmarkDotNet.Artifacts/results > "$RUN_DIR/chrysalis-aot.csv"

# Fill in -1 for any scripts that were given but produced no result
python3 /bench/parsers/fill_failures.py "$RUN_DIR/chrysalis-aot.csv" "$DATA_DIR" chrysalis-aot "$RUN_DIR/chrysalis-aot-raw.log"
