
pipeline {
  environment {
      registry = 'usmanovdanil/devops_lab_1'
    }
  agent { 
        docker { 
            image 'python:3.9.6-alpine3.14'
            args '-u 0'
        } 
    }
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Checkout') { // Checkout (git clone ...) the projects repository
      steps {
        checkout scm
      }
    }
    stage('Install packages') {
            steps {
                bin/sh 'apk add --no-cache gcc musl-dev'
            }
        }
    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh """
          pip install -r requirements.dev.txt -r requirements.txt
          """
        }
      }
    }
    stage('Linting') { // Run pylint against your code
      steps {
        script {
          sh """
          flake8
          """
        }
      }
    }
    stage('Unit Testing') { // Perform unit testing
      steps {
        script {
          sh """
          pytest tests
          """
        }
      }
    }
}
}