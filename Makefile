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
		.
build-arm:
	docker buildx build \
		-t open-sourdough-cam \
		--platform linux/arm \
		.
run:
	docker run \
		-v $(CURDIR)/data:/data \
		--device=/dev/video0:/dev/video0 \
		-e OPEN_SOURDOUGH_ROOT_IMAGE_DIR=/data \
		-it \
		--rm \
		open-sourdough-cam

run-docker:
	docker run \
		-v $(CURDIR)/data:/data \
		--device=/dev/video0:/dev/video0 \
		-e OPEN_SOURDOUGH_ROOT_IMAGE_DIR=/data/$(shell date +%Y-%m-%d)/pics-$(shell mktemp -u XXXXXX) \
		-it \
		--rm \
		--detach \
		ghcr.io/borgstad/open-sourdough-cam

mount-dir:
	nohup sshfs -o allow_root home:/projects/open-sourdough-cam /home/borg/projects/open-sourdough-cam/data
