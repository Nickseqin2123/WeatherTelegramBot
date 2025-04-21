from geopy.geocoders import Nominatim


def get_locality_name(lat: float, lon: float):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.reverse((lat, lon))
    
    address = location.raw.get("address", {})

    locality_keys = ("city", "town", "village", "hamlet", "municipality", "locality")

    for key in locality_keys:
        if key in address:
            return {'type': True, 'data': address[key]}

    return {'type': False, 'data': "Не удалось определить населённый пункт. Проверьте корректность данных, либо напишите в поддержку."}