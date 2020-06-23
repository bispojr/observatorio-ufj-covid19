import datetime
from pprint import pprint


class Card:
    def getCards(data):

        ultimo_registro = data[-1]

        conf_num = ultimo_registro["Confirmados"]
        rec_num = ultimo_registro["Recuperados"]
        int_num = ultimo_registro["Internados"]
        obt_num = ultimo_registro["Óbitos"]
        hora = ultimo_registro["Hora"]

        if ultimo_registro["Confirmados"] == None:
            conf_num = 0
        if ultimo_registro["Recuperados"] == None:
            rec_num = 0
        if ultimo_registro["Internados"] == None:
            int_num = 0
        if ultimo_registro["Óbitos"] == None:
            obt_num = 0

        # Manipulação da data dos cards
        data_atualizacao = ultimo_registro["Data"]
        mes = [
            "jan",
            "fev",
            "mar",
            "abr",
            "mai",
            "jun",
            "jul",
            "ago",
            "set",
            "out",
            "nov",
            "dez",
        ]
        data_card = ""
        if data_atualizacao.day < 10:
            data_card += "0"
        data_card += str(data_atualizacao.day)
        data_card += " "
        data_card += mes[data_atualizacao.month - 1]
        data_card += " "
        data_card += str(data_atualizacao.year)[2:4]
        data_card += " | "

        hora = hora.split(":")
        hora = hora[0] + "h" + hora[1]
        data_card += hora

        # Manipulação da data completa
        data_atualizacao = ultimo_registro["Data"]
        mes = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro",
        ]
        data_completa = str(data_atualizacao.day)
        data_completa += " de "
        data_completa += mes[data_atualizacao.month - 1]
        data_completa += " de " + str(data_atualizacao.year)

        cards = {
            "data": data_card,
            "valores": [
                {
                    "categoria": "Confirmados",
                    "numero": conf_num,
                    "cor": "red",
                    "icone": "fas fa-user-injured",
                },
                {
                    "categoria": "Recuperados",
                    "numero": rec_num,
                    "cor": "purple",
                    "icone": "fas fa-virus-slash",
                },
                {
                    "categoria": "Internados",
                    "numero": int_num,
                    "cor": "blue",
                    "icone": "fas fa-procedures",
                },
                {
                    "categoria": "Óbitos",
                    "numero": obt_num,
                    "cor": "black",
                    "icone": "fas fa-skull-crossbones",
                },
            ],
        }

        return cards, data_completa
