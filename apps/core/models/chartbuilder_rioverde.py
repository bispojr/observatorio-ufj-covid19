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
        cores = ChartBuilder_Rio_Verde()
        
        resumo = {
            "query": 'SELECT A, G, I, B, J',
            "colors": [ 
                cores.getCores()["internados"],
                cores.getCores()["recuperados"],
                cores.getCores()["confirmados"],
                cores.getCores()["obitos"]
            ],
            "idDiv": 'rioverde-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-rioverde"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):
        cores = ChartBuilder_Rio_Verde()

        monitorados = {
            "query": 'SELECT A, C, H',
            "colors": [
                cores.getCores()["descartados"],
                cores.getCores()["monitorados"] 
                
            ],
            "idDiv": 'rioverde-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}

    def __todas(self):
        cores = ChartBuilder_Rio_Verde()

        todas = {
            "query": 'SELECT A, C, D, F, G, H, I, B, J',
            "colors": [
                cores.getCores()["descartados"],
                cores.getCores()["investigados"],
                cores.getCores()["isolados"],
                cores.getCores()["internados"],
                cores.getCores()["monitorados"],
                cores.getCores()["recuperados"],
                cores.getCores()["confirmados"],
                cores.getCores()["obitos"]
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