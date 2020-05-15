from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.

class TendenciasTestCase(TestCase):
    
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    def tearDown(self):
        self.driver.close()
    
    def test_titulo_jatai(self):
        self.driver.get('http://127.0.0.1:8000/tendencias/jatai')
        titulo = "Observatório UFJ Covid-19 - Tendências (Jataí)"
        assert titulo in self.driver.title

    def test_titulo_rioverde(self):
        self.driver.get('http://127.0.0.1:8000/tendencias/rioverde')
        titulo = "Observatório UFJ Covid-19 - Tendências (Rio Verde)"
        assert titulo in self.driver.title