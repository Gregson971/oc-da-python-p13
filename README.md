[![oc-project-shield][oc-project-shield]][oc-project-url]

[oc-project-shield]: https://img.shields.io/badge/OPENCLASSROOMS-PROJECT-blueviolet?style=for-the-badge
[oc-project-url]: https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python

# Openclassrooms - Développeur d'application Python - Projet 13

Mettez à l'échelle une application Django en utilisant une architecture modulaire

![OC-Lettings](https://user.oc-static.com/upload/2023/07/20/1689880374259_Orange%20County%20Lettings%20Ad.png)

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Gregson971/oc-da-python-p13.git`

#### Créer l'environnement virtuel

- `cd /path/to/oc-da-python-p13`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/oc-da-python-p13`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/oc-da-python-p13`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/oc-da-python-p13`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/oc-da-python-p13`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc-da-python-p13_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from oc-da-python-p13_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Le déploiement de cette application se fait via Docker et Docker Compose, permettant une mise en production rapide et efficace sur n'importe quel système supportant Docker. Cela encapsule l'application et ses dépendances dans des conteneurs, facilitant ainsi le déploiement et la gestion.

### Prérequis

- Compte GitHub avec accès en écriture à ce repository
- Compte Docker Hub avec accès en écriture à un repository Docker Hub
- Compte Azure avec accès en écriture à Azure Container Instances
- Compte Sentry avec accès en écriture à un projet Sentry

### Configuration

- Créer un fichier `.env` à la racine du projet avec les variables d'environnement suivantes :

```
DJANGO_SECRET_KEY="your_secret_key"
SENTRY_DSN="https://sentry_dsn_sample.com"
DEBUG_MODE="True or False"
ENVIRONMENT="dev or prod"
DOCKER_USERNAME="username"
DOCKER_PASSWORD="password"
AZURE_CLIENT_ID="clientID"
AZURE_SUBSCRIPTION_ID="subscription_id"
AZURE_TENANT_ID="tenant_id"
```

Ces variables d'environnement sont utilisées pour configurer l'application Django, Sentry, Docker, Azure Container Instances et GitHub Actions.

### Journalisation des erreurs avec Sentry

- Créer un compte Sentry et un projet Sentry.
- Installer le SDK Sentry en utilisant la commande `pip install --upgrade 'sentry-sdk[django]'`.
- Ajouter la clé DSN à votre fichier `.env`.
- Configurer le journal des erreurs dans `settings.py`.

### Conteneurisation de l'application avec Docker

- Créer un compte Docker Hub.
- Créer un repository Docker Hub.
- Installer Docker sur votre machine.
- Créer un fichier `Dockerfile` à la racine du projet.
- Créer un fichier `docker-compose.yml` à la racine du projet.
- Créer un fichier `.dockerignore` à la racine du projet.

### Déploiement de l'image Docker sur Docker Hub

- Se connecter à Docker Hub en utilisant la commande `docker login`.
- Construire l'image Docker en utilisant la commande `docker build -t username/repository:tag .`.
- Pousser l'image Docker sur Docker Hub en utilisant la commande `docker push username/repository:tag`.

### Lancement de l'application en local avec Docker Compose après avoir récupéré l'image Docker

- Récupérer l'image Docker en utilisant la commande `docker pull username/repository:tag`.
- Lancer l'application en utilisant la commande `docker-compose up`.
- Aller sur `http://localhost:8000` dans un navigateur.
- Pour arrêter l'application, utiliser `Ctrl+C`.
- Pour arrêter et supprimer les conteneurs, utiliser `docker-compose down`.

### Déploiement de l'application avec Azure Container Instances

- Créer un compte Azure.
- Configurer les variables d'environnement dans les paramètres de configuration de l'application.
- Configurer le déploiement continu avec GitHub Actions.
- Installer localement l'interface de ligne de commande Azure en fonction de votre OS.
- Se connecter à Azure en utilisant la commande `az login`.
- Déployer l'application en utilisant la commande `az containerapp up --resource-group myResourceGroup --name mycontainer --image username/repository:tag --target-port 8000 --ingress external --query properties.configuration.ingress.fqdn` ou en faisant un push sur la branche `main`.

## Environnement de production

- [Site web Orange County Lettings](https://oc-da-python-p13.ashypond-9589c157.francecentral.azurecontainerapps.io)
- [Panel d'administration](https://oc-da-python-p13.ashypond-9589c157.francecentral.azurecontainerapps.io/admin)
- Utilisateur : `admin`
- Mot de passe : `Abc1234!`

## Documentation

- Vous trouverez toute la documentation de cette application [ici](https://oc-da-python-p13.readthedocs.io/fr/latest/)
- [Django](https://docs.djangoproject.com/en/3.2/)
- [SQLite](https://www.sqlite.org/docs.html)
- [Python](https://docs.python.org/3/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Docker](https://docs.docker.com/)
- [Azure Container Instances](https://learn.microsoft.com/fr-fr/azure/container-instances/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Pytest](https://docs.pytest.org/en/6.2.x/)
- [Sentry](https://docs.sentry.io/)
