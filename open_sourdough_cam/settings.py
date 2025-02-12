import os
from pathlib import Path

OPEN_SOURDOUGH_ROOT_IMAGE_DIR = Path(os.environ["OPEN_SOURDOUGH_ROOT_IMAGE_DIR"])
OPEN_SOURDOUGH_INTERVAL = int(os.environ.get("OPEN_SOURDOUGH_INTERVAL", 10))
OPEN_SOURDOUGH_VIDEO_DIR = Path(
    os.environ.get("OPEN_SOURDOUGH_VIDEO_DIR", "/dev/video0")
)
