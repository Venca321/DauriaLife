
from Backend.core import *
import os, time, multiprocessing

DEBUG_MODE = Data.Settings.debug_mode

def tester_task():
    while True:
        time.sleep(5*60)
        if not Tests.run():
            report(f"{colors.ERROR}Tests failed. Stopping system...")
            exit()

def weather_updater_task():
    WEATHER_DELAY = Data.Weather.update_time_minutes*60
    time.sleep(10)
    while True:
        if DEBUG_MODE: report("Updating weather data...")
        start = time.time()
        if weather.update():
            if DEBUG_MODE: report("Weather data updated successfully.")
        time.sleep(WEATHER_DELAY-(time.time()-start))

if __name__ == "__main__":
    os.system("clear")

    print("\n---------------------------------------------------------------------------------------")
    print(f"\n\n{' '*22}{colors.BOLD}DauriaLife smart calendar system ({Data.System.version})\n{' '*34}© Václav Parma{colors.NORMAL}\n\n")
    print("---------------------------------------------------------------------------------------\n")

    #Flask task
    FLASK_TASK = multiprocessing.Process(target=flask_task, daemon=True)
    FLASK_TASK.start()

    #Weather update task
    WEATHER_UPDATER_TASK = multiprocessing.Process(target=weather_updater_task, daemon=True)
    WEATHER_UPDATER_TASK.start()

    if not Tests.run(True): exit()

    tester_task()

