from django.db import models
import uuid

from django.views.decorators.http import require_GET, require_POST, require_http_methods
import datetime

class BoletimEpidemiologico(models.Model):

    cidade = models.CharField(max_length=256, verbose_name="Cidade")
    data_atualizacao = models.DateTimeField(verbose_name="Data de atualização")
    fonte_oficial = models.URLField(verbose_name="Fonte Oficial (URL)")

    confirmados = models.PositiveIntegerField(verbose_name="Confirmados", null=True)
    recuperados = models.PositiveIntegerField(verbose_name="Recuperados", null=True)
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
        return self.cidade + ": " + str(self.data_atualizacao)


    class Meta:
        unique_together = ('cidade', 'data_atualizacao')
        verbose_name = "Boletim"
        verbose_name_plural = "Boletins"

    def createBoletimEpidemiologico(request):
        upload = BoletimEpidemiologico()
        if request.method == 'POST':
            if (request.POST.get('cidade') and
                request.POST.get('data_atualizacao') and
                request.POST.get('fonte_oficial') and
                request.POST.get('confirmados') and
                request.POST.get('recuperados') and
                request.POST.get('obitos') and
                request.POST.get('suspeitos') and
                request.POST.get('investigados') and
                request.POST.get('descartados') and
                request.POST.get('monitorados') and
                request.POST.get('notificados') and
                request.POST.get('isolados') and
                request.POST.get('internados') and
                request.POST.get('enfermaria') and
                request.POST.get('uti')):

                upload.cidade = request.POST.get('cidade')
                upload.data_atualizacao = request.POST.get('data_atualizacao')
                upload.fonte_oficial = request.POST.get('fonte_oficial')
                upload.confirmados = request.POST.get('confirmados')
                upload.recuperados = request.POST.get('recuperados')
                upload.obitos = request.POST.get('obitos')
                upload.suspeitos = request.POST.get('suspeitos')
                upload.investigados = request.POST.get('investigados')
                upload.descartados = request.POST.get('descartados')
                upload.monitorados = request.POST.get('monitorados')
                upload.notificados = request.POST.get('notificados')
                upload.isolados = request.POST.get('isolados')
                upload.internados = request.POST.get('internados')
                upload.enfermaria = request.POST.get('enfermaria')
                upload.uti = request.POST.get('uti')

                return upload.save()

            else:
                print("Ocorreu um erro durante a operação CREATE!")

    def readBoletimEpidemiologico(request):
        try:
            items = BoletimEpidemiologico.objects.all()
            return items
        except:
            print("Não há objetos no banco!")

    def updateBoletimEpidemiologico(request, cidade, data_atualizacao):
        try:
            boletimSelect = BoletimEpidemiologico.objects.get(cidade = cidade, data_atualizacao = data_atualizacao)
            if (request.POST.get('cidade') or
                request.POST.get('data_atualizacao') or
                request.POST.get('fonte_oficial') or
                request.POST.get('confirmados') or
                request.POST.get('recuperados') or
                request.POST.get('obitos') or
                request.POST.get('suspeitos') or
                request.POST.get('investigados') or
                request.POST.get('descartados') or
                request.POST.get('monitorados') or
                request.POST.get('notificados') or
                request.POST.get('isolados') or
                request.POST.get('internados') or
                request.POST.get('enfermaria') or
                request.POST.get('uti')):

                boletimSelect.cidade = request.POST.get('cidade')
                boletimSelect.data_atualizacao = request.POST.get('data_atualizacao')
                boletimSelect.fonte_oficial = request.POST.get('fonte_oficial')
                boletimSelect.confirmados = request.POST.get('confirmados')
                boletimSelect.recuperados = request.POST.get('recuperados')
                boletimSelect.obitos = request.POST.get('obitos')
                boletimSelect.suspeitos = request.POST.get('suspeitos')
                boletimSelect.investigados = request.POST.get('investigados')
                boletimSelect.descartados = request.POST.get('descartados')
                boletimSelect.monitorados = request.POST.get('monitorados')
                boletimSelect.notificados = request.POST.get('notificados')
                boletimSelect.isolados = request.POST.get('isolados')
                boletimSelect.internados = request.POST.get('internados')
                boletimSelect.enfermaria = request.POST.get('enfermaria')
                boletimSelect.uti = request.POST.get('uti')

                return boletimSelect
        except:
            print("Ocorreu um erro durante a operação de UPDATE!")

    def deleteBoletimEpidemiologico(request, cidade, data_atualizacao):
        try:
            boletimDelete = BoletimEpidemiologico.objects.get(cidade = cidade, data_atualizacao = data_atualizacao)
            boletimDelete.delete()
            return ("Deletado com sucesso!")
        except:
            print("Ocorreu um erro durante a operação DELETE!")
        

