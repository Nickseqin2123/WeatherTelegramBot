from pprint import pprint
import requests


token = 'efa9c10f095a8b0cf62cefbc358e3cd7'
url = f'https://api.openweathermap.org/data/2.5/weather?appid={token}&lang=ru&lat=56.13992&lon=47.247731&units=metric'

response = requests.get(url)
data = response.json()

name = data['name']
description = data['weather'][0]['description']
temp = data['main']['temp']
feels_like = data['main']['feels_like']
wind_speed = data['wind']['speed']

print(
    f'Город: {name}\n'
    
    f'Температура: {temp}°C\n'
    f'Ощущается как: {feels_like}°C\n'
    f'Скорость ветра: {wind_speed} м/с\n'
    f'Описание: {description}'
)