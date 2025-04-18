from configparser import ConfigParser
from pprint import pprint
import requests


cfn = ConfigParser()
cfn.read('data.ini')

ct_cde = 'RU'

headers = {
    'Authorization': f'Bearer {cfn["TOKEN"]["api"]}',
    'Accept-Language': 'ru'
}


req_cou = requests.get(url='https://data-api.oxilor.com/rest/countries', headers=headers)

countries = req_cou.json()

par = []

for i in countries:
    par.append({'id': i['id'], 'name': i['name'], 'type': i['type']})

print(par)
# req_reg = requests.get(url=f'https://data-api.oxilor.com/rest/regions?countryCode={ct_cde}&first=100', headers=headers)

# regions = req_reg.json()

# for i in regions['edges']:
#     print(i)