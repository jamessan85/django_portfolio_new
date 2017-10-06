from base import *



import dj_database_url

DEBUG = False

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY","<MY API KEY>")
