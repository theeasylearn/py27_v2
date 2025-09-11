import datetime as dt

print(f"current date and time {dt.datetime.now()}")
print(f"current date {dt.date.today()}")
# print(f"current date {dt.date.nextday()}")
print(f"current year {dt.date.today().year}")
print(f"current month {dt.date.today().month}")
print(f"current day {dt.date.today().day}")
print(f"current date and time {dt.datetime.now().timestamp()}")
print(f"current date and time {dt.datetime.fromtimestamp(1757595955)}")