from django.db import models

import json, sys

class ChartBuilder(models.Model): 

    __corGrafico = { 
        "confirmados": "red",
        "descartados": "pink",
        "investigados": "yellow",
        "notificados": "green",
        "isolados": "gray",
        "internados": "blue",
        "monitorados": "brown",
        "recuperados": "purple",
        "obitos": "black"
    }

    def __jatai_geral():
        googleSheet = 'https://docs.google.com/spreadsheets/d/'
        googleSheet += '1nCDjAvdEWVzwJjLhRkkVHiw2SK63SKcYXb7doIUI5VQ'
        googleSheet += '/gviz/tq?sheet=Dados&headers=1&tq='

        geral = {
            "googleSheet": googleSheet,
            "xTitle": 'Dia/Mês',
            "yTitle": 'Número de casos'            
        }

        return geral
    
    def __jatai_resumo(self):
        
        resumo = {
            "query": 'SELECT A, B, G, I, J',
            "colors": [
                self.__corGrafico["confirmados"], 
                self.__corGrafico["internados"],
                self.__corGrafico["recuperados"],
                self.__corGrafico["obitos"]
            ],
            "idDiv": 'jatai-grafico-resumo',
            "data_atualizacao": "#data-atualizacao-jatai"
        }

        return {**self.__jatai_geral(), **resumo}

    def __jatai_monitorados(self):

        monitorados = {
            "query": 'SELECT A, H, E',
            "colors": [
                self.__corGrafico["monitorados"], 
                self.__corGrafico["notificados"]
            ],
            "idDiv": 'jatai-grafico-monitorados',
            "data_atualizacao": False
        }

        return {**self.__jatai_geral(), **monitorados}

    def __jatai_todas(self):

        todas = {
            "query": 'SELECT A, B, C, D, E, F, G, H, I, J',
            "colors": [
                self.__corGrafico["confirmados"], 
                self.__corGrafico["descartados"],
                self.__corGrafico["investigados"],
                self.__corGrafico["notificados"],
                self.__corGrafico["isolados"],
                self.__corGrafico["internados"],
                self.__corGrafico["monitorados"],
                self.__corGrafico["recuperados"],
                self.__corGrafico["obitos"]
            ],
            "idDiv": 'jatai-grafico-todas',
            "data_atualizacao": False
        }

        return {**self.__jatai_geral(), **todas}

    def getValoresJatai(self):
        parametros = {
            'resumo': self.__jatai_resumo(self),
            "monitorados": self.__jatai_monitorados(self),
            "todas": self.__jatai_todas(self)
        }

        parametros = json.dumps(parametros)

        return parametros