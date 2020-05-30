from .chartbuilder import ChartBuilder

import json

class ChartBuilder_Chapadao(ChartBuilder): 

    def __init__(self):
        super().__init__()

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
        cores = ChartBuilder_Chapadao()
        
        resumo = {
            "query": 'SELECT A, B, H, J, K',
            "colors": [
                cores.getCores()["confirmados"], 
                cores.getCores()["internados"],
                cores.getCores()["recuperados"],
                cores.getCores()["obitos"]
            ],
            "idDiv": 'chapadao-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-chapadao"
        }

        return {**self.__geral(), **resumo}
    
    def __monitorados(self):
        cores = ChartBuilder_Chapadao()

        monitorados = {
            "query": 'SELECT A, I, C',
            "colors": [
                cores.getCores()["monitorados"], 
                cores.getCores()["descartados"]
            ],
            "idDiv": 'chapadao-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}
    
    def __todas(self):
        cores = ChartBuilder_Chapadao()

        todas = {
            "query": 'SELECT A, B, C, D, F, G, H, I, J, K',
            "colors": [
                cores.getCores()["confirmados"], 
                cores.getCores()["descartados"],
                cores.getCores()["investigados"],
                cores.getCores()["notificados"],
                cores.getCores()["isolados"],
                cores.getCores()["internados"],
                cores.getCores()["monitorados"],
                cores.getCores()["recuperados"],
                cores.getCores()["obitos"]
            ],
            "idDiv": 'chapadao-grafico-todas',
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