from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect, HttpResponse, response
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from observatorio import settings
from .models import User
from django.views.generic import View


class LoginView(View):
    def post(self, request):
        try:
            email = request.POST['email']
            password = request.POST['password']
        except:
            return response({'error': 'Por favor digite o email e senha correta'})

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                # when in test
                return {"authenticated": True}

                # when in production
                # return redirect('account:dashboard')
            else:
                return HttpResponse('Usuário Inativo.')
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        # return render(request, "index.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class dashboardView(View):
    def get(self, request):
        pass