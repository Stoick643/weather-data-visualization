import streamlit as st
import plotly.express as px
import pandas as pd
from utils import get_weather_data, get_forecast_data, process_forecast_data
from constants import FORECAST_DAYS, API_KEY
import requests

def test_api_key():
    test_url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric"
    try:
        response = requests.get(test_url)
        response.raise_for_status()
        st.success("API Key is valid and working")
    except requests.RequestException as e:
        st.error(f"API Key test failed: {e}")

st.set_page_config(page_title="Weather Data Visualization", page_icon="🌤️", layout="wide")

st.title("Weather Data Visualization")

# Test API key
test_api_key()

# Get user input
city = st.text_input("Enter a city name:", "London")

if st.button("Get Weather Data"):
    weather_data = get_weather_data(city)
    if weather_data:
        st.write(f"Current weather in {city}:")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
        st.write(f"Humidity: {weather_data['main']['humidity']}%")
        st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        
        # Fetch and display forecast data
        forecast_data = get_forecast_data(city)
        if forecast_data:
            processed_forecast = process_forecast_data(forecast_data)
            st.subheader(f"{FORECAST_DAYS}-Day Forecast")
            forecast_df = pd.DataFrame(processed_forecast)
            fig = px.line(forecast_df, x='Date', y='Temperature', title=f"Temperature Trend in {city}")
            fig.update_layout(xaxis_title="Date", yaxis_title="Temperature (°C)")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Unable to fetch forecast data. Please try again later.")
    else:
        st.error("Unable to fetch weather data. Please check the city name and try again.")

# Add some information about the app
st.sidebar.title("About")
st.sidebar.info("This app visualizes weather data for a given city using the OpenWeatherMap API. Enter a city name to see current weather conditions and a 5-day forecast.")

# Add a footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
