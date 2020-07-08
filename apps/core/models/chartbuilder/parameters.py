from django.db import models

import json

class Parameters(): 
    """
    Classe para configurar os valores que serão utilizados
    pelos gráficos assim como suas categorias.

    methods:
        - cores
        - categorias
    """
    corGrafico = { 
        "Confirmados": "red",
        "Descartados": "pink",
        "Investigados": "yellow",
        "Notificados": "green",
        "Isolados": "gray",
        "Internados": "blue",
        "Monitorados": "brown",
        "Recuperados": "purple",
        "Óbitos": "black"
    }

    def cores(self, tipo):
        """
        Função para adicionar as cores nas categorias

        args:
            self
            tipo
        
        return:
            cores: concatenação das cores com as categorias.
        """
        cores = []
        
        for cat in self.categorias(self, tipo):
            cores.append(self.corGrafico[cat])
        
        return cores

    def categorias(self, tipo, comData = False):
        """
        Função para configurar as categorias que serão utilizadas
        nos gráficos e cards.

        args:
            self
            tipo('resumo','monitorados','todas')
            comData (default = False)

        return:
            lista com os dados.
        """
        categorias = []
        if(tipo == "resumo"):
            categorias = [
                "Confirmados", "Recuperados",
                "Internados", "Óbitos"
            ]
        if(tipo == "monitorados"):
            categorias = [
                "Monitorados", "Descartados"
            ]
        if(tipo == "todas"):
            categorias = [
                "Confirmados", "Descartados", "Investigados",
                "Notificados", "Isolados","Internados",
                "Monitorados", "Recuperados", "Óbitos"
            ]
        
        if comData == True:
            categorias.insert(0, "Data")
        
        return categorias