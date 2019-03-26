FROM python:3.6-alpine3.7

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

COPY . /app

RUN pip install requirements.txt