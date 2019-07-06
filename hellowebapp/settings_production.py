# Inherit from standard settings file for default
from hellowebapp.settings import *
# Everything below will override our standard settings:
# Parse database configuration from $DATABASE_URL
import dj_database_url
