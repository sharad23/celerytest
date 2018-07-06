FROM python:3
MAINTAINER SHARAD BAIDYA
EXPOSE 8000

COPY . /home/docker/code/
RUN pip install -r /home/docker/code/requirements.txt

WORKDIR /home/docker/code/app