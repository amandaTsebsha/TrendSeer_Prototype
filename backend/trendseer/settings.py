import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'

DEBUG = True

ALLOWED_HOST = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

#URL routing configuration

ROOT_URLCONF = 'trendseer.urls'
# Templates (optional if you plan to use Django's template system)
TEMPLATES = [
{
    'BACKEND':
    'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#WSGI application for serving the app
WSGI_APPLICATION = 'trendseer.wsgi.application'

#Database configuration(using SQLite for simplicity

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3'
    }
}

#Internationalization settings

LANGUAGE_CODE = 'en-uk'
TIME_ZONE = 'UCT'
USE_I18N = True
USE_L10N = True
USE_TZ = True


#Static files (CSS, JavaScript, images)

STATIC_URL = '/static/'

#Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
