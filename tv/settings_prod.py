from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cv',
        'USER': 'dimoka_user',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': ':',
    }
}