#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
BENCH_DIR="/bench/haskell"

echo "plutus-core (Haskell / GHC / Criterion)"

# Symlink canonical flat files into the expected data location
rm -rf "$BENCH_DIR/validation/data"
mkdir -p "$BENCH_DIR/validation"
ln -sf /bench/data/plutus_use_cases "$BENCH_DIR/validation/data"

# Set Cabal Paths module data dir override
export plutus_benchmark_datadir="$BENCH_DIR"

# validation-flat decodes the whole .flat file in the timed loop (full tier);
# validation decodes it before timing (eval tier).
run_tier() {
    local bench="$1" suffix="$2"
    local criterion_csv="$RUN_DIR/haskell${suffix}-criterion.csv"

    # Clean any leftover from aborted runs (Criterion appends, causing duplicate headers)
    rm -f "$criterion_csv"

    # Run Criterion benchmark binary directly with CSV output
    # The binary may exit non-zero after writing CSV (template file not found), so ignore exit code
    "$BENCH_DIR/bin/$bench" --csv "$criterion_csv" \
        2>&1 | tee "$RUN_DIR/haskell${suffix}-raw.log" || true

    # Parse Criterion CSV into unified CSV format
    python3 /bench/parsers/parse_criterion_hs.py "$criterion_csv" > "$RUN_DIR/haskell${suffix}.csv"

    # Fill in -1 for any scripts that were given but produced no result
    python3 /bench/parsers/fill_failures.py "$RUN_DIR/haskell${suffix}.csv" /bench/data/plutus_use_cases haskell "$RUN_DIR/haskell${suffix}-raw.log"
}

run_tier validation-flat ""
run_tier validation "-eval"
