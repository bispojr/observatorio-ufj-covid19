from django.db import models

import json

class ParametersChartBuilder(models.Model): 

    corGrafico = { 
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