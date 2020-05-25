class Cidades():
    def getContext(self):
        return self.__contextCidades(self)

    def __contextCidades(self):
        context = {
            "grupo": "graficos",
            "grupo_link": "mapa",
            "script": "mapa",
            "titulo": "Mapa do estado de Goiás"
        }
        return context