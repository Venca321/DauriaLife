
"""
Dauria life database connector

response will be:
<code>, <data?>
"""

from Backend.core_helper import *
import mysql.connector, datetime, string, random

HOST = Data.Database.host
PORT = Data.Database.port
USER = Data.Database.user
PASSWORD = Data.Database.password
DATABASE = Data.Database.name
DEBUG_MODE = Data.Settings.debug_mode

class Connection():
    """
    Database connection manager
    """
    def connect():
        """
        Connect to database
        """
        if DEBUG_MODE: report("Connecting to database...")
        mydb = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        if DEBUG_MODE: report("Connected to database")
        mycursor = mydb.cursor()

        return mycursor, mydb

class db_setup():
    def remove_db(sure:bool=False):
        """
        Remove all database
        """
        if sure:
            if DEBUG_MODE: report("Removing database...")
            try:
                mydb = mysql.connector.connect(
                    host=HOST,
                    port=PORT,
                    user=USER,
                    password=PASSWORD
                )

                mycursor = mydb.cursor()
                mycursor.execute(f"DROP DATABASE {DATABASE}")
                mydb.close()
                if DEBUG_MODE: report("Database removed")
            except: None
        return 200

    def create_db():
        """
        Connect to MySQL and create database
        """
        if DEBUG_MODE: report("Connecting to database...")
        mydb = mysql.connector.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD
        )

        if DEBUG_MODE: report("Connected to database\nCreating database...")

        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE DATABASE {DATABASE}")
        #mycursor.execute("SET GLOBAL time_zone = %s;", ("Europe/Prague",))
        mydb.close()
        if DEBUG_MODE: report("Database created")
        return 200

    def list_tables():
        """
        List all tables in database
        """
        cursor, connection = Connection.connect()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        connection.close()

        return 200, tables

    def create_tables():
        """
        Setup all the tables
        """
        cursor, connection = Connection.connect()

        #system_info
        if DEBUG_MODE: report("Creating system_info table...")
        cursor.execute(
        """
        CREATE TABLE system_info ( 
            version VARCHAR(255),
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """
        )
        db.System_info.edit(Data.Database.version)

        #users
        if DEBUG_MODE: report("Creating users table...")
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
        if DEBUG_MODE: report("Creating user_settings table...")
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
        if DEBUG_MODE: report("Creating session_tokens table...")
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
        if DEBUG_MODE: report("Creating user_roles table...")
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
        if DEBUG_MODE: report("Creating user_type table...")
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
        if DEBUG_MODE: report("Creating calendars table...")
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
        if DEBUG_MODE: report("Creating events table...")
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
        if DEBUG_MODE: report("Creating todo_lists table...")
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
        if DEBUG_MODE: report("Creating tasks table...")
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
        if DEBUG_MODE: report("Creating notes table...")
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
        if DEBUG_MODE: report("Creating weather_recomendations table...")
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
        if DEBUG_MODE: report("Creating date_recomendations table...")
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
        if DEBUG_MODE: report("All tables successfully created!")
        return 200

class db():
    class System_info():
        """
        Manage system info in database
        """
        def get():
            """
            Get system info
            """
            cursor, connection = Connection.connect()
            if DEBUG_MODE: report("Getting system info...")
            cursor.execute("SELECT * FROM system_info")
            data = cursor.fetchall()
            connection.close()
            if DEBUG_MODE: report("System info successfully getted!")
            return 200, data

        def edit(new_version:str):
            """
            Edit system info
            """
            cursor, connection = Connection.connect()

            if DEBUG_MODE: report("Editing system info...")
            cursor.execute("DELETE FROM system_info;")
            cursor.execute(f"INSERT INTO system_info (version) VALUES (%s);", (new_version, ))
            connection.commit()
            connection.close()
            if DEBUG_MODE: report("System info successfully edited!")

            return 200

    class User():
        """
        Manage all user related
        """
        def __init__(self, lang:str, id:str, name:str, username:str, email:str, password:str, updated_at, created_at):
            if DEBUG_MODE: report("Creating user object...")
            #Variables
            self.lang = lang
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
            if DEBUG_MODE: report("User object successfully created!")

        def create(lang:str, name:str, username:str, email:str, password:str):
            """
            Create new user
            """
            cursor, connection = Connection.connect()

            #Validate email
            if DEBUG_MODE: report("Validating email...")
            cursor.execute("SELECT * FROM users WHERE email = %s", (email, ))
            results = cursor.fetchall()
            if results:
                return 400, Data.Lang.database[lang]["1"]

            #Validate username
            if DEBUG_MODE: report("Validating username...")
            cursor.execute("SELECT * FROM users WHERE username = %s", (username, ))
            results = cursor.fetchall()
            if results:
                return 400, Data.Lang.database[lang]["2"]

            #Create user
            if DEBUG_MODE: report("Creating user...")
            cursor.execute(f"INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s);", 
                           (name, username, email, password,))
            connection.commit()

            #Check
            if DEBUG_MODE: report("Checking user...")
            cursor.execute("SELECT * FROM users WHERE username = %s AND email = %s AND password = %s", 
                           (username, email, password, ))
            results = cursor.fetchall()
            if not results: return 400, Data.Lang.database[lang]["3"]
            id = results[0][0]
            now = results[0][-1]
            if DEBUG_MODE: report("User successfully created!")

            #Setup everything
            if DEBUG_MODE: report("Setting up everything...")
            db.User.Roles.setup(id)
            db.User.Settings.setup(id)
            db.User.Type.setup(id)

            connection.close()
            if DEBUG_MODE: report("User successfully setted up!")

            return 200, db.User(lang, id, name, username, email, password, now, now)

        def login(lang:str, session_token:str):
            """
            Login user using session_token
            """
            cursor, connection = Connection.connect()

            #Validate session_token
            if DEBUG_MODE: report("Validating session_token...")
            cursor.execute("SELECT * FROM session_tokens WHERE token = %s", (session_token, ))
            results = cursor.fetchall()
            if not results: return 400, Data.Lang.database[lang]["4"]

            #Get user data
            id = results[0][1]

            #Get rest of data
            if DEBUG_MODE: report("Getting user data...")
            cursor.execute("SELECT * FROM users WHERE id = %s", (id, ))
            results = cursor.fetchall()

            if not results: return 400, Data.Lang.database[lang]["5"]

            name = results[0][1]
            username = results[0][2]
            email = results[0][3]
            password = results[0][4]
            updated_at = results[0][5]
            created_at = results[0][6]

            connection.close()

            if DEBUG_MODE: report("User successfully logged in!")

            return 200, db.User(lang, id, name, username, email, password, updated_at, created_at)
        
        def sign_in(lang:str, username_or_email:str, password:str):
            """
            Login user - add session token
            """
            cursor, connection = Connection.connect()

            #Validate data
            if DEBUG_MODE: report("Validating data...")
            cursor.execute("SELECT * FROM users WHERE (username = %s OR email = %s) AND password = %s", 
                           (username_or_email, username_or_email, password, ))
            results = cursor.fetchall()

            #Get missing data
            if DEBUG_MODE: report("Getting missing data...")
            id = results[0][0]
            expiration = datetime.datetime.now() + datetime.timedelta(days=7)
            
            #Generate token
            if DEBUG_MODE: report("Generating token...")
            while True:
                token = db.User.Session_token.generate(64)
                cursor.execute("SELECT * FROM session_tokens WHERE token = %s", (token, ))
                results = cursor.fetchall()
                if not results: break

            #Create session_token
            if DEBUG_MODE: report("Creating session_token...")
            cursor.execute("INSERT INTO session_tokens (user_id, token, expiration) VALUES (%s, %s, %s);", (id, token, expiration,))
            connection.commit()

            #Check
            if DEBUG_MODE: report("Checking session_token...")
            cursor.execute("SELECT * FROM session_tokens WHERE token = %s", (token, ))
            results = cursor.fetchall()
            if not results: return 400, Data.Lang.database[lang]["3"]

            connection.close()

            if DEBUG_MODE: report("User successfully logged in!")

            return 200, token

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

            return 200, db.User(self.lang, self.id, name, username, email, password, now, self.created_at)

        def remove(self):
            """
            Remove user
            """
            cursor, connection = Connection.connect()

            if DEBUG_MODE: report("Removing user...")
            cursor.execute("DELETE FROM users WHERE id = %s AND username = %s AND password = %s;", 
            #Removing user
                           (self.id, self.username, self.password, ))
            connection.commit()

            if DEBUG_MODE: report("User successfully removed!")
            connection.close()
            return 200

        class Session_token():
            """
            Manage session tokens
            """
            def __init__(self, user):
                self.user = user

            def generate(length:int):
                chars = string.ascii_letters + string.digits
                random_str = ''.join(random.choice(chars) for _ in range(length))
                return random_str

            def remove(self, session_token):
                """
                Remove session token
                """
                raise NotImplementedError

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
                raise NotImplementedError

            def edit(self):
                """
                Edit user roles
                """
                raise NotImplementedError

            def setup(user_id:str):
                """
                Setup user roles for new user
                """
                cursor, connection = Connection.connect()

                #setup
                if DEBUG_MODE: report("Setting up user roles...")

                cursor.execute("INSERT INTO user_roles (user_id, is_developer, is_betatester, priority) VALUES (%s, %s, %s, %s);", 
                               (user_id, False, False, False, ))
                connection.commit()

                if DEBUG_MODE: report("User roles successfully setted up!")
                connection.close()
                return 200

            def remove(self):
                """
                Remove on user removal
                """
                raise NotImplementedError

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
                raise NotImplementedError

            def edit(self):
                """
                Edit user settings
                """
                raise NotImplementedError

            def setup(user_id:str):
                """
                Setup setting for new user
                """
                cursor, connection = Connection.connect()

                #setup
                if DEBUG_MODE: report("Setting up user settings...")

                cursor.execute("INSERT INTO user_settings (user_id) VALUES (%s);", (user_id, ))
                connection.commit()

                if DEBUG_MODE: report("User settings successfully setted up!")
                connection.close()
                return 200

            def remove(self):
                """
                Remove on user removal
                """
                raise NotImplementedError

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
                raise NotImplementedError

            def edit(self):
                """
                Edit calendar
                """
                raise NotImplementedError

            def remove(self):
                """
                Remove calendar
                """
                raise NotImplementedError

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
                    raise NotImplementedError

                def edit(self):
                    """
                    Edit event
                    """
                    raise NotImplementedError

                def remove(self):
                    """
                    Remove event
                    """
                    raise NotImplementedError

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
                raise NotImplementedError

            def edit(self):
                """
                Edit todo list
                """
                raise NotImplementedError

            def remove(self):
                """
                Remove todo list
                """
                raise NotImplementedError

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
                    raise NotImplementedError

                def edit(self):
                    """
                    Edit task
                    """
                    raise NotImplementedError

                def remove(self):
                    """
                    Remove task
                    """
                    raise NotImplementedError

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
                raise NotImplementedError

            def edit(self):
                """
                Edit note
                """
                raise NotImplementedError

            def remove(self):
                """
                Remove note
                """
                raise NotImplementedError

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
                raise NotImplementedError

            def edit(self):
                """
                Edit user type
                """
                raise NotImplementedError

            def setup(user_id:str):
                """
                Setup for new user
                """
                cursor, connection = Connection.connect()

                #setup
                if DEBUG_MODE: report("Setting up user type...")

                cursor.execute("INSERT INTO user_type (user_id) VALUES (%s);", (user_id, ))
                connection.commit()

                if DEBUG_MODE: report("User type successfully setted up!")
                connection.close()
                return 200

            def remove(self):
                """
                Remove 
                """
                raise NotImplementedError

    class Recomendations():
        """
        Manage system recomendations
        """
        pass
    