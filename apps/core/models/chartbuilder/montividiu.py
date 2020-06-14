from .parameters import Parameters

import json

class Montividiu(): 

    def __geral():
        geral = {
            "xTitle": 'Dia/Mês',
            "yTitle": 'Número de casos',
            "minY": 0 
        }

        return geral

    def __resumo(self):
        
        resumo = {
            "colors": Parameters.cores(Parameters, "resumo"),
            "idDiv": 'montividiu-grafico-resumo',
            "tipo_grafico": "resumo",
            "data_atualizacao": "#data-atualizacao-montividiu"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "colors": Parameters.cores(Parameters, "monitorados"),
            "idDiv": 'montividiu-grafico-monitorados',
            "tipo_grafico": "monitorados",
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}

    def __todas(self):

        todas = {
            "colors": Parameters.cores(Parameters, "todas"),
            "idDiv": 'montividiu-grafico-todas',
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