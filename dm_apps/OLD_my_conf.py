# INSTRUCTIONS:  #
##################
# please refer to the README and the project wiki for the most up-to-update information.
# Duplicate this file and rename it to my_conf.py
# The 'my_conf.py' file is in the .gitignore
# create a file called prod.cnf in the root project dir to specify connection to production db server
# The 'prod.cnf' file is also in the .gitignore
# It is recommended to leave this file unmodified unless you are making improvements

import os
from decouple import config
from .utils import is_connection_available

# DO NOT INTERACT WITH THESE VARIABLES HERE
########################################################################
FORCE_DEV_DB = False
DEV_DB_NAME = None
DEV_DB_HOST = None
USING_LOCAL_DB = False
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
########################################################################

# Should Microsoft Azure AD be used for authentication? By default, if a file called `azure_oauth_settings.yml' is in the root dir, azure aad will be turned on
# this is a manual override. Uncomment to turn off AAD regardless of the presence of the above mentioned file.
AZURE_AD = False

# Should the ticketing app be displayed on the main index page?
SHOW_TICKETING_APP = True

# Should DEBUG mode be turned on? Uncomment the line below to turn on debugging
DEBUG = True

# To add any custom hosts to this application's list of allowed hosts, provide them here
ALLOWED_HOSTS_TO_ADD = []

# Specify the full url of the site. This is used in email templates to link the recipient back to the site
SITE_FULL_URL = "http://localhost:8000"

# If the line below is uncommented, you will connect to the dev database even if production database strings are present
FORCE_DEV_DB = True

# check to see if the which databases are available:
IS_PROD_DB_AVAILABLE = is_connection_available("PROD")
IS_DEV_DB_AVAILABLE = is_connection_available("DEV")

# if a database is listed and we are not forcing dev mode...
if IS_PROD_DB_AVAILABLE and not FORCE_DEV_DB:
    USING_PRODUCTION_DB = True
# otherwise, check to see if we can connect to a dev db
elif IS_DEV_DB_AVAILABLE:
    # There are 3 scenarios: 1) there is no PROD_DB_NAME in the .env file; 2) FORCE_DEV_DB is set to True; or 3) both
    if IS_PROD_DB_AVAILABLE:
        print("production connection string is present however running dev mode since FORCE_DEV_MODE setting is set to True")
    # this variable is used in base.html to indicate which database you are connected to
    USING_PRODUCTION_DB = False
    # if we have a connection to dev, get the names of db and host to pass in as context processors
    DEV_DB_NAME = config('DEV_DB_NAME')
    DEV_DB_HOST = config('DEV_DB_HOST')
else:
    USING_PRODUCTION_DB = False
    USING_LOCAL_DB = True

# add new applications to this dictionary; grey out any app you do not want
# the dict key should be the actual name of the app
# if there is a verbose name, it should be the key value, otherwise None
APP_DICT = {
    'inventory': 'Metadata Inventory',
    # 'grais': 'grAIS',
    # 'oceanography': 'Oceanography',
    # 'herring': 'HerMorrhage',
    'camp': 'CAMP db',
    # 'meq': 'Marine environmental quality (MEQ)',
    # 'diets': 'Marine diets',
    # 'projects': 'Science project planning',
    # 'ihub': 'iHub',  # dependency on masterlist
    # 'scifi': 'SciFi',
    # 'masterlist': 'Masterlist',
    # 'shares': 'Gulf Shares',
    'travel': 'Travel Management System',
    # 'sar_search': "SAR Search",
    # 'spot': 'Grants & Contributions (Spot)',  # dependency on masterlist, sar_search
    # 'ios2': 'Instruments',
    # 'staff': "Staff Planning Tool",
    # 'publications': "Project Publications Inventory",
    # 'trapnet': "TrapNet",
    # 'whalesdb': "Whale Equipment Deployment Inventory",
    # 'vault': "Whale Equipment Deployment Inventory",
    # 'necropsy': "Whale Equipment Deployment Inventory",
}

MY_INSTALLED_APPS = [app for app in APP_DICT]

# Specify your database connection details
if USING_LOCAL_DB:
    print("Database connection information missing from environmental variables. Using local Sqlite db")
    my_default_db = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
else:
    DB_CONNECTION_PREFIX = "PROD" if USING_PRODUCTION_DB else "DEV"
    my_default_db = {
        'ENGINE': 'django.db.backends.mysql',
        'TIME_ZONE': 'America/Halifax',
        'OPTIONS': {
            'host': config(DB_CONNECTION_PREFIX + '_DB_HOST'),
            'port': config(DB_CONNECTION_PREFIX + '_DB_PORT', cast=int),
            'database': config(DB_CONNECTION_PREFIX + '_DB_NAME'),
            'user': config(DB_CONNECTION_PREFIX + '_DB_USER'),
            'password': config(DB_CONNECTION_PREFIX + '_DB_PASSWORD'),
            'init_command': 'SET default_storage_engine=INNODB',
        }}

DATABASES = {
    'default': my_default_db,
}

###########################################################################
# this is for pycharm
WEB_APP_NAME = "DMApps"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
from django.utils.translation import gettext_lazy as _

# Quick-start development set
SECRET_KEY = '***REMOVED***'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrap4',
    'el_pagination',
    'easy_pdf',
    'accounts',
    'lib',
    'shared_models',
    'tickets',
    'inventory',
    'grais',
    'oceanography',
    'herring',
    'camp',
    'meq',
    'diets',
    'projects',
    'ihub',
    'scifi',
    'masterlist',
    'shares',
    'travel',
    'spot',
    'ios2',
    'trapnet',
    'tracking',
    'sar_search',
]

ROOT_URLCONF = 'dm_apps.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dm_apps.context_processor.my_envr'
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Halifax'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]

SITE_FROM_EMAIL = "DoNotReply.DMApps@Azure.Cloud.dfo-mpo.gc.ca"
