import asyncio
from pprint import pprint
from configparser import ConfigParser
import requests
from requestss.ssp import add_region, get_country


async def main():
    cfg = ConfigParser()
    cfg.read('data.ini')

    API = cfg['TOKEN']['API']

    req = requests.get(f'http://geohelper.info/api/v1/cities?filter[countryIso]=RU&pagination[limit]=10&locale[lang]=ru&apiKey={API}')  
    pars = req.json()
    pagi = pars['pagination']
    
    for i in range(1, pagi['totalPageCount'] + 1):
        req = requests.get(f'http://geohelper.info/api/v1/cities?pagination[page]={i}&filter[countryIso]=RU&pagination[limit]=100&locale[lang]=ru&apiKey={API}')
        pars = req.json()
        
        for obj in pars['result']:
            print(obj)
            break
        break

        
    
    # req = requests.get(f'http://geohelper.info/api/v1/districts?filter[cityId]={cities['id']}&pagination[limit]=10&locale[lang]=ru&apiKey={API}')
    # pprint(req.json())
    

asyncio.run(main())