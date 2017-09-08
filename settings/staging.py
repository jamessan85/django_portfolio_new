from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY","<MY API KEY>")
