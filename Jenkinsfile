//pipeline needs to be reformated so that it makes sense and actually works. 
/*
    1) prepare testing (get flake 8, requirements)
    2) prepare docker image with dockerfile
    3) test the code with flake 8
    4) if it passes, then push the code into docker image (remember that the raspberry pi has a different architecture)
    5) docker image goes into docker hub
*/

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
                sh 'python -c Challenge1.py' //cant find the image but it makes sense 
            }
        }
    }
}