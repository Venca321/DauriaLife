
"""
Pytest for Backend/core.py
"""

import sys, os
sys.path.append(f"{os.getcwd()}") #Importing from "Backend/" fix
from Backend.core import *

class Test_imports():
    def test_core_helper(self):
        Data.System()
        
    def test_database(self):
        db()