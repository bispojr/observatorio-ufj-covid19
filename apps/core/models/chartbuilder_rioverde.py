from .chartbuilder import ChartBuilder

import json

class ChartBuilder_Rio_Verde(ChartBuilder): 

    def __init__(self):
        super().__init__()

    def __geral():
        googleSheet = 'https://docs.google.com/spreadsheets/d/'
        googleSheet += '1jrhI1EjA8KJNJ5CKEDe-oREPjeRnYviVKp9AJPPMlLE'
        googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq='

        geral = {
            "googleSheet": googleSheet,
            "xTitle": 'Dia/Mês',
            "yTitle": 'Número de casos'            
        }

        return geral

    def __resumo(self):

        resumo = {
            "query": 'SELECT A, G, I, B, J',
            "colors": [ 
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["internados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["recuperados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["confirmados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["obitos"]
            ],
            "idDiv": 'rioverde-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-rioverde"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "query": 'SELECT A, C, H',
            "colors": [
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["descartados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["monitorados"] 
                
            ],
            "idDiv": 'rioverde-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}

    def __todas(self):

        todas = {
            "query": 'SELECT A, C, D, F, G, H, I, B, J',
            "colors": [
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["descartados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["investigados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["isolados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["internados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["monitorados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["recuperados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["confirmados"],
                ChartBuilder_Rio_Verde()._ChartBuilder__corGrafico["obitos"]
            ],
            "idDiv": 'rioverde-grafico-todas',
            "data_atualizacao": False
        }

        return {**self.__geral(), **todas}

    def getValores(self):
        parametros = {
            'resumo': self.__resumo(self),
            "monitorados": self.__monitorados(self),
            "todas": self.__todas(self)
        }

        parametros = json.dumps(parametros)

        return parametros