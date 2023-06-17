
FROM python:3.11.3-alpine

WORKDIR /app

RUN apk update && apk add --no-cache \
    build-base
    #musl-dev \
    #linux-headers \
    #g++

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN python3 installer.py

COPY . .

EXPOSE 80

CMD ["python3", "main.py"]