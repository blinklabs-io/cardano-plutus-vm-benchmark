#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="/bench/data/plutus_use_cases"
BENCH_DIR="/bench/amaru-uplc"

echo "Amaru UPLC CEK (Rust / Criterion)"

rm -rf "$BENCH_DIR/crates/amaru-uplc/benches/use_cases/plutus_use_cases"
ln -sf "$DATA_DIR" "$BENCH_DIR/crates/amaru-uplc/benches/use_cases/plutus_use_cases"
cd "$BENCH_DIR/crates/amaru-uplc"

BENCH_BIN=$(find "$BENCH_DIR/target" -type f -name 'use_cases-*' -perm -u+x ! -name '*.d' | head -1)
if [[ -z "$BENCH_BIN" ]]; then
    echo "ERROR: could not find use_cases benchmark binary"
    exit 1
fi

rm -rf target/criterion
"$BENCH_BIN" --bench 2>&1 | tee "$RUN_DIR/amaru-uplc-raw.log" || true

if ! find target/criterion -type f -name estimates.json -print -quit 2>/dev/null | grep -q .; then
    echo "ERROR: Criterion produced no benchmark measurements"
    exit 1
fi

FAILED_SCRIPTS=$(grep "^EVAL_FAIL:" "$RUN_DIR/amaru-uplc-raw.log" | sed 's/EVAL_FAIL: //' | sort -u || true)
rm -rf "$RUN_DIR/criterion-output-amaru-uplc"
cp -r target/criterion "$RUN_DIR/criterion-output-amaru-uplc" 2>/dev/null || true
python3 /bench/parsers/parse_criterion.py "$RUN_DIR/criterion-output-amaru-uplc" amaru-uplc > "$RUN_DIR/amaru-uplc-raw.csv"

python3 -c "
import sys
failed = set('''$FAILED_SCRIPTS'''.split())
with open('$RUN_DIR/amaru-uplc-raw.csv') as f:
    lines = f.readlines()
with open('$RUN_DIR/amaru-uplc.csv', 'w') as out:
    out.write(lines[0])
    for line in lines[1:]:
        script = line.split(',')[1] if ',' in line else ''
        if script not in failed:
            out.write(line)
    for script in sorted(failed):
        if script:
            out.write(f'amaru-uplc,{script},-1,-1,-1,-1,-1,0\\n')
"

rm -f "$RUN_DIR/amaru-uplc-raw.csv"
python3 /bench/parsers/fill_failures.py "$RUN_DIR/amaru-uplc.csv" "$DATA_DIR" amaru-uplc "$RUN_DIR/amaru-uplc-raw.log"
