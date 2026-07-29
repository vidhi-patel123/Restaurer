pipeline{
    agent any

    stages{
        stage("Clone code"){
            steps{
                git branch: 'Devops',
                url: 'https://github.com/vidhi-patel123/Restaurer'
            }
        }

        stage("Build docker image"){
            steps{
                sh 'docker build -t python-app .'
            }
        }

        stage("Run docker container"){
            steps{
                sh '''
                docker rm -f python-container || true
                docker run -d \
                --name python-container \
                -p 5000:5000 \
                python-app
                '''
            }
        }
    }
}