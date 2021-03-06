pipeline {
  environment {
      registry = 'usmanovdanil/devops_lab_1'
      PATH = "/usr/local/bin:$PATH"
  }
  agent { 
    docker { 
        image 'python:3.9.6-buster'
        args '-u root -v $HOME/.cache:/root/.cache -v /var/run/docker.sock:/var/run/docker.sock'
    } 
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install packages') {
          steps {
              sh """
              apt update
              apt install --no-install-recommends gcc musl-dev
              """
          }
        }
    stage('Setup') {
      steps {
        script {
          sh """
          pip install -r requirements.dev.txt -r requirements.txt
          """
        }
      }
    }
    stage('Linting') { 
      steps {
        script {
          sh """
          flake8
          """
        }
      }
    }
    stage('Unit Testing') {
      steps {
        script {
          sh """
          pytest app_python/tests
          """
        }
      }
    }

    stage('Build and Deploy') {
          steps {
            script {
                def image = docker.build('$registry:jenci-$BUILD_NUMBER')
                docker.withRegistry('', 'dockerhub') {
                    image.push()
                }
            }
          }
        }  


  }
}