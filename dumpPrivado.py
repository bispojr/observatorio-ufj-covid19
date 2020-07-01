import django
from django.conf import settings
import observatorio.settings as config
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'observatorio.settings')
django.setup()

from django.core import management
from django.core.management.commands import dumpdata


with open('dumpPrivado.json', 'w') as f:
    management.call_command('dumpdata', indent=4, exclude=['contenttypes','auth'], stdout=f)