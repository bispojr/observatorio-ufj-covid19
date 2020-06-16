from urllib.request import (Request, 
                            urlopen, 
                            HTTPError, 
                            build_opener, 
                            HTTPCookieProcessor)
from bs4 import BeautifulSoup
from socket import error as SocketError
from http.cookiejar import CookieJar

from django.test import TestCase

class BoletimTestCase(TestCase):

    def test_chrome(self):
        req = Request('https://www.deolhonocorona.com/', headers={'User-Agent': 'Chrome/81.0.4044.138'})
        req2 = urlopen(req)
        cj = CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj))
        self.assertEqual(req2.getcode(), 200)
    
    def test_mozilla(self):
        req = Request('https://www.deolhonocorona.com/', headers={'User-Agent': 'Mozilla/77.0'})
        req2 = urlopen(req)
        cj = CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj))
        self.assertEqual(req2.getcode(), 200)
    
    def test_safari(self):
        req = Request('https://www.deolhonocorona.com/', headers={'User-Agent': 'Safari/13.1'})
        req2 = urlopen(req)
        cj = CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj))
        self.assertEqual(req2.getcode(), 200)

    def test_safari_mobile(self):
        req = Request('https://www.deolhonocorona.com/', headers={'User-Agent': 'Safari/12.1.2'})
        req2 = urlopen(req)
        cj = CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj))
        self.assertEqual(req2.getcode(), 200)

    def test_edge(self):
        req = Request('https://www.deolhonocorona.com/', headers={'User-Agent': 'Edge/83.0.478.45'})
        req2 = urlopen(req)
        cj = CookieJar()
        opener = build_opener(HTTPCookieProcessor(cj))
        self.assertEqual(req2.getcode(), 200)