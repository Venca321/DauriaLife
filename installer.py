
"""
Creates all needed (installs requerements, creates folders...)
"""

import os, shutil

#Setup
os.system('pip install -r requirements.txt')
os.chdir("Frontend")
os.system("npm install")
os.chdir("../")

#Make folders
LOCATION = os.getcwd()
FOLDERS = ["Data/Settings", "Backend/Weather/WeatherData"]
for folder in FOLDERS:
    try: os.mkdir(f"{LOCATION}/{folder}")
    except: None

#Copy files
shutil.copy(f"{LOCATION}/Data/Defaults/.env.example", f"{LOCATION}/Data/Settings/.env")
shutil.copy(f"{LOCATION}/Data/Defaults/default_settings.json", f"{LOCATION}/Data/Settings/settings.json")