FROM python:3.12
RUN apt update && apt install curl ffmpeg libsm6 libxext6 -y

WORKDIR /app

RUN curl --proto '=https' --tlsv1.2 -LsSf \
    https://github.com/astral-sh/uv/releases/download/0.5.24/uv-installer.sh | sh
ENV PATH="/root/.local/bin/:$PATH"

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.12 \
    UV_PROJECT_ENVIRONMENT=/app/.venv

COPY uv.lock pyproject.toml README.md /app/
COPY open_sourdough_cam /app/open_sourdough_cam

RUN --mount=type=cache,target=/root/.cache \
    uv sync \
        --locked \
        --no-dev \
        --no-editable

ENV PYTHONPATH=/app
ENTRYPOINT [".venv/bin/python", "open_sourdough_cam/main.py"]
