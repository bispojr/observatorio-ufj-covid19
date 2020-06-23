from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.


class FailsTestCase(TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(
            options=options, executable_path=GeckoDriverManager().install()
        )

    def tearDown(self):
        self.driver.close()
