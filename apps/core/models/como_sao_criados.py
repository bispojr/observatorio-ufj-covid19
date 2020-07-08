class ComoSaoCriados:
    def getContext(self):
        return self.__contextComoSaoCriados(self)

    def __contextComoSaoCriados(self):
        context = {
            "grupo": "geral",
            "grupo_link": "graficos",
            "script": "geral",
            "titulo": "Observatório UFJ Covid-19 - Como são criados?",
        }
        return context
