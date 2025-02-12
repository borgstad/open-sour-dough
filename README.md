# Open Sourdough

![Open Sourdough Logo](path/to/logo.png) <!-- Optional: Add a logo image if available -->

Monitor and track the growth of your sourdough starter with automated, continuous picture-taking!

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)

## Introduction

**Open Sourdough** is a Python-based tool designed to help you monitor the growth and activity of your sourdough starter by automatically taking pictures at regular intervals. Visualizing your starter's progress is fun!

## Features

- **Automated Picture-Taking:** Continuously capture images of your sourdough starter at user-defined intervals.
- **Docker Support:** Easily build and run the application in a Docker container for consistent environments.

## Requirements

- **Python:** Version 3.7 or higher
- **uv** The package manager
- **Docker:** [Install Docker](https://docs.docker.com/get-docker/)
- **Make:** [Install Make](https://www.gnu.org/software/make/)
- **Camera:** A webcam connected to your system (e.g., `/dev/video0` on Linux)

## Installation

Follow these steps to set up Open Sourdough on your system:

### Configure Environment Variables

Create a `.env` file in the root of the project and set the required environment variables:

```ini
# .env
OPEN_SOURDOUGH_ROOT_IMAGE_DIR=/path/to/your/image/directory
OPEN_SOURDOUGH_INTERVAL=10  # Interval in seconds between pictures (optional, default is 10)
OPEN_SOURDOUGH_VIDEO_DIR=/dev/video0  # Path to your webcam device (optional, default is /dev/video0)
```

- **OPEN_SOURDOUGH_ROOT_IMAGE_DIR** (required): The root directory where image session folders will be created.
- **OPEN_SOURDOUGH_INTERVAL** (optional): Interval in seconds between consecutive pictures. Defaults to 10 seconds.
- **OPEN_SOURDOUGH_VIDEO_DIR** (optional): Path to the webcam device. Defaults to `/dev/video0`.

## Running the Application

You can run Open Sourdough using the provided Makefile, which builds and runs the application inside a Docker container. The application is cross-platform and supports both `linux/amd64` and `linux/arm` architectures, making it suitable for running on devices like the Raspberry Pi.

### Build and Run with Make

#### For Standard Systems (e.g., Desktop/Laptop)

Ensure Docker is running on your system.

```bash
make build run
```

This command performs the following:

1. **Build:** Creates a Docker image named `open-sourdough` with the necessary dependencies for `linux/amd64`.
2. **Run:** Starts a Docker container from the `open-sourdough` image, mounting your image directory and connecting the webcam device.

#### For Raspberry Pi (ARM Architecture)

To build and run the Docker image on a Raspberry Pi, which uses the `linux/arm` architecture, use the `build-all` target in the Makefile:

```bash
make build-all
```

### Integrate with `open-sourdough-analyze`

After capturing images with Open Sourdough, you can analyze them using the [`open-sourdough-analyze`](https://github.com/borgstad/open-sourdough-analyze) repository. Clone and set up the analysis tool to process the images stored in your designated image directory.


## Alternative: Build for Multiple Platforms

To build Docker images for both `linux/amd64` and `linux/arm` platforms, including support for Raspberry Pi:

```bash
make build-all
```
