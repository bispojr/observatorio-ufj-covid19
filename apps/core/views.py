from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods

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
from apps.core.models import BoletimEpidemiologico

from .forms.createForm import CreateBoletimEpidemiologicoForm
from .forms.deleteForm import DeleteBoletimEpidemiologicoForm

import csv 
from django.conf import settings
from pprint import pprint
from datetime import datetime


@require_GET
def createBoletimEpidemiologico(request):
	url = "forms/createForm.html"
	form = CreateBoletimEpidemiologicoForm(request.POST)
	if form.is_valid():
		req = BoletimEpidemiologico.cleanDataForm(BoletimEpidemiologico, form)
		try:
			BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, req)
		except BoletimEpidemiologico.DoesNotExist:
			return ("Boletim não existe")

	context = {'form': form}
	return render(request, url, context)

@require_GET
def deleteBoletimEpidemiologico(request):	
	url = "forms/deleteForm.html"
	form = DeleteBoletimEpidemiologicoForm(request.GET)
	boletim = None

	if form.is_valid():
		req = {
			'cidade': form.cleaned_data['cidade'],
			'data_atualizacao' : form.cleaned_data['data_atualizacao']
		}
		BoletimEpidemiologico.get_delete_boletim(BoletimEpidemiologico, req)

	context = {'form': form}
	return render(request, url, context)

@require_GET
def readBoletimEpidemiologico(request):
	url = "forms/readForm.html"
	form = DeleteBoletimEpidemiologicoForm(request.GET)
	boletim = None
	if form.is_valid():
		req = {
			'cidade': form.cleaned_data['cidade'],
			'data_atualizacao' : form.cleaned_data['data_atualizacao']
		}
		boletim = BoletimEpidemiologico.get_read_boletim(BoletimEpidemiologico, req)

	context = {'form': form,
		'boletim': boletim}

	return render(request, url, context)

@require_GET
def updateBoletimEpidemiologico(request):	
	url = "forms/updateForm.html"
	form = CreateBoletimEpidemiologicoForm(request.POST)
	if form.is_valid():
		req = BoletimEpidemiologico.cleanDataForm(BoletimEpidemiologico, form)
		try:
			BoletimEpidemiologico.get_update_boletim(BoletimEpidemiologico, req)
		except BoletimEpidemiologico.DoesNotExist:
			return ("Boletim não existe")
	
	context = {'form': form}
	return render(request, url, context)	

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

			registro={}
			# registro = {
			# 	"cidade": "Jataí",
			# 	"data_atualizacao": row[0],
			# 	"fonte_oficial_url": "http://www.google.com",
			# 	"fonte_oficial_tipo": "indefinido",
			# 	"confirmados": row[1],
			# 	"descartados": row[2],
			# 	"sus_investigados": row[3],
			# 	"notificados": row[4],
			# 	"isolados": row[5],
			# 	"iso_hospitalar": row[6],
			# 	"monitorados": row[7],
			# 	"recuperados": row[8],
			# 	"obitos": row[9],
			# }
			# registro = {
			# 	"cidade": "Mineiros",
			# 	"data_atualizacao": row[0],
			# 	"fonte_oficial_url": "http://www.google.com",
			# 	"fonte_oficial_tipo": "indefinido",
			# 	"notificados": row[1],
			# 	"monitorados": row[2],
			# 	"descartados": int(row[3])+int(row[5]),
			# 	"confirmados": row[4],
			# 	"obitos": row[6],
			# 	"recuperados": row[7],
			# 	"iso_hosp_sus_uti": row[8],
			# 	"iso_hosp_sus_enf": row[9],
			# 	"iso_hospitalar": int(row[8]) + int(row[9]),
			# 	"iso_domiciliar": row[10],
			# 	"sus_investigados": row[11],
			# }
			# registro = {
			# 	"cidade": "Chapadão do Ceu",
			# 	"data_atualizacao": row[0],
			# 	"fonte_oficial_url": "http://www.google.com",
			# 	"fonte_oficial_tipo": "indefinido",
			# 	"confirmados": row[1],
			# 	"descartados": row[2],
			# 	"sus_investigados": row[3],
			# 	"suspeitos": row[4],
			# 	"notificados": row[5],
			# 	"isolados": row[6],
			# 	"iso_hospitalar": row[7],
			# 	"monitorados": row[8],
			# 	"recuperados": row[9],
			# 	"obitos": row[10],
			# }
			# registro = {
			# 	"cidade": "Rio Verde",
			# 	"data_atualizacao": row[0],
			# 	"fonte_oficial_url": "http://www.google.com",
			# 	"fonte_oficial_tipo": "indefinido",
			# 	"confirmados": row[1],
			# 	"descartados": row[2],
			# 	"sus_investigados": row[3],
			# 	"notificados": row[4],
			# 	"isolados": row[5],
			# 	"iso_hospitalar": row[6],
			# 	"monitorados": row[7],
			# 	"recuperados": row[8],
			# 	"obitos": row[9],
			# }

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
