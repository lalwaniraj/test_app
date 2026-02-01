pipeline {
    agent any

    environment {
        IMAGE_NAME = "rajkumar179/test_app:latest"
        EC2_USER   = "ec2-user"
        EC2_HOST   = "65.0.74.171"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/lalwaniraj/test_app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'ec2-ssh-key',
                    keyFileVariable: 'SSH_KEY'
                )]) {
                    sh '''
                    ssh -i $SSH_KEY -o StrictHostKeyChecking=no $EC2_USER@$EC2_HOST << EOF
                      docker pull $IMAGE_NAME
                      docker stop test_app || true
                      docker rm test_app || true
                      docker run -d -p 80:5000 --name test_app $IMAGE_NAME
                    EOF
                    '''
                }
            }
        }
    }
}
