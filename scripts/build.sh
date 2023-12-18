#!/bin/bash
set -eufo pipefail

cd "$(dirname "$0")/.."

docker build -t my-tool-backend .
