
"""
All core function to avoid cross referencing
"""

import json, dotenv, os

class Loaded_data():
    SYSTEM_DATA = json.load(open(f"{os.getcwd()}/Data/System/system.json"))
    SETTINGS_DATA = json.load(open(f"{os.getcwd()}/Data/Settings/settings.json"))
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
        pass

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