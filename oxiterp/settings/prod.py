from oxiterp.settings.base import *

# Override base.py settings here


DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'oxit_modaasist',
        'USER': 'oxitowner',
        'PASSWORD': 'oxit2016',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = "/var/www/static/modaasist"

STAICFILES_DIR = [

    "/var/www/static/modaasist"

]

try:
    from oxiterp.settings.local import *
except:
    pass
