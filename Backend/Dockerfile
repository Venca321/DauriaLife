
FROM python:3.11.3-alpine as base

ENV PYTHONUNBUFFERED=1

WORKDIR /app

#RUN apk update && apk add --no-cache build-base

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip

COPY . .

RUN python3 installer.py

EXPOSE 5002

CMD python3 main.py