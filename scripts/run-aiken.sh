#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="${BENCH_DATA_DIR:-/bench/data/${BENCH_CORPUS:-plutus_use_cases}}"
BENCH_DIR="/bench/aiken"
BENCH_BIN="$BENCH_DIR/bin/aiken-bench"
RAW="$RUN_DIR/aiken-raw.log"

echo "Aiken UPLC CEK (Rust / Criterion)"

if [[ ! -x "$BENCH_BIN" ]]; then
    echo "ERROR: could not find aiken-bench binary" | tee "$RAW"
    exit 1
fi

TIMING=(--warm-up-time 3 --measurement-time 5)
if [[ "${BENCH_TIMING:-normal}" == quick ]]; then
    TIMING=(--warm-up-time 1 --measurement-time 1)
fi

cd "$BENCH_DIR"

work=$(mktemp -d /tmp/aiken-one.XXXXXX)
trap 'rm -rf "$work"' EXIT

# The full tier decodes each .flat file in the timed loop; PVB_TIER=eval
# decodes it before timing and times evaluation only.
run_tier() {
    local tier="$1" suffix="$2"
    local raw="$RUN_DIR/aiken${suffix}-raw.log"
    local criterion_home="$BENCH_DIR/target/criterion${suffix}"
    rm -rf "$criterion_home"
    : > "$raw"

    for flat in "$DATA_DIR"/*.flat; do
        name=$(basename "$flat" .flat)
        mkdir -p "$work/$name"
        ln -sf "$flat" "$work/$name/"
        (
            echo "--- $name: process $BASHPID"
            exec env PVB_DATA_DIR="$work/$name" \
                PVB_TIER="$tier" \
                CRITERION_HOME="$criterion_home/$name" \
                "$BENCH_BIN" --bench --noplot "${TIMING[@]}"
        ) 2>&1 | tee -a "$raw" || true
    done

    if ! find "$criterion_home" -type f -name estimates.json -print -quit 2>/dev/null | grep -q .; then
        echo "ERROR: Criterion produced no $tier tier measurements"
        return 1
    fi

    rm -rf "$RUN_DIR/criterion-output-aiken${suffix}"
    cp -r "$criterion_home" "$RUN_DIR/criterion-output-aiken${suffix}"
    python3 /bench/parsers/parse_criterion.py \
        "$RUN_DIR/criterion-output-aiken${suffix}" aiken \
        > "$RUN_DIR/aiken${suffix}.csv"
    python3 /bench/parsers/fill_failures.py \
        "$RUN_DIR/aiken${suffix}.csv" "$DATA_DIR" aiken "$raw"
}

run_tier full ""
run_tier eval "-eval"
