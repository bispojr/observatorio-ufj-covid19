from django.db import models, IntegrityError
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
        """
        Função CREATE do boletim epidemiológico

        Args:(self, request)

        Uma request do tipo POST é recebida pela função,
        as informações da request são armazenadas em um 
        dict (req) e então, caso não haja nenhum erro de 
        integridade, o boletim é criado. Caso contrário,
        uma mensagem de erro é retornada.

        Return: dict com os atributos do boletim

        OBS1.: Não é possível criar um novo item no banco direto pela request
        utilizando **request porque surge uma reclamação que não existe ID.

        OBS2.: Não é possível retornar o objeto boletim porque a função .save()
        não tem retorno: https://docs.djangoproject.com/en/3.0/ref/models/instances/
        """
        return self.__createBoletimEpidemiologico(self, request)
    
    def get_delete_boletim(self, request):
        """
        Função DELETE do boletim epidemiologico

        Args:(self, request)

        A função recebe uma requisição, armazena os dados 
        essenciais em um dict (req), busca no banco de dados 
        se a query existe, se existir, deleta o objeto e 
        retorna quantos objetos foram excluídos.

        Return: Quantidade de objetos excluídos.
        
        Exemplo de retorno: (1, {'core.BoletimEpidemiologico': 1})
        
        Neste caso, uma query do banco foi excluída.
        """
        return self.__deleteBoletimEpidemiologico(self, request)

    def get_read_boletim(self, request):
        """
        Função READ do boletim epidemiologico

        Args:(self, request)

        A função recebe uma requisição, armazena os dados 
        essenciais em um dict (req), busca no banco de dados 
        se a query existe e, se existir, retorna o objeto.

        Return: objeto com os atributos do boletim
        """
        return self.__readBoletimEpidemiologico(self, request)
    
    def get_update_boletim(self, request):
        """
        Função UPDATE do boletim epidemiologico.

        Args:(self, request)

        Uma requisição POST é recebida pelo argumento request,
        as informações contidas na requisição são armazenadas 
        em um dict (req), é feito uma busca no banco com os
        dados da requisição e então, se não houver nenhum
        erro de integridade, o boletim é atualizado.

        Return: objeto com os atributos do boletim
        """
        return self.__updateBoletimEpidemiologico(self, request)

    def __createBoletimEpidemiologico(self, request):
        req = {
            'cidade': request.POST.get('cidade'),
            'data_atualizacao' : request.POST.get('data_atualizacao'),
            'fonte_oficial' : request.POST.get('fonte_oficial'),			
            'confirmados' : request.POST.get('confirmados'),			
            'recuperados' : request.POST.get('recuperados'),			
            'obitos' : request.POST.get('obitos'),			
            'suspeitos' : request.POST.get('suspeitos'),			
            'investigados' : request.POST.get('investigados'),			
            'descartados' : request.POST.get('descartados'),			
            'monitorados' : request.POST.get('monitorados'),			
            'notificados' : request.POST.get('notificados'),			
            'isolados' : request.POST.get('isolados'),			
            'internados' : request.POST.get('internados'),			
            'enfermaria' : request.POST.get('enfermaria'),			
            'uti' : request.POST.get('uti')
        }
        try:
            BoletimEpidemiologico(**req).save()	
        except IntegrityError as e:
            return ("Erro de integridade {}", e)
        
        return req

    def __readBoletimEpidemiologico(self, request):
        req = {
            'cidade': request.POST.get('cidade'),
            'data_atualizacao' : request.POST.get('data_atualizacao')
        }

        try:
            boletim = BoletimEpidemiologico.objects.get(cidade = req['cidade'],
        data_atualizacao = req['data_atualizacao'])

        except boletim.DoesNotExist:
            return ("O Boletim não existe!")

        return boletim
    
    def __updateBoletimEpidemiologico(self, request):	

        req = {
            'cidade': request.POST.get('cidade'),
            'data_atualizacao' : request.POST.get('data_atualizacao'),
            'fonte_oficial' : request.POST.get('fonte_oficial'),			
            'confirmados' : request.POST.get('confirmados'),			
            'recuperados' : request.POST.get('recuperados'),			
            'obitos' : request.POST.get('obitos'),			
            'suspeitos' : request.POST.get('suspeitos'),			
            'investigados' : request.POST.get('investigados'),			
            'descartados' : request.POST.get('descartados'),			
            'monitorados' : request.POST.get('monitorados'),			
            'notificados' : request.POST.get('notificados'),			
            'isolados' : request.POST.get('isolados'),			
            'internados' : request.POST.get('internados'),			
            'enfermaria' : request.POST.get('enfermaria'),			
            'uti' : request.POST.get('uti')
        }

        try:
            boletim = BoletimEpidemiologico.objects.get(cidade = req['cidade'],
        data_atualizacao = req['data_atualizacao'])
        
            boletim.cidade = req['cidade']
            boletim.data_atualizacao = req['data_atualizacao']
            boletim.fonte_oficial = req['fonte_oficial']
            boletim.confirmados = req['confirmados']
            boletim.recuperados = req['recuperados']
            boletim.obitos = req['obitos']
            boletim.suspeitos = req['suspeitos']
            boletim.investigados = req['investigados']
            boletim.descartados = req['descartados']
            boletim.monitorados = req['monitorados']
            boletim.notificados = req['notificados']
            boletim.isolados = req['isolados']
            boletim.internados = req['internados']
            boletim.enfermaria = req['enfermaria']
            boletim.uti = req['uti']
            
            boletim.save()
        except IntegrityError as e:
            return ("Erro de integridade {}", e)
        except boletim.DoesNotExist:
            return ("O Boletim não existe!")

        return boletim

    def __deleteBoletimEpidemiologico(self, request):

        req = {
            'cidade': request.POST.get('cidade'),
            'data_atualizacao' : request.POST.get('data_atualizacao')
        }

        try:
            boletim = BoletimEpidemiologico.objects.get(cidade = req['cidade'],
        data_atualizacao = req['data_atualizacao'])
            result = boletim.delete()

        except boletim.DoesNotExist:
            return ("O Boletim não existe!")

        return result

