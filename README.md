# DJANGO HEROKU DEPLOY

Aplicación Web con Django Framework, configurado para ser desplegado de forma local y de forma productiva sobre heroku.

# ¿Qué es Heroku?

Heroku es un servicio PaaS (Plataforma como servicio) lo que permite poseer herramientas de software y hardware preconfiguradas
con la finalidad de desplegar y publicar aplicaciones web personalizadas.

# Configuración

Se realiza configuración de settings y wsgi, generando un settings-prod y wsgi-prod con la finalidad de poseer configuraciones para despliegue local y despliegue sobre heroku. A continuación se explicará con más detalle las configuraciones realizadas.

A diferencia del entorno local o de desarrollo, heroku posee una configuración distinta para el despliegue. La primera diferencia sustancial que podemos mencionar es el servidor de aplicaciones en donde se desplegará nuestra aplicación web. Si accedemos a la documentación en la página oficial de Django](https://docs.djangoproject.com/en/dev/ref/django-admin/#runserver) se menciona que el servidor por defecto que posee este framework solo esta disponible para programar (de forma local) y que si se desea pasar a un ambiente productivo este no debe ser ocupado, ya que no ha pasado pruebas de auditoria, rendimiento y seguridad. Además señalan que por ser su negocio el de generar un framework de python web y no la de crear un servidor de aplicaciones web, esto seguira siendo de esta forma.

Debido a lo antes mencionado, existen diversas soluciones de terceros que nos permiten desplegar nuestra aplicación web de forma productiva. El servidor que utilizaremos sobre heroku será gunicorn, posteriormente se mencionara como usar.

## Creación settings-prod y wsgi-prod

Para diferenciar configuraciones productivas y de desarrollo, se poseen diversos mecánismos. En este proyecto se eligió la utilización de archivos totalmente independientes para los despliegues, esta verificación se realiza mediante una variable de entorno llamada PROD_SETTINGS, que es verificada en el archivo manage.py. Dicha variable debe existir y poseer el valor igual a **True**, en caso contrario solo se utilizaran los archivos **settings.py** y **wsgi.py** que posee por defecto el proyecto al ser creado con los comando de Django.

[image](django-deploy.png)

## Configuración manage.py

El archivo manage.py es el que posee la configuración de la ruta y el nombre del archivo que será usado en la configuración de nuestro proyecto Django. Para este caso definiremos una regla que permita verificar si existe una variable de entorno que definirá si se utilizará el settings.py por defecto que se posee y se utilizará el settings.prod

