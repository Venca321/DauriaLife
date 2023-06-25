
import csv, os, datetime, random

location = "Working/"
f = open(f'{location}data/calendar-recomendation.csv', 'w')
writer = csv.writer(f)

"""
user = typ uživatele
calendar = co už je v kalendáři (od, do, počasí)
activity = začátek, konec, počasí potřeba
weather_forecast = předpověď počasí

added = kdy to teda bylo přidáno
"""

header = ['user_type', 'calendar', 'activity', 'weather_forecast', "added_to"]
writer.writerow(header)

def random_user():
    num = 0
    text = ""
    return num, text

def populate_calendar(need_to_be_done_in):
    calendar = {}
    for day in range(need_to_be_done_in):
        date = str(today+datetime.timedelta(days=day))
        calendar[date] = []

        last_added = [6, 0]
        for _ in range(random.randint(0, 5)):
            start = [(last_added[0]+random.randint(0, 3)), (last_added[1]+random.randint(0, 60))]
            if start[1] > 60: start = [start[0]+1, start[1]-60]
            end = [(start[0]+random.randint(0, 5)), (start[1]+random.randint(0, 60))]
            if end[1] > 60: end = [end[0]+1, end[1]-60]
            last_added = end

            if not (start[0] > 20 or end[0] > 21):
                calendar[date] = calendar[date] + [{"start": f"{start[0]}:{start[1]}", "end": f"{end[0]}:{end[1]}"}]
    return calendar

def random_weather():
    pass

def random_activity():
    return

while True:
    os.system("clear")

    today = datetime.date.today()
    need_to_be_done_in = random.randint(1, 10)
    calendar = populate_calendar(need_to_be_done_in)

    print("Uživatel:")
    user_type, user_description = random_user()
    print(user_description)

    print("\nKalendář:")
    num = 0
    for date in calendar.keys():
        print(f"    {date} ({num}):")
        for event in calendar[date]:
            print(f"        {event}")
        num += 1

    print("\nPředpověď počasí:")

    print("\nAdktivita:")

    voted = input("\nKterý den si to dáte do kalendáře? ")
    if voted.lower() == "exit": break

    voted_date = list(calendar.keys())[int(voted)]

    data = [user_type, calendar, voted_date]
    writer.writerow(data)

f.close()
