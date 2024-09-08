# Weather Data Visualization App

This Streamlit application visualizes weather data for a given city using the OpenWeatherMap API. Users can enter a city name to see current weather conditions and a 5-day forecast.

## Features

- Current weather display including temperature, humidity, wind speed, and description
- 5-day forecast with temperature trends
- Interactive temperature trend graph
- Weather icons for easy visualization

## Setup

1. Clone this repository
2. Install the required packages:
   ```
   pip install streamlit requests plotly pandas
   ```
3. Set up your OpenWeatherMap API key as an environment variable:
   ```
   export OPENWEATHERMAP_API_KEY='your_api_key_here'
   ```
4. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

## Usage

Enter a city name in the text input field and click "Get Weather Data" to view the current weather and forecast for that city.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

## License

This project is open source and available under the [MIT License](LICENSE).
