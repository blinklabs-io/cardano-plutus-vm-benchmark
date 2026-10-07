#!/bin/bash
set -euo pipefail

# UID is readonly in bash, so the compose user is passed as HOST_UID/HOST_GID
export HOST_UID=$(id -u)
export HOST_GID=$(id -g)

docker compose run --rm benchmark "$@"
