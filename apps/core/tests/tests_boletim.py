from django.test import Client
from django.test import TestCase
from ..models import BoletimEpidemiologico
from ..forms.createForm import CreateBoletimEpidemiologicoForm

class BoletimTestCase(TestCase):
    
    def setUp(self):
        BoletimEpidemiologico.objects.create( cidade= 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00',
            fonte_oficial = 'https://www.google.com/',
            uti = 7)
    
    def tearDown(self):
        data = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')

        data.delete()

    def test_create_Boletim(self):
        uti = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        self.assertEqual(uti.uti, 7)
    
    def test_update_Boletim(self):
        data = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        dataUTI = data.uti
        data.uti = dataUTI + 1

        self.assertEqual(dataUTI + 1, data.uti)
    
    def test_read_Boletim(self):
        data = BoletimEpidemiologico.objects.get(cidade = 'Jataí',
            data_atualizacao = '2020-06-11 00:00:00')
        
        dataUTI = data.uti

        self.assertEqual(dataUTI, data.uti)

        