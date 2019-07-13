from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'simpledjango',
        'USER': 'simpledjangouser',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': ':',
    }
}