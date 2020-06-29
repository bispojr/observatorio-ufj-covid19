from django.db import models, IntegrityError
from django.core.exceptions import ValidationError
import uuid

from django.views.decorators.http import require_GET, require_POST, require_http_methods
import datetime

from ..forms.createForm import CreateBoletimEpidemiologicoForm
from ..forms.deleteForm import DeleteBoletimEpidemiologicoForm

class BoletimEpidemiologico(models.Model):

    cidade = models.CharField(max_length=256, verbose_name="Cidade")
    data_atualizacao = models.DateTimeField(verbose_name="Data de atualização")
    fonte_oficial_url = models.URLField(verbose_name="Fonte Oficial (URL)")
    fonte_oficial_tipo = models.CharField(max_length=256, default="Prefeitura", verbose_name="Fonte Oficial (Tipo)")

    confirmados = models.PositiveIntegerField(verbose_name="Confirmados", null=True)
    conf_reside = models.PositiveIntegerField(verbose_name="Confirmados que residem na cidade", null=True)
    conf_nao_reside = models.PositiveIntegerField(verbose_name="Confirmados que não residem na cidade", null=True)
    recuperados = models.PositiveIntegerField(verbose_name="Recuperados", null=True)
    obitos = models.PositiveIntegerField(verbose_name="Óbitos", null=True)
    isolados = models.PositiveIntegerField(verbose_name="Isolados", null=True)
    iso_domiciliar = models.PositiveIntegerField(verbose_name="Isolados domiciliar", null=True)
    iso_hospitalar = models.PositiveIntegerField(verbose_name="Isolados hospitalar", null=True)
    iso_hosp_sus = models.PositiveIntegerField(verbose_name="Isolados hospitalar SUS", null=True)
    iso_hosp_priv = models.PositiveIntegerField(verbose_name="Isolados hospitalar privado", null=True)
    iso_hosp_sus_enf = models.PositiveIntegerField(verbose_name="Isolados hospitalar SUS enfermaria", null=True)
    iso_hosp_priv_enf = models.PositiveIntegerField(verbose_name="Isolados hospitalar privado enfermaria", null=True)
    iso_hosp_sus_uti = models.PositiveIntegerField(verbose_name="Isolados hospitalar SUS UTI", null=True)
    iso_hosp_priv_uti = models.PositiveIntegerField(verbose_name="Isolados hospitalar privado UTI", null=True)

    suspeitos = models.PositiveIntegerField(verbose_name="Suspeitos", null=True)
    sus_isolados = models.PositiveIntegerField(verbose_name="Suspeitos isolados", null=True)
    sus_iso_domiciliar = models.PositiveIntegerField(verbose_name="Suspeitos isolados domiciliar", null=True)
    sus_iso_hospitalar = models.PositiveIntegerField(verbose_name="Suspeitos isolados hospitalar", null=True)
    sus_investigados = models.PositiveIntegerField(
        verbose_name="Investigados/Análise Laboratorial", null=True)
    
    testados = models.PositiveIntegerField(verbose_name="Testados", null=True)
    test_pcr = models.PositiveIntegerField(verbose_name="Testados RT-PCR", null=True)
    test_rapido = models.PositiveIntegerField(verbose_name="Testados TR-Igm/Igg", null=True)

    descartados = models.PositiveIntegerField(
        verbose_name="Descartados/Excluídos/Negativos", null=True)
    
    monitorados = models.PositiveIntegerField(verbose_name="Monitorados", null=True)
    notificados = models.PositiveIntegerField(verbose_name="Notificados", null=True)

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

        É recebido um dict com os valores que serão
        adicionados ao banco de dados. Caso não haja
        nenhum erro de integridade, os dados são 
        inseridos no banco de dados.

        Return: Objeto criado no banco de dados

        Exemplo:

        BE = BoletimEpidemiologico()
        Item = BE.get_create_boletim(BE, dict)

        assert Item.name = 'Foo'
        """
        return self.__createBoletimEpidemiologico(self, request)
    
    def get_delete_boletim(self, request):
        """
        Função DELETE do boletim epidemiologico

        Args:(self, request)

        A função recebe um dict com o dados essenciais da
        query que deseja apagar. É feito uma busca no 
        banco de dados e se a query existir, o objeto é 
        deletado e é retornado quantos objetos foram excluídos.

        Return: Quantidade de objetos excluídos.
        
        Exemplo de retorno: (1, {'core.BoletimEpidemiologico': 1})
        
        Neste caso, uma query do banco foi excluída.

        BE = BoletimEpidemiologico()
        Item = BE.get_delete_boletim(BE, dict)

        assert Item.name = (1, {'core.BoletimEpidemiologico': 1})
        """
        return self.__deleteBoletimEpidemiologico(self, request)

    def get_read_boletim(self, request):
        """
        Função READ do boletim epidemiologico

        Args:(self, request)

        A função recebe um dict, é feito uma busca no 
        banco de dados e se a query existir, retorna o objeto.

        Return: objeto com os atributos do boletim

        Exemplo:

        BE = BoletimEpidemiologico()
        Item = BE.get_read_boletim(BE, dict)

        assert Item.name = 'Foo'
        """
        return self.__readBoletimEpidemiologico(self, request)
    
    def get_update_boletim(self, request):

        """
        Função UPDATE do boletim epidemiologico.

        Args:(self, request)

        É recebido um dict com os valores que serão
        alterados no banco de dados. É feito uma 
        busca no banco de dados com os valores recebidos.
        Caso o objeto exista, ele é retornado.
        Caso não haja nenhum erro de integridade, os dados são 
        atualizados no banco de dados.

        Return: objeto com os atributos do boletim

        Exemplo:

        BE = BoletimEpidemiologico()
        Item = BE.get_update_boletim(BE, dict)
        """
        return self.__updateBoletimEpidemiologico(self, request)

    def get_dump_privado(self):
        """
        Gera um dump dos dados do banco de dados e 
        cria um arquivo txt com a QuerySet.

        Args:
            BoletimEpidemiologico

        Return:
            QuerySet com os dados do banco de dados.
        """

        return self.__dumpPrivado(self)

    def __createBoletimEpidemiologico(self, request):
        try:
            BoletimEpidemiologico(**request).save()
            boletim = BoletimEpidemiologico.objects.get(cidade = request['cidade'],
        data_atualizacao = request['data_atualizacao'])
        except IntegrityError as e:
            return "Erro de integridade {}".format(e)
        except BoletimEpidemiologico.DoesNotExist:
            return "Boletim não existe"
        except ValidationError as e:
            return "Erro de validação {}".format(e)
        
        return boletim

    def __readBoletimEpidemiologico(self, request):

        try:
            boletim = BoletimEpidemiologico.objects.get(cidade = request['cidade'],
        data_atualizacao = request['data_atualizacao'])

        except BoletimEpidemiologico.DoesNotExist:
            return ("O Boletim não existe!")

        return boletim
    
    def __updateBoletimEpidemiologico(self, request):

        try:
            BoletimEpidemiologico.objects.filter(cidade = request['cidade'],
        data_atualizacao = request['data_atualizacao']).update(**request)
            boletim = BoletimEpidemiologico.objects.get(cidade = request['cidade'],
        data_atualizacao = request['data_atualizacao'])

        except IntegrityError as e:
            return "Erro de integridade {}".format(e)
        except BoletimEpidemiologico.DoesNotExist:
            return "Boletim não existe"
        except ValidationError as e:
            return "Erro de validação {}".format(e)
        
        return boletim

    def __deleteBoletimEpidemiologico(self, request):

        try:
            boletim = BoletimEpidemiologico.objects.get(cidade = request['cidade'],
        data_atualizacao = request['data_atualizacao'])
            result = boletim.delete()

        except BoletimEpidemiologico.DoesNotExist:
            return ("O Boletim não existe!")

        return result

    def cleanDataFactory(self, request):
        """
        Função para limpar os dados recebidos de uma
        RequestFactory.

        Args: request de uma RequestFactory

        Return: dict com os dados limpos
        """
        req = {
            'cidade': request.POST.get('cidade'),
            'data_atualizacao' : request.POST.get('data_atualizacao'),
            'fonte_oficial_url' : request.POST.get('fonte_oficial_url'),			
            'fonte_oficial_tipo' : request.POST.get('fonte_oficial_tipo'),			
            'confirmados' : request.POST.get('confirmados'),			
            'conf_reside' : request.POST.get('conf_reside'),			
            'conf_nao_reside' : request.POST.get('conf_nao_reside'),			
            'recuperados' : request.POST.get('recuperados'),			
            'obitos' : request.POST.get('obitos'),			
            'isolados' : request.POST.get('isolados'),			
            'iso_domiciliar' : request.POST.get('iso_domiciliar'),			
            'iso_hospitalar' : request.POST.get('iso_hospitalar'),			
            'iso_hosp_sus' : request.POST.get('iso_hosp_sus'),			
            'iso_hosp_priv' : request.POST.get('iso_hosp_priv'),			
            'iso_hosp_sus_enf' : request.POST.get('iso_hosp_sus_enf'),			
            'iso_hosp_priv_enf' : request.POST.get('iso_hosp_priv_enf'),			
            'iso_hosp_sus_uti' : request.POST.get('iso_hosp_sus_uti'),			
            'iso_hosp_priv_uti' : request.POST.get('iso_hosp_priv_uti'),			
            'suspeitos' : request.POST.get('suspeitos'),			
            'sus_isolados' : request.POST.get('sus_isolados'),			
            'sus_iso_domiciliar' : request.POST.get('sus_iso_domiciliar'),
            'sus_iso_hospitalar' : request.POST.get('sus_iso_hospitalar'),
            'sus_investigados' : request.POST.get('sus_investigados'),
            'testados' : request.POST.get('testados'),
            'test_pcr' : request.POST.get('test_pcr'),
            'test_rapido' : request.POST.get('test_rapido'),
            'descartados' : request.POST.get('descartados'),
            'monitorados' : request.POST.get('monitorados'),
            'notificados' : request.POST.get('notificados'),
        }
        return req

    def cleanDataForm(self, form):
        
        """
        Função para limpar os dados recebidos de um form.

        Args: form gerado pelo Django

        Return: dict com os dados limpos
        """
        req = {
            'cidade': form.cleaned_data['cidade'],
            'data_atualizacao' : form.cleaned_data['data_atualizacao'],
            'fonte_oficial_url' : form.cleaned_data['fonte_oficial_url'],			
            'fonte_oficial_tipo' : form.cleaned_data['fonte_oficial_tipo'],			
            'confirmados' : form.cleaned_data['confirmados'],			
            'conf_reside' : form.cleaned_data['conf_reside'],			
            'conf_nao_reside' : form.cleaned_data['conf_nao_reside'],			
            'recuperados' : form.cleaned_data['recuperados'],			
            'obitos' : form.cleaned_data['obitos'],			
            'isolados' : form.cleaned_data['isolados'],			
            'iso_domiciliar' : form.cleaned_data['iso_domiciliar'],			
            'iso_hospitalar' : form.cleaned_data['iso_hospitalar'],			
            'iso_hosp_sus' : form.cleaned_data['iso_hosp_sus'],			
            'iso_hosp_priv' : form.cleaned_data['iso_hosp_priv'],			
            'iso_hosp_sus_enf' : form.cleaned_data['iso_hosp_sus_enf'],			
            'iso_hosp_priv_enf' : form.cleaned_data['iso_hosp_priv_enf'],			
            'iso_hosp_sus_uti' : form.cleaned_data['iso_hosp_sus_uti'],			
            'iso_hosp_priv_uti' : form.cleaned_data['iso_hosp_priv_uti'],			
            'suspeitos' : form.cleaned_data['suspeitos'],			
            'sus_isolados' : form.cleaned_data['sus_isolados'],			
            'sus_iso_domiciliar' : form.cleaned_data['sus_iso_domiciliar'],
            'sus_iso_hospitalar' : form.cleaned_data['sus_iso_hospitalar'],
            'sus_investigados' : form.cleaned_data['sus_investigados'],
            'testados' : form.cleaned_data['testados'],
            'test_pcr' : form.cleaned_data['test_pcr'],
            'test_rapido' : form.cleaned_data['test_rapido'],
            'descartados' : form.cleaned_data['descartados'],
            'monitorados' : form.cleaned_data['monitorados'],
            'notificados' : form.cleaned_data['notificados']
        }

        return req

    def __dumpPrivado(self):
        try:
            boletim = BoletimEpidemiologico.objects.values()
            with open("ultimoDump.text", "w", encoding='utf8') as f:
                f.write(str(boletim))
        except BoletimEpidemiologico.DoesNotExist:
            return ("O Boletim não existe!")

        return boletim
