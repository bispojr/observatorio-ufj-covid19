class Sobre:
    def getContext(self):
        return self.__contextSobre(self)

    def __contextSobre(self):
        context = {
            "grupo": "geral",
            "grupo_link": "saiba_mais",
            "script": "geral",
            "titulo": "Observatório UFJ Covid-19 - Sobre",
        }
        return context
