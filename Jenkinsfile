pipeline {
    agent any

    tools{
        node 'nodejs'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                scm checkout
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
