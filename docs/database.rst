Base de données
===============

Les données sont stockées sur une base de données SQLite3 inclue dans le projet Django.

Pour consulter votre base de données, vous pouvez exécuter les commandes suivantes sur votre console.

    - ``cd /path/to/oc-da-python-p13``
    - Ouvrir une session shell ``sqlite3``
    - Se connecter à la base de données ``.open oc-lettings-site.sqlite3``
    - Afficher les tables dans la base de données ``.tables``
    - Afficher les colonnes dans le tableau des profils, ``pragma table_info(oc-da-python-p13_profile);``
    - Lancer une requête sur la table des profils, ``select user_id, favorite_city from oc-da-python-p13_profile where favorite_city like 'B%';``
    - ``.quit`` pour quitter

Les modèles
-----------

Les modèles sont définis dans le fichier ``models.py`` de chaque application.
Les modèles **Address** et **Letting** sont dans l'application ``lettings`` et le modèle **Profile** est dans l'application ``profiles``.

Les modèles sont définis de la manière suivante :

Address
_______

Le modèle "Address" représente une adresse postale.

Il est constitué de :

    * number : nombre entier positif inférieur à 9999 correspondant au numéro de la rue
    * street : texte d'une longueur maximale de 64 caractères correspondant au nom de la rue
    * city : texte d'une longueur maximale de 64 caractères correspondant au nom de la ville
    * state : texte d'une longueur de 2 caractères correspondant à l'acronyme de l'Etat
    * zip_code : nombre entier positif inférieur à 99999 correspondant au code postal
    * country_iso_code : texte d'une longueur de 3 caractères correspondant au code ISO du pays

Letting
_______

Le modèle "Letting" représente un lieu de location.

Il est constitué de :

    * title : texte d'une longueur maximale de 256 caractères correspondant au titre de la location
    * address : relation un-à-un avec le modèle 'Address'

Profile
_______

Le modèle "Profile" représente un profil utilisateur.

Il est constitué de :

    * user : relation un-à-un avec le modèle 'User' par défaut de django
    * favorite_city : texte d'une longueur maximale de 64 caractères correspondant à la ville favorite de l'utilisateur