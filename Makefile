# Include environment from the '.env' file in each rule
include .env
export

build:
	docker buildx build \
	-t open-sourdough-cam \
	--platform linux/amd64 \
	--load \
	.

build-all:
	docker buildx build \
	-t open-sourdough-cam \
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
		open-sourdough-cam
