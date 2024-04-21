import requests


from bs4 import BeautifulSoup
from fake_headers import Headers


def get_fact():
    req = requests.get("https://randstuff.ru/fact/", headers=Headers().generate()).text
    soup = BeautifulSoup(req, "lxml")
    try:
        fact = soup.find(class_="text").text
    except Exception:
        return soup.text
    else:
        return fact