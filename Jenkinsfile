//pipeline needs to be reformated so that it makes sense and actually works. 
/*
    1) prepare testing (installing flake 8, requirements)
    2) prepare docker image with dockerfile
    3) test the code with flake 8
    4) if it passes, then push the code into docker image (remember that the raspberry pi has a different architecture)
    5) docker image goes into docker hub
*/

pipeline {
  agent {
    docker 'python:3.6.1'
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pip install flake8'
      }
    }
  }
}