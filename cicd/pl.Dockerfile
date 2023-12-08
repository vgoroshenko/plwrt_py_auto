FROM python:3.11-slim
# Создаем рабочую директорию внутри контейнера
WORKDIR /app

RUN pip install playwright


RUN playwright install --with-deps

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get install -y \
    xvfb \
    xserver-xephyr \
    xauth \
    python3-tk \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN touch ~/.Xauthority

RUN pip install  pytest-xvfb
