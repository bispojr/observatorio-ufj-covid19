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