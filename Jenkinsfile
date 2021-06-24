pipeline{
  agent none
  //environment{
    //DOCKERHUB_CREDENTIALS = credentials('pepeloperena-dockerhub')
    //credential will only work on a specific user using the pipeline.
  //}
  stages{
    stage('Initialize build'){
      agent{
      docker{
        image 'python:3.9'
        args '-v /root/.m2:/root/.m2' //cache the image.
        }
      }
      steps{
        echo 'im passing'
        sh 'pip install -r requirements.txt'
      }
    }
  stage('Validation'){
    agent{
      docker{
        image 'python:3.9'
      }
    }
    steps{
        sh 'pip install flake8'
        sh 'flake8 Challenge/Challenges.py'
    }
  }
  stage('Build and deploy'){
    agent{
      docker{
        image 'docker'
        args '-u root:root -p 3000:3000 --privileged -v /var/run/docker.sock:/var/run/docker.sock'

      }
    }
    steps{
    sh """
      docker build -t pepeloperena/dockertest:latest .
      docker login -u pepeloperena -p Fuerte2019!
      docker push pepeloperena/dockertest:latest
       """
    }
  }
 }
}
