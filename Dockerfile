
#Alpine python3.11.3 image
FROM python:3.11.3-alpine

WORKDIR /app

#Update and install needed
RUN apk update && apk add --no-cache \
    build-base
    #musl-dev \
    #linux-headers \
    #g++

#Install requrements.txt
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN python3 installer.py

#Copy all files
COPY . .

#Expose port 80
EXPOSE 80

#Run main.py
CMD ["python3", "main.py"]