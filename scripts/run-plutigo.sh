#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="/bench/data/plutus_use_cases"
BENCH_DIR="/bench/plutigo"

echo "Plutigo (Go / testing.B)"

cd "$BENCH_DIR"

export PLUTIGO_BENCH_DIR="$DATA_DIR"

# BenchmarkFlatFiles decodes each .flat file in the timed loop (full tier).
# BenchmarkFlatFilesPrepared decodes and checks it once before timing with
# cek.PrepareProgram, the path a node takes for a cached script (eval tier).
run_tier() {
    local bench="$1" suffix="$2"
    ./plutigo-bench \
        -test.bench="^${bench}\$" \
        -test.benchmem \
        -test.run='^$' \
        -test.count=1 \
        -test.benchtime=5s \
        2>&1 | tee "$RUN_DIR/plutigo${suffix}-raw.log"

    # Parse into unified CSV
    python3 /bench/parsers/parse_go_bench.py "$RUN_DIR/plutigo${suffix}-raw.log" > "$RUN_DIR/plutigo${suffix}.csv"

    # Fill in -1 for any scripts that were given but produced no result
    python3 /bench/parsers/fill_failures.py "$RUN_DIR/plutigo${suffix}.csv" "$DATA_DIR" plutigo "$RUN_DIR/plutigo${suffix}-raw.log"
}

run_tier BenchmarkFlatFiles ""
run_tier BenchmarkFlatFilesPrepared "-eval"
