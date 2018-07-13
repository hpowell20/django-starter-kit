import datetime

from DjangoApp.settings.base import *

# Database Settings
# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'eigen_elp',
#     'USER': 'eigen',
#     'PASSWORD': 'eigen',
#     'HOST': 'localhost',
#     'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': get_env_variable('DATABASE_DRIVER'),
#         'NAME': get_env_variable('DATABASE_NAME'),
#         'USER': get_env_variable('DATABASE_USER'),
#         'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
#         'HOST': get_env_variable('DATABASE_HOST'),
#         'PORT': get_env_variable('DATABASE_PORT'),
#     }
# }

# Absolute filesystem path to the directory that will hold user-uploaded files.
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Go down one level for the media-files
#MEDIA_ROOT = os.path.join(PROJECT_ROOT, os.pardir, 'media-files')
MEDIA_ROOT = '/opt/starter-kit/media-files'

MEDIA_URL = "http://localhost:8000/starter-kit/media/"

S3_MEDIA_URL = "http://localhost:8000/starter-kit/s3-media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, os.pardir, 'static-files')

# Set the default token authentication token timeouts
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=14)
}

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the applications
NOSE_ARGS = [
    #'--with-coverage',
    #'--cover-package=authentication,learning_platform',  # Restrict coverage to selected packages
    '--cover-erase',  # Remove coverage results from the last run
    '--cover-html',  # Enable HTML report
    '--cover-inclusive',  # Scan all files in the working directories
]