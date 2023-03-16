import os
from utils.read_files import read_files_for_rain_days

rain_days = read_files_for_rain_days()


print("Rain Days:")
for day, month, year in rain_days:
    print(f"{day}/{month}/{year}")