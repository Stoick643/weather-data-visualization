import requests
from constants import API_KEY, BASE_URL

def get_weather_data(city):
    """
    Fetch weather data for a given city using OpenWeatherMap API
    """
    print(f"API_KEY length: {len(API_KEY) if API_KEY else 0}")
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use metric units
    }
    url = f"{BASE_URL}?q={city}&units=metric"
    print(f"Requesting URL: {url}")
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
        data['weather'][0]['icon_url'] = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
        return data
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_forecast_data(city):
    """
    Fetch 5-day forecast data for a given city using OpenWeatherMap API
    """
    forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(forecast_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None

def process_forecast_data(data):
    """
    Process the raw forecast data into a list of dictionaries
    """
    if not data:
        return None

    forecast_data = []
    for item in data['list']:
        forecast_data.append({
            'Date': item['dt_txt'],
            'Temperature': item['main']['temp'],
            'Description': item['weather'][0]['description'].capitalize(),
            'Icon': f"http://openweathermap.org/img/wn/{item['weather'][0]['icon']}@2x.png"
        })
    
    return forecast_data
