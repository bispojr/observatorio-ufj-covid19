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
        cores = ChartBuilder_Mineiros()
        
        resumo = {
            "query": 'SELECT A, E, I, H, G',
            "colors": [
                cores.getCores()["confirmados"], 
                cores.getCores()["internados"],
                cores.getCores()["recuperados"],
                cores.getCores()["obitos"]
            ],
            "idDiv": 'mineiros-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-mineiros"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):
        cores = ChartBuilder_Mineiros()

        monitorados = {
            "query": 'SELECT A, C, B',
            "colors": [
                cores.getCores()["monitorados"], 
                cores.getCores()["notificados"]
            ],
            "idDiv": 'mineiros-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}

    def __todas(self):
        cores = ChartBuilder_Mineiros()

        todas = {
            "query": 'SELECT A, E, D, L, B, K, I, C, H, G',
            "colors": [
                cores.getCores()["confirmados"], 
                cores.getCores()["descartados"],
                cores.getCores()["investigados"],
                cores.getCores()["notificados"],
                cores.getCores()["isolados"],
                cores.getCores()["internados"],
                cores.getCores()["monitorados"],
                cores.getCores()["recuperados"],
                cores.getCores()["obitos"]
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