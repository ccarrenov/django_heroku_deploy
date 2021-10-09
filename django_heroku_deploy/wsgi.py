"""
WSGI config for django_heroku_deploy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

prod_settings = os.getenv('PROD_SETTINGS')
print('PROD_SETTINGS: '.format(prod_settings))

if not prod_settings and prod_settings == 'True':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_heroku_deploy.settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_heroku_deploy.settings-prod.py')

application = get_wsgi_application()
