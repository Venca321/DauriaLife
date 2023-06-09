
from Backend.core_helper import *
import time, requests, mysql.connector

class Core():
    def outputer(output:bool, ON:bool, name:str, function):
        if output: print(f"     {name} ...", end="\r")
        if ON:
            try:
                eval(function)
                if output: print(f"     {name} {'.'*(26-len(name))} {colors.OK}ok{colors.NORMAL}")
            except: 
                print(f"     {name} {'.'*(26-len(name))} {colors.ERROR}error{colors.NORMAL}")
                return False
        elif output: print(f"     {name} {'.'*(26-len(name))} {colors.WARNING}skipped{colors.NORMAL}")

        time.sleep(0.1)
        return True

class Tests():
    def database():
        """
        Tests database
        """
        mydb = mysql.connector.connect(
            host = Data.Database.host,
            user = Data.Database.user,
            password = Data.Database.password,
            database = Data.Database.name
        )

        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")

        tables = mycursor.fetchall()
        needed_tables = Data.Database.tables

        for table in tables:
            try: needed_tables.remove(table[0])
            except: raise
        
        if len(needed_tables) > 0: raise

    def flask():
        url = 'http://localhost:5000/api/version'
        r = requests.get(url)
        if not r.json()["version"] == Data.System.version: raise

    def sveltekit():
        url = 'http://localhost:5173/api/status'
        r = requests.get(url)
        if not r.json()["status"] == "ok": raise

    def overall():
        """
        r = requests.get(f"{ngrok_url}/api/status")
        if not r.json()["status"] == "ok": raise
        """
        pass

    def run(output:bool = False):
        """
        Otestuje funkčnost systému
        """
        DATABASE = False #if False test will be skipped
        FLASK = False
        SVELTEKIT = False
        OVERALL = False

        errors, done_tests = 0, 0
        start = time.time()

        if output: print(f" Testing system:{colors.NORMAL} ")

        time.sleep(0.6) # Tady přidejte delay, pokud mátemálo výkonný systém

        #Database_connection
        if not Core.outputer(output, DATABASE, "Database server", "Tests.database()"):
            errors += 1
        done_tests += 1

        #Flask
        if not Core.outputer(output, FLASK, "Flask server", "Tests.flask()"):
            errors += 1
        done_tests += 1

        #Sveltekit
        if not Core.outputer(output, SVELTEKIT, "Sveltekit server", "Tests.sveltekit()"):
            errors += 1
        done_tests += 1

        #Sveltekit přes ngrok
        if not Core.outputer(output, OVERALL, "Overall server", "Tests.overall()"):
            errors += 1
        done_tests += 1

        if output: 
            print(f"\n Run {done_tests} tests in {int((time.time()-start)*1000)/1000}s")
            if errors == 0: 
                print(f" {colors.BOLD}Status:{colors.NORMAL} {colors.OK}OK{colors.NORMAL}")
                print("\n---------------------------------------------------------------------------------------\n")
                time.sleep(0.1)
                print(f" {colors.BOLD}Sveltekit running on{colors.NORMAL} ........ {colors.OK}http://localhost:5173/{colors.NORMAL}")
                print("\n---------------------------------------------------------------------------------------\n")

            else: print(f" {colors.BOLD}Status:{colors.NORMAL} {colors.ERROR}System error ({errors}){colors.NORMAL}\n")

        if errors == 0: return True #System ok
        else: return False #System error