from .chartbuilder import ChartBuilder

import json

class ChartBuilder_Jatai(ChartBuilder): 

    def __init__(self):
        super().__init__()

    def __geral():
        googleSheet = 'https://docs.google.com/spreadsheets/d/'
        googleSheet += '1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ'
        googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq='

        geral = {
            "googleSheet": googleSheet,
            "xTitle": 'Dia/Mês',
            "yTitle": 'Número de casos'            
        }

        return geral

    def __resumo(self):
        resumo = {
            "query": 'SELECT A, B, G, I, J',
            "colors": [
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["confirmados"], 
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["internados"],
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["recuperados"],
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["obitos"]
            ],
            "idDiv": 'jatai-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-jatai"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "query": 'SELECT A, H, E',
            "colors": [
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["monitorados"], 
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["notificados"]
            ],
            "idDiv": 'jatai-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}
    
    def __todas(self):

        todas = {
            "query": 'SELECT A, B, C, D, E, F, G, H, I, J',
            "colors": [
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["confirmados"], 
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["descartados"],
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["investigados"],
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["notificados"],
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["isolados"],
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["internados"],
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["monitorados"],
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["recuperados"],
                ChartBuilder_Jatai()._ChartBuilder__corGrafico["obitos"]
            ],
            "idDiv": 'jatai-grafico-todas',
            "data_atualizacao": False
        }

        return {**self.__geral(), **todas}

    def getValores(self):
        parametros = {
            "resumo": self.__resumo(self),
            "monitorados": self.__monitorados(self),
            "todas": self.__todas(self)
        }

        parametros = json.dumps(parametros)

        return parametros