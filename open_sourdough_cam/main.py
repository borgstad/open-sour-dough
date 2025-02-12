import time
from pathlib import Path

import cv2
import numpy as np

from open_sourdough_cam import log, settings

logger = log.logger


def start_monitoring_session() -> None:
    """
    Initiates the sourdough monitoring session by capturing images at defined intervals
    until the session is manually terminated.

    The function continuously captures images from the specified video source, saves them
    to the designated directory, and logs the actions. It operates indefinitely until interrupted.
    """
    while True:
        video_source = str(settings.OPEN_SOURDOUGH_VIDEO_DIR)
        camera = cv2.VideoCapture(video_source)
        success, frame = camera.read()
        camera.release()

        if not success:
            logger.error("Failed to capture image from camera.")
            time.sleep(settings.OPEN_SOURDOUGH_INTERVAL)
            continue

        image_dir = settings.OPEN_SOURDOUGH_ROOT_IMAGE_DIR
        image_dir.mkdir(parents=True, exist_ok=True)

        timestamp = int(time.time())
        image_filename = f"{timestamp}.jpg"
        image_path = image_dir / image_filename

        save_image(image_path, frame)
        logger.info(f"Captured image: {image_path}")

        time.sleep(settings.OPEN_SOURDOUGH_INTERVAL)


def save_image(image_path: Path, image: np.ndarray) -> None:
    """
    Saves the provided image to the specified filesystem path.

    Args:
        image_path (Path): The absolute path where the image will be saved.
        image (np.ndarray): The image data to be saved.
    """
    success = cv2.imwrite(str(image_path), image)
    if not success:
        logger.error(f"Failed to save image to {image_path}")


if __name__ == "__main__":
    start_monitoring_session()
