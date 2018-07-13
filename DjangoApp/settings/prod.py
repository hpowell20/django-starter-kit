import datetime

from DjangoApp.settings.base import *

# Turn off debugging in production
DEBUG = False
TEMPLATE_DEBUG = False

# Set the list of allowed hosts
ALLOWED_HOSTS = [
    '*',
]

# Media File Settings
MEDIA_ROOT = '/opt/rest-test/backend/media-files/'

# Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': os.environ.get('DATABASE_PORT', ''),
    }
}

# Update the token authentication token timeouts
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7)
}

