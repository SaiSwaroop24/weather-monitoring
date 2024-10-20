

# Weather Monitoring Application

## Table of Contents
1. [Overview](#overview)
2. [Objective](#objective)
3. [Technologies Used](#technologies-used)
4. [Features](#features)
5. [File Structure](#file-structure)
6. [Installation Instructions](#installation-instructions)
   - [Prerequisites](#prerequisites)
   - [Step-by-Step Setup](#step-by-step-setup)
7. [Configuration](#configuration)
8. [Running the Application](#running-the-application)
9. [Testing](#testing)
10. [How to Access the Web Interface](#how-to-access-the-web-interface)
11. [Artifacts Submission](#artifacts-submission)
12. [License](#license)

## Overview
The **Weather Monitoring Application** is a real-time data processing system designed to monitor weather conditions across major metros in India. The application fetches real-time weather data from the OpenWeatherMap API, processes the information to provide aggregated daily summaries, and generates alerts based on configurable thresholds.

## Objective
The main objective of this project is to provide a system that continuously monitors weather data, calculates daily weather summaries, and alerts users to significant changes in weather conditions.

## Technologies Used
- **Programming Language**: Python 3.8.10
- **Web Framework**: Flask (for web interface)
- **Database**: SQLite (for storing weather data and summaries)
- **API**: OpenWeatherMap API (for fetching real-time weather data)
- **Libraries**:
  - `requests`: For making API calls.
  - `flask`: For creating the web application.
  - `sqlite3`: For database interactions.
  - `matplotlib`: For visualizations (if applicable).
  - `schedule`: For running periodic tasks.

## Features
1. **Data Retrieval**: Continuously fetches weather data for the following cities:
   - Delhi
   - Mumbai
   - Chennai
   - Bangalore
   - Kolkata
   - Hyderabad

2. **Real-Time Processing**: Configurable intervals for data fetching (e.g., every 5 minutes).

3. **Daily Weather Summary**: Aggregates and calculates:
   - Average temperature
   - Maximum temperature
   - Minimum temperature
   - Dominant weather condition

4. **Alerting System**: Users can set thresholds for temperature alerts, and the system triggers notifications for significant weather changes.

5. **Visualization**: Displays daily weather summaries and historical trends.

## File Structure
Here's the structure of the project for better understanding:

```
weather-monitoring/
├── src/
│   ├── app.py            # Flask web application to display results
│   ├── main.py           # Main script to fetch and process weather data
│   ├── api.py            # Module for making API calls to OpenWeatherMap
│   ├── database.py       # Module for database interactions
│   ├── config.py         # Configuration file, including API keys and city settings
│   ├── requirements.txt   # List of Python package dependencies
├── README.md             # Project documentation
```

## Installation Instructions

### Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.8 or higher**: Download from [python.org](https://www.python.org/downloads/).
- **pip**: Python package manager (comes with Python installations).

### Step-by-Step Setup
Follow these steps to set up the project:

1. **Clone the Repository**
   Open your terminal (Command Prompt on Windows or Terminal on macOS/Linux) and run:
   ```bash
   git clone <repository-url>
   cd weather-monitoring
   ```

2. **Create a Virtual Environment**
   To avoid dependency conflicts, create a virtual environment:
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**
   Activate the virtual environment:
   - On **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**
   Use pip to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. **API Key Setup**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API key.
   - Open the `config.py` file in the `src` directory.
   - Add your API key:
     ```python
     API_KEY = 'your_api_key_here'
     ```

2. **City Configuration**
   - You can also modify the `CITIES` variable in `config.py` to add or remove cities as needed.

## Running the Application
To start the weather monitoring application, execute the following command in your terminal:
```bash
python src/main.py
```
This command initiates the process of fetching weather data continuously.

### Running the Web Application
To view the results in a web browser, open another terminal (keeping the first running) and execute:
```bash
python src/app.py
```
This command launches the Flask web application.

## Testing
To ensure that the application functions as expected, you can run tests using:
```bash
pytest
```
This command runs all the tests defined in your code.

## How to Access the Web Interface
Once the web application is running, open your web browser and navigate to:
```
http://127.0.0.1:5000
```
You will see the real-time weather data and summaries displayed on the webpage.

## Artifacts Submission
When submitting the assignment, ensure you include the following:
- **Codebase**: Provide a link to your GitHub repository.
- **README file**: Make sure it's comprehensive.
