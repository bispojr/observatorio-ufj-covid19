from django.shortcuts import render
from django.views.decorators.http import require_GET

from apps.core.models.boletim import BoletimEpidemiologico

@require_GET
def boletim_login(request):
	url = "boletim/login.html"
	context = BoletimEpidemiologico.getContext(BoletimEpidemiologico)

	return render(request, url, context)