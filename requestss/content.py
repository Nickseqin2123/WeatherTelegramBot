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
        
        self.__token = cfg['TOKEN']['token_api']
        
    async def weather(self, lat, lon):
        quer_url = f'https://api.openweathermap.org/data/2.5/weather?appid={self.__token}&lang=ru&lat={lat}&lon={lon}&units=metric'
        
        async with ClientSession() as session:
            async with session.get(url=quer_url) as response:
                return await response.json()
        
        return response.text