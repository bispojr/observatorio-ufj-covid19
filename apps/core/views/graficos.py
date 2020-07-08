from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_GET

from apps.core.api import (
    quantidade_estado_goias,
    quantidade_geral_brasil,
    api_brasil_estado,
    api_brasil_geral,
)
from apps.core.models import Graficos
from apps.core.models import Comparacao
from apps.core.models import ComoSaoCriados


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
