import json
from pprint import pprint
from configparser import ConfigParser
import requests



def rayon(id_reg):
    ...


def region(iso, API):
    req = requests.get(f'http://geohelper.info/api/v1/regions?filter[countryIso]={iso}&locale[lang]=ru&apiKey={API}')


def main():
    cfg = ConfigParser()
    cfg.read('data.ini')

    API = cfg['TOKEN']['API']

    req = requests.get(f'http://geohelper.info/api/v1/countries?locale[lang]=ru&apiKey={API}')  
    countries = req.json()

    for i in countries['result']:
        print(i)
        break


main()