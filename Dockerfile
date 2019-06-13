FROM python:3

LABEL MAINTAINER="Gian Biondi"

WORKDIR /usr/src/app

ENV FLASK_APP /usr/src/app/app.py

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./config.py .
COPY ./app.py .
