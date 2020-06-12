from django.db import models
import uuid

from django.views.decorators.http import require_GET, require_POST, require_http_methods
import datetime

from ..forms.createForm import CreateBoletimEpidemiologicoForm
from ..forms.deleteForm import DeleteBoletimEpidemiologicoForm

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

    def get_create_boletim(self, request):
        return self.__createBoletimEpidemiologico(self, request)
    
    def get_delete_boletim(self, request):
        return self.__deleteBoletimEpidemiologico(self, request)

    def get_read_boletim(self, request):
        return self.__readBoletimEpidemiologico(self, request)
    
    def get_update_boletim(self, request):
        return self.__updateBoletimEpidemiologico(self, request)

    def __createBoletimEpidemiologico(self, request):
        if request.method == 'POST':
            form = CreateBoletimEpidemiologicoForm(request.POST)
            if form.is_valid():
                cidade = form.cleaned_data['cidade']
                data_atualizacao = form.cleaned_data['data_atualizacao']
                fonte_oficial = form.cleaned_data['fonte_oficial']			
                confirmados = form.cleaned_data['confirmados']			
                recuperados = form.cleaned_data['recuperados']			
                obitos = form.cleaned_data['obitos']			
                suspeitos = form.cleaned_data['suspeitos']			
                investigados = form.cleaned_data['investigados']			
                descartados = form.cleaned_data['descartados']			
                monitorados = form.cleaned_data['monitorados']			
                notificados = form.cleaned_data['notificados']			
                isolados = form.cleaned_data['isolados']			
                internados = form.cleaned_data['internados']			
                enfermaria = form.cleaned_data['enfermaria']			
                uti = form.cleaned_data['uti']	

                BoletimEpidemiologico(cidade = cidade, data_atualizacao = data_atualizacao, 
                fonte_oficial = fonte_oficial, confirmados = confirmados, 
                recuperados = recuperados, obitos = obitos, suspeitos = suspeitos, 
                investigados = investigados, descartados = descartados, 
                monitorados = monitorados, notificados = notificados, isolados = isolados, 
                internados = internados, enfermaria = enfermaria, uti = uti).save()	
        else:
            form = CreateBoletimEpidemiologicoForm()

        context = {'form': form}

        return context

    def __readBoletimEpidemiologico(self, request):
        if request.method == 'GET':
            form = DeleteBoletimEpidemiologicoForm(request.GET)
            boletim = None
            if form.is_valid():
                cidade = form.cleaned_data['cidade']
                data_atualizacao = form.cleaned_data['data_atualizacao']
                boletim = BoletimEpidemiologico.objects.get(cidade = cidade,
                data_atualizacao = data_atualizacao)
        else:
            form = DeleteBoletimEpidemiologicoForm()

        context = {'form': form,
                'boletim': boletim}

        return context

    
    def __updateBoletimEpidemiologico(self, request):	
        boletim = None
        if request.method == 'POST':
            form = CreateBoletimEpidemiologicoForm(request.POST)
            if form.is_valid():
                cidade = form.cleaned_data['cidade']
                data_atualizacao = form.cleaned_data['data_atualizacao']
                fonte_oficial = form.cleaned_data['fonte_oficial']			
                confirmados = form.cleaned_data['confirmados']			
                recuperados = form.cleaned_data['recuperados']			
                obitos = form.cleaned_data['obitos']			
                suspeitos = form.cleaned_data['suspeitos']			
                investigados = form.cleaned_data['investigados']			
                descartados = form.cleaned_data['descartados']			
                monitorados = form.cleaned_data['monitorados']			
                notificados = form.cleaned_data['notificados']			
                isolados = form.cleaned_data['isolados']			
                internados = form.cleaned_data['internados']			
                enfermaria = form.cleaned_data['enfermaria']			
                uti = form.cleaned_data['uti']	

                try:
                    boletim = BoletimEpidemiologico.objects.get(cidade = cidade,
                data_atualizacao = data_atualizacao)
                    boletim.cidade = cidade 
                    boletim.data_atualizacao = data_atualizacao
                    boletim.fonte_oficial = fonte_oficial
                    boletim.confirmados = confirmados
                    boletim.recuperados = recuperados
                    boletim.obitos = obitos
                    boletim.suspeitos = suspeitos
                    boletim.investigados = investigados
                    boletim.descartados = descartados
                    boletim.monitorados = monitorados
                    boletim.notificados = notificados
                    boletim.isolados = isolados
                    boletim.internados = internados
                    boletim.enfermaria = enfermaria
                    boletim.uti = uti
                    
                    boletim.save()
                except boletim.DoesNotExist:
                    return False
        else:
            form = CreateBoletimEpidemiologicoForm()
        context = {'form': form,
                'boletim': boletim}

        return context

    def __deleteBoletimEpidemiologico(self, request):
        if request.method == 'GET':
            form  = DeleteBoletimEpidemiologicoForm(request.GET)
            if form.is_valid():
                cidade = form.cleaned_data['cidade']
                data_atualizacao = form.cleaned_data['data_atualizacao']
                try:
                    boletim = BoletimEpidemiologico.objects.get(cidade = cidade,
                    data_atualizacao = data_atualizacao)
                    boletim.delete()
                except boletim.DoesNotExist:
                    return False
        else:
            form = DeleteBoletimEpidemiologicoForm()

        context = {'form': form}

        return context

