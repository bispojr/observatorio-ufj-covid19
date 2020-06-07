from django.db import models

from .chartbuilder.chapadao import Chapadao
from .chartbuilder.jatai import Jatai
from .chartbuilder.mineiros import Mineiros
from .chartbuilder.rioverde import RioVerde
from .chartbuilder.datatable import DataTable

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
    
    def _chapadao(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Chapadão do Céu"
        url_fonte = "http://www.chapadaodoceu.go.gov.br/"
        tableJson, ticks, cards, data_completa = DataTable.chapadao(DataTable)

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": Chapadao.getValores(Chapadao),
            "tableJson": tableJson,
            "ticks": ticks,
            "cards": cards,
            "data_completa": data_completa
        }

        return context

    def _jatai(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Jataí"
        url_fonte = "https://www.jatai.go.gov.br/"
        tableJson, ticks, cards, data_completa = DataTable.jatai(DataTable)

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": Jatai.getValores(Jatai),
            "tableJson": tableJson,
            "ticks": ticks,
            "cards": cards,
            "data_completa": data_completa
            
        }

        return context

    def _mineiros(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Mineiros"
        url_fonte = "http://mineiros.go.gov.br/covid-19.php"
        tableJson, ticks, cards, data_completa = DataTable.mineiros(DataTable)

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": Mineiros.getValores(Mineiros),
            "tableJson": tableJson,
            "ticks": ticks,
            "cards": cards,
            "data_completa": data_completa
        }
        
        return context

    def _rioverde(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Rio Verde"
        url_fonte = "https://www.rioverde.go.gov.br/covid19/"
        tableJson, ticks, cards, data_completa = DataTable.rioverde(DataTable)

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": RioVerde.getValores(RioVerde),
            "tableJson": tableJson,
            "ticks": ticks,
            "cards": cards,
            "data_completa": data_completa
        }
        
        return context