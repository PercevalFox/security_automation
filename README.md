# Security Automation Framework

## Description

Le Security Automation Framework est un outil pour automatiser les tests de sécurité et les audits de vulnérabilités pour vos applications et réseaux. Ce framework exécute régulièrement des scans de vulnérabilités, des tests de sécurité, et génère des rapports de conformité. 

## Tech Stack

- **Python** : Langage de programmation principal pour l'automatisation.
- **Jenkins** : Serveur d'intégration continue pour exécuter les tâches de manière périodique.
- **OWASP Dependency-Check** : Outil pour identifier les vulnérabilités dans les dépendances.
- **Nikto** : Scanneur de vulnérabilités pour les serveurs web.
- **Nmap** : Outil de scan de ports et de découverte de services.

## Fonctionnalités

- Automatisation des tests de sécurité périodiques (scans de ports, vulnérabilités web).
- Génération de rapports personnalisés en JSON.
- Alertes en cas de non-conformité (à personnaliser selon les besoins).

## Structure du Projet

security_automation/  
├── automation.py  
├── reports/  
│ ├── report.html  
│ └── report.json  
├── scans/  
│ ├── nmap_scan.py  
│ ├── nikto_scan.py  
│ └── dependency_check.py  
└── Jenkinsfile  


## Prérequis

Avant de commencer, assurez-vous que les outils suivants sont installés sur votre système :

- Python 3
- Jenkins
- OWASP Dependency-Check
- Nikto
- Nmap

## Installation

1. **Cloner le dépôt** :
    ```
    git clone https://github.com/PercevalFox/security_automation
    cd security_automation
    ```

2. **Installer les dépendances Python** :
    Vous pouvez utiliser `pip` pour installer les dépendances nécessaires.
    ```
    pip install schedule
    ```

3. **Configurer Jenkins** :
   - Créez un nouveau projet dans Jenkins.
   - Configurez le pipeline en utilisant le `Jenkinsfile` fourni.

## Utilisation

1. **Exécuter les scans localement** :
    Pour exécuter les scans manuellement, utilisez les scripts suivants :
    ```
    python3 scans/nmap_scan.py
    python3 scans/nikto_scan.py
    python3 scans/dependency_check.py
    ```

2. **Exécuter le script d'automatisation** :
    Le script `automation.py` exécute tous les scans périodiquement en utilisant la bibliothèque `schedule`.
    ```bash
    python3 automation.py
    ```

3. **Configurer les horaires de scan dans Jenkins** :
    Le `Jenkinsfile` est configuré pour exécuter les scans quotidiennement. Vous pouvez ajuster la fréquence selon vos besoins.

## Rapports

Les rapports générés par les scans seront stockés dans le répertoire `reports/`. Ils sont au format JSON et peuvent être personnalisés en fonction de vos besoins.

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre vos pull requests et nous aider à améliorer le framework.
