
"""
Engine module for the smart callendar system
"""

from Backend.core import *

class Engine():
    class UserType():
        def process(user:db.User):
            pass

    class Recommendations():
        class Weather():
            def train():
                pass

            def recommend():
                pass

        class Datetime():
            def train():
                pass

            def recommend():
                pass