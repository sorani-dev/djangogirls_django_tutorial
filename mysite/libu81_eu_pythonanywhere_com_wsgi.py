# This file contains the WSGI configuration required to serve up your
# Django app
import os
import sys

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

my_project_dir = "~/libu81.eu.pythonanywhere.com"

project_folder = os.path.expanduser(my_project_dir)  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# Add your project directory to the sys.path
settings_path = '/home/libu81/libu81.eu.pythonanywhere.com'
sys.path.insert(0, settings_path)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# Set the 'application' variable to the Django wsgi app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
