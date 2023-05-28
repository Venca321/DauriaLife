
"""
Creates all needed (installs requerements, creates folders...)
"""

import os, shutil

#Setup
os.system('pip install -r requirements.txt')
#os.chdir("Frontend")
#os.system("npm install")
#os.chdir("../")

#Make folders
FOLDERS = []
for folder in FOLDERS:
    try: os.mkdir(folder)
    except: None

#Copy files
shutil.copy("Data/Defaults/.env.example", "Data/Settings/.env")
shutil.copy("Data/Defaults/default_settings.json", "Data/Settings/settings.json")