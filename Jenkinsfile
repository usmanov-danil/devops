pipeline {
    environment {
      git_repo = 'https://github.com/usmanov-danil/devops'
      registry = 'usmanovdanil/devops_lab_1'
    }

    agent {
      docker {
        image 'python:3.7-alpine'
        // args '-u 0'
      }
    }

    stages {
        stage('test') {
            steps {
              dir(path: env.BUILD_ID) {
                sh 'apk add git build-base'
                sh 'git clone ${git_repo}'
                sh 'cd devops && pip install -r requirements.txt'
                sh 'cd devops && pytest tests'
              }
            }
        }
        stage('build') {
          steps {
            dir(path: env.BUILD_ID) {
              sh 'apk add docker openrc'
              sh 'rc-update add docker boot && service docker start'
              sh "cd devops && docker build -t ${registry}:latest ."
            }
          }
        }
    }
}
