pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        pytest
                    '''
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        docker build -t my-python-app:latest .
                    '''
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        kubectl apply -f k8s/deployment.yaml
                    '''
                }
            }
        }
    }
}