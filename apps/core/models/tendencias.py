class Tendencias:
    def get_informações(self, cidade):
        return self.__informacoesTendencias(self, cidade)

    def __informacoesTendencias(self, cidade):
        if cidade == "jatai":
            informacoes = {
                "grupo": "tendencias",
                "grupo_link": "tendencias",
                "script": "tendencias-jatai",
                "titulo": "Observatório UFJ Covid-19 - Tendências (Jataí)",
                "cidade": "Jataí (GO)",
                "nome_base": "jatai",
            }
        else:
            informacoes = {
                "grupo": "tendencias",
                "grupo_link": "tendencias",
                "script": "tendencias-rioverde",
                "titulo": "Observatório UFJ Covid-19 - Tendências (Rio Verde)",
                "cidade": "Rio Verde (GO)",
                "nome_base": "rioverde",
            }
        return informacoes
