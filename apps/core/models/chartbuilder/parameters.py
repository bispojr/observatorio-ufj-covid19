from django.db import models

import json


class Parameters:

    corGrafico = {
        "Confirmados": "red",
        "Descartados": "pink",
        "Investigados": "yellow",
        "Notificados": "green",
        "Isolados": "gray",
        "Internados": "blue",
        "Monitorados": "brown",
        "Recuperados": "purple",
        "Óbitos": "black",
    }

    def cores(self, tipo):
        cores = []

        for cat in self.categorias(self, tipo):
            cores.append(self.corGrafico[cat])

        return cores

    def categorias(self, tipo, comData=False):
        categorias = []
        if tipo == "resumo":
            categorias = ["Confirmados", "Recuperados", "Internados", "Óbitos"]
        if tipo == "monitorados":
            categorias = ["Monitorados", "Descartados"]
        if tipo == "todas":
            categorias = [
                "Confirmados",
                "Descartados",
                "Investigados",
                "Notificados",
                "Isolados",
                "Internados",
                "Monitorados",
                "Recuperados",
                "Óbitos",
            ]

        if comData == True:
            categorias.insert(0, "Data")

        return categorias
