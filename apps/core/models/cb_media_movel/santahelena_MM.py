from .parameters_MM import ParametersMM

import json

class SantaHelenaMM(): 
    
    def __geral():

        geral = {
            "xTitle": 'Dia/Mês',
            "yTitle": 'Número de casos',
            "minY": 0
        }

        return geral

    def __resumo(self):

        resumo = {
            "colors": ParametersMM.cores(ParametersMM, "media-movel"),
            "idDiv": 'santa-helena-grafico-resumo',
            "tipo_grafico": "resumo",
            "data_atualizacao": "#data-atualizacao-santa-helena"
        }

        return {**self.__geral(), **resumo}

    def getValores(self):
        parametros = {
            'resumo': self.__resumo(self)
        }

        parametros = json.dumps(parametros)

        return parametros