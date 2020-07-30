import datetime
from pprint import pprint

class CardMM():

    def getCards(data):

        primeiro_registro = data[-15]
        ultimo_registro = data[-1]

        variacao = 100*(ultimo_registro["Média Móvel"] - primeiro_registro["Média Móvel"])/primeiro_registro["Média Móvel"]
        variacao *= 100
        variacao = int(variacao/100)

        situacao = ""
        cor_situacao = ""
        if abs(variacao) < 15:
            situacao = "Estável"
            cor_situacao = "orange"
        elif variacao > 15:
            situacao = "Crescente"
            cor_situacao = "red"
        else:
            situacao = "Queda"
            cor_situacao = "green"
        
        var_num = variacao
        sit_num = situacao
        hora = ultimo_registro["Hora"]

        nov_num = ultimo_registro["Novos Casos"]

        mm_num = ultimo_registro["Média Móvel"]
        mm_num *= 10
        mm_num = int(mm_num)/10

        """int_num = ultimo_registro["Internados"]
        obt_num = ultimo_registro["Óbitos"]
        

        if ultimo_registro["Confirmados"] == None:
            conf_num = 0
        if ultimo_registro["Recuperados"] == None:
            rec_num = 0
        if ultimo_registro["Internados"] == None:
            int_num = 0
        if ultimo_registro["Óbitos"] == None:
            obt_num = 0
        """
        #Manipulação da data dos cards
        data_atualizacao = ultimo_registro["Data"]
        mes = [
            "jan", "fev", "mar", 
            "abr", "mai", "jun", 
            "jul", "ago", "set", 
            "out", "nov", "dez"
        ]
        data_card = ""
        if data_atualizacao.day < 10:
            data_card += "0"
        data_card += str(data_atualizacao.day)
        data_card += " " 
        data_card += mes[data_atualizacao.month-1]
        data_card += " " 
        data_card += str(data_atualizacao.year)[2:4]
        data_card += " | "

        hora = hora.split(":")
        hora = hora[0] + "h" + hora[1]
        data_card += hora

        #Manipulação da data completa
        data_atualizacao = ultimo_registro["Data"]
        mes = [
            "janeiro", "fevereiro", "março", 
            "abril", "maio", "junho", 
            "julho", "agosto", "setembro", 
            "outubro", "novembro", "dezembro"
        ]
        data_completa = str(data_atualizacao.day)
        data_completa += " de " 
        data_completa += mes[data_atualizacao.month-1]
        data_completa += " de " + str(data_atualizacao.year)        

        cards = {
            "data": data_card,
            "valores": [
                {
                    "categoria": "Novos Casos",
                    "numero": nov_num,
                    "cor": "red",
                    "icone": "fas fa-user-injured"
                },
                {
                    "categoria": "Média Móvel",
                    "numero": mm_num,
                    "cor": "blue",
                    "icone": "fas fa-user-injured"
                },
                {
                    "categoria": "Var. (15d)",
                    "numero": str(var_num) + " %",
                    "cor": "purple",
                    "icone": "fas fa-chart-line"
                },
                {
                    "categoria": "Situação",
                    "numero": sit_num,
                    "cor": cor_situacao,
                    "icone": "fas fa-traffic-light"
                }
            ]
        }

        return cards, data_completa