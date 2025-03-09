from time import sleep
from constants import headers, cookies
from funcs.randomag import randomUserAgent
import requests
from bs4 import BeautifulSoup
from funcs.punctswk import punctsPars
from funcs.regions import regionPars


def countrr(name, url):
    print(f'Начата работа над страной: "{name}"')
    
    agent = randomUserAgent()
    headers['User-Agent'] = agent
    sleep(0.5)
    request = requests.get(f'https://www.gismeteo.ru{url}', headers=headers, cookies=cookies)
    txt_req = request.text
    
    bs = BeautifulSoup(txt_req, 'lxml')
    section_content = bs.find_all('section', class_='catalog-body') 
    
    result = section_content[-1].find(class_='catalog-subtitle').text
    
    if result == 'Пункты':
        punctsPars(txt_req, name)
    elif result == 'Регионы':
        bs = BeautifulSoup(txt_req, 'lxml')
    
        region_groups = bs.find_all(class_='catalog-group-with-letter')

        for group in region_groups:
            region_links = group.find_all('a', class_='catalog-group-item link link-hover')
    
            for punct in region_links:
                region_name = punct.find(class_='catalog-group-item-name').text.strip()
                region_href = punct['href']
                
                regionPars(name, region_name, region_href)