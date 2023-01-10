FROM python:3

COPY requirements.txt .


COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
