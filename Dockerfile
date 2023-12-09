FROM python:3.11-slim
ENV allurever=ALLUREVER
# Создаем рабочую директорию внутри контейнера
WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    jq \
    curl \
    wget \
    openjdk-17-jdk

RUN mkdir /allure
RUN wget https://github.com/allure-framework/allure2/releases/download/$allurever/allure-$allurever.tgz
RUN tar zxf allure-$allurever.tgz -C /allure

ENV PATH="/allure/allure-2.25.0/bin:${PATH}"

