import os
from datetime import timedelta
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).parents[2]
SECRET_KEY = 'django-insecure-gsixjqq$e#2qf1#b34ur&@_czsbav)ia4d(!ytkux)((m6mw$t'
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
ALLOWED_HOSTS = ['0.0.0.0']
SITE_ID = 1

##################################################################
# Debug settings (with docker)
##################################################################

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

##################################################################
# Databases settings (with docker)
##################################################################

DATABASES = {'default': dj_database_url.config()}

###################################################################
# Templates, middleware settings
##################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://0.0.0.0:8000",
]

CORS_ALLOW_CREDENTIALS = True

##################################################################
# Password validation settings
##################################################################

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

##################################################################
# Static files settings (CSS, JavaScript, Images)
##################################################################

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
STATICFILES_DIRS = ('static',)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

FILE_UPLOAD_PERMISSIONS = 0o777
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o777

##################################################################
# REST FRAMEWORK
##################################################################

ANONYMOUS_USER_THROTTLE_RATE = os.environ.get('ANONYMOUS_USER_THROTTLE_RATE', 10_000)
AUTHENTICATED_USER_THROTTLE_RATE = os.environ.get('AUTHENTICATED_USER_THROTTLE_RATE', 10_000)

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': f'{ANONYMOUS_USER_THROTTLE_RATE}/day',
        'user': f'{AUTHENTICATED_USER_THROTTLE_RATE}/day',
    }
}

##################################################################
# Redis setting
##################################################################

REDIS_HOST = 'redis'
REDIS_PORT = '6379'

##################################################################
# Celery setting
##################################################################

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

##################################################################
# Custom user settings
##################################################################

AUTH_USER_MODEL = 'users.User'

##################################################################
# Default auto field settings
##################################################################

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
