import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gviz_api
from pprint import pprint
from datetime import datetime
from django.conf import settings
import json

class DataTable(): 
    
    def jatai():
        scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
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

        resumoJson = data_table.ToJSon(
            columns_order=(
                "Data", "Confirmados", "Internados",
                "Recuperados", "Óbitos"
            ),
            order_by="Data"
        )

        monitoradosJson = data_table.ToJSon(
            columns_order=(
                "Data", "Monitorados", "Notificados"
            ),
            order_by="Data"
        )

        todasJson = data_table.ToJSon(
            columns_order=(
                "Data", "Confirmados", "Descartados",
                "Investigados", "Notificados", "Isolados",
                "Internados", "Monitorados", "Recuperados",
                "Óbitos"
            ),
            order_by="Data"
        )

        tableJson = {
            "resumo": resumoJson,
            "monitorados": monitoradosJson,
            "todas": todasJson
        }
        return tableJson

    def chapadao():
        scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
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

        resumoJson = data_table.ToJSon(
            columns_order=(
                "Data", "Confirmados", "Internados",
                "Recuperados", "Óbitos"
            ),
            order_by="Data"
        )

        monitoradosJson = data_table.ToJSon(
            columns_order=(
                "Data", "Monitorados", "Descartados"
            ),
            order_by="Data"
        )

        todasJson = data_table.ToJSon(
            columns_order=(
                "Data", "Confirmados", "Descartados",
                "Investigados", "Notificados", "Isolados",
                "Internados", "Monitorados", "Recuperados",
                "Óbitos"
            ),
            order_by="Data"
        )

        tableJson = {
            "resumo": resumoJson,
            "monitorados": monitoradosJson,
            "todas": todasJson
        }
        return tableJson

    def mineiros():
        scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
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
            'Internados': ("number", "Internados (UTI)"),
            'Monitorados': ("number", "Monitorados"),
            'Recuperados': ("number", "Recuperados"),
            'Óbitos': ("number", "Óbitos")
        }
        # Loading it into gviz_api.DataTable
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)

        resumoJson = data_table.ToJSon(
            columns_order=(
                "Data", "Confirmados", "Internados",
                "Recuperados", "Óbitos"
            ),
            order_by="Data"
        )

        monitoradosJson = data_table.ToJSon(
            columns_order=(
                "Data", "Monitorados", "Descartados"
            ),
            order_by="Data"
        )

        todasJson = data_table.ToJSon(
            columns_order=(
                "Data", "Confirmados", "Descartados",
                "Investigados", "Notificados", "Isolados",
                "Internados", "Monitorados", "Recuperados",
                "Óbitos"
            ),
            order_by="Data"
        )

        tableJson = {
            "resumo": resumoJson,
            "monitorados": monitoradosJson,
            "todas": todasJson
        }
        return tableJson

    def rioverde():
        
        scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

        dictJson = json.loads(settings.CREDENTIALS_GOOGLE_DRIVE)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(dictJson, scope)
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

        resumoJson = data_table.ToJSon(
            columns_order=(
                "Data", "Internados",
                "Recuperados", "Confirmados",  "Óbitos"
            ),
            order_by="Data"
        )

        monitoradosJson = data_table.ToJSon(
            columns_order=(
                "Data", "Descartados", "Monitorados",
            ),
            order_by="Data"
        )

        todasJson = data_table.ToJSon(
            columns_order=(
                "Data", "Descartados", "Investigados", "Isolados", 
                "Internados", "Monitorados", "Recuperados", "Confirmados", 
                "Óbitos"
            ),
            order_by="Data"
        )

        tableJson = {
            "resumo": resumoJson,
            "monitorados": monitoradosJson,
            "todas": todasJson
        }
        return tableJson