
pipeline {
  environment {
      git_repo = 'https://github.com/usmanov-danil/devops'
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
    failure {
      script {
        msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
        
        slackSend message: msg, channel: env.SLACK_CHANNEL
    }
  }
}
}