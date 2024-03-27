pipeline {
    agent any

    tools{
        nodejs 'nodejs'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']], // Specify the branch to checkout
                    userRemoteConfigs: [[url: 'https://github.com/decheverri123/xliff-testing-app.git']] // Specify the repository URL
                ])
            }
        }

        stage('Run Node.js tests') {
            steps {
                // Install the dependencies
                sh 'npm install'

                // Run the tests in the scripts directory
                sh 'npm test:node'
            }
        }



        stage('Generate .xlf file') {
            steps {
                // Run the Python script to generate the .xlf file
                // Replace 'prefix', 'input.xlf', and 'output.xlf' with your actual values
                sh 'python3 scripts/xlfConverter.py xx locale/messages.xlf locale/output.xlf'
            }
        }
    }
}
