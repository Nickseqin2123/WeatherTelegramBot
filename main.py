import requests
from bs4 import BeautifulSoup
from constants import headers, cookies
from funcs.randomag import randomUserAgent
from funcs.countryfunc import countrr


def main():
        
    agent = randomUserAgent()
    headers['User-Agent'] = agent

    request = requests.get('https://www.gismeteo.ru/catalog/', headers=headers, cookies=cookies)
        
    bs = BeautifulSoup(request.text, 'lxml')
    countries_groups = bs.find_all(class_='catalog-group-with-letter')

    for group in countries_groups:
        country_links = group.find_all('a', class_='catalog-group-item link link-hover')
    
        for country in country_links:
            country_name = country.find(class_='catalog-group-item-name').text.strip()
            country_url = country['href']
            # counrtyAdd(name)
            
            countrr(country_name, country_url)


main()