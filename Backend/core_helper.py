
"""
All core function to avoid cross referencing
"""

import json, dotenv, os, datetime

def report(text:str):
    """
    Prints text with time info
    """
    time = datetime.datetime.now().strftime("%H:%M:%S")
    if text.startswith("\n"):
        text = text.replace("\n", "")
        print(f"\n[{time}] {text}")
    else:
        print(f"[{time}] {text}")

class colors():
    BOLD = '\033[1m'
    OK = f'{BOLD}\033[92m'
    WARNING = f'{BOLD}\033[93m'
    ERROR = f'{BOLD}\033[91m'
    NORMAL = '\033[0m'

class Loaded_data():
    SYSTEM_DATA = json.load(open(f"{os.getcwd()}/Data/System/system.json"))
    SETTINGS_DATA = json.load(open(f"{os.getcwd()}/Data/Settings/settings.json"))
    WEATHER_SETTINGS = json.load(open(f"{os.getcwd()}/Data/System/weather.json"))
    ENV_DATA = dotenv.dotenv_values(f"{os.getcwd()}/Data/Settings/.env")

class Data():
    """
    All data needed for system
    """
    class System():
        """
        System data
        """
        version:str = "PRE V.0.0"
        location:str = f"{os.getcwd()}"

    class Settings():
        """
        System settings
        """
        try: open_weather_api_key:str = os.environ["OPEN_WEATHER_API_KEY"]
        except: open_weather_api_key:str = Loaded_data.ENV_DATA["OPEN_WEATHER_API_KEY"]
        debug_mode:bool = Loaded_data.SETTINGS_DATA["debug_mode"]

    class Database():
        """
        Database data
        """
        version:str = Loaded_data.SYSTEM_DATA["database"]["version"]
        name:str = Loaded_data.SYSTEM_DATA["database"]["name"]
        tables:list = Loaded_data.SYSTEM_DATA["database"]["tables"]
        try:
            host:str = os.environ["DATABASE_HOST"]
            port:int = int(os.environ["DATABASE_PORT"])
            user:str = os.environ["DATABASE_USER"]
            password:str = os.environ["DATABASE_PASSWORD"]
        except:
            host:str = Loaded_data.ENV_DATA["DATABASE_HOST"]
            port:int = int(Loaded_data.ENV_DATA["DATABASE_PORT"])
            user:str = Loaded_data.ENV_DATA["DATABASE_USER"]
            password:str = Loaded_data.ENV_DATA["DATABASE_PASSWORD"]

    class Weather():
        """
        Weather settings
        """
        max_calls_per_minute:int = Loaded_data.WEATHER_SETTINGS["max_calls_per_minute"]
        update_time_minutes:int = Loaded_data.WEATHER_SETTINGS["update_time_minutes"]
        cities:dict = Loaded_data.WEATHER_SETTINGS["cities"]

    class Lang():
        database:dict = {"cz": json.load(open(f"{os.getcwd()}/Data/Language/cz/database.json"))}
        weather:dict = {"cz": json.load(open(f"{os.getcwd()}/Data/Language/cz/weather.json"))}
