#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="/bench/data/plutus_use_cases"
BENCH_DIR="/bench/amaru-uplc"
BENCH_BIN="$BENCH_DIR/bin/use_cases"
RAW="$RUN_DIR/amaru-uplc-raw.log"

echo "Amaru UPLC CEK (Rust / Criterion)"

if [[ ! -x "$BENCH_BIN" ]]; then
    echo "ERROR: could not find use_cases benchmark binary" | tee "$RAW"
    exit 1
fi

TIMING=(--warm-up-time 3 --measurement-time 5)
if [[ "${BENCH_TIMING:-normal}" == quick ]]; then
    TIMING=(--warm-up-time 1 --measurement-time 1)
fi

cd "$BENCH_DIR"
rm -rf target/criterion
: > "$RAW"

work=$(mktemp -d /tmp/amaru-uplc-one.XXXXXX)
trap 'rm -rf "$work"' EXIT

for flat in "$DATA_DIR"/*.flat; do
    name=$(basename "$flat" .flat)
    mkdir -p "$work/$name"
    ln -sf "$flat" "$work/$name/"
    (
        echo "--- $name: process $BASHPID"
        exec env PVB_DATA_DIR="$work/$name" \
            CRITERION_HOME="$BENCH_DIR/target/criterion" \
            "$BENCH_BIN" --bench --noplot "${TIMING[@]}"
    ) 2>&1 | tee -a "$RAW" || true
done

if ! find target/criterion -type f -name estimates.json -print -quit 2>/dev/null | grep -q .; then
    echo "ERROR: Criterion produced no benchmark measurements"
    exit 1
fi

rm -rf "$RUN_DIR/criterion-output-amaru-uplc"
cp -r target/criterion "$RUN_DIR/criterion-output-amaru-uplc"
python3 /bench/parsers/parse_criterion.py \
    "$RUN_DIR/criterion-output-amaru-uplc" amaru-uplc \
    > "$RUN_DIR/amaru-uplc.csv"
python3 /bench/parsers/fill_failures.py \
    "$RUN_DIR/amaru-uplc.csv" "$DATA_DIR" amaru-uplc "$RAW"
