from constants import headers, cookies
from funcs.randomag import randomUserAgent
from funcs.punctswk import punctsPars
from time import sleep


def rayonPars(country, region, name, rayon_href, session):
    agent = randomUserAgent()
    headers['User-Agent'] = agent

    sleep(0.5)
    request = session.get(f'https://www.gismeteo.ru{rayon_href}', headers=headers, cookies=cookies, impersonate="chrome110")
    
    punctsPars(request.text, country, region, name)