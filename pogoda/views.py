import requests
from django.shortcuts import render
from .models import City


def index(request):
    appid = '0a1ddb1d008cf9a37ce6899405f5e20b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        # Проверяем, что API вернул правильный ответ с ключами 'main' и 'weather'
        if "main" in res and "weather" in res:
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"]
            }
            all_cities.append(city_info)
        else:
            # Если API вернул ошибку, добавляем город с информацией о том, что данные недоступны
            city_info = {
                'city': city.name,
                'temp': 'N/A',
                'icon': 'N/A'
            }
            all_cities.append(city_info)

    context = {'all_info': all_cities}

    return render(request, 'index.html', context)
