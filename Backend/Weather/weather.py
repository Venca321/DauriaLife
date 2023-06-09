
from geopy.geocoders import Nominatim
from Backend.core_helper import Data
import requests, datetime, time, sqlite3

API_KEY = Data.Settings.open_weather_api_key

def coords(pos:str):
    """
    Function, returning coords of set place [lat, long]
    """
    geolocator = Nominatim(user_agent="DauriaLife") #Geolocator setup
    location = geolocator.geocode(pos)
    return location.latitude, location.longitude

class weather():
    def forecast(lang:str, location:str):
        """
        Function returning weather forecast
        """
        lat, lon = coords(location)
        url = f"http://api.openweathermap.org/data/2.5/forecast?appid={API_KEY}&lat={lat}&lon={lon}&lang={lang}&units=metric"

        r = requests.get(url)
        data = r.json()

        if data["cod"] == "200":
            sunrise = datetime.datetime.fromtimestamp(data["city"]["sunrise"]).strftime("%H:%M:%S")
            sunset = datetime.datetime.fromtimestamp(data["city"]["sunset"]).strftime("%H:%M:%S")
            raw_weather = data["list"]

            weather_forecast = []
            for record in raw_weather:
                date_time = datetime.datetime.fromtimestamp(record["dt"]) #Datetime
                date_var = date_time.strftime("%d-%m-%Y") #21-4-2023
                time_var = date_time.strftime("%H:%M:%S") #16:24:00
                try: rain = record["rain"]["3h"] #mm of rain for last 3h
                except: rain = 0

                weather_forecast.append([
                    date_var,
                    time_var,
                    record["main"]["temp"],
                    record["main"]["feels_like"],
                    record["main"]["pressure"],
                    record["main"]["humidity"],
                    record["weather"][0]["description"],
                    record["clouds"]["all"],
                    record["wind"]["speed"],
                    record["wind"]["deg"],
                    rain,
                    sunrise,
                    sunset
                ])

            return weather_forecast
        else:
            raise NotImplementedError

    def update():
        """
        Updates local weather database
        """
        connection = sqlite3.connect("Backend/Weather/WeatherData/data.db")
        cursor = connection.cursor()

        cities = Data.weather.cities
        city_counter = 0
        for state in cities.keys():
            for city in cities[state]:
                city_counter += 1
                name = f"{city}, {state}"
                table_name = name.replace(", ", "_").lower()
                if state == "Česko":
                    weather_forecast = weather.forecast("cz", name)
                else:
                    raise NotImplementedError
                
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                connection.commit()

                sql = f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    date TEXT,
                    time TEXT,
                    temp INTEGER,
                    feel_temp INTEGER,
                    pressure INTEGER,
                    humidity INTEGER,
                    weather_desc TEXT,
                    clouds INTEGER,
                    wind_speed INTEGER,
                    wind_deg INTEGER,
                    rain INTEGER,
                    sunrise TEXT,
                    sunset TEXT
                )
                '''

                cursor.execute(sql)
                connection.commit()

                for record in weather_forecast:
                    sql = f'''
                    INSERT INTO {table_name} 
                    (
                    date, time, temp, feel_temp, pressure, humidity, 
                    weather_desc, clouds, wind_speed, wind_deg, rain, 
                    sunrise, sunset
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    '''

                    cursor.execute(sql, record)
                    connection.commit()

                time.sleep(1)

                max_updates = Data.weather.max_calls_per_minute*Data.weather.update_time_minutes
                if city_counter >= max_updates - (max_updates/100):
                    raise NotImplementedError
        connection.close()

    def search(location:str):
        """
        Returns weather forecast from local database
        """
        location = location.replace(", ", "_").lower()
        connection = sqlite3.connect("Backend/Weather/WeatherData/data.db")
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {location}")
        rows = cursor.fetchall()
        connection.close()

        return rows
