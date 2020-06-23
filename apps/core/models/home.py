class Home:
    def getContext(self):
        return self.__contextHome(self)

    def __contextHome(self):
        context = {
            "grupo": "geral",
            "script": "geral",
            "grupo_link": "principal",
            "titulo": "Observatório UFJ Covid-19 - Principal",
        }
        return context
