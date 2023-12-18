#I've added the weather for all my districts.
#You can choose any city from the 'locations' table, and it will display the weather there.

import requests

class WeatherData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?q={},IL&appid={}"

    def get_weather(self, district):
        url = self.base_url.format(district, self.api_key)
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                'District': district,
                'Temperature': data['main']['temp'],
                'Description': data['weather'][0]['description'],
                'Humidity': data['main']['humidity'],
                'Wind_speed': data['wind']['speed']
            }
            return weather_info
        else:
            return f"Failed to fetch weather data for {district}. Error: {response.status_code}"

api_key = '9fc6732ac540b661b319cb11ec5cb076' 
israel_weather = WeatherData(api_key)

district = 'Tel Aviv'  # we can check any city of the district(from Table locations) we want to fetch weather data for
weather_data = israel_weather.get_weather(district)

if isinstance(weather_data, dict):
    print(f"Weather in {weather_data['District']}:")
    print(f"Temperature: {weather_data['Temperature']} Kelvin")
    print(f"Description: {weather_data['Description']}")
    print(f"Humidity: {weather_data['Humidity']}%")
    print(f"Wind Speed: {weather_data['Wind_speed']} m/s")
else:
    print(weather_data)
