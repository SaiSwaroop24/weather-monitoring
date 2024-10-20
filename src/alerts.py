ALERT_THRESHOLD = 35.0  # Celsius

def check_alerts(weather_data):
    if weather_data['temp'] > ALERT_THRESHOLD:
        print(f"ALERT! {weather_data['city']} temperature exceeds {ALERT_THRESHOLD}°C!")
        # Send email or console notification if required
