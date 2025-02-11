FROM python:3.10.0-alpine
MAINTAINER Thermondo GmbH

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN python manage.py migrate

RUN adduser -D user
USER user
