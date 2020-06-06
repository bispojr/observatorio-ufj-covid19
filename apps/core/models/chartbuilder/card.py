import datetime
from pprint import pprint

class Card():

    def getCards(data):

        ultimo_registro = data[-1]
        
        conf_num = ultimo_registro["Confirmados"]
        rec_num = ultimo_registro["Recuperados"]
        int_num = ultimo_registro["Internados"]
        obt_num = ultimo_registro["Óbitos"]

        if ultimo_registro["Confirmados"] == None:
            conf_num = 0
        if ultimo_registro["Recuperados"] == None:
            rec_num = 0
        if ultimo_registro["Internados"] == None:
            int_num = 0
        if ultimo_registro["Óbitos"] == None:
            obt_num = 0

        #Manipulação da data
        data_atualizacao = ultimo_registro["Data"]
        mes = [
            "janeiro", "fevereiro", "março", 
            "abril", "maio", "junho", 
            "julho", "agosto", "setembro", 
            "outubro", "novembro", "dezembro"
        ]
        data_card = str(data_atualizacao.day)
        data_card += " de " 
        data_card += mes[data_atualizacao.month-1]

        cards = {
            "data": data_card,
            "valores": [
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
        }

        return cards