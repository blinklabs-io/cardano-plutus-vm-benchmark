#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="/bench/data/plutus_use_cases"
BENCH_DIR="/bench/plutus-machine"
RAW_JSON="$RUN_DIR/plutus-machine-raw.json"
RAW_LOG="$RUN_DIR/plutus-machine-raw.log"
NATIVE_JSON="$BENCH_DIR/bench/results/plutus_use_cases.json"

echo "Harmonic Labs plutus-machine CEK (TypeScript / Node.js)"

rm -rf "$BENCH_DIR/bench/results"
BENCH_DATA="$DATA_DIR" node "$BENCH_DIR/bench/bench.mjs" 2>&1 | tee "$RAW_LOG"
cp "$NATIVE_JSON" "$RAW_JSON"

python3 /bench/parsers/parse_plutus_machine_json.py "$RAW_JSON" > "$RUN_DIR/plutus-machine.csv"
python3 /bench/parsers/fill_failures.py \
    "$RUN_DIR/plutus-machine.csv" "$DATA_DIR" plutus-machine "$RAW_LOG"
