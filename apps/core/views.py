from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_GET

from apps.core.api import (quantidade_estado_goias, quantidade_geral_brasil, 
			api_brasil_estado, api_brasil_geral)
from .models import Graficos
from .models import Comparacao
from .models import Home
from .models import ComoSaoCriados
from .models import Sobre
from .models import NaMidia
from .models import Colabore
from .models import Tendencias
from .models import Equipe
from .models import Noticias

import csv 
from django.conf import settings
from pprint import pprint
from datetime import datetime
from apps.core.models.boletimEpidemiologico import BoletimEpidemiologico

def home(request):
	url = "base.html"
	context = Home.getContext(Home)

	jatai = {"header": [], "data": []}
	with open(settings.BASE_DIR + '/dados/mineiros-dados-20-05-25.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				i = 0
				for header in row:
					jatai["header"].append(header)
					i += 1
				line_count += 1
			else:
				i = 0
				data = []
				for value in row:
					if(value == '' or value == '-'):
						data.append(0)
					else:
						data.append(value)
					i += 1
				jatai["data"].append(data)
				line_count += 1
			
		pprint(jatai)

		for row in jatai["data"]:
			str_date = row[0]
			date = datetime.strptime(str_date, '%d/%m/%Y').date()
			row[0] =  date

			registro = {
				"cidade": "mineiros",
				"data_atualizacao": row[0],
				"fonte_oficial": "http://www.google.com",
				"confirmados": row[4],
				"recuperados": row[7],
				"obitos": row[6],
				"suspeitos": None,
				"investigados":  row[3],
				"descartados": int(row[3]) + int(row[5]),
				"monitorados": row[2],
				"notificados": row[1],
				"isolados": row[10],
				"internados": int(row[9]) + int(row[8]),
				"enfermaria": row[9],
				"uti": row[8]
			}

			insercao = BoletimEpidemiologico(**registro)
			insercao.save()
		

	return render(request, url, context)


@require_GET
def grafico(request, cidade):
	url = "grafico/cidade.html"
	context = Graficos.getContext(Graficos, cidade)

	return render(request, url, context)


@require_GET
def comparacao(request):
	url = "grafico/comparacao.html"
	context = Comparacao.getContext(Comparacao, request)

	return render(request, url, context)


@require_GET
def como_sao_criados(request):
	url = "grafico/como-sao-criados.html"
	context = ComoSaoCriados.getContext(ComoSaoCriados)

	return render(request, url, context)


@require_GET
def equipe(request):
    context = Equipe.getContext(Equipe)
    url = "saiba_mais/equipe.html"

    return render(request, url, context)


@require_GET
def sobre(request):
	url = "saiba_mais/sobre.html"
	context = Sobre.getContext(Sobre)

	return render(request, url, context)


@require_GET
def na_midia(request):
	url = "saiba_mais/na-midia.html"
	context = NaMidia.getContext(NaMidia)

	return render(request, url, context)


@require_GET
def colabore(request):
	url = "saiba_mais/colabore.html"
	context = Colabore.getContext(Colabore)

	return render(request, url, context)


@require_GET
def noticias(request):
	url = "saiba_mais/noticias.html"
	context = Noticias.getContext(Equipe)

	return render(request, url, context)


@require_GET
def tendencias(request, cidade):
    informacoes = Tendencias.get_informações(Tendencias, cidade)
    url = "tendencias/cidade.html"

    return render(request, url, informacoes)
