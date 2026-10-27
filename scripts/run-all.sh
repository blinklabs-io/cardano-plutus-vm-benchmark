#!/bin/bash
set -euo pipefail

RESULTS_DIR="${RESULTS_DIR:-/results}"

# Use RUN_DIR if set (for updating an existing run), otherwise create a new one
if [[ -z "${RUN_DIR:-}" ]]; then
    DATE=$(date +%Y-%m-%d)
    RUN_DIR="${RESULTS_DIR}/${DATE}"
    # Avoid clobbering an existing run — append a suffix if needed
    if [[ -d "$RUN_DIR" ]]; then
        N=0
        while [[ -d "${RUN_DIR}-${N}" ]]; do
            N=$((N + 1))
        done
        RUN_DIR="${RUN_DIR}-${N}"
    fi
fi
mkdir -p "$RUN_DIR"

echo "============================================="
echo " Cardano Plutus VM Benchmark Suite"
echo " $(date)"
echo "============================================="

# arm64 /proc/cpuinfo has no "model name", and lscpu reports "-" for Apple
# silicon under Docker, so fall back to the vendor; HOST_CPU overrides both
# because a Docker VM on macOS cannot see the host CPU model.
detect_cpu() {
    local model
    model=$(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2 | xargs)
    if [[ -z "$model" ]]; then
        model=$(lscpu 2>/dev/null | awk -F: '/^Model name/ {print $2}' | xargs)
        [[ "$model" == "-" ]] && model=""
    fi
    if [[ -z "$model" ]]; then
        model=$(lscpu 2>/dev/null | awk -F: '/^Vendor ID/ {print $2}' | xargs)
    fi
    echo "${model:-unknown} ($(uname -m))"
}

# Record hardware fingerprint
{
    echo "date: $(date -Iseconds)"
    echo "kernel: $(uname -r)"
    echo "cpu: ${HOST_CPU:-$(detect_cpu)}"
    echo "cores: $(nproc)"
    echo "memory: $(free -h | awk '/Mem:/ {print $2}')"
} > "$RUN_DIR/environment.txt"

cat "$RUN_DIR/environment.txt"
echo ""

# Track which VMs to run (default: all)
VMS="${BENCH_VMS:-chrysalis,chrysalis-aot,amaru-uplc,uplc-turbo-bc,plutigo,blaze-jsc,blaze-v8,plutuz,opshin,haskell,scalus-cek,scalus-jit,julc-java,llvm-uplc-jit}"

# Keep source revisions and toolchains alongside each run so generated reports
# identify the exact implementations that produced the measurements.
version_row() {
    local vm="$1" repo="" version="" revision="" toolchain=""
    case "$vm" in
        chrysalis|chrysalis-aot) repo="${CHRYSALIS_REPO:-}"; version="${CHRYSALIS_VERSION:-}"; revision="${CHRYSALIS_SHA:-}"; toolchain=".NET SDK ${DOTNET_VERSION:-unknown}" ;;
        amaru-uplc) repo="${AMARU_UPLC_REPO:-}"; version="${AMARU_UPLC_VERSION:-}"; revision="${AMARU_UPLC_SHA:-}"; toolchain="rustc ${AMARU_UPLC_RUST_TOOLCHAIN:-${AMARU_UPLC_RUST_VERSION:-${RUST_VERSION:-unknown}}}" ;;
        uplc-turbo|uplc-turbo-bc) repo="${UPLC_TURBO_BC_REPO:-}"; version="${UPLC_TURBO_BC_VERSION:-}"; revision="${UPLC_TURBO_BC_SHA:-}"; toolchain="rustc ${RUST_VERSION:-unknown}" ;;
        plutigo) repo="${PLUTIGO_REPO:-}"; version="${PLUTIGO_VERSION:-}"; revision="${PLUTIGO_SHA:-}"; toolchain="Go ${GO_VERSION:-unknown}" ;;
        blaze-jsc) repo="${BLAZE_REPO:-}"; version="${BLAZE_VERSION:-}"; revision="${BLAZE_SHA:-}"; toolchain="Bun ${BUN_VERSION:-unknown}" ;;
        blaze-v8) repo="${BLAZE_REPO:-}"; version="${BLAZE_VERSION:-}"; revision="${BLAZE_SHA:-}"; toolchain="Node.js ${NODE_MAJOR:-unknown}" ;;
        plutuz) repo="${PLUTUZ_REPO:-}"; version="${PLUTUZ_VERSION:-}"; revision="${PLUTUZ_SHA:-}"; toolchain="Zig ${ZIG_VERSION:-unknown}" ;;
        opshin) repo="${OPSHIN_REPO:-}"; version="${OPSHIN_VERSION:-}"; revision="${OPSHIN_SHA:-}"; toolchain="Python ${PYTHON_VERSION:-unknown}" ;;
        haskell) repo="${HASKELL_REPO:-}"; version="${HASKELL_VERSION:-}"; revision="${HASKELL_SHA:-}"; toolchain="GHC ${GHC_VERSION:-unknown}" ;;
        scalus-cek|scalus-jit) repo="${SCALUS_REPO:-}"; version="${SCALUS_VERSION:-}"; revision="${SCALUS_SHA:-}"; toolchain="JDK ${JDK_VERSION:-unknown} / Scala 3" ;;
        julc-java) repo="${JULC_REPO:-}"; version="${JULC_VERSION:-}"; revision="${JULC_SHA:-}"; toolchain="GraalVM ${JDK_SDK_VERSION:-unknown}" ;;
        llvm-uplc-jit) repo="${LLVM_UPLC_REPO:-}"; version="${LLVM_UPLC_VERSION:-}"; revision="${LLVM_UPLC_SHA:-}"; toolchain="LLVM ${LLVM_VERSION:-unknown}" ;;
    esac
    if [[ -z "$version" || "$version" == "commit" ]]; then
        version="commit:${revision:0:7}"
    fi
    printf '%s,%s,%s,%s,%s\n' "$vm" "${repo:-unknown}" "$version" "${revision:-unknown}" "${toolchain:-unknown}"
}

declare -A VERSION_ROWS=()
VERSION_ORDER=()
if [[ -f "$RUN_DIR/versions.csv" ]]; then
    while IFS= read -r row; do
        [[ -z "$row" || "$row" == vm,* ]] && continue
        vm=${row%%,*}
        if [[ -z "${VERSION_ROWS[$vm]+present}" ]]; then
            VERSION_ORDER+=("$vm")
        fi
        VERSION_ROWS[$vm]="$row"
    done < "$RUN_DIR/versions.csv"
fi

IFS=',' read -ra VERSION_VMS <<< "$VMS"
for vm in "${VERSION_VMS[@]}"; do
    vm=$(echo "$vm" | xargs)
    if [[ -z "${VERSION_ROWS[$vm]+present}" ]]; then
        VERSION_ORDER+=("$vm")
    fi
    VERSION_ROWS[$vm]=$(version_row "$vm")
done

{
    echo "vm,repo,version,revision,toolchain"
    for vm in "${VERSION_ORDER[@]}"; do
        printf '%s\n' "${VERSION_ROWS[$vm]}"
    done
} > "$RUN_DIR/versions.csv"

# Without SYS_NICE in the bounding set (plain docker run), exec of the
# capability-bearing nice fails outright, so probe once and fall back.
if nice -n -20 true 2>/dev/null; then
    PRIORITY=(nice -n -20)
else
    echo "WARN: cannot raise priority (add SYS_NICE); running at normal priority"
    PRIORITY=()
fi

run_vm() {
    local vm_name="$1"
    local script="/bench/scripts/run-${vm_name}.sh"

    if [[ ! -f "$script" ]]; then
        echo "SKIP: no runner script for ${vm_name}"
        return 0
    fi

    echo ""
    echo "---------------------------------------------"
    echo " Running: ${vm_name}"
    echo "---------------------------------------------"

    if "${PRIORITY[@]}" bash "$script" "$RUN_DIR"; then
        echo "OK: ${vm_name} completed"
    else
        echo "FAIL: ${vm_name} exited with code $?"
    fi
}

IFS=',' read -ra VM_LIST <<< "$VMS"
for vm in "${VM_LIST[@]}"; do
    vm=$(echo "$vm" | xargs)  # trim whitespace
    run_vm "$vm"
done

echo ""
echo "---------------------------------------------"
echo " Normalizing results"
echo "---------------------------------------------"

python3 /bench/parsers/normalize.py "$RUN_DIR"

echo ""
echo "---------------------------------------------"
echo " Generating report"
echo "---------------------------------------------"

python3 /bench/report/generate_report.py "$RUN_DIR"

echo ""
echo "============================================="
echo " Benchmark suite complete"
echo " Results: ${RUN_DIR}"
echo "============================================="
