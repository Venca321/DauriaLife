
"""
Dauria life database connector
"""

from Backend.core_helper import *
import mysql.connector

HOST = Data.Database.host
USER = Data.Database.user
PASSWORD = Data.Database.password
DATABASE = Data.Database.name

class Connection():
    """
    Database connection manager
    """
    def connect():
        """
        Connect to database
        """
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        mycursor = mydb.cursor()

        return mycursor, mydb
    
    def close(mydb):
        """
        Close connection to database
        """
        mydb.close()

class db():
    class System_info():
        """
        Manage system info in database
        """
        def get():
            """
            Get system info
            """
            pass

        def edit():
            """
            Edit system info
            """
            pass

    