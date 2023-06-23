
"""
Core of system, import this to get all needed
"""

from Backend.core_helper import *

from Tests.Tester.tester import Tests
from Backend.Engine.engine import Engine

from Frontend.main import sveltekit, start_server
from Backend.Console.console import process
from Backend.Database.database import db, db_setup
from Backend.Weather.weather import weather