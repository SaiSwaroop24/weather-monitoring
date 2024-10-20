# database.py

import sqlite3
from datetime import datetime
from config import DATABASE_NAME

def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY,
            city TEXT,
            temp REAL,
            feels_like REAL,
            main TEXT,
            dt INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            id INTEGER PRIMARY KEY,
            city TEXT,
            date TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_weather_data(weather_data):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, temp, feels_like, main, dt)
        VALUES (?, ?, ?, ?, ?)
    ''', (weather_data['city'], weather_data['temp'], weather_data['feels_like'], weather_data['main'], weather_data['dt']))
    conn.commit()
    conn.close()

def calculate_daily_summary():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT city, 
               DATE(dt, 'unixepoch') as date,
               AVG(temp) as avg_temp,
               MAX(temp) as max_temp,
               MIN(temp) as min_temp,
               main
        FROM weather
        GROUP BY city, date
    ''')

    daily_data = cursor.fetchall()
    for row in daily_data:
        city, date, avg_temp, max_temp, min_temp, main = row
        cursor.execute('''
            INSERT INTO daily_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (city, date, avg_temp, max_temp, min_temp, main))
    
    conn.commit()
    conn.close()
