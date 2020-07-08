
class Colabore():
    """
    Classe para criar o context da página Colabore

    methods:
        getContext
    """
    def getContext(self):
        """
        Retorna o contexto da página contendo:
            - grupo
            - grupo_link
            - titulo
        
        args:
            self
        
        return:
            Dict com os dados do contexto da página.
        """
        return self.__contextColabore(self)

    def __contextColabore(self):
        context = {
		"grupo": "geral",
		"grupo_link": "saiba_mais",
		"titulo": "Observatório UFJ Covid-19 - Colabore"
		}
        return context