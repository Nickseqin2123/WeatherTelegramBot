from configparser import ConfigParser
from aiohttp import ClientSession


class Content:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    def __init__(self):
        cfg = ConfigParser()
        cfg.read('data.ini')
        
        self.url = 'https://data-api.oxilor.com/rest/'
        self.__token = cfg['TOKEN']['api']
        self.__headers = {
            'Authorization': f'Bearer {self.__token}',
            'Accept-Language': 'ru'
        }
    
    async def countries(self, **params):
        ready_params = await self.make_params_query(**params)
        full_url = f'{self.url}/countries{ready_params}'
        
        async with ClientSession() as session:
            async with session.get(full_url, headers=self.__headers) as response:
                return await response.json()
    
    async def make_params_query(self, **params):
        txt = [f'{key}={value}' for key, value in params.items()]
        return '?' + '&'.join(txt)