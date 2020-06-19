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
            fonte_oficial = 'https://www.google.com/',
            uti = 7)

    def test_create_Boletim(self):
        uti = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        self.assertEqual(uti.uti, 7)
    
    def test_update_Boletim(self):
        data = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        try:
            dataUTI = data.uti
            data.uti = -1

            status = data.save()
        except IntegrityError as e:
            self.assertRaisesMessage(e, "django.db.utils.IntegrityError: CHECK constraint failed: core_boletimepidemiologico")
    
    def test_read_Boletim(self):
        data = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        dataUTI = data.uti

        self.assertEqual(dataUTI, data.uti)

    def test_factory_create(self):
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial': 'https://www.google.com/', 
        'uti': 9})
        a = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, req)

        self.assertEqual(int(a['uti']),9)

    def test_factory_update(self):
        rf = RequestFactory()
        req = rf.post('/update/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-16 00:00:00', 
        'fonte_oficial': 'https://www.google.com/', 
        'uti': 6})

        item = BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, req)

        self.assertEqual(int(item['uti']), 6)

        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-16 00:00:00', 
        'fonte_oficial': 'https://www.google.com/', 
        'uti': 9})

        a = BoletimEpidemiologico.get_update_boletim(BoletimEpidemiologico, req)

        self.assertEqual(int(a.uti), 9)

    def test_factory_read(self):
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial': 'https://www.google.com/', 
        'uti': 9})
        BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, req)

        a = BoletimEpidemiologico.get_read_boletim(BoletimEpidemiologico, req)

        self.assertEqual(int(a.uti),9)

    def test_factory_delete(self):
        rf = RequestFactory()
        req = rf.post('/create/', {'cidade': 'Jataí', 
        'data_atualizacao': '2020-06-15 00:00:00', 
        'fonte_oficial': 'https://www.google.com/', 
        'uti': 9})
        BoletimEpidemiologico.get_create_boletim(BoletimEpidemiologico, req)

        a = BoletimEpidemiologico.get_delete_boletim(BoletimEpidemiologico, req)

        self.assertEqual(a, (1, {'core.BoletimEpidemiologico': 1}))
