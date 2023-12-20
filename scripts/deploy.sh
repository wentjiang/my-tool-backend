#!/bin/bash
set -eufo pipefail

cd "$(dirname "$0")/.."

. scripts/config.sh

echo "部署到远程服务器"

ssh root@"${REMOTE_SERVER}" "docker stop ${DOCKER_IMAGE_NAME} || true"
ssh root@"${REMOTE_SERVER}" "docker rm ${DOCKER_IMAGE_NAME} || true"
ssh root@"${REMOTE_SERVER}" "docker pull ${DOCKER_IMAGE_NAME}:latest"
ssh root@"${REMOTE_SERVER}" "docker run -d --name my-tool-backend -p 5001:5001 ${DOCKER_IMAGE_NAME}:latest"

echo "部署完成!"
