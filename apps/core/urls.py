from django.urls import path, include
from .views import ( home, grafico, comparacao, 
                     como_sao_criados, tendencias,
                     sobre, equipe, na_midia, colabore,
                     noticias
                    )

app_name = "core"
urlpatterns = [
    path("", home, name="home"),

    # graficos
    path("grafico/<str:cidade>/", grafico, name="grafico"),
    path("comparacao/", comparacao, name="comparacao"),
    path("como_sao_criados/", como_sao_criados, name="como-sao-criados"),

    # tendencias
    path("tendencias/<str:cidade>/", tendencias, name="tendencias"),

    # saiba mais
    path("sobre/", sobre, name="sobre"),
    path("equipe/", equipe, name="equipe"),
    path("na_midia/", na_midia, name="na-midia"),
    path("colabore/", colabore, name="colabore"),
    path("noticias/", noticias, name="noticia")
]