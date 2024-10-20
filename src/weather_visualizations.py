# visualizations.py

import sqlite3
import matplotlib.pyplot as plt
from config import DATABASE_NAME

def plot_daily_summary():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT date, city, AVG(avg_temp) as avg_temp, MAX(max_temp) as max_temp, MIN(min_temp) as min_temp
        FROM daily_summary
        GROUP BY date, city
        ORDER BY date
    ''')

    data = cursor.fetchall()
    
    dates = sorted(set(row[0] for row in data))
    cities = sorted(set(row[1] for row in data))

    # Preparing data for plotting
    avg_temps = {city: [] for city in cities}
    max_temps = {city: [] for city in cities}
    min_temps = {city: [] for city in cities}

    for date in dates:
        for city in cities:
            avg_temp = next((row[2] for row in data if row[0] == date and row[1] == city), None)
            max_temp = next((row[3] for row in data if row[0] == date and row[1] == city), None)
            min_temp = next((row[4] for row in data if row[0] == date and row[1] == city), None)

            avg_temps[city].append(avg_temp)
            max_temps[city].append(max_temp)
            min_temps[city].append(min_temp)

    # Plotting
    for city in cities:
        plt.plot(dates, avg_temps[city], label=f'{city} Average Temp')
        plt.plot(dates, max_temps[city], label=f'{city} Max Temp', linestyle='--')
        plt.plot(dates, min_temps[city], label=f'{city} Min Temp', linestyle=':')

    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Weather Summary')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    conn.close()
