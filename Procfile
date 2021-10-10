export PROD_SETTINGS=$PROD_SETTINGS
web: gunicorn -e PROD_SETTINGS=$PROD_SETTINGS django_heroku_deploy.wsgi --log-level debug