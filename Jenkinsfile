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

}

