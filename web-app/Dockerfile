FROM python:3.11.1-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /web-app/src

RUN pip install --upgrade pip
COPY ./requirements.txt /web-app/requirements.txt
RUN pip install -r /web-app/requirements.txt

COPY . /web-app

EXPOSE 8000
