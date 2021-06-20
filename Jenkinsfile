//pipeline needs to be reformated so that it makes sense and actually works. 
/*
    1) prepare testing (installing flake 8, requirements)
    2) prepare docker image with dockerfile
    3) test the code with flake 8
    4) if it passes, then push the code into docker image (remember that the raspberry pi has a different architecture)
    5) docker image goes into docker hub
*/

/*pipeline {
  agent {
    docker{
      image 'python:3.9'
      args '-v /root/.m2:/root/.m2' //this is to cache the docker image so that it is used around the pipeline
    } 
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    } 
     stage ('Testing Students code'){
      steps{
        sh 'flake8 Challenge/Challenges.py'
      }
    }
    stage ('Build docker image'){
      agent any
        steps{
          script{
            def myImage = docker.build("challenge-image:latest")
            myImage.push();
          }
        }
    }
  }  
}*/

pipeline{
  agent none
  stages{
    stage('Initialize build'){
      agent{
      docker{
        image 'python:3.9'
        args '-v /root/.m2:/root/.m2' //cache the image.
        }
      }
      steps{
        sh 'pip install -r requirements.txt'
        sh 'pip install flake8'
      }
    }
  stage('Validation'){
    agent{
      docker{
        image 'python:3.9'
      }
    }
    steps{
      sh 'flake8 Challenges/Challenge.py'
    }
  }
  stage('Build and deploy'){
    agent{
      docker{
        image 'docker'
      }
    }
    steps{
      sh 'docker version'
    }
  }
 }
}
