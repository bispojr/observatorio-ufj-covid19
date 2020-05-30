from .chartbuilder import ChartBuilder

import json

class ChartBuilder_Jatai(ChartBuilder): 

    def __init__():
        self.__corGrafico = super.__corGrafico

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
                self.__corGrafico["confirmados"], 
                self.__corGrafico["internados"],
                self.__corGrafico["recuperados"],
                self.__corGrafico["obitos"]
            ],
            "idDiv": 'jatai-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-jatai"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "query": 'SELECT A, H, E',
            "colors": [
                self.__corGrafico["monitorados"], 
                self.__corGrafico["notificados"]
            ],
            "idDiv": 'jatai-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}
    
    def __todas(self):

        todas = {
            "query": 'SELECT A, B, C, D, E, F, G, H, I, J',
            "colors": [
                self.__corGrafico["confirmados"], 
                self.__corGrafico["descartados"],
                self.__corGrafico["investigados"],
                self.__corGrafico["notificados"],
                self.__corGrafico["isolados"],
                self.__corGrafico["internados"],
                self.__corGrafico["monitorados"],
                self.__corGrafico["recuperados"],
                self.__corGrafico["obitos"]
            ],
            "idDiv": 'jatai-grafico-todas',
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