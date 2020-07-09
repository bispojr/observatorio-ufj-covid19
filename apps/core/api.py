from observatorio import settings
from django.views.decorators.http import require_GET
import datetime
import requests


@require_GET
def obtem_ultimo_dia(request): 
	"""
	Função para pegar a última data 
	de atualização da API do brasil.io.

	args:
		- request
	
	return:
		- objeto contendo a data do último dia
		disponibilizado pela API.
	
	requisitos:
		- datetime
	"""
	# a API do brasil.io so exibe os dados do ultimo dia
	hoje = datetime.date.today() 
	um_dia = datetime.timedelta(days=1) 
	ontem = hoje - um_dia  
	return ontem


@require_GET
def quantidade_estado_goias(request):
	"""
	Função para pegar a quantidade de casos
	do estado de goiás da API do brasil.io.

	args:
		- request
	
	return:
		- inteiro com a quantidade de casos
		do estado de goiás.
	
	requisitos:
		- Função api_brasil_estado do arquivo
	"""
	# obtem massa de dados
	results = api_brasil_estado(request)
	# cada estado possui um informativo geral
	# na ultima linha do dataset, facilitando as consultas
	quantidade = results["results"][0]["last_available_confirmed"]
	return int(quantidade)


@require_GET
def api_brasil_estado(request):
	"""
	Função para pegar os dados do último dia
	do estado de Goiás.

	args:
		- request
	
	return:
		- JSON contendo os dados do último dia
		do estado de goiás.
	
	requisitos:
		- Função obtem_ultimo_dia do arquivo.
	"""
	data = obtem_ultimo_dia(request)

	payload = {"state": "GO", "date": data, "city": "None"}
	headers = {'content-type': 'application/json'}
	url = settings.URL_BRASIL_IO
	results = requests.get(url, params=payload, headers=headers).json()

	return results


def quantidade_geral_brasil(request):
	"""
	Função para obter o subtotal de casos
	por estado

	args:
		- request

	return:
		- lista com o subtotal de casos
		por estado

	requisitos:
		- Função api_brasil_geral do arquivo
	"""
	# obtem massa de dados
	results = api_brasil_geral(request)

	# obtem o subtotal por estado
	quantidade = 0
	for r in results["results"]:
		quantidade += r["last_available_confirmed"]
	return quantidade
    		

@require_GET
def api_brasil_geral(request):
	"""
	Função para obter os dados da API
	do brasil.io para o Brasil.

	args:
		- request
	
	return:
		- JSON contendo os dados do Brasil
		segundo a API do brasil.io
	
	requisitos:
		- Função obtem_ultimo_dia do arquivo.
	"""
	data = obtem_ultimo_dia(request)

	payload = {"date": data, "city": "None"}
	headers = {'content-type': 'application/json'}
	url = settings.URL_BRASIL_IO
	results = requests.get(url, params=payload, headers=headers).json()
	return results
	