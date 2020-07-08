
class NaMidia():
    """
    Classe para criar o context da página Na Mídia

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
        return self.__contextNaMidia(self)
    
    def __contextNaMidia(self):
        context = {
		"grupo": "geral", 
		"grupo_link": "saiba_mais",
		"script": "na-midia",
		"titulo": "Observatório UFJ Covid-19 - Na Mídia"
		}
        return context