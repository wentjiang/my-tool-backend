#!/bin/bash
set -eufo pipefail

REMOTE_SERVER=172.245.156.103

CONTAINER_NAME=my-tool-backend
DOCKER_IMAGE_NAME=wentjiang/${CONTAINER_NAME}

export REMOTE_SERVER
export DOCKER_IMAGE_NAME
