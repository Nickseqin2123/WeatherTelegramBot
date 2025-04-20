import configparser

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy import create_engine


class Configurator:
    
    def __init__(self, type_connect: str = 'async'):
        settings = configparser.RawConfigParser()
        settings.read('data.ini')
        
        db = settings['DATABASE']
        self.__USERNAME = db['USERNAME']
        self.__PASSWORD = db['PASSWORD']
        self.__HOST = db['HOST']
        self.__DB_NAME = db['DB_NAME']
        
        self.token = settings['TOKEN']['token']
        
        connectors = {
            'async': create_async_engine(self.async_connect_url),
            'sync': create_engine(self.sync)
        }

        self.engine: AsyncEngine = connectors[type_connect]
    
    @property
    def async_connect_url(self):
        return f'mysql+aiomysql://{self.__USERNAME}:{self.__PASSWORD}@{self.__HOST}/{self.__DB_NAME}'
    
    @property
    def sync(self):
        return f'mysql+pymysql://{self.__USERNAME}:{self.__PASSWORD}@{self.__HOST}/{self.__DB_NAME}'
    

cfg = Configurator()