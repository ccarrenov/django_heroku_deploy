#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    prod_settings = os.environ.get('PROD_SETTINGS')
    print('PROD_SETTINGS: '.format(prod_settings))

    if prod_settings and prod_settings == 'True':
        print('LOAD PROD SETTINGS')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_heroku_deploy.settings-prod')
    else:
        print('LOAD DEVELOPMENT SETTINGS')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_heroku_deploy.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
