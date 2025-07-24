FROM python:3.13-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache postgresql-client build-base

RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
RUN uv export > requirements.txt
RUN uv pip install --system -r requirements.txt

COPY . .
