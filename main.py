from time import sleep

from curl_cffi.requests.session import Session
from bs4 import BeautifulSoup
from constants import headers, cookies
from funcs.randomag import randomUserAgent
from funcs.countryfunc import countrr


def main():
        
    agent = randomUserAgent()
    headers['User-Agent'] = agent

    session = Session()
    request = session.get('https://www.gismeteo.ru/catalog/', headers=headers, cookies=cookies, impersonate="chrome110")
        
    bs = BeautifulSoup(request.text, 'lxml')
    countries_groups = bs.find_all(class_='catalog-group-with-letter')

    for group in countries_groups:
        country_links = group.find_all('a', class_='catalog-group-item link link-hover')
    
        for country in country_links:
            country_name = country.find(class_='catalog-group-item-name').text.strip()
            country_url = country['href']
            # counrtyAdd(name)
            
            countrr(country_name, country_url, session)
            sleep(5)

main()