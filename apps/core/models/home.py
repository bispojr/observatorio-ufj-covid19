
class Home():
    """
    Classe para criar o context da Home

    methods:
        getContext
    """
    def getContext(self):
         """
        Retorna o contexto da página contendo:
            - grupo
            - grupo_link
            - titulo
            - script
        
        args:
            self
        
        return:
            Dict com os dados do contexto da página.
        """
        return self.__contextHome(self)

    def __contextHome(self):
        context = {
            "grupo": "geral",
            "script": "geral",
            "grupo_link": "principal",
            "titulo": "Observatório UFJ Covid-19 - Principal"
        }
        return context