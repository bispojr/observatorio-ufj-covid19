import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gviz_api
from pprint import pprint
from datetime import datetime
from django.conf import settings
import json

from .card import Card
from .tick import Tick
from .parameters import Parameters

class DataTable(): 
    
    def credentials():
        scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        #dictJson = json.loads(settings.CREDENTIALS_GOOGLE_DRIVE)
        #creds = ServiceAccountCredentials.from_json_keyfile_dict(dictJson, scope)
        creds = ServiceAccountCredentials.from_json_keyfile_name("google-credentials.json", scope)

        return creds
    
    def chapadao(self):
        creds = self.credentials()
        client = gspread.authorize(creds)
        sheet = client.open("Chapadão do Céu").sheet1  # Open the spreadhseet

        data = sheet.get_all_records()  # Get a list of all records

        #Convertendo para o formato de data do Python
        #Convertendo para Null os campos sem valor
        for row in data:
            row["Data"] = datetime.strptime(row["Data"], '%d/%m/%Y')
            for val in row:
                if row[val] == '-' or row[val] == '':
                    row[val] = None

        description = {
            'Data': ("date", "Data"),
            'Confirmados': ("number", "Confirmados"),
            'Descartados': ("number", "Descartados"),
            'Investigados': ("number", "Investigados"),
            'Suspeitos': ("number", "Suspeitos"),
            'Notificados': ("number", "Notificados"),
            'Isolados': ("number", "Isolados"),
            'Internados': ("number", "Internados"),
            'Monitorados': ("number", "Monitorados"),
            'Recuperados': ("number", "Recuperados"),
            'Óbitos': ("number", "Óbitos")
        }
        # Loading it into gviz_api.DataTable
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)

        # Resumo
        categorias = Parameters.categorias(Parameters, "resumo", True)
        resumoJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksResumo = Tick.getTicks(data, categorias)

        # Monitorados
        categorias = Parameters.categorias(Parameters, "monitorados", True)
        monitoradosJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksMonitorados = Tick.getTicks(data, categorias)

        # Todas
        categorias = Parameters.categorias(Parameters, "todas", True)
        todasJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksTodas = Tick.getTicks(data, categorias)

        # Preparação da saída
        tableJson = {
            "resumo": resumoJson,
            "monitorados": monitoradosJson,
            "todas": todasJson
        }

        ticks = {
            "resumo": json.dumps(ticksResumo),            
            "monitorados": json.dumps(ticksMonitorados),
            "todas": json.dumps(ticksTodas)
        }

        cards, data_completa = Card.getCards(data)

        return tableJson, ticks, cards, data_completa

    def jatai(self):
        
        creds = self.credentials()
        client = gspread.authorize(creds)
        sheet = client.open("Jataí").sheet1  # Open the spreadhseet

        data = sheet.get_all_records()  # Get a list of all records

        #Convertendo para o formato de data do Python
        #Convertendo para Null os campos sem valor
        for row in data:
            row["Data"] = datetime.strptime(row["Data"], '%d/%m/%Y')
            for val in row:
                if row[val] == '-' or row[val] == '':
                    row[val] = None

        description = {
            'Data': ("date", "Data"),
            'Confirmados': ("number", "Confirmados"),
            'Descartados': ("number", "Descartados"),
            'Investigados': ("number", "Investigados"),
            'Notificados': ("number", "Notificados"),
            'Isolados': ("number", "Isolados"),
            'Internados': ("number", "Internados"),
            'Monitorados': ("number", "Monitorados"),
            'Recuperados': ("number", "Recuperados"),
            'Óbitos': ("number", "Óbitos")
        }
        # Loading it into gviz_api.DataTable
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)

        # Resumo
        categorias = Parameters.categorias(Parameters, "resumo", True)
        resumoJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksResumo = Tick.getTicks(data, categorias)

        # Monitorados
        categorias = Parameters.categorias(Parameters, "monitorados", True)
        monitoradosJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksMonitorados = Tick.getTicks(data, categorias)

        # Todas
        categorias = Parameters.categorias(Parameters, "todas", True)
        todasJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksTodas = Tick.getTicks(data, categorias)

        # Preparação da saída
        tableJson = {
            "resumo": resumoJson,
            "monitorados": monitoradosJson,
            "todas": todasJson
        }

        ticks = {
            "resumo": json.dumps(ticksResumo),            
            "monitorados": json.dumps(ticksMonitorados),
            "todas": json.dumps(ticksTodas)
        }

        cards, data_completa = Card.getCards(data)

        return tableJson, ticks, cards, data_completa

    def mineiros(self):
        creds = self.credentials()
        client = gspread.authorize(creds)
        sheet = client.open("Mineiros").sheet1  # Open the spreadhseet

        data = sheet.get_all_records()  # Get a list of all records

        #Convertendo para o formato de data do Python
        #Convertendo para Null os campos sem valor
        for row in data:
            row["Data"] = datetime.strptime(row["Data"], '%d/%m/%Y')
            for val in row:
                if row[val] == '-' or row[val] == '':
                    row[val] = None

        description = {
            'Data': ("date", "Data"),
            'Confirmados': ("number", "Confirmados"),
            'Descartados': ("number", "Descartados"),
            'Investigados': ("number", "Investigados"),
            'Suspeitos': ("number", "Suspeitos"),
            'Notificados': ("number", "Notificados"),
            'Isolados': ("number", "Isolados"),
            'Internados': ("number", "Internados"),
            'Monitorados': ("number", "Monitorados"),
            'Recuperados': ("number", "Recuperados"),
            'Óbitos': ("number", "Óbitos")
        }
        # Loading it into gviz_api.DataTable
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)

        # Resumo
        categorias = Parameters.categorias(Parameters, "resumo", True)
        resumoJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksResumo = Tick.getTicks(data, categorias)

        # Monitorados
        categorias = Parameters.categorias(Parameters, "monitorados", True)
        monitoradosJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksMonitorados = Tick.getTicks(data, categorias)

        # Todas
        categorias = Parameters.categorias(Parameters, "todas", True)
        todasJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksTodas = Tick.getTicks(data, categorias)

        # Preparação da saída
        tableJson = {
            "resumo": resumoJson,
            "monitorados": monitoradosJson,
            "todas": todasJson
        }

        ticks = {
            "resumo": json.dumps(ticksResumo),            
            "monitorados": json.dumps(ticksMonitorados),
            "todas": json.dumps(ticksTodas)
        }

        cards, data_completa = Card.getCards(data)

        return tableJson, ticks, cards, data_completa

    def rioverde(self):
        creds = self.credentials()
        client = gspread.authorize(creds)
        sheet = client.open("Rio Verde").sheet1  # Open the spreadhseet

        data = sheet.get_all_records()  # Get a list of all records

        #Convertendo para o formato de data do Python
        #Convertendo para Null os campos sem valor
        for row in data:
            row["Data"] = datetime.strptime(row["Data"], '%d/%m/%Y')
            for val in row:
                if row[val] == '-' or row[val] == '':
                    row[val] = None

        description = {
            'Data': ("date", "Data"),
            'Confirmados': ("number", "Confirmados"),
            'Descartados': ("number", "Descartados"),
            'Investigados': ("number", "Investigados"),
            'Notificados': ("number", "Notificados"),
            'Isolados': ("number", "Isolados"),
            'Internados': ("number", "Internados"),
            'Monitorados': ("number", "Monitorados"),
            'Recuperados': ("number", "Recuperados"),
            'Óbitos': ("number", "Óbitos")
        }
        # Loading it into gviz_api.DataTable
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)

        # Resumo
        categorias = Parameters.categorias(Parameters, "resumo", True)
        resumoJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksResumo = Tick.getTicks(data, categorias)

        # Monitorados
        categorias = Parameters.categorias(Parameters, "monitorados", True)
        monitoradosJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksMonitorados = Tick.getTicks(data, categorias)

        # Todas
        categorias = Parameters.categorias(Parameters, "todas", True)
        todasJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksTodas = Tick.getTicks(data, categorias)

        # Preparação da saída
        tableJson = {
            "resumo": resumoJson,
            "monitorados": monitoradosJson,
            "todas": todasJson
        }

        ticks = {
            "resumo": json.dumps(ticksResumo),            
            "monitorados": json.dumps(ticksMonitorados),
            "todas": json.dumps(ticksTodas)
        }

        cards, data_completa = Card.getCards(data)

        return tableJson, ticks, cards, data_completa