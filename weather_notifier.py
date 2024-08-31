#importing all necessary dependencies
#Send HTTP requests.
import requests  
#Create desktop notifications on Windows.
from win10toast import ToastNotifier

# Define the base URL for the API
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

#API
API_KEY='d1b27c498319f07ba309e009ffdb7435'


# Function to get weather data
def get_Weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    try:
        response=requests.get(BASE_URL,params=params)
        response.raise_for_status() # Raise an exception for HTTP errors
        data=response.json()

        # Extract relevant information
        temp=data['main']['temp']
        weather=data['weather'][0]['description']

        return f"Temperature: {temp}°C\nWeather: {weather.capitalize()}"
    
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return "Could not retrieve weather data."
    
# List of cities in Nepal
cities = ['Kathmandu', 'Seoul', 'Beijing']

#Creating an object of ToastNotifier class.
n=ToastNotifier()

for city in cities:
    print(f"Fetching weather for {city}...")
    weather_info = get_Weather(city)
    print(f"Weather info for {city}: {weather_info if weather_info else 'No data available'}")


     # Check if weather_info is valid
    if weather_info:
        n.show_toast(f'Weather update for {city}', weather_info, duration=10)
    else:
        n.show_toast(f'Weather update for {city}', "Could not retrieve weather data.", duration=10)