from django.urls import path, include
from .views import ( home, grafico, comparacao, 
                     como_sao_criados, equipe
                    )

app_name = "core"
urlpatterns = [
    path("", home, name="home"),

    # graficos
    path("grafico/<str:cidade>/", grafico, name="grafico"),
    path("comparacao/", comparacao, name="comparacao"),
    path("como_sao_criados/", como_sao_criados, name="como-sao-criados"),

    # tendencias

    # saiba mais
    path("equipe/", equipe, name="equipe")



]