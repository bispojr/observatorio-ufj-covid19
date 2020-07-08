class Noticias:
    def getContext(self):
        return self.__contextNoticias(self)

    def __contextNoticias(self):
        context = {
            "grupo": "",
            "grupo_link": "noticias",
            "script": "noticias",
            "titulo": "Observatório UFJ Covid-19 - Notícias",
        }
        return context
