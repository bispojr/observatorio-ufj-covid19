from django.urls import path, include
from .views import home

app_name = "core"
urlpatterns = [
    path("", home, name="home")
]