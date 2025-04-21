pipeline{
	agent any
	environment {
		DOCKERHUB_CREDENTIALS=credentials('priyanka-dockerhub')
	}
	stages {
	    
	    stage('gitclone') {

			steps {
			    checkout([$class: 'GitSCM', branches: [[name: '**']],
                 extensions: [], userRemoteConfigs:
                  [[url: 'https://github.com/priyankajagota/ETL-Pipeline.git']]])
			}
		}

		stage('Build') {

		  steps {
                script {
                    dockerImage = docker.build("12120211/etl-repo:${env.BUILD_NUMBER}")
                }
            }
		}
		
		 stage('Run') {

			steps {
			   bat "docker run 12120211/etl-repo:${env.BUILD_NUMBER}"
			}
		}
		
		stage('Push') {

		steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'priyanka-dockerhub') {
                        dockerImage.push()
                    }
                }
		}
	}

}

}