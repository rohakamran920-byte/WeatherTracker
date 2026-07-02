import requests
from config import 783f3e4a29c03f4c1771332612657be2, https://api.openweathermap.org/data/2.5/weather


def get_weather(city):
    params = {
        "q": city,
        "appid": 783f3e4a29c03f4c1771332612657be2,
        "units": "metric"
    }

    response = requests.get(https://api.openweathermap.org/data/2.5/weather, params=params)

    if response.status_code == 200:
        data = response.json()

        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind": data["wind"]["speed"],
            "description": data["weather"][0]["description"].title(),
            "icon": data["weather"][0]["icon"]
        }

        return weather

    return None