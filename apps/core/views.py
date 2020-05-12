from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_GET
from django.http import JsonResponse

import requests
import datetime
import json
from collections import Counter
from observatorio import settings
from apps.core.api import (quantidade_estado_goias, quantidade_geral_brasil, 
							api_brasil_estado, api_brasil_geral)
from .models import Graficos

def home(request):
	context = {
		"grupo": "geral",
		"script": "geral",
		"grupo_link": "principal",
		"titulo": "Observatório UFJ Covid-19 - Principal"
	}
	return render(request, "base.html", context)


@require_GET
def grafico(request, cidade):
	url = "grafico/cidade.html"
	context = Graficos.getContext(Graficos, cidade)

	return render(request, url, context)


@require_GET
def comparacao(request):
	quantidade_goias = quantidade_estado_goias(request)
	quantidade_brasil = quantidade_geral_brasil(request)
	context = {
		"grupo": "graficos",
		"grupo_link": "graficos",
		"script": "graficos-comparacao",
		"titulo": "Observatório UFJ Covid-19 - Comparação entre as cidades",
		"nome_base": "jatai",
		"goias": quantidade_goias,
		"brasil": quantidade_brasil
	}
	return render(request, "grafico/comparacao.html", context)


@require_GET
def como_sao_criados(request):
	context = {
		"grupo": "geral",
		"grupo_link": "graficos",
		"script": "geral",
		"titulo": "Observatório UFJ Covid-19 - Créditos"
	}
	return render(request, "grafico/como-sao-criados.html", context)


@require_GET
def equipe(request):
    context = {
		"script": "geral",
		"grupo": "equipe",
		"grupo_link": "saiba_mais",
		"titulo": "Observatório UFJ Covid-19 - Equipe",
        "parceiros": [
            {  
				"nome": "#TodosContraoCorona",
				"short": "todoscontraocorona",
				"url": "https://www.facebook.com/centrouniversitariodemineiros",
				"plataforma": "Facebook",
				"content": "Projeto de conscientização diária em relação ao combate ao Covid-19 promovido pela Unifimes."
			},
			{
				"nome":	"Covid Goiás",
				"short": "covid-goias",
				"url": "https://covidgoias.ufg.br/",
				"plataforma": "Link",
				"content": "Observatório estadual conduzido pelo LAPIG-UFG com dados sobre o Covid-19 do estado de Goiás."
            }
        ],
        "querysets": [
            {
				"nome": "Prof. Esdras L. Bispo Jr.",
				"short": "esdras",
				"url": "http://lattes.cnpq.br/1022072289836952",
				"plataforma": "Lattes",
				"content": "Idealizador do Observatório. Pesquisador na área de Educação e Inteligência Artificial"
			},
			{
				"nome": "Profa. Joslaine Jeske",
				"short": "joslaine",
				"url": "http://lattes.cnpq.br/2394348610492496",
				"plataforma": "Lattes",
				"content": "Responsável pelos dados da cidade de Rio Verde. Pesquisadora na área de Inteligência Artificial."
			},
			{
				"nome":	"Profa. Franciny Medeiros",
				"short": "franciny",
				"url": "http://lattes.cnpq.br/2821748091466181",
				"plataforma": "Lattes",
				"content": "Responsável pelos dados de Jataí e pela comunicação. Pesquisadora na área de Engenharia de Software."
			},
			{
				"nome":	"Prof. Márcio Lopes",
				"short": "marcio",
				"url": "http://lattes.cnpq.br/8846703586256426",
				"plataforma": "Lattes",
				"content": "Responsável pelos dados da cidade de Mineiros. Pesquisador na área de Computação em Névoa."
			},
			{
				"nome":	"Prof. Marcelo Freitas",
				"short": "marcelo",
				"url": "http://lattes.cnpq.br/0972390630476077",
				"plataforma": "Lattes",
				"content": "Responsável pelas notícias em relação ao Covid-19. Pesquisa sobre Sistemas Operacionais."
			},
			{
				"nome": "Prof. Zaqueu Souza",
				"short": "zaqueu",
				"url": "http://lattes.cnpq.br/8132493439297747",
				"plataforma": "Lattes",
				"content": "Colaborador-parceiro do Todos Contra o Corona. Professor de Engenharia Ambiental na Unifimes."
			},
			{
				"nome":	"Profa. Edlaine Vilela",
				"short": "edlaine",
				"url": "http://lattes.cnpq.br/8767578610764666",
				"plataforma": "Lattes",
				"content": "Consultora sobre questões epidemiológicas. Professora de Medicina na UFJ."
			},
			{
				"nome": "Prof. Manuel Ferreira",
				"short": "manuel",
				"url": "http://lattes.cnpq.br/4498594723433539",
				"plataforma": "Lattes",
				"content": "Colaborador-parceiro do Covid-Goiás. Professor da área de Geoprocessamento na UFG."
			},
			{
				"nome": "Prof. Luiz Pascoal",
				"short" :"luiz",
				"url": "http://lattes.cnpq.br/9189310566441445",
				"plataforma": "Lattes",
				"content": "Colaborador-parceiro do Covid-Goiás. Professor da área de Sistemas Distribuídos no SENAI."
			},
			{
				"nome": "Diego Costa",
				"short" :"diego",
				"url": "https://www.diegocosta.dev/",
				"plataforma": "Link",
				"content": "Colaborador no desenvolvimento da página. Analista Programador na Unimed na cidade de Rio Verde."
			},
			{
				"nome": "Felipe Nedopetalski",
				"short": "felipe",
				"url": "https://www.linkedin.com/in/felipe-nedopetalski-91b93b154/",
				"plataforma": "LinkedIn",
				"content": "Colaborador no desenvolvimento da página. Graduando em Ciências da Computação na UFJ."
			},
			{
				"nome": "Gabriel Santos",
				"short": "gabriel",
				"url": "https://www.linkedin.com/in/dev-gabriel-santos/",
				"plataforma": "LinkedIn",
				"content": "Colaborador no desenvolvimento da página. Graduando em Ciências da Computação na UFJ."
            }
        ]
    }
    template = "saiba_mais/equipe.html"
    return render(request, template, context)


@require_GET
def sobre(request):
    context = {
		"grupo": "geral",
		"grupo_link": "saiba_mais",
		"script": "geral",
		"titulo": "Observatório UFJ Covid-19 - Sobre"
		}
    return render(request, "saiba_mais/sobre.html", context)


@require_GET
def na_midia(request):
	context = {
		"grupo": "geral", 
		"grupo_link": "saiba_mais",
		"script": "na-midia",
		"titulo": "Observatório UFJ Covid-19 - Na Mídia"
		}
	return render(request, "saiba_mais/na-midia.html", context)


@require_GET
def colabore(request):
	context = {
		"grupo": "geral",
		"grupo_link": "saiba_mais",
		"script": "Observatório UFJ Covid-19 - Colabore"
		}
	return render(request, "saiba_mais/colabore.html", context)


@require_GET
def noticias(request):
	context = {
		"grupo": "", 
		"grupo_link": "noticias",
		"script": "noticias",
		"titulo": "Observatório UFJ Covid-19 - Notícias"
		}
	return render(request, "saiba_mais/noticias.html", context)


@require_GET
def tendencias(request, cidade):
    if cidade == "jatai":
        informacoes = {
			"grupo": "tendencias",
			"grupo_link": "tendencias",
			"script": "tendencias-jatai",
			"titulo": "Observatório UFJ Covid-19 - Tendências (Jataí)",
            "cidade": "Jataí (GO)",
	        "nome_base": "jatai"
        }
    else:
        informacoes = {
			"grupo": "tendencias",
			"grupo_link": "tendencias",
			"script": "tendencias-rioverde",
			"titulo": "Observatório UFJ Covid-19 - Tendência (Rio Verde)",
            "cidade": "Rio Verde (GO)",
	        "nome_base": "rioverde"
        }
    url = "tendencias/cidade.html"

    return render(request, url, informacoes)