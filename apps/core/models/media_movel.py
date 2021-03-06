from django.db import models

from .cb_media_movel.cacu_MM import CacuMM
from .cb_media_movel.chapadao_MM import ChapadaoMM
from .cb_media_movel.jatai_MM import JataiMM
from .cb_media_movel.mineiros_MM import MineirosMM
from .cb_media_movel.montividiu_MM import MontividiuMM
from .cb_media_movel.rioverde_MM import RioVerdeMM
from .cb_media_movel.santahelena_MM import SantaHelenaMM

from .cb_media_movel.datatable_MM import DataTableMM


from unidecode import unidecode

class MediaMovel(models.Model): 
    
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
            "grupo_link": "media-movel",
            "script": "media-movel",
            "titulo": "Observatório UFJ Covid-19 - Média Móvel (" + cidade +")",
            "cidade": cidade,
            "nome_base": basename,
        }

        return context
    
    def _cacu(self):
        #Informações Específicas
        nome_fonte = "Rede Social Oficial da Prefeitura de Caçu"
        url_fonte = "https://www.facebook.com/PrefeituraCacu/"
        tableJson, ticks, cards, data_completa = DataTableMM.cidade(DataTableMM, "Caçu")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": CacuMM.getValores(CacuMM),
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
        tableJson, ticks, cards, data_completa = DataTableMM.cidade(DataTableMM, "Chapadão do Céu")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": ChapadaoMM.getValores(ChapadaoMM),
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
        tableJson, ticks, cards, data_completa = DataTableMM.cidade(DataTableMM, "Jataí")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": JataiMM.getValores(JataiMM),
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
        tableJson, ticks, cards, data_completa = DataTableMM.cidade(DataTableMM, "Mineiros")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": MineirosMM.getValores(MineirosMM),
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
        tableJson, ticks, cards, data_completa = DataTableMM.cidade(DataTableMM, "Montividiu")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": MontividiuMM.getValores(MontividiuMM),
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
        tableJson, ticks, cards, data_completa = DataTableMM.cidade(DataTableMM, "Rio Verde")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": RioVerdeMM.getValores(RioVerdeMM),
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
        tableJson, ticks, cards, data_completa = DataTableMM.cidade(DataTableMM, "Santa Helena")

        context = {
            "nome_fonte": nome_fonte,
            "url_fonte": url_fonte,
            "google_charts": SantaHelenaMM.getValores(SantaHelenaMM),
            "tableJson": tableJson,
            "ticks": ticks,
            "cards": cards,
            "data_completa": data_completa
        }
        
        return context