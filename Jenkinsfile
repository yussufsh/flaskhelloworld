pipeline {
    agent none
    stages {
        stage('Run On') {
            parallel {
                stage('Run On amd64') {
                    agent {
                        label 'jenkins-slave-amd64'
                    }
                    steps {
                        sh 'uname -a'
                        runSteps('amd64')
                    }
                }
                stage('Run On ppc64le') {
                    agent {
                        label 'jenkins-slave-ppc64le'
                    }
                    steps {
                        sh 'uname -a'
                        runSteps('ppc64le')
                    }
                }
            }
        }
        stage('Publish') {
            agent {
                label 'jenkins-slave-ppc64le'
            }
            environment {
                DOCKER_CLI_EXPERIMENTAL='enabled'
            }
            steps {
                script {
                    docker.withRegistry('', 'dockerhubcredentials') {
                        sh '''
                            docker manifest create --amend \
                                yussuf/flaskdemo:latest \
                                yussuf/flaskdemo:amd64 \
                                yussuf/flaskdemo:ppc64le
                            docker manifest push yussuf/flaskdemo:latest
                        '''
                    }
                }
            }
        }
    }
}
void runSteps(label) {
    stage('Compile On ' + label) {
        git branch: 'master', url: 'https://github.com/yussufsh/flaskhelloworld.git'
        sh 'pip install -r requirements.txt'
    }
    stage('Test On ' + label) {
        sh 'python test.py'
    }
    stage('Publish On ' + label) {
        docker.withRegistry('', 'dockerhubcredentials') {
            demoImage = docker.build 'yussuf/flaskdemo:' + label
            demoImage.push()
        }
    }
}
