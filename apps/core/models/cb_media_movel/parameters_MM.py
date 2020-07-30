from django.db import models

import json

class ParametersMM(): 

    corGrafico = { 
        "Novos Casos": "pink",
        "Média Móvel": "red"
    }

    def cores(self, tipo):
        cores = []
        
        for cat in self.categorias(self, tipo):
            cores.append(self.corGrafico[cat])
        
        return cores

    def categorias(self, tipo, comData = False):
        categorias = []
        if(tipo == "media-movel"):
            categorias = [
                "Novos Casos",
                "Média Móvel"
            ]
        
        if comData == True:
            categorias.insert(0, "Data")
        
        return categorias