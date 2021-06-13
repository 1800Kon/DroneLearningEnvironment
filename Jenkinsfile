pipeline {
    agent none
    stages {
        stage('Build') {
            agent{
                docker{
                    image 'python:3'
                }
            }
            steps{
                sh 'python -c Challenge1.py'
            }
        }
    }
}