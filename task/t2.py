import os

from utils.read_files import read_files


file_values = read_files()

temperatures = {}
for file_value in file_values:
    if file_value and file_value[1]:
        temperatures[file_value[0]] = float(file_value[1])

dates_with_difference_of_7 = set()
for date1, temp1 in temperatures.items():
    for date2, temp2 in temperatures.items():
        if date1 < date2 and abs(temp1 - temp2) == 7:
            dates_with_difference_of_7.add((date1, date2))

if dates_with_difference_of_7:
    print("Dates with a difference of exactly 7 between Min and Max TemperatureC:")
    for date1, date2 in dates_with_difference_of_7:
        print(date1, "and", date2)
else:
    print("No dates found with a difference of exactly 7 between Min and Max TemperatureC.")
