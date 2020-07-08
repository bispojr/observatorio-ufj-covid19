
class ComoSaoCriados():
    """
    Classe para criar o context da página ComoSaoCriados

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
        return self.__contextComoSaoCriados(self)

    def __contextComoSaoCriados(self):
        context = {
            "grupo": "geral",
            "grupo_link": "graficos",
            "script": "geral",
            "titulo": "Observatório UFJ Covid-19 - Como são criados?"
        }  
        return context