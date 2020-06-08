from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_GET

from apps.core.models import Sobre
from apps.core.models import NaMidia
from apps.core.models import Colabore
from apps.core.models import Equipe

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