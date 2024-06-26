Installation
============

Pour installer le code de cette application, vous devez disposer au
préalable d'un compte GitHub, le Git CLI, le SQLite3 CLI et un interpréteur
Python avec une version 3.6 ou supérieure.

Une fois que vous vous êtes assuré d'avoir chacun de ces prérequis,
l'installation se fait en plusieures étapes, et dépend de votre OS.

.. note::

    Si vous utilisez Windows et PowerShell, les commandes seront les
    mêmes que celles présentées ci-dessous sauf :

        - pour activer l'environnement virtuel : ``.\venv\Scripts\Activate.ps1``
        - remplacer ``which <my-command>`` par ``(Get-Command <my-command>).Path``

Cloner le repository GitHub
---------------------------

Exécutez les commandes suivantes :

.. code-block:: bash

    cd /path/to/put/project/in
    git clone https://github.com/Gregson971/oc-da-python-p13.git

Créer un environnement virtuel
------------------------------

.. note::

    Si vous utilisez Windows, remplacez ``python3`` par ``python``.

.. code-block:: bash
    
        cd oc-da-python-p13
        python3 -m venv venv
        apt-get install python3-venv # Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu
        source venv/bin/activate

Installer les dépendances
--------------------------

.. code-block:: bash

    pip install -r requirements.txt

Configurer les variables d'environnement
-----------------------------------------

.. code-block:: bash

    cp .env_sample .env

.. note::
    
        Vous pouvez modifier les valeurs des variables d'environnement dans le fichier ``.env``.

Lier le projet à Sentry
-----------------------

Sentry est une plateforme qui signale automatiquement les erreurs et les
exceptions du projet. Il permet également la surveillance des performances.

Exécutez les commandes suivantes :

    - Créer un compte Sentry_
    - Créer un projet avec la plateforme ``Django``
    - Récupérer la clé dsn et l'intégrer dans votre fichier ``.env``

    .. code-block:: bash

        SENTRY_DSN=<la clé dsn de votre projet Sentry>

    - Se connecter sur votre compte Sentry pour visualiser les logs récupérés par Sentry

.. _Sentry: <https://sentry.io/signup/>

