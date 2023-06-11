
from Backend.core import *
import os, time, multiprocessing, signal

def tester_task():
    while True:
        time.sleep(5*60)
        if not Tests.run(): raise NotImplementedError

def weather_updater_task():
    WEATHER_DELAY = Data.weather.update_time_minutes*60
    time.sleep(10)
    while True:
        report("Updating weather data...")
        start = time.time()
        if weather.update():
            report("Weather data updated successfully.")
        time.sleep(WEATHER_DELAY-(time.time()-start))

def handle_exit(signum, frame):

    #Stop sveltekit
    WEATHER_UPDATER_TASK.kill()

    report(f"\n{colors.WARNING}System stopped successfully.{colors.NORMAL}\n")
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

    tester_task()