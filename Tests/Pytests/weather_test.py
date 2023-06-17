
"""
Pytest for Backend/Weather/weather.py
"""

import sys, os
sys.path.append(f"{os.getcwd()}") #Importing from "Backend/" fix
from Backend.Weather.weather import *

def test_coords():
    data = coords("Louny, Česko")
    assert data == (50.3572914, 13.7969195)

def test_table_name():
    data = weather.create_table_name("Určite pravá-lokace, Česko")
    assert data == "určite_pravá_lokace_česko"

def test_forecast():
    data = weather.forecast("cz", "Louny, Česko")
    assert isinstance(data, list)
    assert len(data) == 40

def test_decoder():
    assert weather.decode_weather_id("cz", 202) == "bouře s prudkým deštěm"