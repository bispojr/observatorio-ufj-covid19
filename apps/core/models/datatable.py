import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gviz_api
from pprint import pprint
from datetime import datetime

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
                "Data", "Confirmados", "Recuperados", 
                "Internados", "Óbitos"
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