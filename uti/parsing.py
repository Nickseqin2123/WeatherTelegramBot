async def get_weather_emoji(description, feels_like_temp):
    weather_emoji = {
        'ясно': '☀️',
        'немного облаков': '🌤️',
        'облачно с прояснениями': '☁️',
        'переменная облачность': '🌥️',
        'дождь': '🌧️',
        'ливень': '🌧️',
        'гроза': '⚡',
        'снег': '❄️',
        'туман': '🌫️'
    }
    
    emoji_description = weather_emoji.get(description.lower(), '🌥️')
    
    if feels_like_temp <= 0:
        emoji_feels_like = '🥶'
    elif feels_like_temp <= 10:
        emoji_feels_like = '😌'
    elif feels_like_temp <= 20:
        emoji_feels_like = '🙂'
    elif feels_like_temp <= 30:
        emoji_feels_like = '😊'
    else:
        emoji_feels_like = '🥵'
    
    return emoji_description, emoji_feels_like


async def parser(data: dict):
    name = data['name']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    wind_speed = data['wind']['speed']

    emoji_description, emoji_feels_like = await get_weather_emoji(description=description, feels_like_temp=feels_like)
    
    return f'''
<b>Местоположение</b>: {name} 🌆

<b>Температура</b>: {temp}°C 🌡️
<b>Ощущается как</b>: {feels_like}°C {emoji_feels_like}
<b>Скорость ветра</b>: {wind_speed} м/с 🌬️
<b>Описание</b>: {description} {emoji_description}
'''