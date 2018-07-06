def IMAGE_NAME="modana-api"
def CONTAINER_NAME ="modana-api-cont"
def CONTAINER_TAG="latest"
def HTTP_PORT="8000"

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
