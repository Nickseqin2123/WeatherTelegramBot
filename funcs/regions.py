from time import sleep
from bs4 import BeautifulSoup
from constants import headers, cookies
from funcs.randomag import randomUserAgent
import requests
from bs4 import BeautifulSoup
from funcs.punctswk import punctsPars
from funcs.rayons import rayonPars


def regionPars(country_name, name, region_href):
    print(f'Начата работа над регионом: "{name}" Страна: {country_name}')
    
    agent = randomUserAgent()
    headers['User-Agent'] = agent
    sleep(1)
    request = requests.get(f'https://www.gismeteo.ru{region_href}', headers=headers, cookies=cookies)
    txt_req = request.text
    
    bs = BeautifulSoup(txt_req, 'lxml')
    section_content = bs.find_all('section', class_='catalog-body') 
    result = section_content[-1].find(class_='catalog-subtitle').text
    sleep(0.2)
    if result == 'Пункты':
        punctsPars(txt_req, country_name, region=name)
    elif result == 'Районы':
        bs = BeautifulSoup(txt_req, 'lxml')
    
        rayon_groups = bs.find_all(class_='catalog-group-with-letter')

        for group in rayon_groups:
            rayon_links = group.find_all('a', class_='catalog-group-item link link-hover')
    
            for rayon in rayon_links:
                rayon_name = rayon.find(class_='catalog-group-item-name').text.strip()
                rayon_href = rayon['href']
                
                rayonPars(country_name, name, rayon_name, rayon_href)