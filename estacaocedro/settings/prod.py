from .base import *
import os

SITE_ID = 1
DOMAIN = 'estacaocedro.com.br'
NAME = 'estacaocedro'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'estacaocedro',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': ''
    }
}

INTERNAL_IPS = ('127.0.0.1', '45.55.192.213')

ALLOWED_HOSTS = ('*')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'generic': {
            'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            '()': 'logging.Formatter',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'server_file': {
            'class': 'logging.FileHandler',
            'formatter': 'generic',
            'filename': BASE_DIR + '/log/server.log',
        },
        'request_file': {
            'class': 'logging.FileHandler',
            'formatter': 'generic',
            'filename': BASE_DIR + '/log/request.log',
        },
        'template_file': {
            'class': 'logging.FileHandler',
            'formatter': 'generic',
            'filename': BASE_DIR + '/log/template.log',
        },
        'gunicorn_file': {
            'class': 'logging.FileHandler',
            'formatter': 'generic',
            'filename': BASE_DIR + '/log/gunicorn.log',
        },
    },
    'loggers': {
        'django.server':{
            'handlers': ['server_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.request':{
            'handlers': ['request_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template':{
            'handlers': ['template_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'gunicorn.errors':{
            'handlers': ['gunicorn_file'],
            'level': 'ERROR',
            'propagate': True,
        }
    },
}