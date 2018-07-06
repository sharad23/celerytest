def APP_IMAGE_NAME="apple-api"
def APP_CONTAINER_NAME ="apple-api-cont"
def MQ_CONTAINER_NAME="mq-container-name"
def CELERY
def CONTAINER_TAG="latest"
def HTTP_PORT="8080"

pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3'
                }
            }
            steps {

                sh 'pip install -r requirements.txt'
                sh './manage.py test'
            }
        }
    }
}

node {
    stage('Build') {
        sh "docker build -t $IMAGE_NAME ."

    }
    stage('Deploy'){
        sh "docker run -d  -p 15672:15672  -p 5672:5672 --name rabbit1 rabbitmq:3"
        sh "docker run -p $HTTP_PORT:8080 -d  --link rabbit1:rabbit --name=$CONTAINER_NAME  $IMAGE_NAME "

    }

