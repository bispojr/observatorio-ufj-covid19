import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gviz_api
from pprint import pprint
from datetime import datetime
from django.conf import settings
import json

from .card_mm import CardMM
from apps.core.models.chartbuilder.tick import Tick
from .parameters_MM import ParametersMM

class DataTableMM(): 
    
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
            cidade != "Caçu" and 
            cidade != "Chapadão do Céu" and 
            cidade != "Jataí" and
            cidade != "Mineiros" and 
            cidade != "Montividiu" and
            cidade != "Rio Verde" and
            cidade != "Santa Helena"
        ):
            print("Cidade inexistente em nossa base de dados")
        
        # Open the spreadhseet
        sheet = client.open(cidade).sheet1 
        dados = sheet.get_all_records()  # Get a list of all records
        
        # Preparação dos dados
        ultimo_registro = -1
        dados_preparados = []
        for row in dados:
            #Convertendo para o formato de data do Python
            row["Data"] = datetime.strptime(row["Data"], '%d/%m/%Y')

            #Convertendo para Null os campos sem valor
            
            for val in row:
                if row[val] == '-' or row[val] == '':
                    row[val] = 0

            novalinha = {}
            novalinha["Data"] = row["Data"]
            novalinha["Hora"] = row["Hora"]
            if ultimo_registro == -1:
                novalinha["Novos Casos"] = row["Confirmados"]    
            else:
                novalinha["Novos Casos"] = row["Confirmados"] - ultimo_registro
            
            ultimo_registro = row["Confirmados"]
            dados_preparados.append(novalinha)

            # Mantém apenas o registro mais atual do dia
            if (
                len(dados_preparados) > 1 and
                dados_preparados[-1]["Data"] == dados_preparados[-2]["Data"]
            ):
                val = dados_preparados[-2]
                dados_preparados.remove(val)

        qtd = 1
        for row in dados_preparados:
            if qtd < 7:
                row["Média Móvel"] = 0
                for i in range(qtd):
                    row["Média Móvel"] += dados_preparados[i]["Novos Casos"]
                row["Média Móvel"] /= qtd +1
            else:
                row["Média Móvel"] = 0
                for i in range(7):
                    row["Média Móvel"] += dados_preparados[qtd-7+i]["Novos Casos"]
                row["Média Móvel"] /= 7

            qtd += 1

        description = {
            'Data': ("date", "Data"),
            'Novos Casos': ("number", "Novos Casos"),
            'Média Móvel': ("number", "Média Móvel")
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
        categorias = ParametersMM.categorias(ParametersMM, "media-movel", True)
        resumoJson = data_table_resumo.ToJSon(
            columns_order=tuple(categorias),
            order_by="Data"
        )
        ticksResumo = Tick.getTicks(dados_preparados, categorias)

        # Preparação da saída
        tableJson = {
            "resumo": resumoJson
        }

        ticks = {
            "resumo": json.dumps(ticksResumo)
        }

        cards, data_completa = CardMM.getCards(dados_preparados)

        return tableJson, ticks, cards, data_completa