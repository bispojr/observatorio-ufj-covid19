from django.db import models

class Graficos(models.Model): 
    
    def getContext(self, cidade):
        if cidade == "jatai":
            return self.__jatai(self)
        if cidade == "mineiros":
            return self.__mineiros(self)
        if cidade == "rioverde":
            return self.__rioverde(self)
    
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

    def __jatai(self):
        context = {
            "script": "graficos-jatai",
            "titulo": "Observatório UFJ Covid-19 - Gráficos (Jataí)",
            "informacoes": {                
                "cidade": "Jataí",
                "nome_base": "jatai",
                "url_fonte": "https://www.jatai.go.gov.br/",
                "nome_fonte": "Secretária de Saúde de Jataí",
                "data": "18 de maio"
            },
            "querysets": self.__cardDict(34, 14, 1, 1),
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
                "nome_fonte": "Secretária de Saúde de Mineiros",
                "data": "17 de maio"
            },
            "querysets": self.__cardDict(15, 6, 1, 0),
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
                "nome_fonte": "Secretária de Saúde de Rio Verde",
                "data": "17 de maio"
            },
            "querysets": self.__cardDict(27, 18, 4, 2),
        }

        return {**self.__commonValues(), **context}