# Python imports
import os
from os.path import join
from pathlib import Path

# project imports
from .development import *
from .common import *

# uncomment the following line to include i18n
# from .i18n import *

BASE_DIR = Path(__file__).resolve().parent.parent
# ##### DEBUG CONFIGURATION ###############################
DEBUG = True
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.user.apps.UserConfig',
    'django_crontab'
]
# allow all hosts during development
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# adjust the minimal login
# LOGIN_URL = 'core_login'
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = 'core_login'


# ##### DATABASE CONFIGURATION ############################
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': join(PROJECT_ROOT, 'run', 'dev.sqlite3'),
#     }
# }


