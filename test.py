import json
from pprint import pprint
import requests


API = '1xz87sfCI5go5njQ5jHumYmK6OcCLn1u'


req = requests.get(f'http://geohelper.info/api/v1/countries?locale[lang]=ru&apiKey={API}')


for i in req.json()['result']:
    print(f'ID страны: {i['id']} | Название страны: {i['name']}')