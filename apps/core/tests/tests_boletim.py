from django.test import RequestFactory
from django.test import TestCase
from ..models import BoletimEpidemiologico
from ..forms.createForm import CreateBoletimEpidemiologicoForm
from django.db import IntegrityError
from pprint import pprint
from datetime import datetime

class BoletimTestCase(TestCase):
    
    def setUp(self):
        BoletimEpidemiologico.objects.create( cidade= 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00',
            fonte_oficial_url= 'https://www.google.com/', 
            fonte_oficial_tipo= 'Instagram',
            obitos = 7)

    def test_create_Boletim(self):
        """
        Teste para verificação das funções básicas do
        bando de dados
        """
        obitos = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        self.assertEqual(obitos.obitos, 7)
    
    def test_update_Boletim(self):
        """
        Teste para verificação das funções básicas do
        bando de dados
        """
        data = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        try:
            dataobito = data.obitos
            data.obitos = -1

            status = data.save()
        except IntegrityError as e:
            self.assertRaisesMessage(e, "django.db.obitols.IntegrityError: CHECK constraint failed: core_boletimepidemiologico")
    
    def test_read_Boletim(self):
        """
        Teste para verificação das funções básicas do
        bando de dados
        """
        data = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        dataobito = data.obitos

        self.assertEqual(dataobito, data.obitos)

    def test_factory_create(self):
        """
        Teste para a funcionalidade da função CREATE
        do banco de dados passando um dict com dados
        """
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'obitos': 9})

        request = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)
        a = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        self.assertEqual(int(a.obitos),9)

    def test_factory_update(self):
        """
        Teste para a funcionalidade da função UPDATE
        do banco de dados passando um dict com dados
        """
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-16 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram', 
        'obitos': 6})

        request = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)

        item = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        self.assertEqual(int(item.obitos), 6)

        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-16 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'confirmados' : 1,
        'conf_reside' : 5,
        'conf_nao_reside' : 5,
        'recuperados' : 5,
        'obitos': 9,
        'isolados' : 5,
        'iso_domiciliar' : 5,
        'iso_hospitalar' : 5,
        'iso_hosp_sus' : 5,
        'iso_hosp_priv' : 5,
        'iso_hosp_sus_enf' : 5,
        'iso_hosp_priv_enf' : 5,
        'iso_hosp_sus_uti' : 5,
        'iso_hosp_priv_uti' : 5,
        'suspeitos' : 5,
        'sus_isolados' : 5,
        'sus_iso_domiciliar' : 5,
        'sus_iso_hospitalar' : 5,
        'sus_investigados' : 5,
        'testados' : 5,
        'test_pcr' : 5,
        'test_rapido' : 5,
        'descartados' : 5,
        'monitorados' : 5,
        'notificados' : 5})

        request2 = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)

        a = BoletimEpidemiologico.get_update_boletim(BoletimEpidemiologico, request2)

        self.assertEqual(a.cidade, 'Jataí')
        self.assertEqual(a.data_atualizacao, datetime(2020, 6, 16, 0, 0))
        self.assertEqual(a.fonte_oficial_url, 'https://www.google.com/')
        self.assertEqual(a.fonte_oficial_tipo, 'Instagram')
        self.assertEqual(int(a.confirmados), 1)
        self.assertEqual(int(a.conf_reside), 5)
        self.assertEqual(int(a.conf_nao_reside), 5)
        self.assertEqual(int(a.recuperados), 5)
        self.assertEqual(int(a.obitos), 9)
        self.assertEqual(int(a.isolados), 5)
        self.assertEqual(int(a.iso_domiciliar), 5)
        self.assertEqual(int(a.iso_hospitalar), 5)
        self.assertEqual(int(a.iso_hosp_sus), 5)
        self.assertEqual(int(a.iso_hosp_priv), 5)
        self.assertEqual(int(a.iso_hosp_sus_enf), 5)
        self.assertEqual(int(a.iso_hosp_priv_enf), 5)
        self.assertEqual(int(a.iso_hosp_sus_uti), 5)
        self.assertEqual(int(a.iso_hosp_priv_uti), 5)
        self.assertEqual(int(a.suspeitos), 5)
        self.assertEqual(int(a.sus_isolados), 5)
        self.assertEqual(int(a.sus_iso_domiciliar), 5)
        self.assertEqual(int(a.sus_iso_hospitalar), 5)
        self.assertEqual(int(a.sus_investigados), 5)
        self.assertEqual(int(a.testados), 5)
        self.assertEqual(int(a.test_pcr), 5)
        self.assertEqual(int(a.test_rapido), 5)
        self.assertEqual(int(a.descartados), 5)
        self.assertEqual(int(a.monitorados), 5)
        self.assertEqual(int(a.notificados), 5)

    def test_factory_read(self):
        """
        Teste para a funcionalidade da função READE
        do banco de dados passando um dict com dados
        """
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram', 
        'obitos': 9})

        request = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)
        BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        a = BoletimEpidemiologico.get_read_boletim(BoletimEpidemiologico, request)

        self.assertEqual(int(a.obitos),9)

    def test_factory_delete(self):
        """
        Teste para a funcionalidade da função DELETE
        do banco de dados passando um dict com dados
        """
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'obitos': 9})

        request = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)
        BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        a = BoletimEpidemiologico.get_delete_boletim(BoletimEpidemiologico, request)

        self.assertEqual(a, (1, {'core.BoletimEpidemiologico': 1}))

    def test_integrity_error_negativo(self):
        """
        Teste de erro de integridade para numero 
        negativo. Retorna uma exception
        """
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'confirmados' : -1,
        'conf_reside' : -5,
        'conf_nao_reside' : -5,
        'recuperados' : -5,
        'obitos': -9,
        'isolados' : -5,
        'iso_domiciliar' : -5,
        'iso_hospitalar' : -5,
        'iso_hosp_sus' : -5,
        'iso_hosp_priv' : -5,
        'iso_hosp_sus_enf' : -5,
        'iso_hosp_priv_enf' : -5,
        'iso_hosp_sus_uti' : -5,
        'iso_hosp_priv_uti' : -5,
        'suspeitos' : -5,
        'sus_isolados' : -5,
        'sus_iso_domiciliar' : -5,
        'sus_iso_hospitalar' : -5,
        'sus_investigados' : -5,
        'testados' : -5,
        'test_pcr' : -5,
        'test_rapido' : -5,
        'descartados' : -5,
        'monitorados' : -5,
        'notificados' : -5})

        request = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)

        a = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        self.assertEqual(a, "Erro de integridade CHECK constraint failed: core_boletimepidemiologico")

    def test_validation_error_data(self):
        """
        Teste de erro de validação de formato
        de data. Retorna uma exception
        """
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '12341', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'confirmados' : 1,
        'conf_reside' : 5,
        'conf_nao_reside' : 5,
        'recuperados' : 5,
        'obitos': 9,
        'isolados' : 5,
        'iso_domiciliar' : 5,
        'iso_hospitalar' : 5,
        'iso_hosp_sus' : 5,
        'iso_hosp_priv' : 5,
        'iso_hosp_sus_enf' : 5,
        'iso_hosp_priv_enf' : 5,
        'iso_hosp_sus_uti' : 5,
        'iso_hosp_priv_uti' : 5,
        'suspeitos' : 5,
        'sus_isolados' : 5,
        'sus_iso_domiciliar' : 5,
        'sus_iso_hospitalar' : 5,
        'sus_investigados' : 5,
        'testados' : 5,
        'test_pcr' : 5,
        'test_rapido' : 5,
        'descartados' : 5,
        'monitorados' : 5,
        'notificados' : 5})

        request = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)
        a = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        self.assertEqual(a, 
        "Erro de validação ['O valor “{}” tem um formato inválido. Deve estar no formato YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ].']".format(request['data_atualizacao']))

    def test_validation_error_data2(self):
        """
        Teste de erro de validação para entrada 
        somente com horas. Retorna uma exception
        """
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'confirmados' : 1,
        'conf_reside' : 5,
        'conf_nao_reside' : 5,
        'recuperados' : 5,
        'obitos': 9,
        'isolados' : 5,
        'iso_domiciliar' : 5,
        'iso_hospitalar' : 5,
        'iso_hosp_sus' : 5,
        'iso_hosp_priv' : 5,
        'iso_hosp_sus_enf' : 5,
        'iso_hosp_priv_enf' : 5,
        'iso_hosp_sus_uti' : 5,
        'iso_hosp_priv_uti' : 5,
        'suspeitos' : 5,
        'sus_isolados' : 5,
        'sus_iso_domiciliar' : 5,
        'sus_iso_hospitalar' : 5,
        'sus_investigados' : 5,
        'testados' : 5,
        'test_pcr' : 5,
        'test_rapido' : 5,
        'descartados' : 5,
        'monitorados' : 5,
        'notificados' : 5})

        request = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)
        a = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        self.assertEqual(a, 
        "Erro de validação ['O valor “{}” tem um formato inválido. Deve estar no formato YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ].']".format(request['data_atualizacao']))

    def test_update_negativo(self):
        """
        Teste de erro de integridade para numero 
        negativo na função UPDATE. Retorna uma exception
        """
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-16 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'confirmados' : 1,
        'conf_reside' : 5,
        'conf_nao_reside' : 5,
        'recuperados' : 5,
        'obitos': 9,
        'isolados' : 5,
        'iso_domiciliar' : 5,
        'iso_hospitalar' : 5,
        'iso_hosp_sus' : 5,
        'iso_hosp_priv' : 5,
        'iso_hosp_sus_enf' : 5,
        'iso_hosp_priv_enf' : 5,
        'iso_hosp_sus_uti' : 5,
        'iso_hosp_priv_uti' : 5,
        'suspeitos' : 5,
        'sus_isolados' : 5,
        'sus_iso_domiciliar' : 5,
        'sus_iso_hospitalar' : 5,
        'sus_investigados' : 5,
        'testados' : 5,
        'test_pcr' : 5,
        'test_rapido' : 5,
        'descartados' : 5,
        'monitorados' : 5,
        'notificados' : 5})

        request = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)
        item = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        self.assertEqual(int(item.obitos), 9)

        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-16 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'confirmados' : 1,
        'conf_reside' : 5,
        'conf_nao_reside' : 5,
        'recuperados' : 5,
        'obitos': 9,
        'isolados' : 5,
        'iso_domiciliar' : 5,
        'iso_hospitalar' : 5,
        'iso_hosp_sus' : 5,
        'iso_hosp_priv' : 5,
        'iso_hosp_sus_enf' : 5,
        'iso_hosp_priv_enf' : 5,
        'iso_hosp_sus_uti' : 5,
        'iso_hosp_priv_uti' : 5,
        'suspeitos' : 5,
        'sus_isolados' : 5,
        'sus_iso_domiciliar' : 5,
        'sus_iso_hospitalar' : 5,
        'sus_investigados' : 5,
        'testados' : 5,
        'test_pcr' : 5,
        'test_rapido' : 5,
        'descartados' : 5,
        'monitorados' : 5,
        'notificados' : -5})

        request2 = {
            'cidade': req.POST.get('cidade'),
            'data_atualizacao' : req.POST.get('data_atualizacao'),
            'fonte_oficial_url' : req.POST.get('fonte_oficial_url'),			
            'fonte_oficial_tipo' : req.POST.get('fonte_oficial_tipo'),			
            'confirmados' : req.POST.get('confirmados'),			
            'conf_reside' : req.POST.get('conf_reside'),			
            'conf_nao_reside' : req.POST.get('conf_nao_reside'),			
            'recuperados' : req.POST.get('recuperados'),			
            'obitos' : req.POST.get('obitos'),			
            'isolados' : req.POST.get('isolados'),			
            'iso_domiciliar' : req.POST.get('iso_domiciliar'),			
            'iso_hospitalar' : req.POST.get('iso_hospitalar'),			
            'iso_hosp_sus' : req.POST.get('iso_hosp_sus'),			
            'iso_hosp_priv' : req.POST.get('iso_hosp_priv'),			
            'iso_hosp_sus_enf' : req.POST.get('iso_hosp_sus_enf'),			
            'iso_hosp_priv_enf' : req.POST.get('iso_hosp_priv_enf'),			
            'iso_hosp_sus_uti' : req.POST.get('iso_hosp_sus_uti'),			
            'iso_hosp_priv_uti' : req.POST.get('iso_hosp_priv_uti'),			
            'suspeitos' : req.POST.get('suspeitos'),			
            'sus_isolados' : req.POST.get('sus_isolados'),			
            'sus_iso_domiciliar' : req.POST.get('sus_iso_domiciliar'),
            'sus_iso_hospitalar' : req.POST.get('sus_iso_hospitalar'),
            'sus_investigados' : req.POST.get('sus_investigados'),
            'testados' : req.POST.get('testados'),
            'test_pcr' : req.POST.get('test_pcr'),
            'test_rapido' : req.POST.get('test_rapido'),
            'descartados' : req.POST.get('descartados'),
            'monitorados' : req.POST.get('monitorados'),
            'notificados' : req.POST.get('notificados'),
        }

        a = BoletimEpidemiologico.get_update_boletim(BoletimEpidemiologico, request2)

        self.assertEqual(a, "Erro de integridade CHECK constraint failed: core_boletimepidemiologico")

    def test_update_data(self):

        """
        Teste de erro de validação para UPDATE 
        de data. Retorna uma exception
        """
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-16 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'confirmados' : 1,
        'conf_reside' : 5,
        'conf_nao_reside' : 5,
        'recuperados' : 5,
        'obitos': 9,
        'isolados' : 5,
        'iso_domiciliar' : 5,
        'iso_hospitalar' : 5,
        'iso_hosp_sus' : 5,
        'iso_hosp_priv' : 5,
        'iso_hosp_sus_enf' : 5,
        'iso_hosp_priv_enf' : 5,
        'iso_hosp_sus_uti' : 5,
        'iso_hosp_priv_uti' : 5,
        'suspeitos' : 5,
        'sus_isolados' : 5,
        'sus_iso_domiciliar' : 5,
        'sus_iso_hospitalar' : 5,
        'sus_investigados' : 5,
        'testados' : 5,
        'test_pcr' : 5,
        'test_rapido' : 5,
        'descartados' : 5,
        'monitorados' : 5,
        'notificados' : 5})

        request = BoletimEpidemiologico.cleanDataFactory(BoletimEpidemiologico, req)

        item = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        self.assertEqual(int(item.obitos), 9)

        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '1234', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'confirmados' : 1,
        'conf_reside' : 5,
        'conf_nao_reside' : 5,
        'recuperados' : 5,
        'obitos': 9,
        'isolados' : 5,
        'iso_domiciliar' : 5,
        'iso_hospitalar' : 5,
        'iso_hosp_sus' : 5,
        'iso_hosp_priv' : 5,
        'iso_hosp_sus_enf' : 5,
        'iso_hosp_priv_enf' : 5,
        'iso_hosp_sus_uti' : 5,
        'iso_hosp_priv_uti' : 5,
        'suspeitos' : 5,
        'sus_isolados' : 5,
        'sus_iso_domiciliar' : 5,
        'sus_iso_hospitalar' : 5,
        'sus_investigados' : 5,
        'testados' : 5,
        'test_pcr' : 5,
        'test_rapido' : 5,
        'descartados' : 5,
        'monitorados' : 5,
        'notificados' : 5})

        request2 = {
            'cidade': req.POST.get('cidade'),
            'data_atualizacao' : req.POST.get('data_atualizacao'),
            'fonte_oficial_url' : req.POST.get('fonte_oficial_url'),			
            'fonte_oficial_tipo' : req.POST.get('fonte_oficial_tipo'),			
            'confirmados' : req.POST.get('confirmados'),			
            'conf_reside' : req.POST.get('conf_reside'),			
            'conf_nao_reside' : req.POST.get('conf_nao_reside'),			
            'recuperados' : req.POST.get('recuperados'),			
            'obitos' : req.POST.get('obitos'),			
            'isolados' : req.POST.get('isolados'),			
            'iso_domiciliar' : req.POST.get('iso_domiciliar'),			
            'iso_hospitalar' : req.POST.get('iso_hospitalar'),			
            'iso_hosp_sus' : req.POST.get('iso_hosp_sus'),			
            'iso_hosp_priv' : req.POST.get('iso_hosp_priv'),			
            'iso_hosp_sus_enf' : req.POST.get('iso_hosp_sus_enf'),			
            'iso_hosp_priv_enf' : req.POST.get('iso_hosp_priv_enf'),			
            'iso_hosp_sus_uti' : req.POST.get('iso_hosp_sus_uti'),			
            'iso_hosp_priv_uti' : req.POST.get('iso_hosp_priv_uti'),			
            'suspeitos' : req.POST.get('suspeitos'),			
            'sus_isolados' : req.POST.get('sus_isolados'),			
            'sus_iso_domiciliar' : req.POST.get('sus_iso_domiciliar'),
            'sus_iso_hospitalar' : req.POST.get('sus_iso_hospitalar'),
            'sus_investigados' : req.POST.get('sus_investigados'),
            'testados' : req.POST.get('testados'),
            'test_pcr' : req.POST.get('test_pcr'),
            'test_rapido' : req.POST.get('test_rapido'),
            'descartados' : req.POST.get('descartados'),
            'monitorados' : req.POST.get('monitorados'),
            'notificados' : req.POST.get('notificados'),
        }

        a = BoletimEpidemiologico.get_update_boletim(BoletimEpidemiologico, request2)

        self.assertEqual(a, 
        "Erro de validação ['O valor “{}” tem um formato inválido. Deve estar no formato YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ].']".format(request2['data_atualizacao']))

