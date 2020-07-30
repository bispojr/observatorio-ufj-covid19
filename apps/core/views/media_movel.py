from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_GET

from apps.core.models import MediaMovel

@require_GET
def media_movel(request, cidade):
	url = "media_movel/cidade.html"
	context = MediaMovel.getContext(MediaMovel, cidade)

	return render(request, url, context)