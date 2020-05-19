from django.test import TestCase
from django.test import Client

# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Chrome

# Create your tests here.

class FailsTestCase(TestCase):
    
    def setUp(self):
        # options = Options()
        # options.headless = True
        self.driver = Chrome() # executable_path=GeckoDriverManager().install()

    def tearDown(self):
        self.driver.close()
    
    #Teste com chrome retornando OK deste modo
    def test_menu_ativo(self):
        self.driver.get('http://127.0.0.1:8000/graficos/jatai')
        elements = self.driver.find_elements_by_id("navbarDropdownGraficos")
        assert len(elements) > 0 

    