FROM python:3-alpine3.20
WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt
cmd python ./run.py