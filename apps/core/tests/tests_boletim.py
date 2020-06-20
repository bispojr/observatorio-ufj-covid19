from django.test import RequestFactory
from django.test import TestCase
from ..models import BoletimEpidemiologico
from ..forms.createForm import CreateBoletimEpidemiologicoForm
from django.db import IntegrityError
from pprint import pprint

class BoletimTestCase(TestCase):
    
    def setUp(self):
        BoletimEpidemiologico.objects.create( cidade= 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00',
            fonte_oficial_url= 'https://www.google.com/', 
            fonte_oficial_tipo= 'Instagram',
            obitos = 7)

    def test_create_Boletim(self):
        obitos = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        self.assertEqual(obitos.obitos, 7)
    
    def test_update_Boletim(self):
        data = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        try:
            dataobito = data.obitos
            data.obitos = -1

            status = data.save()
        except IntegrityError as e:
            self.assertRaisesMessage(e, "django.db.obitols.IntegrityError: CHECK constraint failed: core_boletimepidemiologico")
    
    def test_read_Boletim(self):
        data = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        dataobito = data.obitos

        self.assertEqual(dataobito, data.obitos)

    def test_factory_create(self):
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'obitos': 9})

        request = {
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
        a = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        self.assertEqual(int(a.obitos),9)

    def test_factory_update(self):
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-16 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram', 
        'obitos': 6})

        request = {
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

        item = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        self.assertEqual(int(item.obitos), 6)

        req = rf.post('/update/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-16 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram', 
        'obitos': 9})

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

        self.assertEqual(int(a.obitos), 9)

    def test_factory_read(self):
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram', 
        'obitos': 9})

        request = {
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
        BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        a = BoletimEpidemiologico.get_read_boletim(BoletimEpidemiologico, request)

        self.assertEqual(int(a.obitos),9)

    def test_factory_delete(self):
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial_url': 'https://www.google.com/', 
        'fonte_oficial_tipo': 'Instagram',
        'obitos': 9})

        request = {
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
        BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, request)

        a = BoletimEpidemiologico.get_delete_boletim(BoletimEpidemiologico, request)

        self.assertEqual(a, (1, {'core.BoletimEpidemiologico': 1}))
