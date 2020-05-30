from .parameters_chartbuilder import ParametersChartBuilder

import json

class ChartBuilder_Mineiros(): 

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
                ParametersChartBuilder.corGrafico["confirmados"], 
                ParametersChartBuilder.corGrafico["internados"],
                ParametersChartBuilder.corGrafico["recuperados"],
                ParametersChartBuilder.corGrafico["obitos"]
            ],
            "idDiv": 'mineiros-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-mineiros"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "query": 'SELECT A, C, B',
            "colors": [
                ParametersChartBuilder.corGrafico["monitorados"], 
                ParametersChartBuilder.corGrafico["notificados"]
            ],
            "idDiv": 'mineiros-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}

    def __todas(self):

        todas = {
            "query": 'SELECT A, E, D, L, B, K, I, C, H, G',
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