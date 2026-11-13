#!/bin/bash
# Move every VM pin in .env to the newest upstream source.
#
# This benchmark tracks the latest code of each VM, not its latest stable
# release:
#   - a VM built from git is pinned to the newest commit on its default branch;
#   - a VM used through a package registry (amaru-uplc on crates.io,
#     plutus-machine on npm) is pinned to its newest published version,
#     pre-releases included, and its adapter lockfile is regenerated.
#
# Pins stay exact (full commit SHAs, exact package versions), so a run is
# still reproducible from the .env committed with it. Toolchain versions are
# not changed. Run from the repository root; needs git, curl, python3 and
# docker (for the Cargo and npm lockfiles).
set -euo pipefail

ENV_FILE=".env"
[[ -f "$ENV_FILE" && -f Dockerfile ]] || { echo "run from the repository root" >&2; exit 1; }

env_get() { sed -n "s/^$1=//p" "$ENV_FILE" | head -1; }

env_set() {
    local key="$1" value="$2"
    if grep -q "^${key}=" "$ENV_FILE"; then
        sed -i "s|^${key}=.*|${key}=${value}|" "$ENV_FILE"
    else
        echo "${key}=${value}" >> "$ENV_FILE"
    fi
}

# Replace the comment line directly above KEY= (the human-readable label).
env_comment() {
    local key="$1" comment="$2"
    python3 - "$ENV_FILE" "$key" "$comment" <<'EOF'
import sys
path, key, comment = sys.argv[1:]
lines = open(path).read().split("\n")
for i, line in enumerate(lines):
    if line.startswith(key + "="):
        if i > 0 and lines[i - 1].startswith("#"):
            lines[i - 1] = "# " + comment
        else:
            lines.insert(i, "# " + comment)
        break
open(path, "w").write("\n".join(lines))
EOF
}

# Git-sourced VMs: <env prefix>
GIT_VMS=(CHRYSALIS PLUTIGO BLAZE PLUTUZ OPSHIN HASKELL SCALUS JULC LLVM_UPLC)

for vm in "${GIT_VMS[@]}"; do
    repo=$(env_get "${vm}_REPO")
    old=$(env_get "${vm}_SHA")
    sha=$(git ls-remote "$repo" HEAD | cut -f1)
    [[ -n "$sha" ]] || { echo "${vm}: cannot resolve HEAD of $repo" >&2; exit 1; }
    branch=$(git ls-remote --symref "$repo" HEAD | sed -n 's|^ref: refs/heads/\([^[:space:]]*\).*|\1|p')
    # Label the pin by its tag when the head is tagged, otherwise by branch
    # and commit. (git describe would name the nearest ancestor tag, which in
    # monorepos and release-branch workflows is often another package's or an
    # older release's.)
    tag=$(git ls-remote --tags "$repo" | awk -v s="$sha" '$1 == s && !found { sub("refs/tags/", "", $2); sub("\\^\\{\\}$", "", $2); print $2; found = 1 }')
    label="${tag:-${branch}@${sha:0:7}}"
    env_set "${vm}_SHA" "$sha"
    env_set "${vm}_VERSION" "$label"
    env_comment "${vm}_SHA" "${branch} head on $(date -u +%F)"
    if [[ "$old" == "$sha" ]]; then
        echo "${vm}: unchanged ${label}"
    else
        echo "${vm}: ${old:0:12} -> ${sha:0:12} ${label}"
    fi
done

# amaru-uplc: newest crates.io version, pre-releases included.
amaru=$(curl -fsSL -A "cardano-plutus-vm-benchmark update-pins" \
    https://crates.io/api/v1/crates/amaru-uplc |
    python3 -c 'import json,sys; print(json.load(sys.stdin)["crate"]["max_version"])')
if [[ "$amaru" != "$(env_get AMARU_UPLC_VERSION)" ]]; then
    sed -i -E "s/^(amaru-(uplc|kernel) = [^\"]*\")=[^\"]+\"/\1=${amaru}\"/" harness/amaru-uplc/Cargo.toml
    docker run --rm -u "$(id -u):$(id -g)" -e CARGO_HOME=/tmp/cargo -e RUSTUP_TOOLCHAIN=stable \
        -v "$PWD/harness/amaru-uplc:/w" -w /w "rust:$(env_get AMARU_UPLC_RUST_VERSION)-bookworm" \
        cargo update -p amaru-uplc -p amaru-kernel
fi
env_set AMARU_UPLC_VERSION "$amaru"
env_set AMARU_UPLC_REPO "https://crates.io/crates/amaru-uplc/${amaru}"
env_comment AMARU_UPLC_REPO "newest crates.io release (${amaru})"
echo "AMARU_UPLC: ${amaru}"

# plutus-machine: newest npm version by publish time, pre-releases included.
pm=$(curl -fsSL https://registry.npmjs.org/@harmoniclabs/plutus-machine |
    python3 -c 'import json,sys; t=json.load(sys.stdin)["time"]; t.pop("created",None); t.pop("modified",None); print(max(t, key=t.get))')
if [[ "$pm" != "$(env_get PLUTUS_MACHINE_VERSION)" ]]; then
    sed -i -E "s|(\"@harmoniclabs/plutus-machine\": )\"[^\"]+\"|\1\"${pm}\"|" harness/plutus-machine/package.json
    docker run --rm -u "$(id -u):$(id -g)" -e npm_config_cache=/tmp/npm \
        -v "$PWD/harness/plutus-machine:/w" -w /w "node:$(env_get NODE_MAJOR)-bookworm" \
        npm install --package-lock-only --ignore-scripts --no-audit --no-fund
fi
env_set PLUTUS_MACHINE_VERSION "$pm"
env_set PLUTUS_MACHINE_REPO "https://www.npmjs.com/package/@harmoniclabs/plutus-machine/v/${pm}"
env_comment PLUTUS_MACHINE_REPO "newest npm release (${pm})"
echo "PLUTUS_MACHINE: ${pm}"

echo
echo "Updated ${ENV_FILE}. Rebuild with: docker compose build"
