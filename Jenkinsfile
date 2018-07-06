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
        imagePrune(APP_CONTAINER_NAME)
        sh "docker build -t $APP_IMAGE_NAME ."

    }

}

def imagePrune(containerName){
    try {
        sh "docker image prune -f"
        sh "docker stop $containerName"
        sh "docker rm $containerName"
    } catch(error){
        sh "echo $error"

    }
}

