
1. Cloner le projet :
   Exécute la commande suivante pour cloner le projet :
   git clone https://votre-repository.git
   cd gestion_de_stock

2. Créer un fichier .env :
   Crée un fichier .env à la racine du projet :
   touch .env
   
   Ajoute la configuration SMTP dans le fichier .env :
   DEBUG=True
   SECRET_KEY=votre_clé_secrète

   # Configuration SMTP
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=ton-email@gmail.com
   EMAIL_HOST_PASSWORD=ton-mot-de-passe

3. Vérifier la configuration de la base de données SQLite dans settings.py :
   Assure-toi que la base de données SQLite est bien configurée :
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',  # Fichier SQLite local
       }
   }

4. Entrer dans le répertoire Django :
   cd gest_stock

5. Lancer Docker Compose :
   Exécute la commande suivante pour construire et démarrer l'application avec Docker Compose :
   docker-compose up --build

6. Vérifier les logs de l'application :
   Si tu veux vérifier que tout fonctionne correctement, utilise cette commande :
   docker-compose logs

7. Accéder à l'application :
   - API Backend : http://localhost:8089
   - Admin Django : http://localhost:8085/admin/
   
8. Arrêter les conteneurs :
   Une fois terminé, arrête et supprime les conteneurs en exécutant :
   docker-compose down
