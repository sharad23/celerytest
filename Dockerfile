FROM python:3
MAINTAINER SHARAD BAIDYA
EXPOSE 8080

COPY . /home/docker/code/
RUN pip install -r /home/docker/code/requirements.txt

WORKDIR /home/docker/code
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]