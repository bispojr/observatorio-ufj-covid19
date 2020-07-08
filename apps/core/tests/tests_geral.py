from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.

class GeralTestCase(TestCase):
    """
    Classe de testes geral.

    methods:
        - setUp
        - tearDown
        - test_home_acesso
        - test_titulo_sobre
        - test_titulo_equipe
        - test_reportagem_tv_sudoeste
        - test_titulo_colabore
    """
    
    def setUp(self):
        """
        Função para fazer o setUp dos drivers que serão utilizados
        nos testes
        """
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    def tearDown(self):
        """
        Função para fechar o drive quando o teste acabar
        """
        self.driver.close()
    
    def test_home_acesso(self):
        """
        Função para testar se o título e page source da página estão corretos
        """
        self.driver.get('http://127.0.0.1:8000/')
        assert "Observatório UFJ Covid-19 - Principal" in self.driver.title
        assert "Este observatório é uma iniciativa do" in self.driver.page_source

    def test_titulo_sobre(self):  
        """
        Função para testar se o título da página está correto
        """      
        self.driver.get('http://127.0.0.1:8000/sobre')
        titulo = "Observatório UFJ Covid-19 - Sobre"
        assert titulo in self.driver.title

    def test_titulo_equipe(self): 
        """
        Função para testar se o título da página está correto
        """          
        self.driver.get('http://127.0.0.1:8000/equipe')
        titulo = "Observatório UFJ Covid-19 - Equipe"
        assert titulo in self.driver.title

    def test_titulo_naMidia(self):  
        """
        Função para testar se o título da página está correto
        """         
        self.driver.get('http://127.0.0.1:8000/na-midia')
        titulo = "Observatório UFJ Covid-19 - Na Mídia"
        assert titulo in self.driver.title
    
    def test_reportagem_tv_sudoeste(self):  
        """
        Função para testar se o page source da página está correto
        """         
        self.driver.get('http://127.0.0.1:8000/na-midia')
        manchete = "Projeto de extensão da UFJ traz informações atualizadas sobre casos de coronavírus"
        assert manchete in self.driver.page_source

    def test_titulo_colabore(self):   
        """
        Função para testar se o título da página está correto
        """        
        self.driver.get('http://127.0.0.1:8000/colabore')
        titulo = "Observatório UFJ Covid-19 - Colabore"
        assert titulo in self.driver.title

    