from .parameters import Parameters

import json

class Chapadao():
    """
    Classe para gerar os gráficos da cidade 
    de Chapadão do Céu.
    """
    def __geral():
        """
        Função privada para gerar os títulos dos 
        eixos X e Y do gráfico e também para 
        que não haja números negativos.

        args:
            None
        
        return:
            Dict com os valores:
                - xTitle
                - yTitle
                - minY
        """
        geral = {
            "xTitle": 'Dia/Mês',
            "yTitle": 'Número de casos',
            "minY": 0            
        }

        return geral
    
    def __resumo(self):
        """
        Função privada para configurar o 
        gráfico de resumo, atualizando as 
        variáveis: cores, ID da <div>, 
        tipo do gráfico e a
        data de atualização do gráfico.

        args:
            self
        
        return:
            Concatenação dos valores gerais com os
            seguintes valores atualizados:
                - colors
                - idDiv
                - tipo_grafico
                - data_atualizacao
        """
        resumo = {
            "colors": Parameters.cores(Parameters, "resumo"),
            "idDiv": 'chapadao-do-ceu-grafico-resumo',
            "tipo_grafico": "resumo",
            "data_atualizacao": "#data-atualizacao-chapadao-do-ceu"
        }

        return {**self.__geral(), **resumo}
    
    def __monitorados(self):
        """
        Função privada para configurar o gráfico de 
        monitorados, atualizando os valores:
        cores, ID da <div>, o tipo do gráfico 
        e a data de atualização do gráfico.

        args:
            self

        return:
            Concatenação dos valores gerais com os
            seguintes valores atualizados:
                - colors
                - idDiv
                - tipo_grafico
                - data_atualizacao
        """
        monitorados = {
            "colors": Parameters.cores(Parameters, "monitorados"),
            "idDiv": 'chapadao-do-ceu-grafico-monitorados',
            "tipo_grafico": "monitorados",
            "data_atualizacao": False
        }

        return {**self.__geral(), **monitorados}
    
    def __todas(self):
        """
        Função para configurar o gráfico de todos
        os dados de Chapadão do Céu, atualizando 
        os valores: cores, ID da <div>, tipo do 
        gráfico e a data de atualização.

        args:
            self
        
        return:
            Concatenação dos valores gerais com os
            seguintes valores atualizados:
                - colors
                - idDiv
                - tipo_grafico
                - data_atualizacao
        """
        todas = {
            "colors": Parameters.cores(Parameters, "todas"),
            "idDiv": 'chapadao-do-ceu-grafico-todas',
            "tipo_grafico": "todas",
            "data_atualizacao": False
        }

        return {**self.__geral(), **todas}
    
    def getValores(self):
        """
        Função para agrupar os dados da 
        funções que atualizam os dados dos gráficos
        de resumo, monitorados e todos os dados.

        args:
            self

        return:
            JSON com os valores:
                - resumo
                - monitorados
                - todas
        """
        parametros = {
            'resumo': self.__resumo(self),
            "monitorados": self.__monitorados(self),
            "todas": self.__todas(self)
        }

        parametros = json.dumps(parametros)

        return parametros