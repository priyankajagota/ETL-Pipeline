pipeline {
    agent any
    environment {
       DOCKERHUB_CREDENTIALS = credentials('priyanka-dockerhub')
    stages {
        stage('Git Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '**']],
                 extensions: [], userRemoteConfigs:
                  [[url: 'https://github.com/priyankajagota/ETL-Pipeline.git']]])
            }
        }
        stage('Build Docker Image') {
            steps {
              sh 'docker build -t myfirstpythonapp .'
            }
        }

        stage('Login To Docker') {
            steps {
               sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u SDOCKERHUB_CREDENTIALS_USR -password-stdin'
                }
            }
        
        stage('Push Docker Image') {
            steps {
                sh 'docker push myfirstpythonapp'
                }
            }
        }
    }
}