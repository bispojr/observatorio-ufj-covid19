from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.

class AcessosViewTestCase(TestCase):
    
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    def tearDown(self):
        self.driver.close()
    
    def test_home_acesso(self):
        self.driver.get('http://127.0.0.1:8000/')
        assert "Observatório UFJ Covid-19 - Principal" in self.driver.title
        assert "Este observatório é uma iniciativa do" in self.driver.page_source

    def test_reportagem_tv_sudoeste(self):        
        self.driver.get('http://127.0.0.1:8000/na-midia')
        manchete = "Projeto de extensão da UFJ traz informações atualizadas sobre casos de coronavírus"
        assert manchete in self.driver.page_source

    def test_titulo_grafico_jatai(self):
        self.driver.get('http://127.0.0.1:8000/graficos/jatai')
        titulo = "Observatório UFJ Covid-19 - Gráficos (Jataí)"
        assert titulo in self.driver.title
    
    def test_titulo_grafico_mineiros(self):
        self.driver.get('http://127.0.0.1:8000/graficos/mineiros')
        titulo = "Observatório UFJ Covid-19 - Gráficos (Mineiros)"
        assert titulo in self.driver.title

    def test_titulo_grafico_rioverde(self):        
        self.driver.get('http://127.0.0.1:8000/graficos/rioverde')
        titulo = "Observatório UFJ Covid-19 - Gráficos (Rio Verde)"
        assert titulo in self.driver.title