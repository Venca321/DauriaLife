
from geopy.geocoders import Nominatim
from Backend.core_helper import Data, report
import requests, datetime, time, sqlite3, json

API_KEY = Data.Settings.open_weather_api_key

def coords(pos:str):
    """
    Function, returning coords of set place [lat, long]
    """
    geolocator = Nominatim(user_agent="DauriaLife") #Geolocator setup
    location = geolocator.geocode(pos)
    return location.latitude, location.longitude

class weather_db():
    def create_table(cursor, connection, table_name: str) -> None:
        """Creates table in database."""
        sql = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            date TEXT,
            time TEXT,
            temp INTEGER,
            feel_temp INTEGER,
            pressure INTEGER,
            humidity INTEGER,
            weather_id INTEGER,
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

    def insert_data(cursor, connection, table_name: str, record: list) -> None:
        """Inserts data into database."""
        sql = f'''
        INSERT INTO {table_name} 
        (
        date, time, temp, feel_temp, pressure, humidity, 
        weather_id, clouds, wind_speed, wind_deg, rain, 
        sunrise, sunset
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        cursor.execute(sql, record)
        connection.commit()

class weather():
    def create_table_name(name:str):
        """
        Returns name, that is valid for database
        """
        return name.replace(", ", "_").replace(" ", "_").replace("-", "_").lower()

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

            weather_forecast = []
            for record in data["list"]:
                date_time = datetime.datetime.fromtimestamp(record["dt"]) #Datetime
                date_var = date_time.strftime("%d-%m-%Y") #21-4-2023
                time_var = date_time.strftime("%H:%M:%S") #16:24:00
                try: rain = record["rain"]["3h"] #mm of rain for last 3h
                except: rain = 0

                weather_forecast.append([
                    date_var, time_var, int(record["main"]["temp"]),
                    int(record["main"]["feels_like"]), int(record["main"]["pressure"]),
                    int(record["main"]["humidity"]), int(record["weather"][0]["id"]),
                    int(record["clouds"]["all"]), int(record["wind"]["speed"]),
                    int(record["wind"]["deg"]), int(rain), sunrise, sunset
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

        try:
            with open("Backend/Weather/WeatherData/info.json", 'r') as openfile: json_object = json.load(openfile)
            last_time = datetime.datetime.strptime(json_object["last_update"], "%H:%M:%S")
            if last_time < datetime.datetime.now() + datetime.timedelta(minutes=int(Data.Weather.update_time_minutes)-10): 
                report(f"Weather data updated at {json_object['last_update']}, updated stopped.")
                return False
        except: None

        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        json_object = json.dumps({"last_update": time_now}, indent=4)
        with open("Backend/Weather/WeatherData/info.json", "w") as outfile: outfile.write(json_object)

        cities = Data.Weather.cities
        city_counter = 0
        for state in cities.keys():
            for city in cities[state]:
                city_counter += 1
                name = f"{city}, {state}"
                table_name = weather.create_table_name(name)
                if state == "Česko":
                    weather_forecast = weather.forecast("cz", name)
                else:
                    raise NotImplementedError
                
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                connection.commit()

                weather_db.create_table(cursor, connection, table_name)

                for record in weather_forecast:
                    weather_db.insert_data(cursor, connection, table_name, record)

                    time.sleep(0.1)

                    max_updates = Data.Weather.max_calls_per_minute*Data.Weather.update_time_minutes
                    if city_counter >= max_updates - (max_updates/100):
                        raise NotImplementedError
        return True

    def search(location:str):
        """
        Returns weather forecast from local database
        """
        location = weather.create_table_name(location)
        connection = sqlite3.connect("Backend/Weather/WeatherData/data.db")
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {location}")
        rows = cursor.fetchall()
        connection.close()

        return rows

    def decode_weather_id(lang:str, id:int):
        return Data.Lang.weather[lang][str(id)]