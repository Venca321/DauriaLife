
"""
Creates all needed (installs requerements, creates folders...)
"""

import os, shutil

#Setup
try: os.system('pip install -r requirements.txt')
except: os.system('pip install -r Backend/requirements.txt')

#Make folders
LOCATION = os.getcwd()
FOLDERS = ["Data/Settings", "Backend/Weather/WeatherData"]
for folder in FOLDERS:
    try: os.mkdir(f"{LOCATION}/{folder}")
    except: None

#Copy files
import dotenv
try:
    #if .env doesn't exist, create it
    values = dotenv.dotenv_values(f"{LOCATION}/Data/Settings/.env")
    needed_values = dotenv.dotenv_values(f"{LOCATION}/Data/Defaults/.env.example")
    for key in needed_values:
        if not key in values:
            raise
except:
    shutil.copy(f"{LOCATION}/Data/Defaults/.env.example", f"{LOCATION}/Data/Settings/.env")

#if settings.json doesn't exist, create it
if not os.path.exists(f"{LOCATION}/Data/Settings/settings.json"):
    shutil.copy(f"{LOCATION}/Data/Defaults/default_settings.json", f"{LOCATION}/Data/Settings/settings.json")