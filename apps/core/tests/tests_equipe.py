from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.

class EquipeTestCase(TestCase):
    """
    Classe de testes para as equipes.

    methods:
        - setUp
        - tearDown
        - test_equipe
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

    def test_equipe(self):
        """
        Função para testar se os nomes estão na página de Equipe.
        """
        self.driver.get('http://127.0.0.1:8000/equipe')
        assert "Críscilla Rezende" in self.driver.page_source
        assert "Diego Costa" in self.driver.page_source
        assert "Douglas Cedrim" in self.driver.page_source
        assert "Dyeimys Correa" in self.driver.page_source
        assert "Edlaine Vilela" in self.driver.page_source
        assert "Esdras L. Bispo Jr." in self.driver.page_source
        assert "Felipe Nedopetalski" in self.driver.page_source
        assert "Franciny Medeiros" in self.driver.page_source
        assert "Gabriel Santos" in self.driver.page_source
        assert "Joslaine Jeske" in self.driver.page_source
        assert "Luiz Pascoal" in self.driver.page_source
        assert "Manuel Ferreira" in self.driver.page_source
        assert "Marcelo Freitas" in self.driver.page_source
        assert "Marcos Alves" in self.driver.page_source
        assert "Márcio Lopes" in self.driver.page_source
        assert "Paulo Freitas" in self.driver.page_source
        assert "Zaqueu Souza" in self.driver.page_source

        assert "#TodosContraoCorona" in self.driver.page_source
        assert "Covid Goiás" in self.driver.page_source
        