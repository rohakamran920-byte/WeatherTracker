import requests
from config import 783f3e4a29c03f4c1771332612657be2 , https://api.openweathermap.org/data/2.5/forecast

def get_forecast(city):
    """
    Fetch 5-day weather forecast for a city.
    Returns a list of forecast dictionaries.
    """

    params = {
        "q": city,
        "appid": "783f3e4a29c03f4c1771332612657be2",
        "units": "metric"
    }

    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
        response.raise_for_status()

        data = response.json()

        forecast_list = []
        added_dates = set()

        # OpenWeather returns data every 3 hours.
        # We take one forecast entry for each new day.
        for item in data["list"]:

            date = item["dt_txt"].split(" ")[0]

            if date not in added_dates:

                forecast = {
                    "date": date,
                    "min_temp": item["main"]["temp_min"],
                    "max_temp": item["main"]["temp_max"],
                    "temperature": item["main"]["temp"],
                    "humidity": item["main"]["humidity"],
                    "weather": item["weather"][0]["main"],
                    "description": item["weather"][0]["description"].title(),
                    "icon": item["weather"][0]["icon"]
                }

                forecast_list.append(forecast)
                added_dates.add(date)

            # Limit to 5 days
            if len(forecast_list) == 5:
                break

        return forecast_list

    except requests.exceptions.RequestException:
        return None