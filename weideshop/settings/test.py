# -*- coding: utf-8 -*-
from .base import *  

# Turn debug off so tests run faster
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = False

SECRET_KEY = 'password'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'HOST': '127.0.0.1',
    }
}

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# PASSWORD HASHING
# ------------------------------------------------------------------------------
# Use fast password hasher so tests run faster
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

SHOW_TOOLBAR_CALLBACK = False

INTERNAL_IPS = ['127.0.0.1',]
