"""
Django settings for eurocard project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '655ogv2f!6=x5a(kk603$op3gnjb*c11@^nje9morq^ta@g+m5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '.eurocard.naminteresno.ru',
    '.eurocard.naminteresno.ru.',
    '.eurocard.ru',
    '.eurocard.ru.',

]

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'south',
    'config',
    'menu',
    'articles',
    'orders',
    "mailshelf",
    "sorl.thumbnail",
    "rollyourown.seo",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

ROOT_URLCONF = 'eurocard.urls'

WSGI_APPLICATION = 'eurocard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    '/home/www/eurocard/theme',
)

try:
    from local_settings import *
except ImportError, exp:
    pass

