import json
from pprint import pprint
from configparser import ConfigParser
import requests


def districts(region_id, API):
    req = requests.get(f'http://geohelper.info/api/v1/districts?pagination[limit]=100&regionId={region_id}&locale[lang]=ru&apiKey={API}')
    rayons = req.json()
    print(rayons)


def region(iso, API):
    req = requests.get(f'http://geohelper.info/api/v1/regions?pagination[limit]=100&filter[countryIso]={iso}&locale[lang]=ru&apiKey={API}')
    regions = req.json()
    pagination = regions['pagination']

    for page in range(pagination['totalPageCount']):
        req = requests.get(f'http://geohelper.info/api/v1/regions?pagination[page]={page}&pagination[limit]=100&filter[countryIso]={iso}&locale[lang]=ru&apiKey={API}')
        regions = req.json()
        
        for i in regions['result']:
            print(f'    ---> ID: {i['id']} Имя региона: {i['name']}')
            # districts(i['id'], API)
            break


def main():
    cfg = ConfigParser()
    cfg.read('data.ini')

    API = cfg['TOKEN']['API']

    req = requests.get(f'http://geohelper.info/api/v1/countries?locale[lang]=ru&apiKey={API}')  
    countries = req.json()
    
    for i in countries['result']:
        # print(f'ISO: {i['iso']} Имя страны: {i['name']}')
        region(i['iso'], API)
        break


main()