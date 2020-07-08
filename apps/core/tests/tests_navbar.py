from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.

class NavbarTestCase(TestCase):
    """
    Classe de testes para a navbar.

    methods:
        - setUp
        - tearDown
        - test_pag_default
        - test_pag_grafico_cacu
        - test_pag_grafico_chapadao
        - test_pag_grafico_jatai
        - test_pag_grafico_mineiros
        - test_pag_grafico_montividiu
        - test_pag_grafico_rioverde
        - test_pag_grafico_santahelena
        - test_pag_como_sao_criados
        - test_pag_sobre
        - test_pag_equipe
        - test_pag_na_midia
        - test_pag_colabore
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
    
    def test_pag_default(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == True 
        assert is_active_grafico == False  
        #assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False

    def test_pag_grafico_cacu(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/graficos/cacu/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == True  
        #assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False
    
    def test_pag_grafico_chapadao(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/graficos/chapadao/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == True  
        #assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False
    
    def test_pag_grafico_jatai(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/graficos/jatai/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == True  
        #assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False
    
    def test_pag_grafico_mineiros(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/graficos/mineiros/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == True  
        #assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False

    def test_pag_grafico_montividiu(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/graficos/montividiu/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == True  
        #assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False
    
    def test_pag_grafico_rioverde(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/graficos/rioverde/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == True  
        #assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False

    def test_pag_grafico_santahelena(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/graficos/santahelena/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == True  
        #assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False

    """ def test_pag_comparacao(self):
        self.driver.get('http://127.0.0.1:8000/comparacao/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == True  
        assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False """

    def test_pag_como_sao_criados(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/como-sao-criados/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == True  
        #assert  is_active_tendencias == False 
        assert is_active_saiba_mais == False

    # def test_pag_tendencias_jatai(self):
    #     self.driver.get('http://127.0.0.1:8000/tendencias/jatai/')

    #     principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
    #     grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
    #     #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
    #     saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

    #     is_active_main = "active" in principal_element.get_attribute("class")
    #     is_active_grafico = "active" in grafico_element.get_attribute("class")
    #     #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
    #     is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

    #     assert is_active_main == False 
    #     assert is_active_grafico == False 
    #     #assert  is_active_tendencias == True 
    #     assert is_active_saiba_mais == False

    # def test_pag_tendencias_rioverde(self):
    #     self.driver.get('http://127.0.0.1:8000/tendencias/rioverde/')

    #     principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
    #     grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
    #     #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
    #     saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

    #     is_active_main = "active" in principal_element.get_attribute("class")
    #     is_active_grafico = "active" in grafico_element.get_attribute("class")
    #     #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
    #     is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

    #     assert is_active_main == False 
    #     assert is_active_grafico == False 
    #     #assert  is_active_tendencias == True 
    #     assert is_active_saiba_mais == False
    
    def test_pag_sobre(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/sobre/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == False 
        #assert  is_active_tendencias == False
        assert is_active_saiba_mais == True
    
    def test_pag_equipe(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/equipe/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == False 
        #assert  is_active_tendencias == False
        assert is_active_saiba_mais == True
    
    def test_pag_na_midia(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/na-midia/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == False 
        #assert  is_active_tendencias == False
        assert is_active_saiba_mais == True

    def test_pag_colabore(self):
        """
        Teste para verificar se a navbar da página está correta
        """
        self.driver.get('http://127.0.0.1:8000/colabore/')

        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        #tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        #is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")

        assert is_active_main == False 
        assert is_active_grafico == False 
        #assert  is_active_tendencias == False
        assert is_active_saiba_mais == True