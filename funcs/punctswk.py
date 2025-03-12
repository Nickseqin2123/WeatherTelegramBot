from bs4 import BeautifulSoup
from time import sleep


def punctsPars(html, country, region=None, rayon=None):
    print(f"Парсим пункты: '{country}' регион: {region} район: {rayon}")
    
    bs = BeautifulSoup(html, 'lxml')
    sleep(1)
    puncts_groups = bs.find_all(class_='catalog-group-with-letter')

    for group in puncts_groups:
        puncts_links = group.find_all('a', class_='catalog-group-item link link-hover')
    
        for punct in puncts_links:
            punct_name = punct.find(class_='catalog-group-item-name').text.strip()
            #addPunct(punct_name, country, region, rayon)
            print(f'|Пункт: {punct_name}; Страна: {country}; Регион: {region}; Район: {rayon};|')
    else:
        print('\n')