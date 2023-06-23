
from Backend.core import *
import os, time, multiprocessing, signal, sys

DEBUG_MODE = Data.Settings.debug_mode

def console_task():
    if DEBUG_MODE: report("Started console")
    while True:
        user_input = input("")
        sys.stdout.write("\033[F")
        print(f">>> {user_input}")
        if user_input == "exit" or user_input == "stop": handle_exit(None, None)
        else: 
            response = process(user_input)
            if response:
                report(response)

def tester_task():
    if DEBUG_MODE: report("Started automatic testing")
    while True:
        time.sleep(5*60)
        if not Tests.run():
            report(f"{colors.ERROR}Tests failed. Stopping system...")
            handle_exit(None, None)

def weather_updater_task():
    if DEBUG_MODE: report("Started weather updater")
    WEATHER_DELAY = Data.Weather.update_time_minutes*60
    time.sleep(10)
    while True:
        if DEBUG_MODE: report("Updating weather data...")
        start = time.time()
        if weather.update():
            if DEBUG_MODE: report("Weather data updated successfully.")
        time.sleep(WEATHER_DELAY-(time.time()-start))

def handle_exit(signum, frame):
    #Stop sveltekit
    WEATHER_UPDATER_TASK.kill()
    TESTER_TASK.kill()

    report(f"{colors.WARNING}System stopped successfully.{colors.NORMAL}\n")
    os._exit(1)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler=handle_exit)
    os.system("clear")

    print("\n---------------------------------------------------------------------------------------")
    print(f"\n\n{' '*22}{colors.BOLD}DauriaLife smart calendar system ({Data.System.version})\n{' '*34}© Václav Parma{colors.NORMAL}\n\n")
    print("---------------------------------------------------------------------------------------\n")

    time.sleep(0.2)
    if not Tests.run(True): exit()
    time.sleep(0.5)

    #Weather update task
    WEATHER_UPDATER_TASK = multiprocessing.Process(target=weather_updater_task, daemon=True)
    WEATHER_UPDATER_TASK.start()

    #Tester task
    TESTER_TASK = multiprocessing.Process(target=tester_task, daemon=True)
    TESTER_TASK.start()

    console_task()