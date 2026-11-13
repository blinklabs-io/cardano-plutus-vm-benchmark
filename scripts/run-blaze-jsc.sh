#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="/bench/data/plutus_use_cases"
BENCH_DIR="/bench/blaze-plutus"

echo "blaze-jsc (TypeScript / Bun / JavaScriptCore)"

# Symlink canonical flat files into expected location
rm -rf "$BENCH_DIR/packages/blaze-plutus/bench/plutus_use_cases"
ln -sf "$DATA_DIR" "$BENCH_DIR/packages/blaze-plutus/bench/plutus_use_cases"

cd "$BENCH_DIR/packages/blaze-plutus"

# Run vitest bench on Bun (JavaScriptCore engine). --bun is required: vitest's
# CLI starts with #!/usr/bin/env node, so without it `bun run` hands the
# benchmark to Node (V8).
# The full tier decodes each .flat file in the timed loop; PVB_TIER=eval
# (harness/blaze/pvb.patch) decodes it before timing.
run_tier() {
    local tier="$1" suffix="$2"
    local raw="$RUN_DIR/blaze-jsc${suffix}-raw.log"
    PVB_TIER="$tier" bun --bun run vitest bench --run \
        2>&1 | tee "$raw"
    # harness/blaze/pvb.patch prints the runtime that ran the benchmark.
    if ! grep -q "PVB_RUNTIME: bun " "$raw"; then
        echo "ERROR: blaze-jsc did not run on bun: $(grep -o 'PVB_RUNTIME: .*' "$raw" | head -1)" >&2
        exit 1
    fi
    python3 /bench/parsers/parse_vitest.py blaze-jsc "$raw" > "$RUN_DIR/blaze-jsc${suffix}.csv"
    python3 /bench/parsers/fill_failures.py "$RUN_DIR/blaze-jsc${suffix}.csv" "$DATA_DIR" blaze-jsc "$raw"
}

run_tier full ""
run_tier eval "-eval"
