import json
from pprint import pprint
from configparser import ConfigParser
import requests


cfg = ConfigParser()
cfg.read('data.ini')

API = cfg['TOKEN']['API']


req = requests.get(f'http://geohelper.info/api/v1/countries?locale[lang]=ru&apiKey={API}')


for i in req.json()['result']:
    print(f'ID страны: {i['id']} | Название страны: {i['name']}')