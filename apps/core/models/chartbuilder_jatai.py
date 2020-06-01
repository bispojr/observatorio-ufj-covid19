from .parameters_chartbuilder import ParametersChartBuilder

import json

class ChartBuilder_Jatai(): 

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
                ParametersChartBuilder.corGrafico["confirmados"], 
                ParametersChartBuilder.corGrafico["internados"],
                ParametersChartBuilder.corGrafico["recuperados"],
                ParametersChartBuilder.corGrafico["obitos"]
            ],
            "idDiv": 'jatai-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-jatai"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "query": 'SELECT A, H, E',
            "colors": [
                ParametersChartBuilder.corGrafico["monitorados"], 
                ParametersChartBuilder.corGrafico["notificados"]
            ],
            "idDiv": 'jatai-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}
    
    def __todas(self):

        todas = {
            "query": 'SELECT A, B, C, D, E, F, G, H, I, J',
            "colors": [
                ParametersChartBuilder.corGrafico["confirmados"], 
                ParametersChartBuilder.corGrafico["descartados"],
                ParametersChartBuilder.corGrafico["investigados"],
                ParametersChartBuilder.corGrafico["notificados"],
                ParametersChartBuilder.corGrafico["isolados"],
                ParametersChartBuilder.corGrafico["internados"],
                ParametersChartBuilder.corGrafico["monitorados"],
                ParametersChartBuilder.corGrafico["recuperados"],
                ParametersChartBuilder.corGrafico["obitos"]
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