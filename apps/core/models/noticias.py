import json
from urllib.request import (Request, 
                            urlopen, 
                            HTTPError, 
                            build_opener, 
                            HTTPCookieProcessor)
from bs4 import BeautifulSoup
from socket import error as SocketError
from http.cookiejar import CookieJar
import pandas as pd

class Noticias():
    
    def __getNoticias(self):
        try:
            with open('noticias.json', 'r', encoding='utf8') as fp:
                lista = json.load(fp)
        except ValueError as err:
            if str(err) == "Expecting value: line 1 column 1 (char 0)":
                print("Arquivo vazio")
        return lista


    def __contextNoticias(self):
        context = {
            "grupo": "", 
            "grupo_link": "noticias",
            "script": "noticias",
            "titulo": "Observatório UFJ Covid-19 - Notícias",
            "lista": self.__getNoticias(self)
            }
        return context

    def getContext(self):
        return self.__contextNoticias(self)

    def __noticias(self):

        googleSheetId = '178wCqYRbSXRQui2l3pLOI3Yz5OktNzNvWr_AE2GWPEg'
        worksheetName = 'Dados'
        URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
            googleSheetId,
            worksheetName
        )

        data_frame = pd.read_csv(URL)

        links = data_frame.Link

        metadados = []

        for i in links:
            metadados.append(MetaDataReader.MetaDataReader.get_url_metadata(i)) 

        keys = range(len(metadados))

        dados = dict(zip(metadados))

        with open("noticias.json", "w", encoding='utf8') as f:
            json.dump(dados, f, indent=4)

        return True


class MetaDataReader:

    @staticmethod
    def get_url_metadata(external_sites_url):
        req = Request(external_sites_url, headers={'User-Agent': 'Chrome/81.0.4044.138'})
        cj = CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj))
        external_sites_html = opener.open(req).read()
        soup = BeautifulSoup(external_sites_html, "html.parser")

        title = soup.title.text
        image = ""
        link = ""
        # description = ""

        for meta in soup.findAll("meta"):
            title = MetaDataReader.get_meta_property(meta, "og:title", title)
            if MetaDataReader.get_meta_property(meta, "og:image", image) == "":
                image = "https://image.flaticon.com/icons/svg/2150/2150342.svg"
            else:
                image = MetaDataReader.get_meta_property(meta, "og:image", image)
            link = external_sites_url
            # description = MetaDataReader.get_meta_property(meta, "og:description", description)

        return {'title': title, 'image': image, 'link': link}

    @staticmethod
    def get_meta_property(meta, property_name, default_value=""):
        if 'property' in meta.attrs and meta.attrs['property'] == property_name:
            return meta.attrs['content']
        return default_value