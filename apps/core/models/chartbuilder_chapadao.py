from .parameters_chartbuilder import ParametersChartBuilder

import json

class ChartBuilder_Chapadao():
    
    def __geral():
        googleSheet = 'https://docs.google.com/spreadsheets/d/'
        googleSheet += '1ZiLNQfPNrvY8kW18P-KsDiNvUtLoApyWPcUsf1kIiFg'
        googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq='

        geral = {
            "googleSheet": googleSheet,
            "xTitle": 'Dia/Mês',
            "yTitle": 'Número de casos'            
        }

        return geral
    
    def __resumo(self):

        resumo = {
            "colors": [
                ParametersChartBuilder.corGrafico["confirmados"], 
                ParametersChartBuilder.corGrafico["internados"],
                ParametersChartBuilder.corGrafico["recuperados"],
                ParametersChartBuilder.corGrafico["obitos"]
            ],
            "idDiv": 'chapadao-do-ceu-grafico-resumo',
            "tipo_grafico": "resumo",
            "data_atualizacao": "#data-atualizacao-chapadao-do-ceu"
        }

        return {**self.__geral(), **resumo}
    
    def __monitorados(self):

        monitorados = {
            "query": 'SELECT A, I, C',
            "colors": [
                ParametersChartBuilder.corGrafico["monitorados"], 
                ParametersChartBuilder.corGrafico["descartados"]
            ],
            "idDiv": 'chapadao-do-ceu-grafico-monitorados',
            "tipo_grafico": "monitorados",
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}
    
    def __todas(self):

        todas = {
            "query": 'SELECT A, B, C, D, F, G, H, I, J, K',
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
            "idDiv": 'chapadao-do-ceu-grafico-todas',
            "tipo_grafico": "todas",
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