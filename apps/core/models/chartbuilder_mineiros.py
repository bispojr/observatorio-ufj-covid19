from .chartbuilder import ChartBuilder

import json

class ChartBuilder_Mineiros(ChartBuilder): 

    def __init__(self):
        super().__init__()

    def __geral():
        googleSheet = 'https://docs.google.com/spreadsheets/d/'
        googleSheet += '1MPFPI6nZvoPjSanXFcVqh3TrWDRJ7J5SXbhKkW6p5NY'
        googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq='

        geral = {
            "googleSheet": googleSheet,
            "xTitle": 'Dia/Mês',
            "yTitle": 'Número de casos'            
        }

        return geral

    def __resumo(self):
        
        resumo = {
            "query": 'SELECT A, E, I, H, G',
            "colors": [
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["confirmados"], 
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["internados"],
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["recuperados"],
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["obitos"]
            ],
            "idDiv": 'mineiros-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-mineiros"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "query": 'SELECT A, C, B',
            "colors": [
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["monitorados"], 
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["notificados"]
            ],
            "idDiv": 'mineiros-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}

    def __todas(self):

        todas = {
            "query": 'SELECT A, E, D, L, B, K, I, C, H, G',
            "colors": [
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["confirmados"], 
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["descartados"],
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["investigados"],
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["notificados"],
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["isolados"],
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["internados"],
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["monitorados"],
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["recuperados"],
                ChartBuilder_Mineiros()._ChartBuilder__corGrafico["obitos"]
            ],
            "idDiv": 'mineiros-grafico-todas',
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