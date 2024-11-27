pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        export PYTHONPATH=$PYTHONPATH:$(pwd)/..
                        pytest tests/test_analysis.py
                    '''
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        docker build -t my-python-app:latest .
                    '''
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        kubectl apply -f k8s/deployment.yaml
                    '''
                }
            }
        }
    }
}