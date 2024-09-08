import os

# OpenWeatherMap API key
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
print(f"API_KEY length: {len(API_KEY) if API_KEY else 0}")

# Base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Number of days for forecast
FORECAST_DAYS = 5
