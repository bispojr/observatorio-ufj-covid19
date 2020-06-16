from django.db import models

from .chartbuilder.cacu import Cacu
from .chartbuilder.chapadao import Chapadao
from .chartbuilder.jatai import Jatai
from .chartbuilder.mineiros import Mineiros
from .chartbuilder.montividiu import Montividiu
from .chartbuilder.rioverde import RioVerde
from .chartbuilder.santahelena import SantaHelena

from .chartbuilder.datatable import DataTable


from unidecode import unidecode

class Graficos(models.Model): 
    
    def getContext(self, cidade):
        if cidade == "cacu":
            return {**self._geral("Caçu"), **self._cacu(self)}
        if cidade == "chapadao":
            return {**self._geral("Chapadão do Céu"), **self._chapadao(self)}
        if cidade == "jatai":
            return {**self._geral("Jataí"), **self._jatai(self)}
        if cidade == "mineiros":
            return {**self._geral("Mineiros"), **self._mineiros(self)}
        if cidade == "montividiu":
            return {**self._geral("Montividiu"), **self._montividiu(self)}
        if cidade == "rioverde":
            return {**self._geral("Rio Verde"), **self._rioverde(self)}
        if cidade == "santahelena":
            return {**self._geral("Santa Helena"), **self._santahelena(self)}
        
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
    
    def _cacu(self):
        #Informações Específicas
        nome_fonte = "Rede Social Oficial da Prefeitura de Caçu"
        url_fonte = "https://www.facebook.com/PrefeituraCacu/"
        tableJson, ticks, cards, data_completa = DataTable.cidade(DataTable, "Caçu")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": Cacu.getValores(Cacu),
            "tableJson": tableJson,
            "ticks": ticks,
            "cards": cards,
            "data_completa": data_completa
        }

        return context
    
    def _chapadao(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Chapadão do Céu"
        url_fonte = "http://www.chapadaodoceu.go.gov.br/"
        tableJson, ticks, cards, data_completa = DataTable.cidade(DataTable, "Chapadão do Céu")

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
        tableJson, ticks, cards, data_completa = DataTable.cidade(DataTable, "Jataí")

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
        tableJson, ticks, cards, data_completa = DataTable.cidade(DataTable, "Mineiros")

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

    def _montividiu(self):
        #Informações Específicas
        nome_fonte = "Rede Social Oficial da Prefeitura de Montividiu"
        url_fonte = "https://www.facebook.com/prefeiturademontividiu/"
        tableJson, ticks, cards, data_completa = DataTable.cidade(DataTable, "Montividiu")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": Montividiu.getValores(Montividiu),
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
        tableJson, ticks, cards, data_completa = DataTable.cidade(DataTable, "Rio Verde")

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

    def _santahelena(self):
        #Informações Específicas
        nome_fonte = "Secretaria de Saúde de Santa Helena"
        url_fonte = "https://www.santahelena.go.gov.br/pagina/41"
        tableJson, ticks, cards, data_completa = DataTable.cidade(DataTable, "Santa Helena")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": SantaHelena.getValores(SantaHelena),
            "tableJson": tableJson,
            "ticks": ticks,
            "cards": cards,
            "data_completa": data_completa
        }
        
        return context