"""
Django settings for DjangoApp project.
"""

import os

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#xhuzxixskc+is0j0=((#v_^8f)ae=nj(2yc#z=)-xi5hkm$q2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
DEFAULT_APPS = (
    # Site administration applications
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Common applications
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    # Third party applications
    'rest_framework',
    'django_filters',

    # Code coverage applications
    'django_nose',
)

LOCAL_APPS = (
    # Internal applications
    'authentication.apps.AuthenticationConfig',
    'users.apps.UsersConfig'
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    # Site Administration Middleware Classes (used by API Log In button on API list)
    # Not required if headless or using JWT authentication
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # Common Middleware Classes
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Internal middleware
    'users.api.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'DjangoApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'DjangoApp.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

# Set the timezone information
USE_TZ = True

# The timezone of the running application used by the display forms
#TIME_ZONE = 'Canada/Atlantic'
TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# Set the default REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50
}

# Set the custom auth user model and authentication scheme
AUTH_USER_MODEL = 'authentication.User'
AUTHENTICATION_BACKENDS = (
    'authentication.backends.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


