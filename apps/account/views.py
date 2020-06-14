from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import User

@require_http_methods(["POST", "GET"])
def login(request):
    template_name = "registration/login.html"
    context = User.login(request)
    if context[2]:
        return redirect("core:report_list")
    else:
        return render(request, template_name, context)



