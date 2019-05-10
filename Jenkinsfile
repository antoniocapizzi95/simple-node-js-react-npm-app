pipeline {
    agent {
        docker {
            image 'antoniocapizzi95/node-python:v1.0'
            args '-p 3000:3000 --name production'
            }
        }
        environment {
                CI = 'true'
            }
        stages {
            stage('Pull') {
                agent none
                steps {
                    sh 'git pull /var/repository/simple-node-js-react-npm-app'
                    //slackSend color: 'good', message: 'Build done'
                }
                        }
            stage('Build') {
                steps {
                    sh 'npm install'
                    //slackSend color: 'good', message: 'Build done'
                }
            }
             stage('Test') {
                steps {
                    sh './jenkins/scripts/test.sh'
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