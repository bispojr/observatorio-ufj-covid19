from .parameters_chartbuilder import ParametersChartBuilder

import json

class ChartBuilder_Rio_Verde(): 
    
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
                ParametersChartBuilder.corGrafico["internados"],
                ParametersChartBuilder.corGrafico["recuperados"],
                ParametersChartBuilder.corGrafico["confirmados"],
                ParametersChartBuilder.corGrafico["obitos"]
            ],
            "idDiv": 'rioverde-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-rioverde"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "query": 'SELECT A, C, H',
            "colors": [
                ParametersChartBuilder.corGrafico["descartados"],
                ParametersChartBuilder.corGrafico["monitorados"] 
                
            ],
            "idDiv": 'rioverde-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}

    def __todas(self):

        todas = {
            "query": 'SELECT A, C, D, F, G, H, I, B, J',
            "colors": [
                ParametersChartBuilder.corGrafico["descartados"],
                ParametersChartBuilder.corGrafico["investigados"],
                ParametersChartBuilder.corGrafico["isolados"],
                ParametersChartBuilder.corGrafico["internados"],
                ParametersChartBuilder.corGrafico["monitorados"],
                ParametersChartBuilder.corGrafico["recuperados"],
                ParametersChartBuilder.corGrafico["confirmados"],
                ParametersChartBuilder.corGrafico["obitos"]
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