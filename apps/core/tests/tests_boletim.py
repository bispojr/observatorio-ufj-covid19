from django.test import Client
from django.test import TestCase
from ..models import BoletimEpidemiologico
from ..forms.createForm import CreateBoletimEpidemiologicoForm
from django.db import IntegrityError

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

        