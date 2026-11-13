#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="/bench/data/plutus_use_cases"
BENCH_DIR="/bench/plutus-machine"

echo "Harmonic Labs plutus-machine CEK (TypeScript / Node.js)"

rm -rf "$BENCH_DIR/bench/results"

# The full tier decodes each .flat file in the timed loop; PVB_TIER=eval
# decodes it before timing and times evaluation only.
run_tier() {
    local tier="$1" suffix="$2"
    local raw_log="$RUN_DIR/plutus-machine${suffix}-raw.log"
    local raw_json="$RUN_DIR/plutus-machine${suffix}-raw.json"
    local native_json="$BENCH_DIR/bench/results/plutus_use_cases${suffix}.json"

    BENCH_DATA="$DATA_DIR" PVB_TIER="$tier" node "$BENCH_DIR/bench/bench.mjs" 2>&1 | tee "$raw_log"
    cp "$native_json" "$raw_json"
    python3 /bench/parsers/parse_plutus_machine_json.py "$raw_json" > "$RUN_DIR/plutus-machine${suffix}.csv"
    python3 /bench/parsers/fill_failures.py \
        "$RUN_DIR/plutus-machine${suffix}.csv" "$DATA_DIR" plutus-machine "$raw_log"
}

run_tier full ""
run_tier eval "-eval"
