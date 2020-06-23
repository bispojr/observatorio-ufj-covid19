from django.urls import path
from .views import login

app_name = "account"
urlpatterns = [
    path("login", login, name="login"),
    # path("logout/", logout, name="logout")
]
