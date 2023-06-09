
"""
All core function to avoid cross referencing
"""

import json, dotenv, os

class Loaded_data():
    SYSTEM_DATA = json.load(open(f"{os.getcwd()}/Data/System/system.json"))
    SETTINGS_DATA = json.load(open(f"{os.getcwd()}/Data/Settings/settings.json"))
    ENV_DATA = dotenv.dotenv_values(f"{os.getcwd()}/Data/Settings/.env")
    WEATHER_SETTINGS = json.load(open(f"{os.getcwd()}/Data/System/weather.json"))

class colors():
    BOLD = '\033[1m'
    OK = f'{BOLD}\033[92m'
    WARNING = f'{BOLD}\033[93m'
    ERROR = f'{BOLD}\033[91m'
    NORMAL = '\033[0m'

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
        open_weather_api_key:str = Loaded_data.ENV_DATA["open_weather_api_key"]

    class Database():
        """
        Database data
        """
        version:str = Loaded_data.SYSTEM_DATA["database"]["version"]
        name:str = Loaded_data.SYSTEM_DATA["database"]["name"]
        tables:list = Loaded_data.SYSTEM_DATA["database"]["tables"]
        host:str = Loaded_data.ENV_DATA["database_host"]
        user:str = Loaded_data.ENV_DATA["database_user"]
        password:str = Loaded_data.ENV_DATA["database_password"]

    class weather():
        """
        Weather settings
        """
        max_calls_per_minute:int = Loaded_data.WEATHER_SETTINGS["max_calls_per_minute"]
        update_time_minutes:int = Loaded_data.WEATHER_SETTINGS["update_time_minutes"]
        cities:dict = Loaded_data.WEATHER_SETTINGS["cities"]
