from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.

class EquipeTestCase(TestCase):
    
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    def tearDown(self):
        self.driver.close()

    def test_dyeimys(self):
        self.driver.get('http://127.0.0.1:8000/equipe')
        assert "Dyeimys Correa" in self.driver.page_source

    def test_paulo(self):
        self.driver.get('http://127.0.0.1:8000/equipe')
        assert "Paulo Freitas" in self.driver.page_source

    def test_esdras(self):
        self.driver.get('http://127.0.0.1:8000/equipe')
        assert "Esdras L. Bispo Jr." in self.driver.page_source