from random import randint
import json
import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': None,
    'accept': '*/*'
    }

cookies = {
    'i': 'kak3ly7sOUNOxKXaDeEHm/XNtgQDFT/2SXprkgwW8Em4jh7XVl6roPfyQSnr7ocviU07ZsIFIJmLoK23MqItK/iuNag=',
    'yandexuid': '5668957341739692972',
    'yashr': '2468207511739692972',
    'yuidss': '5668957341739692972',
    'ymex': '2055052973.yrts.1739692973',
    'amcuid': '6124189171739694426',
    'skid': '29188211740908297',
    '_ym_uid': '17409082995751043',
    '_ym_d': '1740908299',
    'yabs-sid': '1057871171741356008',
    'receive-cookie-deprecation': '1',
    'bh': 'EkEiTm90KEE6QnJhbmQiO3Y9Ijk5IiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjEzMyIsICJDaHJvbWl1bSI7dj0iMTMzIioCPzA6CSJXaW5kb3dzImDEnqy+Bmoe3Mrh/wiS2KGxA5/P4eoD+/rw5w3r//32D6K4zocI'
}


def main():

    for i in range(1):
        
        with open('Agents\\solo.txt', encoding='utf-8') as f:
            alls = f.readlines()
        
        user_agent = alls[randint(0, 1107)]
        headers['User-Agent'] = user_agent.strip()

        request = requests.get('https://www.gismeteo.ru/catalog/russia/', headers=headers, cookies=cookies)
        
        bs = BeautifulSoup(request.text, 'lxml')
        print(bs.find('section', class_='catalog-body').find(class_='catalog-subtitle'))


main()