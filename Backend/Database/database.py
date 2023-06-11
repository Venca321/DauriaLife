
"""
Dauria life database connector
"""

from Backend.core_helper import *
import mysql.connector, datetime

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

class db_setup():
    def remove_db(sure:bool=False):
        if sure:
            try:
                mydb = mysql.connector.connect(
                    host=HOST,
                    user=USER,
                    password=PASSWORD
                )

                mycursor = mydb.cursor()
                mycursor.execute(f"DROP DATABASE {DATABASE}")
                mydb.close()
            except: None

    def create_db():
        """
        Connect to MySQL and create database
        """
        mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
        )

        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE DATABASE {DATABASE}")
        mydb.close()

    def list_tables():
        cursor, connection = Connection.connect()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        connection.close()

        return tables

    def create_tables():
        """
        Setup all the tables
        """
        cursor, connection = Connection.connect()

        #system_info
        cursor.execute(
        """
        CREATE TABLE system_info ( 
            version VARCHAR(255),
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """
        )

        #users
        cursor.execute(
        """
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255),
            username VARCHAR(255) UNIQUE,
            email VARCHAR(255) UNIQUE,
            password VARCHAR(255),
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        )

        #user_settings
        cursor.execute(
        """
        CREATE TABLE user_settings (
            user_id INT PRIMARY KEY, 
            display_mode VARCHAR(255) DEFAULT "system", 
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        )

        #session_tokens
        cursor.execute(
        """
        CREATE TABLE session_tokens (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            user_id INT, 
            token VARCHAR(255), 
            expiration DATETIME,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        )

        #user_roles
        cursor.execute(
        """
        CREATE TABLE user_roles (
            user_id INT PRIMARY KEY, 
            is_developer BOOLEAN DEFAULT false,
            is_betatester BOOLEAN DEFAULT false,
            priority BOOLEAN DEFAULT false,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        )

        #user_type
        cursor.execute(
        """
        CREATE TABLE user_type (
            user_id INT PRIMARY KEY, 
            type INT DEFAULT 000,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        )

        #calendars
        cursor.execute(
        """
        CREATE TABLE calendars (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            user_id INT, 
            name VARCHAR(255), 
            description VARCHAR(255) NULL, 
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        )

        #events
        cursor.execute(
        """
        CREATE TABLE events (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            calendar_id INT, 
            name VARCHAR(255), 
            description VARCHAR(255) NULL, 
            weather_needed VARCHAR(255) NULL,
            datetime DATETIME,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
            FOREIGN KEY (calendar_id) REFERENCES calendars(id)
        )
        """
        )

        #todo_lists
        cursor.execute(
        """
        CREATE TABLE todo_lists (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            user_id INT, 
            name VARCHAR(255),
            description VARCHAR(255) NULL, 
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        )

        #tasks
        cursor.execute(
        """
        CREATE TABLE tasks (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            list_id INT, 
            name VARCHAR(255), 
            description VARCHAR(255) NULL, 
            weather_needed VARCHAR(255) NULL, 
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
            FOREIGN KEY (list_id) REFERENCES todo_lists(id)
        )
        """
        )

        #notes
        cursor.execute(
        """
        CREATE TABLE notes (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            user_id INT, 
            name VARCHAR(255), 
            note VARCHAR(255) NULL, 
            delete_at DATETIME NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        )

        #weather_recomendations
        cursor.execute(
        """
        CREATE TABLE weather_recomendations (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255),
            description VARCHAR(255),
            weather VARCHAR(255) NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """
        )

        #date_recomendations
        cursor.execute(
        """
        CREATE TABLE date_recomendations (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            user_type INT,
            event_id INT,
            weather_forecast VARCHAR(255),
            calendar_data VARCHAR(255),
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (event_id) REFERENCES events(id)
        )
        """
        )

        connection.close()

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

    class User():
        """
        Manage all user related
        """
        def __init__(self, id:str, name:str, username:str, email:str, password:str, updated_at, created_at):
            #Variables
            self.id = id
            self.name = name
            self.username = username
            self.email = email
            self.password = password
            self.updated_at = updated_at
            self.created_at = created_at

            #Other classes
            self.session_token = self.Session_token(self)
            self.roles = self.Roles(self)
            self.settings = self.Settings(self)
            self.calendar = self.Calendar(self)
            self.todo_list = self.Todo_list(self)
            self.note = self.Note(self)
            self.type = self.Type(self)

        def create(name:str, username:str, email:str, password:str):
            """
            Create new user
            """

            #Validate data

            now = datetime.datetime.now().timestamp()
            #Create user

            id = ""
            
            #Setup everything

            return db.User(id, name, username, email, password, now, now)

        def login(session_token:str):
            """
            Login user using session_token
            """

            #Validate session_token

            #Get user data
            id = ""
            name = ""
            username = ""
            email = ""
            password = ""
            updated_at = ""
            created_at = ""

            return db.User(id, name, username, email, password, updated_at, created_at)
        
        def sign_in(username_or_email:str, password:str):
            """
            Login user - add session token
            """

            #Validate data

            #Get missing data
            id = ""
            name = ""
            username = ""
            email = ""
            updated_at = ""
            created_at = ""

            #Create session_token

            return db.User(id, name, username, email, password, updated_at, created_at)

        def edit(self, name:str=None, username:str=None, email:str=None, password:str=None):
            """
            Edit user
            """

            if not name: name = self.name
            if not username: username = self.username
            if not email: email = self.email
            if not password: password = self.password

            now = datetime.datetime.now().timestamp()
            #Edit user
            id = ""
            created_at = ""

            return db.User(id, name, username, email, password, now, created_at)

        def remove(self):
            """
            Remove user
            """
            pass

        class Session_token():
            """
            Manage session tokens
            """
            def __init__(self, user):
                self.user = user

            def add(self, session_token):
                """
                Add session token
                """
                pass

            def remove(self, session_token):
                """
                Remove session token
                """
                pass

        class Roles():
            """
            Manage user roles
            """
            def __init__(self, user):
                self.user = user

            def get(self):
                """
                Get user roles
                """
                pass

            def edit(self):
                """
                Edit user roles
                """
                pass

            def setup(user_id:str):
                """
                Setup user roles for new user
                """
                pass

            def remove(self):
                """
                Remove on user removal
                """
                pass

        class Settings():
            """
            Manage user settings
            """
            def __init__(self, user):
                self.user = user

            def get(self):
                """
                Get user settings
                """
                pass

            def edit(self):
                """
                Edit user settings
                """
                pass

            def setup(user_id:str):
                """
                Setup setting for new user
                """
                pass

            def remove(self):
                """
                Remove on user removal
                """
                pass

        class Calendar():
            """
            Manage calendar related
            """
            def __init__(self, user):
                self.user = user
                self.event = self.Event(self)

            def get(self):
                """
                Get calendar
                """
                pass

            def edit(self):
                """
                Edit calendar
                """
                pass

            def remove(self):
                """
                Remove calendar
                """
                pass

            class Event():
                """
                Manage events in calendar
                """
                def __init__(self, calendar):
                    self.calendar = calendar

                def get(self):
                    """
                    Get event
                    """
                    pass

                def edit(self):
                    """
                    Edit event
                    """
                    pass

                def remove(self):
                    """
                    Remove event
                    """
                    pass

        class Todo_list():
            """
            Manage user todo_lists
            """
            def __init__(self, user):
                self.user = user

            def get(self):
                """
                Get todo list
                """
                pass

            def edit(self):
                """
                Edit todo list
                """
                pass

            def remove(self):
                """
                Remove todo list
                """
                pass

            class Task():
                """
                Manage tasks in todo list
                """
                def __init__(self, todo_list):
                    self.todo_list = todo_list

                def get(self):
                    """
                    Get task
                    """
                    pass

                def edit(self):
                    """
                    Edit task
                    """
                    pass

                def remove(self):
                    """
                    Remove task
                    """
                    pass

        class Note():
            """
            Manage notes
            """
            def __init__(self, user):
                self.user = user

            def get(self):
                """
                Get note
                """
                pass

            def edit(self):
                """
                Edit note
                """
                pass

            def remove(self):
                """
                Remove note
                """
                pass

        class Type():
            """
            Manage user type
            """
            def __init__(self, user):
                self.user = user

            def get(self):
                """
                Get user type
                """
                pass

            def edit(self):
                """
                Edit user type
                """
                pass

            def setup(user_id:str):
                """
                Setup for new user
                """
                pass

            def remove(self):
                """
                Remove 
                """
                pass

    class Recomendations():
        """
        Manage system recomendations
        """
        pass
    