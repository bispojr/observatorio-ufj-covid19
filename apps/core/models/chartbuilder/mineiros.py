from .parameters import Parameters

import json

class Mineiros(): 

    def __geral():
        geral = {
            "xTitle": 'Dia/Mês',
            "yTitle": 'Número de casos',
            "minY": 0 
        }

        return geral

    def __resumo(self):
        
        resumo = {
            "colors": [
                Parameters.corGrafico["confirmados"], 
                Parameters.corGrafico["internados"],
                Parameters.corGrafico["recuperados"],
                Parameters.corGrafico["obitos"]
            ],
            "idDiv": 'mineiros-grafico-resumo',
            "tipo_grafico": "resumo",
            "data_atualizacao": "#data-atualizacao-mineiros"
        }

        return {**self.__geral(), **resumo}

    def __monitorados(self):

        monitorados = {
            "colors": [
                Parameters.corGrafico["monitorados"], 
                Parameters.corGrafico["notificados"]
            ],
            "idDiv": 'mineiros-grafico-monitorados',
            "tipo_grafico": "monitorados",
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}

    def __todas(self):

        todas = {
            "colors": [
                Parameters.corGrafico["confirmados"], 
                Parameters.corGrafico["descartados"],
                Parameters.corGrafico["investigados"],
                Parameters.corGrafico["notificados"],
                Parameters.corGrafico["isolados"],
                Parameters.corGrafico["internados"],
                Parameters.corGrafico["monitorados"],
                Parameters.corGrafico["recuperados"],
                Parameters.corGrafico["obitos"]
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