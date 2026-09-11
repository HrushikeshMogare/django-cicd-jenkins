pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python manage.py test'
            }
        }

        stage('Docker Test') {
            steps {
                bat '''
                    set PATH=C:\\Users\\HP\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%
                    docker --version
                    docker run hello-world
                '''
            }
        }
    }
}