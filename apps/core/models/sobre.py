
class Sobre():
    """
    Classe para criar o context da página Sobre

    methods:
        getContext
    """
    def getContext(self):
        """
        Retorna o contexto da página contendo:
            - grupo
            - grupo_link
            - script
            - titulo
        
        args:
            self
        
        return:
            Dict com os dados do contexto da página.
        """
        return self.__contextSobre(self)

    def __contextSobre(self):
        context = {
            "grupo": "geral",
            "grupo_link": "saiba_mais",
            "script": "geral",
            "titulo": "Observatório UFJ Covid-19 - Sobre"
            }
        return context