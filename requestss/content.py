import json
import os
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
        if hasattr(self, "initialized") and self.initialized:
            return
        
        cfg = ConfigParser()
        cfg.read('data.ini')

        self.url = 'https://yandex.ru/pogoda/cheboksary?'
        self.session = AsyncSession(impersonate='chrome120')

        self.initialized = True
        
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
        
        self.init_dynamic_headers()
        self.headers.update({
            'referer': quer_url
        })
                
        if os.path.exists('cookies.json'):
            await self.load_cookies()
    
        response = await self.session.get(url=quer_url, headers=self.headers)
        await self.save_cookies()
        
        return response.text
    
    async def save_cookies(self, filename='cookies.json'):          
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.session.cookies.get_dict(), f, ensure_ascii=False)

    async def load_cookies(self, filename='cookies.json'):
        with open(filename, encoding='utf-8') as f:
            cookies = json.load(f)
            self.session.cookies.update(cookies)