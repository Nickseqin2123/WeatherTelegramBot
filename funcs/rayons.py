from time import sleep
from bs4 import BeautifulSoup
from constants import headers, cookies
from funcs.randomag import randomUserAgent
from funcs.punctswk import punctsPars
import requests


def rayonPars(country, region, name, rayon_href):
    agent = randomUserAgent()
    headers['User-Agent'] = agent
    sleep(1)
    request = requests.get(f'https://www.gismeteo.ru{rayon_href}', headers=headers, cookies=cookies)
    
    punctsPars(request.text, country, region, name)