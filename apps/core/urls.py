from django.urls import path, include
from .views import home, graficos

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("grafico/<str:cidade>/", graficos, name="graficos")
]