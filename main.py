
from Backend.core import *
import os, time

if __name__ == "__main__":
    os.system("clear")

    print("\n---------------------------------------------------------------------------------------")
    print(f"\n\n{' '*22}{colors.BOLD}DauriaLife smart calendar system ({Data.System.version})\n{' '*34}© Václav Parma{colors.NORMAL}\n\n")
    print("---------------------------------------------------------------------------------------\n")

    time.sleep(0.2)
    if not Tests.run(True): exit()
    time.sleep(0.5)

    #multiprocessing