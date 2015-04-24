# -*- coding: utf-8 -*-
"""
Django settings for openshift project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Running on OpenShift ?
ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
     ON_OPENSHIFT = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if ON_OPENSHIFT:
    try:
        SECRET_KEY = os.environ['DJANGO_SETTINGS_SECRET_KEY']
    except KeyError:
        print("Please create env variable DJANGO_SETTINGS_SECRET_KEY (cf README)")
else:
    SECRET_KEY = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz' # dev key

# SECURITY WARNING: don't run with debug turned on in production!
if ON_OPENSHIFT:
     DEBUG = False
else:
     DEBUG = True

TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'openshift','templates') ,)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
     "django.core.context_processors.request",
     "django.core.context_processors.csrf",
)

GRAPPELLI_ADMIN_TITLE = "Videopills"


# Enable debug for only selected hosts
if DEBUG:
     ALLOWED_HOSTS = []
else:
     ALLOWED_HOSTS = ['*']

# List of admins (+ 500 error report by mail)
ADMINS = (
    ('Simone Chiorazzo', 'chiora93@gmail.com'),
    ('Gabriele Ursino', 'ursinogabriele.0@gmail.com'),

)

# Application definition

INSTALLED_APPS = (
    'grappelli', # customizzatore dell'interfaccia di admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'video_manager',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'openshift.urls'

WSGI_APPLICATION = 'openshift.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if socket.gethostname() == "raspberrypi"  : # production settings
    DATABASES = {
        'default': { # you can change the backend to any django supported
                     'ENGINE':   'mysql.connector.django', # setto un ENGINE compatibile con python3 ...
                     'NAME':     "videopills_prod",
                     'USER':     "supercu",
                     'PASSWORD': "A3ternatenebrae",
                     'HOST':     "localhost",
                     'PORT':     3306,
                     }
    }
else: # dev settings

    #   Da commentare per test in locale!!!!!!!!!
    ####
    #   Imposto il db mysql che abbiamo in locale (il portatile senza schemo xD)
    ####
    DATABASES = {
        'default': { # you can change the backend to any django supported
                     'ENGINE':   'mysql.connector.django', # setto un ENGINE compatibile con python3 ...
                     'NAME':     "videopills",
                     'USER':     "supercu",
                     'PASSWORD': "A3ternatenebrae",
                     'HOST':    "192.168.1.100",
                     'PORT':     3306,
                     }
    }
    #Da scommentare per test in locale!!!!!!!!!!




# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
#

LANGUAGE_CODE = 'it_IT'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
if ON_OPENSHIFT:
    STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static',)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, '..' ,'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    #/home/admin/videopills/wsgi/static/ ,
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'..', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'