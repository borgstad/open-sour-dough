# Include environment from the '.env' file in each rule
include .env
export

build:
	uv pip freeze | grep -v "^-e" > requirements.txt && \
	docker buildx build \
	-t open-sourdough \
	--platform linux/amd64 \
	--load \
	.

build-all:
	uv pip freeze > requirements.txt && \
	docker buildx build \
	-t open-sourdough \
	--platform linux/amd64,linux/arm \
	--load \
	.
run:
	docker run \
		-v /data/:${PWD}/data \
		--device=/dev/video0:/dev/video0 \
		-e OPEN_SOURDOUGH_ROOT_IMAGE_DIR=/data \
		-it \
		--rm \
		open-sourdough /bin/bash
