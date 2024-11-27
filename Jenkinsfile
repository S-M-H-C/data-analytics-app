pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    sh '''
                        if [ -d "venv" ]; then
                            rm -rf venv
                        fi
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Setup Minikube Environment') {
            steps {
                script {
                    sh '''
                        minikube delete
                        minikube start --cpus=4 --memory=4096
                        kubectl config use-context minikube
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
                        eval $(minikube docker-env)
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
                        kubectl apply -f k8s/service.yaml
                    '''
                }
            }
        }
        stage('Get Minikube IP and Port') {
            steps {
                script {
                    sh '''
                        MINIKUBE_IP=$(minikube ip)
                        NODE_PORT=$(kubectl get svc myapp-service -o=jsonpath='{.spec.ports[0].nodePort}')
                        echo "Application is accessible at http://$MINIKUBE_IP:$NODE_PORT"
                    '''
                }
            }
        }
    }
}