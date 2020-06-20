from django.test import TestCase

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

class InterfaceBoletimTestCase(TestCase):

    def test_tipo_do_campo(self):
        options = Options()
        options.headless = True
        driver = Chrome(options=options)

        driver.get('http://127.0.0.1:8000/create/')

        cidade = driver.find_element_by_id('id_cidade')
        data_atualizacao = driver.find_element_by_id('id_data_atualizacao')
        fonte_oficial_url = driver.find_element_by_id('id_fonte_oficial_url')
        fonte_oficial_tipo = driver.find_element_by_id('id_fonte_oficial_tipo')
        confirmados = driver.find_element_by_id('id_confirmados')
        conf_reside = driver.find_element_by_id('id_conf_reside')
        conf_nao_reside = driver.find_element_by_id('id_conf_nao_reside')
        recuperados = driver.find_element_by_id('id_recuperados')
        obitos = driver.find_element_by_id('id_obitos')
        isolados = driver.find_element_by_id('id_isolados')
        iso_domiciliar = driver.find_element_by_id('id_iso_domiciliar')
        iso_hospitalar = driver.find_element_by_id('id_iso_hospitalar')
        iso_hosp_sus = driver.find_element_by_id('id_iso_hosp_sus')
        iso_hosp_priv = driver.find_element_by_id('id_iso_hosp_priv')
        iso_hosp_sus_enf = driver.find_element_by_id('id_iso_hosp_sus_enf')
        iso_hosp_priv_enf = driver.find_element_by_id('id_iso_hosp_priv_enf')
        iso_hosp_sus_uti = driver.find_element_by_id('id_iso_hosp_sus_uti')
        iso_hosp_priv_uti = driver.find_element_by_id('id_iso_hosp_priv_uti')
        suspeitos = driver.find_element_by_id('id_suspeitos')
        sus_isolados = driver.find_element_by_id('id_sus_isolados')
        sus_iso_domiciliar = driver.find_element_by_id('id_sus_iso_domiciliar')
        sus_iso_hospitalar = driver.find_element_by_id('id_sus_iso_hospitalar')
        sus_investigados = driver.find_element_by_id('id_sus_investigados')
        testados = driver.find_element_by_id('id_testados')
        test_pcr = driver.find_element_by_id('id_test_pcr')
        test_rapido = driver.find_element_by_id('id_test_rapido')
        descartados = driver.find_element_by_id('id_descartados')
        monitorados = driver.find_element_by_id('id_monitorados')
        notificados = driver.find_element_by_id('id_notificados')

        is_cidade = "text" in cidade.get_attribute("type")
        is_data_atualizacao = "text" in data_atualizacao.get_attribute("type")
        is_fonte_oficial_url = "url" in fonte_oficial_url.get_attribute("type")
        is_fonte_oficial_tipo = "text" in fonte_oficial_tipo.get_attribute("type")
        is_confirmados = "number" in confirmados.get_attribute("type")
        is_conf_reside = "number" in conf_reside.get_attribute("type")
        is_conf_nao_reside = "number" in conf_nao_reside.get_attribute("type")
        is_recuperados = "number" in recuperados.get_attribute("type")
        is_obitos = "number" in obitos.get_attribute("type")
        is_isolados = "number" in isolados.get_attribute("type")
        is_iso_domiciliar = "number" in iso_domiciliar.get_attribute("type")
        is_iso_hospitalar = "number" in iso_hospitalar.get_attribute("type")
        is_iso_hosp_sus = "number" in iso_hosp_sus.get_attribute("type")
        is_iso_hosp_priv = "number" in iso_hosp_priv.get_attribute("type")
        is_iso_hosp_sus_enf = "number" in iso_hosp_sus_enf.get_attribute("type")
        is_iso_hosp_priv_enf = "number" in iso_hosp_priv_enf.get_attribute("type")
        is_iso_hosp_sus_uti = "number" in iso_hosp_sus_uti.get_attribute("type")
        is_iso_hosp_priv_uti = "number" in iso_hosp_priv_uti.get_attribute("type")
        is_suspeitos = "number" in suspeitos.get_attribute("type")
        is_sus_isolados = "number" in sus_isolados.get_attribute("type")
        is_sus_iso_domiciliar = "number" in sus_iso_domiciliar.get_attribute("type")
        is_sus_iso_hospitalar = "number" in sus_iso_hospitalar.get_attribute("type")
        is_sus_investigados = "number" in sus_investigados.get_attribute("type")
        is_testados = "number" in testados.get_attribute("type")
        is_test_pcr = "number" in test_pcr.get_attribute("type")
        is_test_rapido = "number" in test_rapido.get_attribute("type")
        is_descartados = "number" in descartados.get_attribute("type")
        is_monitorados = "number" in monitorados.get_attribute("type")
        is_notificados = "number" in notificados.get_attribute("type")

        self.assertTrue(is_cidade)
        self.assertTrue(is_data_atualizacao)
        self.assertTrue(is_fonte_oficial_url)
        self.assertTrue(is_fonte_oficial_tipo)
        self.assertTrue(is_confirmados)
        self.assertTrue(is_conf_reside)
        self.assertTrue(is_conf_nao_reside)
        self.assertTrue(is_recuperados)
        self.assertTrue(is_obitos)
        self.assertTrue(is_isolados)
        self.assertTrue(is_iso_domiciliar)
        self.assertTrue(is_iso_hospitalar)
        self.assertTrue(is_iso_hosp_sus)
        self.assertTrue(is_iso_hosp_priv)
        self.assertTrue(is_iso_hosp_sus_enf)
        self.assertTrue(is_iso_hosp_priv_enf)
        self.assertTrue(is_iso_hosp_sus_uti)
        self.assertTrue(is_iso_hosp_priv_uti)
        self.assertTrue(is_suspeitos)
        self.assertTrue(is_sus_isolados)
        self.assertTrue(is_sus_iso_domiciliar)
        self.assertTrue(is_sus_iso_hospitalar)
        self.assertTrue(is_sus_investigados)
        self.assertTrue(is_testados)
        self.assertTrue(is_test_pcr)
        self.assertTrue(is_test_rapido)
        self.assertTrue(is_descartados)
        self.assertTrue(is_monitorados)
        self.assertTrue(is_notificados)

        driver.close()
    
    def test_template_used(self):
        options = Options()
        options.headless = True
        driver = Chrome(options=options)

        driver.get('http://127.0.0.1:8000/create/')

        self.assertTemplateUsed('forms/createForm.html')