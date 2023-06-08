
from geopy.geocoders import Nominatim
from collections import defaultdict
from Backend.core import Data
import requests, datetime

API_KEY = Data.Settings.open_weather_api_key

def coords(pos:str):
    """
    Function, returning coords of set place [lat, long]
    """
    geolocator = Nominatim(user_agent="DauriaLife") #Geolocator setup
    location = geolocator.geocode(pos)
    return location.latitude, location.longitude

def weather(lang:str, location:str):
    """
    Function returning weather forecast
    """
    lat, lon = coords(location)
    url = f"http://api.openweathermap.org/data/2.5/forecast?appid={API_KEY}&lat={lat}&lon={lon}&lang={lang}&units=metric"

    print(url)

    r = requests.get(url)
    data = r.json()

    if data["cod"] == "200":
        sunrise = datetime.datetime.fromtimestamp(data["city"]["sunrise"]).strftime("%H:%M:%S")
        sunset = datetime.datetime.fromtimestamp(data["city"]["sunset"]).strftime("%H:%M:%S")
        raw_weather = data["list"]

        weather_forecast = defaultdict(dict)
        for record in raw_weather:
            date_time = datetime.datetime.fromtimestamp(record["dt"]) #Datetime
            date = date_time.strftime("%d-%m-%Y") #21-4-2023
            time = date_time.strftime("%H:%M:%S") #16:24:00

            temp = record["main"]["temp"] #Real temp
            feel_temp = record["main"]["feels_like"] #Feels like temp
            pressure = record["main"]["pressure"]
            humidity = record["main"]["humidity"]
            weather_desc = record["weather"][0]["description"] #Description of weather in lang
            clouds = record["clouds"]["all"] #Clouds %
            wind_speed = record["wind"]["speed"]
            wind_deg = record["wind"]["deg"]
            try: rain = record["rain"]["3h"] #mm of rain for last 3h
            except: rain = None

            weather_forecast[date][time] = {
                "temp": temp,
                "feel_temp": feel_temp,
                "pressure": pressure,
                "humidity": humidity,
                "weather_decs": weather_desc,
                "clouds": clouds,
                "wind_speed": wind_speed,
                "wind_deg": wind_deg,
                "rain": rain
            }

        return weather_forecast, sunrise, sunset
    else:
        print("Error")

if "__main__" == __name__:
    weather_forecast, sunrise, sunset = weather("cz", "Louny, Česko")

    print(f"Slunce vyjde v {sunrise}")
    print(f"Slunce zapadne v {sunset}")

    for record in weather_forecast.keys():
        print(f"\n{record}:")
        for time in weather_forecast[record].keys():
            print(f"    {time}:")
            for value in weather_forecast[record][time].keys():
                print(f"        {value}: {weather_forecast[record][time][value]}")
