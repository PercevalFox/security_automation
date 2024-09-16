pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Install necessary tools if needed
                    sh 'apt-get update && apt-get install -y nmap nikto'
                }
            }
        }
        stage('Run Security Scans') {
            steps {
                script {
                    sh 'python3 scans/nmap_scan.py'
                    sh 'python3 scans/nikto_scan.py'
                    sh 'python3 scans/dependency_check.py'
                }
            }
        }
        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/*.json', allowEmptyArchive: true
            }
        }
    }
}
