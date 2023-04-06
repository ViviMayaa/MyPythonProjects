import requests
# https://api.openweathermap.org/data/2.5/weather?lat=-23.5506507&lon=-46.6333824&appid=49e4df2e9245c6c026178457260ea902

URL_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = '49e4df2e9245c6c026178457260ea902'
LAT = '-23.5506507'
LONG = '-46.6333824'

parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY

}

weather_get = requests.get(url=URL_ENDPOINT, params=parameters)
weather_get.raise_for_status()
weather_data = weather_get.json()
# print(weather_data.status_code)
print(weather_data)
print(weather_data['weather'][0]['main'])
print(f"The weather is mainly {weather_data['weather'][0]['main']}, with "
      f"{weather_data['weather'][0]['description']} and temperature of {round((weather_data['main']['temp'] -32 )/1.8)} celsius")