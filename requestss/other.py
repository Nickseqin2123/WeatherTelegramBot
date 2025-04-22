from geopy.geocoders import Nominatim


async def get_locality_name(lat: float, lon: float):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.reverse((lat, lon), language="ru")

    if not location or not location.raw:
        return {'type': False, 'data': "Не удалось получить ответ от геосервера."}

    address = location.raw.get("address", {})

    locality_keys = (
        "city", "town", "village", "hamlet",
        "municipality", "locality", "county", "state_district"
    )

    for key in locality_keys:
        if key in address:
            return {'type': True, 'data': address[key]}

    return {'type': False, 'data': "Не удалось определить населённый пункт. Проверьте координаты или напишите в поддержку."}