# app.py

from flask import Flask, render_template
from api import get_weather
from config import CITIES
import time

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    weather_data_list = []
    for city in CITIES:
        weather_data = get_weather(city)
        if weather_data:
            weather_data_list.append({
                'city': city,
                'temp': weather_data['temp'],
                'feels_like': weather_data['feels_like'],
                'main': weather_data['main'],
                'dt': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(weather_data['dt'])),
            })
    return render_template('index.html', weather_data_list=weather_data_list)

if __name__ == "__main__":
    app.run(debug=True)
