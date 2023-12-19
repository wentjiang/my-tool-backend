#!/bin/bash
set -eufo pipefail

cd "$(dirname "$0")/.."

. scripts/config.sh

docker build -t "${DOCKER_IMAGE_NAME}" .
