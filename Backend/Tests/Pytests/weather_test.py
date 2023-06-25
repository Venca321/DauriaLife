
"""
Pytest for Backend/Weather/weather.py
"""

import sys, os
sys.path.append(f"{os.getcwd()}") #Importing from "Backend/" fix
try:
    from Backend.Weather.weather import *
except:
    from Backend.Backend.Weather.weather import *

def test_table_name():
    data = weather.create_table_name("Určite pravá-lokace, Česko")
    assert data == "určite_pravá_lokace_česko"

def test_decoder():
    assert weather.decode_weather_id("cz", 202) == "bouře s prudkým deštěm"