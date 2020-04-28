from django.shortcuts import render
from django.views.decorators.http import require_GET

def home(request):
    return render(request, "base.html", {})

@require_GET
def graficos(request, cidade):
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
        context = {
            "informacoes": informacoes,
            "querysets": [
                {
                    "categoria": "Confirmados",
                    "numero": "6",
                    "cor": "red",
                    "icone": "fas fa-user-injured"
                },
                {
                    "categoria": "Recuperados",
                    "numero": "6",
                    "cor": "purple",
                    "icone": "fas fa-virus-slash"
                },
                {
                    "categoria": "Internados",
                    "numero": "0",
                    "cor": "blue",
                    "icone": "fas fa-procedures"
                },
                {
                    "categoria": "Óbitos",
                    "numero": "0",
                    "cor": "black",
                    "icone": "fas fa-skull-crossbones"
                }
            ]
        }
        url = "graficos/jatai.html"
    elif cidade == "mineiros":
        url = "graficos/mineiros.html"

    else:
        url = "graficos/rio-verde.html"
    return render(request, url, context)

    