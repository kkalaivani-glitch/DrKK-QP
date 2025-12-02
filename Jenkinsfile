pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }
        
        stage('Setup') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 --version || python --version
                    pip3 install -r requirements.txt || pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    python3 -m pytest tests/ --verbose --junit-xml=test-results.xml || \
                    python -m pytest tests/ --verbose --junit-xml=test-results.xml
                '''
            }
        }
        
        stage('Test Report') {
            steps {
                echo 'Publishing test results...'
                junit 'test-results.xml'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying to GitHub Pages...'
                echo 'GitHub Pages deployment happens automatically via git push to main branch'
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
