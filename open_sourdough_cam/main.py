import datetime
import time
from datetime import datetime
from pathlib import Path

import cv2
import numpy as np

from open_sourdough_cam import log, settings

logger = log.logger


def start_session() -> None:
    """
    Starts the sourdough monitoring session by taking pictures at regular intervals
    until the session end time is reached.
    """
    while True:
        camera = cv2.VideoCapture(str(settings.OPEN_SOURDOUGH_VIDEO_DIR))
        success, image = camera.read()
        camera.release()
        if not success:
            logger.error("failed to read image from camera")

        img_location = settings.OPEN_SOURDOUGH_ROOT_IMAGE_DIR
        img_location.mkdir(exist_ok=True)
        img_name = str(int(time.time())) + ".jpg"

        save_picture_to_dir(img_location / img_name, image)
        logger.info(f"took picture {img_name}")
        time.sleep(settings.OPEN_SOURDOUGH_INTERVAL)


def save_picture_to_dir(img_abs_path: Path, image: np.ndarray) -> None:
    """
    Saves a picture it to the designated directory.

    :param image: The image to be saved.
    """
    # Image name is the unix timestamp
    cv2.imwrite(str(img_abs_path), image)


if __name__ == "__main__":
    start_session()
