
from Backend.core import *
import os, time, multiprocessing

def tester_task():
    while True:
        time.sleep(5*60)
        if not Tests.run(): raise

def weather_updater_task():
    WEATHER_DELAY = Data.weather.update_time_minutes*60
    time.sleep(10)
    while True:
        start = time.time()
        weather.update()
        time.sleep(WEATHER_DELAY-(time.time()-start))

if __name__ == "__main__":
    os.system("clear")

    print("\n---------------------------------------------------------------------------------------")
    print(f"\n\n{' '*22}{colors.BOLD}DauriaLife smart calendar system ({Data.System.version})\n{' '*34}© Václav Parma{colors.NORMAL}\n\n")
    print("---------------------------------------------------------------------------------------\n")

    time.sleep(0.2)
    if not Tests.run(True): exit()
    time.sleep(0.5)

    #multiprocessing
    multiprocessing.Process(target=weather_updater_task, daemon=True).start()
    tester_task()