"""
Este arquivo realiza um dump do banco de dados
e salva em um arquivo chamado: dumpPrivado.json

Para utilizar este arquivo basta estar no diretório
raiz do projeto e digitar o comando:

python dumpPrivado.py

O arquivo será criado com o dump dos dados que estão
no banco.

Dados como contenttypes e auth não estão no dump.

É possível realizar esta ação diretamente no terminal
pelo seguinte comando:

python manage.py dumpdata --exclude auth --exclude contenttypes --indent 4 > dump.json

Um arquivo json com nome dump.json será criado com as mesmas
informações.
"""

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