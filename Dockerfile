FROM python:3.10

RUN apt update && apt install ffmpeg libsm6 libxext6 -y

RUN useradd -ms /bin/bash open-sourdough && \
  usermod -a -G video open-sourdough
USER open-sourdough
WORKDIR /app

COPY open_sourdough_cam /app/open_sourdough_cam
COPY pyproject.toml README.md requirements.txt /app/

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app
ENTRYPOINT ["python", "open_sourdough_cam/main.py"]
