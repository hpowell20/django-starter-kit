from DjangoApp.settings.base import *

#if 'test' in sys.argv:
    # Turn off debugging when running the tests
    #DEBUG = True
    #TEMPLATE_DEBUG = True

    # Set the database to be in memory
    #DATABASES['default'] = {
     #   'ENGINE': 'django.db.backends.sqlite3',
      #  'NAME': 'unit_test_db'
    #}

    # Change the password hashing used
    #PASSWORD_HASHERS = (
     #   'django.contrib.auth.hashers.MD5PasswordHasher',
    #)

# Turn off debugging when running the tests
DEBUG = False
TEMPLATE_DEBUG = False

# Define the in memory database to be used
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'unit_test_db',
    }
}

# Change the password hashing used
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)