FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y \
    jq \
    curl \
    wget \
    openjdk-17-jdk

RUN mkdir /allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.tgz
RUN tar zxf allure-2.25.0.tgz -C /allure

ENV PATH="/allure/allure-2.25.0/bin:${PATH}"

