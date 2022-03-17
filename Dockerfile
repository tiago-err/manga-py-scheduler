# Dockerfile to create image with cron services
FROM ubuntu:latest

COPY . /manga-scheduler

RUN apt-get update

RUN apt-get install -y python3-pip
RUN python3 -m pip install pillow~=8.3 lxml
RUN python3 -m pip install manga-py

WORKDIR /manga-scheduler
RUN python3 -m pip install -r requirements.txt
CMD ["python3", "main.py"]