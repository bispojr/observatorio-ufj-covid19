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
    
    def cidade(self, cidade):
        creds = self.credentials()
        client = gspread.authorize(creds)
        
        if (
            cidade != "Chapadão do Céu" and 
            cidade != "Jataí" and
            cidade != "Mineiros" and 
            cidade != "Rio Verde" and
            cidade != "Santa Helena"
        ):
            print("Cidade inexistente em nossa base de dados")
        
        # Open the spreadhseet
        sheet = client.open(cidade).sheet1 
        dados = sheet.get_all_records()  # Get a list of all records
        
        # Preparação dos dados
        dados_preparados = []
        for row in dados:
            #Convertendo para o formato de data do Python
            row["Data"] = datetime.strptime(row["Data"], '%d/%m/%Y')

            #Convertendo para Null os campos sem valor
            for val in row:
                if row[val] == '-' or row[val] == '':
                    row[val] = None
            dados_preparados.append(row)
            
            # Mantém apenas o registro mais atual do dia
            if (
                len(dados_preparados) > 1 and
                dados_preparados[-1]["Data"] == dados_preparados[-2]["Data"]
            ):
                val = dados_preparados[-2]
                dados_preparados.remove(val)

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
        data_table.LoadData(dados_preparados)

        # Preparados os dados para o gráfico de resumo
        corte = len(dados_preparados) - 15
        dados_preparados_resumo = dados_preparados[corte:]
        data_table_resumo = gviz_api.DataTable(description)
        data_table_resumo.LoadData(dados_preparados_resumo)

        # Resumo
        categorias = Parameters.categorias(Parameters, "resumo", True)
        resumoJson = data_table_resumo.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksResumo = Tick.getTicks(dados_preparados, categorias)

        # Monitorados
        categorias = Parameters.categorias(Parameters, "monitorados", True)
        monitoradosJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksMonitorados = Tick.getTicks(dados_preparados, categorias)

        # Todas
        categorias = Parameters.categorias(Parameters, "todas", True)
        todasJson = data_table.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksTodas = Tick.getTicks(dados_preparados, categorias)

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

        cards, data_completa = Card.getCards(dados_preparados)

        return tableJson, ticks, cards, data_completa