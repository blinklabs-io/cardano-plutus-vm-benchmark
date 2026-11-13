#!/bin/bash
set -euo pipefail

RUN_DIR="$1"
DATA_DIR="/bench/data/plutus_use_cases"
BENCH_DIR="/bench/opshin"

echo "opshin-uplc (Python)"

cd "$BENCH_DIR"

# Patch the hardcoded multi-line BENCH_DIR assignment to use canonical data
python3 -c "
import re
with open('bench_plutus_use_cases.py') as f:
    code = f.read()
code = re.sub(
    r'BENCH_DIR\s*=\s*os\.path\.expanduser\([^)]+\)',
    'BENCH_DIR = \"${DATA_DIR}\"',
    code,
)
with open('bench_plutus_use_cases.py', 'w') as f:
    f.write(code)
"

# The full tier decodes each .flat file in the timed loop; PVB_TIER=eval
# decodes it before timing and times evaluation only.
run_tier() {
    local tier="$1" suffix="$2"
    local raw="$RUN_DIR/opshin${suffix}-raw.log"
    local csv="$RUN_DIR/opshin${suffix}.csv"

    # Run benchmark (use the Python from the build stage, not Ubuntu's 3.12)
    PVB_TIER="$tier" "python${PYTHON_VERSION:-3.14}" bench_plutus_use_cases.py 2>&1 | tee "$raw"

    # Parse into unified CSV
    python3 /bench/parsers/parse_opshin.py "$raw" > "$csv"

    # Append failures from log as -1 entries
    { grep "SKIP (eval error)" "$raw" || true; } | while read -r line; do
        script=$(echo "$line" | awk '{print $1}')
        echo "opshin,$script,-1,-1,-1,-1,-1,0" >> "$csv"
    done

    # Fill in -1 for any scripts that were given but produced no result
    python3 /bench/parsers/fill_failures.py "$csv" "$DATA_DIR" opshin "$raw"
}

run_tier full ""
run_tier eval "-eval"
