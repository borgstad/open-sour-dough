import time
from pathlib import Path
import os


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
        image_dir = settings.OPEN_SOURDOUGH_ROOT_IMAGE_DIR
        image_dir.mkdir(parents=True, exist_ok=True)

        timestamp = int(time.time())
        image_filename = f"{timestamp}.jpg"
        image_path = image_dir / image_filename

        capture_image(image_path)
        logger.info(f"Captured image: {image_path}")

        time.sleep(settings.OPEN_SOURDOUGH_INTERVAL)


def capture_image(image_path: Path) -> None:
    """
    Saves the provided image to the specified filesystem path.

    Args:
        image_path (Path): The absolute path where the image will be saved.
        image (np.ndarray): The image data to be saved.
    """
    os.system(f"ffmpeg -f video4linux2 -i /dev/video0 -frames:v 1 {image_path} > /dev/null 2>&1")


if __name__ == "__main__":
    start_monitoring_session()
