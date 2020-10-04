"""
WSGI config for Apis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""


import os
import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
from django.core.wsgi import get_wsgi_application
from os.path import join, dirname, abspath


PROJECT_DIR = dirname(dirname(abspath(__file__)))

sys.path.insert(0, PROJECT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Apis.settings')

application = get_wsgi_application()
