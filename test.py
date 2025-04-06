import asyncio
import time
from pprint import pprint
from configparser import ConfigParser
import requests
from requestss.ssp import get_counties, add_rayon


async def main():
    cfg = ConfigParser()
    cfg.read('data.ini')

    API = cfg['TOKEN']['API']
    countries = await get_counties()
    
    for country in countries:
        country = country[0]
        iso = country.iso
        cou_id = country.id
        
        req = requests.get(f'http://geohelper.info/api/v1/cities?filter[countryIso]={iso}&pagination[limit]=100&locale[lang]=ru&apiKey={API}')  
        time.sleep(1)
        pars = req.json()
        pagi = pars['pagination']
        
        for i in range(1, pagi['totalPageCount'] + 1):
            req = requests.get(f'http://geohelper.info/api/v1/cities?pagination[page]={i}&filter[countryIso]={iso}&pagination[limit]=100&locale[lang]=ru&apiKey={API}')
            time.sleep(1)
            pars = req.json()
            
            for obj in pars['result']:
                rayon = obj.get('area')
                
                if rayon:
                    region_id = obj['regionId']
                    await add_rayon(cou_id, region_id, rayon)
    print('ВСЁ!')
    

asyncio.run(main())