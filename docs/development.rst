Développement
=============

Le site affiche les éléments contenus dans la base de données et se divise en trois sections principales :

    - Home : La page d'accueil.
    - Lettings : Une page répertoriant tous les lieux de location.
    - Profiles : Une page listant tous les profils d'utilisateurs.

Les sections « Lettings » et « Profiles » offrent un accès aux pages de détails pour chaque élément. 
Par exemple, depuis la page « Lettings », vous pouvez accéder à une page qui présente les détails du lieu « Oceanview Retreat », y compris son adresse complète.

Exécuter l'application en local avec Django
-------------------------------------------

Pour exécuter l'application en local, exécutez les commandes suivantes :

    .. code-block:: bash

        cd /path/to/oc-da-python-p13
        source venv/bin/activate
        python manage.py collectstatic  # Pour collecter les fichiers statiques
        python manage.py runserver

    - L'application est accessible à l'adresse http://localhost:8000.
    - Pour accéder à l'interface d'administration, rendez-vous sur http://localhost:8000/admin.

Exécuter l'application en local avec Docker
-------------------------------------------

Docker est un outil qui permet de créer, de déployer et d'exécuter des applications dans des conteneurs.

Pour exécuter l'application en local avec Docker, exécutez les commandes suivantes :

    - Créer un compte DockerHub 
    - Installer Docker Desktop en fonction de votre OS.
    - Récupérer l'image Docker de l'application sur DockerHub. ``docker pull gregson971/oc-da-python-p13:latest``
    - Lancer le server avec Docker compose. ``docker-compose up``
    - L'application est accessible à l'adresse http://localhost:8000.
    - Pour accéder à l'interface d'administration, rendez-vous sur http://localhost:8000/admin.
    - Pour arrêter le serveur sans supprimer la ressource, utilisez la combinaison de touches ``Ctrl + C``.
    - Pour arrêter le serveur et supprimer la ressource, utilisez la combinaison de touches ``Ctrl + C`` puis ``docker-compose down``.
    - Pour supprimer l'image Docker de l'application, utilisez la commande ``docker rmi gregson971/oc-da-python-p13:latest``.
    
Configurer et lancer la CI/CD avec GitHub Actions
-------------------------------------------------

GitHub Actions est un service d'intégration et de déploiement continu (CI/CD) qui permet d'automatiser les tests et le déploiement du code.

Pour configurer et lancer la CI/CD avec GitHub Actions, exécutez les commandes suivantes :

    - Créer un compte GitHub
    - Créer un repository sur GitHub
    - Créer un fichier ``.github/workflows/ci-cd.yml`` à la racine du projet
    - Copier le contenu du fichier ``.github/workflows/ci-cd.yml`` disponible sur le repository GitHub
    - Pousser les modifications sur le repository GitHub
    - Accéder à l'onglet ``Actions`` de votre repository pour visualiser les workflows
    - Pour chaque push sur le repository, GitHub Actions exécute les tests et déploie le code sur Azure

Dans les paramètres du repository, vous pouvez ajouter des secrets pour les variables d'environnement.

    .. note::

        Pour plus d'informations sur la configuration de GitHub Actions, consultez la `documentation officielle de GitHub Actions <https://docs.github.com/en/actions>`_.

Déployer l'application avec Azure Container Instances
-----------------------------------------------------

Azure Container Instances est un service Azure qui permet de déployer des conteneurs sans serveur.

Pour déployer l'application avec Azure Container Instances, exécutez les commandes suivantes :

    - Créer un compte Azure
    - Créer un groupe de ressources
    - Créer un registre de conteneurs
    - Créer une instance de conteneur
    - Récupérer l'URL de l'instance de conteneur
    - Accéder à l'URL de l'instance de conteneur pour visualiser l'application

En ligne de commande, vous pouvez exécuter les commandes suivantes :

    .. code-block:: bash

        az containerapp up --resource-group myResourceGroup --name mycontainer --image username/repository:tag --target-port 8000 --ingress external --query properties.configuration.ingress.fqdn


Dans les paramètres de l'instance de conteneur, vous pouvez ajouter des variables d'environnement.

    .. note::

        Pour plus d'informations sur le déploiement avec Azure Container Instances, consultez la `documentation officielle de Azure Container Instances <https://learn.microsoft.com/fr-fr/azure/container-instances/>`.