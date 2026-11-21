#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="${BENCH_DATA_DIR:-/bench/data/${BENCH_CORPUS:-plutus_use_cases}}"
BENCH_DIR="/bench/plutus-machine"

echo "Harmonic Labs plutus-machine CEK (TypeScript / Bun JSC)"

# A reused RUN_DIR may hold this VM's results from an earlier run, possibly
# on another runtime; a failed run must not leave them to be reported.
rm -f "$RUN_DIR"/plutus-machine{,-eval}{.csv,-raw.log,-raw.json}

rm -rf "$BENCH_DIR/bench/results"

# The full tier decodes each .flat file in the timed loop; PVB_TIER=eval
# decodes it before timing and times evaluation only.
run_tier() {
    local tier="$1" suffix="$2"
    local raw_log="$RUN_DIR/plutus-machine${suffix}-raw.log"
    local raw_json="$RUN_DIR/plutus-machine${suffix}-raw.json"
    local native_json="$BENCH_DIR/bench/results/plutus_use_cases${suffix}.json"

    BENCH_DATA="$DATA_DIR" PVB_TIER="$tier" bun "$BENCH_DIR/bench/bench.mjs" 2>&1 | tee "$raw_log"
    if ! grep -q "PVB_RUNTIME: bun " "$raw_log"; then
        echo "ERROR: plutus-machine did not run on bun: $(grep -o 'PVB_RUNTIME: .*' "$raw_log" | head -1)" >&2
        # Status 3 tells run-all.sh to abort rather than report this run.
        exit 3
    fi
    cp "$native_json" "$raw_json"
    python3 /bench/parsers/parse_plutus_machine_json.py "$raw_json" > "$RUN_DIR/plutus-machine${suffix}.csv"
    python3 /bench/parsers/fill_failures.py \
        "$RUN_DIR/plutus-machine${suffix}.csv" "$DATA_DIR" plutus-machine "$raw_log"
}

run_tier full ""
run_tier eval "-eval"
