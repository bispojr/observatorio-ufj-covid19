from django.db import models

from .chartbuilder_chapadao import ChartBuilder_Chapadao
from .chartbuilder_jatai import ChartBuilder_Jatai
from .chartbuilder_mineiros import ChartBuilder_Mineiros
from .chartbuilder_rioverde import ChartBuilder_Rio_Verde

class Graficos(models.Model): 
    
    def getContext(self, cidade):
        if cidade == "jatai":
            return self.__jatai(self)
        if cidade == "mineiros":
            return self.__mineiros(self)
        if cidade == "rioverde":
            return self.__rioverde(self)
        if cidade == "chapadao":
            return self.__chapadao(self)
    
    def __commonValues():
        context = {            
            "grupo": "graficos",
            "grupo_link": "graficos",
            "goias": 10,
		    "brasil": 100,
        }

        return context

    def __cardDict(conf_num, rec_num, int_num, obt_num):
        values = [
            {
                "categoria": "Confirmados",
                "numero": conf_num,
                "cor": "red",
                "icone": "fas fa-user-injured"
            },
            {
                "categoria": "Recuperados",
                "numero": rec_num,
                "cor": "purple",
                "icone": "fas fa-virus-slash"
            },
            {
                "categoria": "Internados",
                "numero": int_num,
                "cor": "blue",
                "icone": "fas fa-procedures"
            },
            {
                "categoria": "Óbitos",
                "numero": obt_num,
                "cor": "black",
                "icone": "fas fa-skull-crossbones"
            }
        ]

        return values

    def __chapadao(self):
        context = {
            "script": "graficos-chapadao",
            "titulo": "Observatório UFJ Covid-19 - Gráficos (Chapadão do Céu)",
		    "informacoes": {                
                "grupo": "graficos",
                "cidade": "Chapadão do Céu",
                "nome_base": "chapadao",
                "url_fonte": "http://www.chapadaodoceu.go.gov.br/",
                "nome_fonte": "Secretaria de Saúde de Chapadão do Céu",
                "data": "04 de junho"
            },
            "querysets": self.__cardDict(14, 7, 0, 0),
            "google_charts": ChartBuilder_Chapadao.getValores(ChartBuilder_Chapadao)
        }

        return {**self.__commonValues(), **context}

    def __jatai(self):
        context = {
            "script": "graficos-jatai",
            "titulo": "Observatório UFJ Covid-19 - Gráficos (Jataí)",
            "informacoes": {                
                "cidade": "Jataí",
                "nome_base": "jatai",
                "url_fonte": "https://www.jatai.go.gov.br/",
                "nome_fonte": "Secretaria de Saúde de Jataí",
                "data": "04 de junho"
            },
            "querysets": self.__cardDict(99, 45, 2, 2),
            "google_charts": ChartBuilder_Jatai.getValores(ChartBuilder_Jatai)
        }

        return {**self.__commonValues(), **context}

    def __mineiros(self):
        context = {
            "script": "graficos-mineiros",
            "titulo": "Observatório UFJ Covid-19 - Gráficos (Mineiros)",
		    "informacoes": {
                "grupo": "graficos",
                "cidade": "Mineiros",
                "nome_base": "mineiros",
                "url_fonte": "http://mineiros.go.gov.br/covid-19.php",
                "nome_fonte": "Secretaria de Saúde de Mineiros",
                "data": "04 de junho"
            },
            "querysets": self.__cardDict(52, 26, 0, 0),
            "google_charts": ChartBuilder_Mineiros.getValores(ChartBuilder_Mineiros)
        }

        return {**self.__commonValues(), **context}

    def __rioverde(self):
        context = {
            "script": "graficos-rioverde",
            "titulo": "Observatório UFJ Covid-19 - Gráficos (Rio Verde)",
		    "informacoes": {                
                "grupo": "graficos",
                "cidade": "Rio Verde",
                "nome_base": "rioverde",
                "url_fonte": "https://www.rioverde.go.gov.br/covid19/",
                "nome_fonte": "Secretaria de Saúde de Rio Verde",
                "data": "03 de junho"
            },
            "querysets": self.__cardDict(179, 31, 35, 2),
            "google_charts": ChartBuilder_Rio_Verde.getValores(ChartBuilder_Rio_Verde)
        }

        return {**self.__commonValues(), **context}