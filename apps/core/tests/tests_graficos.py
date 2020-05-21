from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.

class GraficosTestCase(TestCase):
    
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    def tearDown(self):
        self.driver.close()
    
    def test_titulo_jatai(self):
        self.driver.get('http://127.0.0.1:8000/graficos/jatai')
        titulo = "Observatório UFJ Covid-19 - Gráficos (Jataí)"
        assert titulo in self.driver.title
        assert "Resumo" in self.driver.page_source
        assert "Todas as categorias" in self.driver.page_source
        assert "Monitorados" in self.driver.page_source
        assert "Secretaria de Saúde de Jataí" in self.driver.page_source
    
    def test_titulo_mineiros(self):
        self.driver.get('http://127.0.0.1:8000/graficos/mineiros')
        titulo = "Observatório UFJ Covid-19 - Gráficos (Mineiros)"
        assert titulo in self.driver.title
        assert "Resumo" in self.driver.page_source
        assert "Todas as categorias" in self.driver.page_source
        assert "Monitorados" in self.driver.page_source
        assert "Secretaria de Saúde de Mineiros" in self.driver.page_source

    def test_titulo_rioverde(self):        
        self.driver.get('http://127.0.0.1:8000/graficos/rioverde')
        titulo = "Observatório UFJ Covid-19 - Gráficos (Rio Verde)"
        assert titulo in self.driver.title
        assert "Resumo" in self.driver.page_source
        assert "Todas as categorias" in self.driver.page_source
        assert "Monitorados" in self.driver.page_source
        assert "Secretaria de Saúde de Rio Verde" in self.driver.page_source

    def test_titulo_comparacao(self):        
        self.driver.get('http://127.0.0.1:8000/comparacao')
        titulo = "Observatório UFJ Covid-19 - Comparação entre as cidades"
        assert titulo in self.driver.title

    def test_titulo_comoSaoCriados(self):        
        self.driver.get('http://127.0.0.1:8000/como-sao-criados')
        titulo = "Observatório UFJ Covid-19 - Como são criados?"
        assert titulo in self.driver.title