from django.db import models
import uuid

class BoletimEpidemiologico(models.Model):

    cidade = models.CharField(max_length=256, verbose_name="Cidade")
    data_atualizacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de atualização")
    fonte_oficial = models.URLField(verbose_name="Fonte Oficial (URL)")

    confirmados = models.PositiveIntegerField(verbose_name="Confirmados", null=True)
    recupados = models.PositiveIntegerField(verbose_name="Recuperados", null=True)
    obitos = models.PositiveIntegerField(verbose_name="Óbitos", null=True)
    suspeitos = models.PositiveIntegerField(verbose_name="Suspeitos", null=True)
    investigados = models.PositiveIntegerField(
        verbose_name="Investigados/Análise Laboratorial", null=True)
    descartados = models.PositiveIntegerField(
        verbose_name="Descartados/Excluídos/Negativos", null=True)
    
    monitorados = models.PositiveIntegerField(verbose_name="Monitorados", null=True)
    notificados = models.PositiveIntegerField(verbose_name="Notificados", null=True)
    isolados = models.PositiveIntegerField(verbose_name="Isolados", null=True)

    internados = models.PositiveIntegerField(verbose_name="Internados", null=True)
    enfermaria = models.PositiveIntegerField(verbose_name="Enfermaria", null=True)
    uti = models.PositiveIntegerField(verbose_name="UTI", null=True)

    uuid = models.UUIDField(
        verbose_name="Uuid", default=uuid.uuid4, editable=False
    )


    def __str__(self):
        return self.cidade + ": " + self.data_atualizacao


    class Meta:
        unique_together = ('cidade', 'data_atualizacao')
        verbose_name = "Boletim"
        verbose_name_plural = "Boletins"

class Graficos(models.Model): 
    
    def getContext(self, cidade):
        if cidade == "jatai":
            return self.__jatai(self)
        if cidade == "mineiros":
            return self.__mineiros()
        if cidade == "rioverde":
            return self.__rioverde()
    
    def __commonValues():
        context = {            
            "grupo": "graficos",
            "grupo_link": "graficos",
            "goias": 10,
		    "brasil": 100,
        }

        return context

    def __cardDict(conf_num, rec_num, int_num, obt_num):
        values = [
            {
                "categoria": "Confirmados",
                "numero": conf_num,
                "cor": "red",
                "icone": "fas fa-user-injured"
            },
            {
                "categoria": "Recuperados",
                "numero": rec_num,
                "cor": "purple",
                "icone": "fas fa-virus-slash"
            },
            {
                "categoria": "Internados",
                "numero": int_num,
                "cor": "blue",
                "icone": "fas fa-procedures"
            },
            {
                "categoria": "Óbitos",
                "numero": obt_num,
                "cor": "black",
                "icone": "fas fa-skull-crossbones"
            }
        ]

        return values

    def __jatai(self):
        context = {
            "script": "graficos-jatai",
            "informacoes": {
                "titulo": "Observatório UFJ Covid-19 - Gráficos (Jataí)",
                "cidade": "Jataí",
                "nome_base": "jatai",
                "url_fonte": "https://www.jatai.go.gov.br/",
                "nome_fonte": "Secretária de Saúde de Jataí",
                "data": "12 de maio",
                "conf_num": "32",
                "rec_num": "13",
                "int_num": "1",
                "obt_num": "0"
            },
            "querysets": self.__cardDict(32, 13, 1, 0),
        }

        return {**self.__commonValues(), **context}

    def __mineiros():
        context = {
            "grupo": "graficos",
            "grupo_link": "graficos",
            "script": "graficos-mineiros",
		    "informacoes": {
                "titulo": "Observatório UFJ Covid-19 - Gráficos (Mineiros)",
                "grupo": "graficos",
                "cidade": "Mineiros",
                "nome_base": "mineiros",
                "url_fonte": "http://mineiros.go.gov.br/covid-19.php",
                "nome_fonte": "Secretária de Saúde de Mineiros",

                "data": "13 de maio",
                "conf_num": "10",
                "rec_num": "5",
                "int_num": "1",
                "obt_num": "0"
            },
            "goias": 10,
		    "brasil": 100,
            "querysets": [
                {
                    "categoria": "Confirmados",
                    "numero": "10",
                    "cor": "red",
                    "icone": "fas fa-user-injured"
                },
                {
                    "categoria": "Recuperados",
                    "numero": "5",
                    "cor": "purple",
                    "icone": "fas fa-virus-slash"
                },
                {
                    "categoria": "Internados",
                    "numero": "1",
                    "cor": "blue",
                    "icone": "fas fa-procedures"
                },
                {
                    "categoria": "Óbitos",
                    "numero": "0",
                    "cor": "black",
                    "icone": "fas fa-skull-crossbones"
                }
            ]
        }

        return context

    def __rioverde():
        context = {
            "grupo": "graficos",
            "grupo_link": "graficos",
            "script": "graficos-rioverde",
		    "informacoes": {
                "titulo": "Observatório UFJ Covid-19 - Gráficos (Rio Verde)",
                "grupo": "graficos",
                "cidade": "Rio Verde",
                "nome_base": "rioverde",
                "url_fonte": "https://www.rioverde.go.gov.br/covid19/",
                "nome_fonte": "Secretária de Saúde de Rio Verde",

                "data": "10 de maio",
                "conf_num": "23",
                "rec_num": "14",
                "int_num": "0",
                "obt_num": "1"
            },
            "goias": 10,
		    "brasil": 100,
            "querysets": [
                {
                    "categoria": "Confirmados",
                    "numero": "23",
                    "cor": "red",
                    "icone": "fas fa-user-injured"
                },
                {
                    "categoria": "Recuperados",
                    "numero": "14",
                    "cor": "purple",
                    "icone": "fas fa-virus-slash"
                },
                {
                    "categoria": "Internados",
                    "numero": "0",
                    "cor": "blue",
                    "icone": "fas fa-procedures"
                },
                {
                    "categoria": "Óbitos",
                    "numero": "1",
                    "cor": "black",
                    "icone": "fas fa-skull-crossbones"
                }
            ]
        }

        return context