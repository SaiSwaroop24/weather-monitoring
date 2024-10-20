# main.py

import time
from datetime import datetime
from api import get_weather
from database import store_weather_data, create_tables, calculate_daily_summary
from weather_visualizations import plot_daily_summary
from config import CITIES

# Alerting thresholds
TEMPERATURE_THRESHOLD = 35  # degrees Celsius
ALERT_CONSECUTIVE_COUNT = 2  # Number of consecutive updates exceeding threshold

# Maintain a count of consecutive alerts
consecutive_alerts = {city: 0 for city in CITIES}

def check_alerts(weather_data):
    global consecutive_alerts
    for city in CITIES:
        if weather_data['city'] == city:
            if weather_data['temp'] > TEMPERATURE_THRESHOLD:
                consecutive_alerts[city] += 1
                if consecutive_alerts[city] == ALERT_CONSECUTIVE_COUNT:
                    print(f"Alert! {city}: Temperature has exceeded {TEMPERATURE_THRESHOLD}°C for {ALERT_CONSECUTIVE_COUNT} consecutive updates.")
            else:
                consecutive_alerts[city] = 0  # Reset counter if below threshold

def fetch_weather_data():
    while True:
        for city in CITIES:
            weather_data = get_weather(city)
            if weather_data:
                store_weather_data(weather_data)
                check_alerts(weather_data)  # Check for alerts after storing data
                
                # Display the fetched weather data
                print(f"Weather data for {city}:")
                print(f"  Temperature: {weather_data['temp']} °C")
                print(f"  Feels Like: {weather_data['feels_like']} °C")
                print(f"  Main Condition: {weather_data['main']}")
                print(f"  Time of Update: {datetime.utcfromtimestamp(weather_data['dt']).strftime('%Y-%m-%d %H:%M:%S')}")
                print("-" * 40)  # Separator for readability
                
        time.sleep(60)  # Fetch data every 5 minutes

if __name__ == "__main__":
    create_tables()  # Ensure tables are created before fetching data
    try:
        fetch_weather_data()
    except KeyboardInterrupt:
        print("Program terminated.")
        calculate_daily_summary()  # Calculate daily summaries before exiting
        plot_daily_summary()  # Generate and show visualizations
