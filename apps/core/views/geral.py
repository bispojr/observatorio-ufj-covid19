from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_GET

from apps.core.models import Home
from apps.core.models import Tendencias
from apps.core.models import Noticias


def home(request):
    url = "base.html"
    context = Home.getContext(Home)

    return render(request, url, context)


@require_GET
def noticias(request):
    url = "saiba_mais/noticias.html"
    context = Noticias.getContext(Equipe)

    return render(request, url, context)


# @require_GET
# def tendencias(request, cidade):
#     informacoes = Tendencias.get_informações(Tendencias, cidade)
#     url = "tendencias/cidade.html"

#     return render(request, url, informacoes)
