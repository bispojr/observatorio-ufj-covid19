from django.urls import path, include
from .views import ( home, grafico, comparacao, 
                     como_sao_criados, tendencias,
                     sobre, equipe, na_midia, colabore,
                     noticias, api_brasil_estado, api_brasil_geral,
                     quantidade_estado_goias, quantidade_geral_brasil
                    )

app_name = "core"
urlpatterns = [
    path("", home, name="home"),

    # graficos
    path("graficos/<str:cidade>/", grafico, name="grafico"),
    path("comparacao/", comparacao, name="comparacao"),
    path("como-sao-criados/", como_sao_criados, name="como-sao-criados"),

    # tendencias
    path("tendencias/<str:cidade>/", tendencias, name="tendencias"),

    # saiba mais
    path("sobre/", sobre, name="sobre"),
    path("equipe/", equipe, name="equipe"),
    path("na-midia/", na_midia, name="na-midia"),
    path("colabore/", colabore, name="colabore"),
    path("noticias/", noticias, name="noticia"),

    # https://brasil.io/api/dataset/covid19/caso/data/
    path("api_brasil_estado/", api_brasil_estado, name="api_brasil_estado"),
    path("api_brasil_geral/", api_brasil_geral, name="api_brasil_geral"),

    # https://covid19-brazil-api-docs.now.sh/
    # path("api_covid_brasil/", api_covid_brasil, name="api_covid_brasil"),

    # quantidade de casos em goias
    path("quantidade_goias/", quantidade_estado_goias, name="quantidade_goias"),
    path("quantidade_brasil/", quantidade_geral_brasil, name="quantidade_brasil"),
]