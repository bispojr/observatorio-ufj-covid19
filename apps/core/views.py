from django.shortcuts import render
from django.views.decorators.http import require_GET

def home(request):
    return render(request, "base.html", {})

@require_GET
def grafico(request, cidade):
    if cidade == "jatai":
        informacoes = {
            "cidade": "Jataí",
	        "nome_base": "jatai",
	        "url_fonte": "https://www.jatai.go.gov.br/",
	        "nome_fonte": "Secretária de Saúde de Jataí",

            "data": "22 de abril",
            "conf_num": "6",
            "rec_num": "6",
            "int_num": "0",
            "obt_num": "0"
        }
    elif cidade == "mineiros":
        informacoes = {
            "cidade": "Mineiros",
	        "nome_base": "mineiros",
	        "url_fonte": "http://mineiros.go.gov.br/covid-19.php",
	        "nome_fonte": "Secretária de Saúde de Mineiros",

            "data": "22 de abril",
            "conf_num": "4",
            "rec_num": "0",
            "int_num": "4",
            "obt_num": "0"
        }
    else:
        informacoes = {
            "cidade": "Rio Verde",
	        "nome_base": "mineiros",
	        "url_fonte": "https://www.rioverde.go.gov.br/covid19/",
	        "nome_fonte": "Secretária de Saúde de Rio Verde",

            "data": "22 de abril",
            "conf_num": "13",
            "rec_num": "9",
            "int_num": "1",
            "obt_num": "1"
        }

    url = "grafico/cidade.html"
    context = {
        "informacoes": informacoes,
        "querysets": [
            {
                "categoria": "Confirmados",
                "numero": informacoes["conf_num"],
                "cor": "red",
                "icone": "fas fa-user-injured"
            },
            {
                "categoria": "Recuperados",
                "numero": informacoes["rec_num"],
                "cor": "purple",
                "icone": "fas fa-virus-slash"
            },
            {
                "categoria": "Internados",
                "numero": informacoes["int_num"],
                "cor": "blue",
                "icone": "fas fa-procedures"
            },
            {
                "categoria": "Óbitos",
                "numero": informacoes["obt_num"],
                "cor": "black",
                "icone": "fas fa-skull-crossbones"
            }
        ]
    }
    return render(request, url, context)

    