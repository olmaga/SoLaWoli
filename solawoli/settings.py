"""
Django settings for solawoli project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8cd-j&jo=-#ecd1jjulp_s*7y$n4tad(0d_g)l=6@n^r8fg3rn'

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'True')=='True'

ALLOWED_HOSTS = ['my','solawoli.juntagrico.science', 'localhost',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'juntagrico',
    'impersonate',
    'solawoli',
]

ROOT_URLCONF = 'solawoli.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','solawoli.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'juntagrico.personalisation.loaders.personal_directories.Loader'
            ],
            'debug' : True
        },
    },
]

WSGI_APPLICATION = 'solawoli.wsgi.application'


LANGUAGE_CODE = 'de_CH'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware'
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/my/home"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

MEMBER_STRING = "Mitglied"
MEMBERS_STRING = "Mitglieder"
ASSIGNMENT_STRING = "Mitglied"
ASSIGNMENTS_STRING = "Arbeitseinsätze"
ORGANISATION_NAME = "solawoli"
ORGANISATION_LONG_NAME = "solawoli"
ORGANISATION_ADDRESS = {"name":"solawoli", 
            "street" : "Bahnhofstrasse",
            "number" : "3",
            "zip" : "8001",
            "city" : "Zürich",
            "extra" : "Nüüüt"}
ORGANISATION_PHONE =''
ORGANISATION_BANK_CONNECTION = {"PC" : "fig di selber",
            "IBAN" : "PC soöppis",
            "BIC" : "088080",
            "NAME" : "ZKB",
            "ESR" : ""}
INFO_EMAIL = "oliver.ganz@gmail.com"
SERVER_URL = "www.solawoli.org"
ADMINPORTAL_NAME = "mySoLaWoli"
ADMINPORTAL_SERVER_URL = "my"
BUSINESS_REGULATIONS = "/static/docs/business_regulations.pdf"
BYLAWS = "/static/docs/bylaws.pdf"
STYLE_SHEET = "/static/css/personal.css"
BOOTSTRAP = "/static/external/bootstrap-3.3.1/css/bootstrap.min.css"
FAVICON = "/static/img/favicono.ico"
FAQ_DOC = "/static/doc/fac.pdf"
EXTRA_SUB_INFO = "/static/doc/extra_sub_info.pdf"
ACTIVITY_AREA_INFO = "/static/doc/activity_area_info.pdf"
SHARE_PRICE = "200"
PROMOTED_JOB_TYPES = []
PROMOTED_JOBS_AMOUNT = 2
DEPOT_LIST_GENERATION_DAYS = [1,2,3,4,5,6,7]	
BILLING = False
BUSINESS_YEAR_START = {"day":1, "month":1}
BUSINESS_YEAR_CANCELATION_MONTH = 10
IMAGES = {'status_100': '/static/img/status_100.png',
            'status_75': '/static/img/status_75.png',
            'status_50': '/static/img/status_50.png',
            'status_25': '/static/img/status_25.png',
            'status_0': '/static/img/status_0.png',
            'single_full': '/static/img/single_full.png',
            'single_empty': '/static/img/single_empty.png',
            'single_core': '/static/img/single_core.png',
            'core': '/static/img/core.png'}
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
EMAILS = {
    'welcome': 'mails/welcome_mail.txt',
    'co_welcome': 'mails/welcome_added_mail.txt',
    'password': 'mails/password_reset_mail.txt',
    'j_reminder': 'mails/job_reminder_mail.txt',
    'j_canceled': 'mails/job_canceled_mail.txt',
    'confirm': 'mails/confirm.txt',
    'j_changed': 'mails/job_time_changed_mail.txt',
    'j_signup': 'mails/job_signup_mail.txt',
    'd_changed': 'mails/depot_changed_mail.txt',
    's_canceled': 'mails/subscription_canceled_mail.txt',
    'b_share': 'mails/bill_share.txt',
    'b_sub': 'mails/bill_sub.txt',
    'b_esub': 'mails/bill_extrasub.txt'
}