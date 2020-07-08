from apps.core.api import (quantidade_estado_goias, quantidade_geral_brasil, 
							api_brasil_estado, api_brasil_geral)

class Comparacao():
	"""
    Classe para criar o context da página Comparacao

    methods:
        getContext
    """
	def getContext(self, request):
		"""
        Retorna o contexto da página contendo:
            - grupo
            - grupo_link
			- script
            - titulo
			- nome_base
			- goias
			- brasil
        
        args:
            self
        
        return:
            Dict com os dados do contexto da página.
        """
		return self.__contextComparacao(self, request)

	def __contextComparacao(self, request):
		quantidade_goias = quantidade_estado_goias(request)
		quantidade_brasil = quantidade_geral_brasil(request)

		context = {
			"grupo": "graficos",
			"grupo_link": "graficos",
			"script": "graficos-comparacao",
			"titulo": "Observatório UFJ Covid-19 - Comparação entre as cidades",
			"nome_base": "jatai",
			"goias": quantidade_goias,
			"brasil": quantidade_brasil
		}
		return context