from django.urls import path, include
from .views import home, grafico

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("grafico/<str:cidade>/", grafico, name="grafico")
]