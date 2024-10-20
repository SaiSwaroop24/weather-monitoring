# api.py

import requests
from config import API_KEY, CITIES

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'main': data['weather'][0]['main'],
            'dt': data['dt']
        }
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None
