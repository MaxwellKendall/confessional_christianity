"""
WSGI config for confessional_christianity_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'confessional_christianity_api.settings')

application = get_wsgi_application()
