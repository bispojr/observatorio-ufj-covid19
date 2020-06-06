from django.db import models

from .chartbuilder_chapadao import ChartBuilder_Chapadao
from .chartbuilder_jatai import ChartBuilder_Jatai
from .chartbuilder_mineiros import ChartBuilder_Mineiros
from .chartbuilder_rioverde import ChartBuilder_Rio_Verde
from .datatable import DataTable

from unidecode import unidecode

class Graficos(models.Model): 
    
    def getContext(self, cidade):
        if cidade == "chapadao":
            return {**self._geral("Chapadão do Céu"), **self._chapadao(self)}
        if cidade == "jatai":
            return {**self._geral("Jataí"), **self._jatai(self)}
        if cidade == "mineiros":
            return {**self._geral("Mineiros"), **self._mineiros(self)}
        if cidade == "rioverde":
            return {**self._geral("Rio Verde"), **self._rioverde(self)}
        
    def _geral(cidade):

        #Normalização
        basename = unidecode(cidade)  #remove acentos
        basename = basename.lower().replace(" ", "-")

        context = {            
            "grupo": "graficos",
            "grupo_link": "graficos",
            "script": "graficos-" + basename,
            "titulo": "Observatório UFJ Covid-19 - Gráficos (" + cidade +")",
            "cidade": cidade,
            "nome_base": basename,
        }

        return context

    def _cardDict(conf_num, rec_num, int_num, obt_num):
        
        cards = {
            "data": "05 de junho",
            "valores": [
                {
                    "categoria": "Confirmados",
                    "numero": conf_num,
                    "cor": "red",
                    "icone": "fas fa-user-injured"
                },
                {
                    "categoria": "Recuperados",
                    "numero": rec_num,
                    "cor": "purple",
                    "icone": "fas fa-virus-slash"
                },
                {
                    "categoria": "Internados",
                    "numero": int_num,
                    "cor": "blue",
                    "icone": "fas fa-procedures"
                },
                {
                    "categoria": "Óbitos",
                    "numero": obt_num,
                    "cor": "black",
                    "icone": "fas fa-skull-crossbones"
                }
            ]
        }

        return cards
    
    def _chapadao(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Chapadão do Céu"
        url_fonte = "http://www.chapadaodoceu.go.gov.br/"

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "cards": self._cardDict(14, 7, 0, 0),
            "google_charts": ChartBuilder_Chapadao.getValores(ChartBuilder_Chapadao),
            "tableJson": DataTable.chapadao(DataTable)
        }

        return context

    def _jatai(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Jataí"
        url_fonte = "https://www.jatai.go.gov.br/"

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "cards": self._cardDict(14, 7, 0, 0),
            "google_charts": ChartBuilder_Jatai.getValores(ChartBuilder_Jatai),
            "tableJson": DataTable.jatai(DataTable)
        }

        return context

    def _mineiros(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Mineiros"
        url_fonte = "http://mineiros.go.gov.br/covid-19.php"

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "cards": self._cardDict(14, 7, 0, 0),
            "google_charts": ChartBuilder_Mineiros.getValores(ChartBuilder_Mineiros),
            "tableJson": DataTable.mineiros(DataTable)
        }
        
        return context

    def _rioverde(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Rio Verde"
        url_fonte = "https://www.rioverde.go.gov.br/covid19/"

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "cards": self._cardDict(283, 33, 39, 4),
            "google_charts": ChartBuilder_Rio_Verde.getValores(ChartBuilder_Rio_Verde),
            "tableJson": DataTable.rioverde(DataTable)
        }
        
        return context