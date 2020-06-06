from .parameters_chartbuilder import ParametersChartBuilder

import json

class ChartBuilder_Mineiros(): 

    def __geral():
        geral = {
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
            "idDiv": 'mineiros-grafico-resumo',
            "tipo_grafico": "resumo",
            "data_atualizacao": "#data-atualizacao-mineiros"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "colors": [
                ParametersChartBuilder.corGrafico["monitorados"], 
                ParametersChartBuilder.corGrafico["notificados"]
            ],
            "idDiv": 'mineiros-grafico-monitorados',
            "tipo_grafico": "monitorados",
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}

    def __todas(self):

        todas = {
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