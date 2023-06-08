
"""
Pytest for core_helper.py
"""

import sys, os
sys.path.append(f"{os.getcwd()}") #Importing from "Backend/" fix
from Backend.core_helper import *

class Test_loaded_data():
    def test_system(self):
        assert Loaded_data.SYSTEM_DATA

    def test_settings(self):
        #assert Loaded_data.SETTINGS_DATA
        pass

    def test_env(self):
        assert Loaded_data.ENV_DATA

    def test_env(self):
        assert Loaded_data.WEATHER_SETTINGS

class Test_system_data():
    def test_version(self):
        assert isinstance(Data.System.version, str)

    def test_location(self):
        assert isinstance(Data.System.location, str)

class Test_settings():
    def test_open_weather_api_key(self):
        assert isinstance(Data.Settings.open_weather_api_key, str)
    
class Test_database_data():
    def test_version(self):
        assert isinstance(Data.Database.version, str)

    def test_name(self):
        assert isinstance(Data.Database.name, str)

    def test_tables(self):
        assert isinstance(Data.Database.tables, list)

    def test_host(self):
        assert isinstance(Data.Database.host, str)

    def test_user(self):
        assert isinstance(Data.Database.user, str)

    def test_password(self):
        assert isinstance(Data.Database.password, str)

class Test_weather_settings():
    def test_max_calls_per_minute(self):
        assert isinstance(Data.weather.max_calls_per_minute, int)

    def test_update_time_minutes(self):
        assert isinstance(Data.weather.update_time_minutes, int)

    def test_cities(self):
        assert isinstance(Data.weather.cities, dict)