from django.db import models
from .chartbuilder import ChartBuilder

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
                "data": "25 de maio"
            },
            "querysets": self.__cardDict(8, 2, 0, 0),
            "google_charts": ChartBuilder.getValoresChapadao(ChartBuilder)
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
                "data": "26 de maio"
            },
            "querysets": self.__cardDict(73, 38, 2, 1),
            "google_charts": ChartBuilder.getValoresJatai(ChartBuilder)
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
                "data": "26 de maio"
            },
            "querysets": self.__cardDict(24, 16, 0, 0),
            "google_charts": ChartBuilder.getValoresMineiros(ChartBuilder)
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
                "data": "26 de maio"
            },
            "querysets": self.__cardDict(50, 22, 2, 2),
            "google_charts": ChartBuilder.getValoresRioVerde(ChartBuilder)
        }

        return {**self.__commonValues(), **context}