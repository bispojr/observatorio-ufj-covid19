from .parameters_MM import ParametersMM

import json

class MontividiuMM(): 

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
            "idDiv": 'montividiu-grafico-resumo',
            "tipo_grafico": "resumo",
            "data_atualizacao": "#data-atualizacao-montividiu"
        }

        return {**self.__geral(), **resumo}

    def getValores(self):
        parametros = {
            'resumo': self.__resumo(self)
        }

        parametros = json.dumps(parametros)

        return parametros