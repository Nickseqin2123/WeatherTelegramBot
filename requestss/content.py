import asyncio

from configparser import ConfigParser
from curl_cffi.requests import AsyncSession
from fake_headers import Headers


class Content:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    def __init__(self):
        cfg = ConfigParser()
        cfg.read('data.ini')
        
        self.url = 'https://yandex.ru/pogoda/cheboksary?'
        self.init_dynamic_headers()
    
    def init_dynamic_headers(self):
        headers = Headers(browser="chrome", os="win", headers=True).generate()
        headers.update({
            "authority": "yandex.ru",
            "referer": "",
            "accept-encoding": "gzip, deflate, br, zstd",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "cache-control": "max-age=0",
            })
        
        self.headers = headers
        
    async def weather(self, lat, lon):
        quer_url = f'{self.url}lat={lat}&lon={lon}'
        self.headers.update({
            'referer': quer_url
        })
        
        session = AsyncSession(impersonate='chrome120')
        
        response = await session.get(url=quer_url, headers=self.headers)

        with open('base.html', 'w', encoding='utf-8') as f:
            f.write(response.text)