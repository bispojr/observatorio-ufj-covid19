from observatorio import settings
from django.views.decorators.http import require_GET
import datetime
import requests


@require_GET
def obtem_ultimo_dia(request): 
	# a API do brasil.io so exibe os dados do ultimo dia
	hoje = datetime.date.today() 
	um_dia = datetime.timedelta(days=1) 
	ontem = hoje - um_dia  
	return ontem


@require_GET
def quantidade_estado_goias(request):
	# obtem massa de dados
	results = api_brasil_estado(request)
	print(results)
	# cada estado possui um informativo geral
	# na ultima linha do dataset, facilitando as consultas
	quantidade = results["results"][0]["last_available_confirmed"]
	return int(quantidade)


@require_GET
def api_brasil_estado(request):
	data = obtem_ultimo_dia(request)

	payload = {"state": "GO", "date": data, "city": "None"}
	headers = {'content-type': 'application/json'}
	url = settings.URL_BRASIL_IO
	results = requests.get(url, params=payload, headers=headers).json()

	return results


def quantidade_geral_brasil(request):
	# obtem massa de dados
	results = api_brasil_geral(request)

	# obtem o subtotal por estado
	quantidade = 0
	for r in results["results"]:
		quantidade += r["last_available_confirmed"]
	return quantidade
    		

@require_GET
def api_brasil_geral(request):
	data = obtem_ultimo_dia(request)

	payload = {"date": data, "city": "None"}
	headers = {'content-type': 'application/json'}
	url = settings.URL_BRASIL_IO
	results = requests.get(url, params=payload, headers=headers).json()
	return results
	