FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements.txt
COPY transport_helper /transport_helper
WORKDIR /transport_helper
EXPOSE  8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password app-user
USER app-user

