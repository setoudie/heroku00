# Comment deployer un app flask avec Heroku

1. Ecriture et creation d'un repo pour le code
2. Installation de **gunicorn**
3. Creation des fichier de configurations 
   * Procfile : `echo web: gunicorn --app:app_name > Procfile`
   * requirements.txt : `pip freeze > requirements.txt`
4. conexion a Heroku
   `heroku login`
5. Creation de l'app 
   `heroku create app_nqame`
6. Choix de plan d'abonnement
   `heroku addons:create heroku-postgresql:hobby-dev --app app_nam`
7. verifiez les configurations
   `heroku config --app test001`
8. Tout pusher avec heroku pour lancer l'app
   `git push heroku main`
