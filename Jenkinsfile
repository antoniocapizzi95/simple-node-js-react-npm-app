pipeline {
    agent {
        docker {
            image 'antoniocapizzi95/node-python:v1.0'
            args '-p 3000:3000'
            }
        }
        environment {
                CI = 'true'
            }
        stages {
            stage('Build') {
                steps {
                    sh 'npm install'
                }
            }
             stage('Test') {
                steps {
                    sh './jenkins/scripts/test.sh'
                }
             }
             stage('Sonarqube') {
                 environment {
                     scannerHome = tool 'SonarQubeScanner'
                 }
                 steps {
                     withSonarQubeEnv('sonarqube') {
                         sh "${scannerHome}/bin/sonar-scanner"
                     }
                     timeout(time: 10, unit: 'MINUTES') {
                         waitForQualityGate abortPipeline: true
                     }
                 }
             }
             stage('Deliver') {
                         steps {
                             sh './jenkins/scripts/deliver.sh'
                             input message: 'Finished using the web site? (Click "Proceed" to continue)'
                             sh './jenkins/scripts/kill.sh'
                         }
                     }
        }
}