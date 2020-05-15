from apps.core.api import (quantidade_estado_goias, quantidade_geral_brasil, 
							api_brasil_estado, api_brasil_geral)

class Comparacao():

	def getContext(self, request):
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