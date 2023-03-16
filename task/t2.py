import os
from utils.read_files import read_files

file_values = read_files()

temperatures = {}
for file_value in file_values:
    if file_value and file_value[1]:
        temperatures[file_value[0]] = {"max_temp": float(file_value[1]), "min_temp": float(file_value[3])}

dates_with_difference_of_7 = set()
for date1, temp1 in temperatures.items():
    for date2, temp2 in temperatures.items():
        if date1 < date2 and abs(temp1["max_temp"] - temp2["min_temp"]) == 7:
            dates_with_difference_of_7.add((date1, date2))

if dates_with_difference_of_7:
    print("Dates with a difference of exactly 7 between Max and Min TemperatureC:")
    for date1, date2 in dates_with_difference_of_7:
        print("Date:", date1, ", Max TemperatureC:", temperatures[date1]["max_temp"], ", Min TemperatureC:", temperatures[date2]["min_temp"])
else:
    print("No dates found with a difference of exactly 7 between Max and Min TemperatureC.")
