import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {'name': city, 'count': 1, 'format': 'json'}
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if not data['results']:
            print(f"City not found: {city}")
            return None, None
        
        result = data['results'][0]
        return result['latitude'], result['longitude']
    except:
        print("Could not connect")
        return None, None

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': lat,
        'longitude': lon,
        'current': 'temperature_2m,weather_code,wind_speed_10m',
        'temperature_unit': 'celsius'
    }
    
    response = requests.get(url, params=params)
    return response.json()['current']

def weather_description(code):
    codes = {
        0: 'Clear',
        1: 'Mainly clear',
        2: 'Partly cloudy',
        3: 'Overcast',
        45: 'Foggy',
        48: 'Foggy with rime',
        51: 'Light drizzle',
        53: 'Moderate drizzle',
        55: 'Heavy drizzle',
        61: 'Light rain',
        63: 'Moderate rain',
        65: 'Heavy rain',
        71: 'Light snow',
        73: 'Moderate snow',
        75: 'Heavy snow',
        77: 'Snow grains',
        80: 'Rain showers',
        81: 'Heavy showers',
        82: 'Violent showers',
        85: 'Snow showers',
        86: 'Heavy snow showers',
        95: 'Thunderstorm',
        96: 'Thunderstorm with hail',
        99: 'Thunderstorm with heavy hail'
    }
    return codes.get(code, 'Unknown')

city = input("City: ")
print(f"\nFetching {city}...")

lat, lon = get_coordinates(city)
if lat is None:
    exit()

weather = get_weather(lat, lon)
temp_c = weather['temperature_2m']
temp_f = (temp_c * 9/5) + 32
desc = weather_description(weather['weather_code'])

print(f"\n{city}")
print(f"Temp: {temp_c}°C ({temp_f:.0f}°F)")
print(f"Wind: {weather['wind_speed_10m']} km/h")
print(f"Weather: {desc}")
