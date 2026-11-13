#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="/bench/data/plutus_use_cases"
BENCH_DIR="/bench/plutuz"

echo "Plutuz (Zig)"

# Symlink canonical flat files into expected location
rm -rf "$BENCH_DIR/bench/plutus_use_cases"
ln -sf "$DATA_DIR" "$BENCH_DIR/bench/plutus_use_cases"

# Ensure results directory exists
mkdir -p "$BENCH_DIR/bench/results"

cd "$BENCH_DIR"

# The full tier decodes each .flat file in the timed loop; PVB_TIER=eval
# (harness/plutuz/eval-tier.patch) decodes it before the timer starts.
run_tier() {
    local tier="$1" suffix="$2"
    local raw="$RUN_DIR/plutuz${suffix}-raw.log"

    # Run pre-compiled bench binary
    PVB_TIER="$tier" ./zig-out/bin/bench 2>&1 | tee "$raw"

    # Copy JSON output
    cp "bench/results/plutus_use_cases${suffix}.json" "$RUN_DIR/plutuz${suffix}-raw.json" 2>/dev/null || true

    # Parse into unified CSV
    python3 /bench/parsers/parse_plutuz_json.py "$RUN_DIR/plutuz${suffix}-raw.json" > "$RUN_DIR/plutuz${suffix}.csv"

    # Fill in -1 for any scripts that were given but produced no result
    python3 /bench/parsers/fill_failures.py "$RUN_DIR/plutuz${suffix}.csv" "$DATA_DIR" plutuz "$raw"
}

run_tier full ""
run_tier eval "-eval"
