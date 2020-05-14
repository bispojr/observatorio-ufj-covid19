from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

# Create your tests here.

class AcessosViewTestCase(TestCase):

    def test_home_acesso(self):

        driver = webdriver.Firefox()
        
        driver.get('http://127.0.0.1:8000/')
        assert "Observatório UFJ Covid-19 - Principal" in driver.title
        assert "Este observatório é uma iniciativa do" in driver.page_source

        driver.close()
