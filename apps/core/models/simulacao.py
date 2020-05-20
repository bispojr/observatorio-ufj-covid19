
class Simulacao():

    def getContext(self):
        return self.__contextSobre(self)

    def __contextSobre(self):
        context = {
            "grupo": "geral",
            "grupo_link": "simulacao",
            "script": "simulacao",
            "titulo": "Observatório UFJ Covid-19 - Simulação"
        }
        return context
