#!/bin/bash
set -eufo pipefail

cd "$(dirname "$0")/.."

. scripts/config.sh

echo "部署到远程服务器"

echo "停止docker容器"
ssh root@"${REMOTE_SERVER}" "docker stop ${CONTAINER_NAME} || true"
echo "拉取最新的镜像"
ssh root@"${REMOTE_SERVER}" "docker pull ${DOCKER_IMAGE_NAME}:latest"
echo "启动新版本的镜像"
ssh root@"${REMOTE_SERVER}" "docker run -d --rm --name my-tool-backend -p 5001:5001 ${DOCKER_IMAGE_NAME}:latest"

echo "部署完成!"
