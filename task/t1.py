import os
from utils.read_files import read_files


file_values = read_files()

Temperatures = {}
for file_value in file_values:
    if file_value and file_value[1]:
        Temperatures[file_value[0]] = float(file_value[1])

min_temp = None
max_temp = None

for year, temp in Temperatures.items():
    if min_temp is None or temp < min_temp:
        min_temp = temp
        min_temp_year = year

    if max_temp is None or temp > max_temp:
        max_temp = temp
        max_temp_year = year

print("Minimum Temperature C :", min_temp, "in", min_temp_year)
print("Maximum Temperature C :", max_temp, "in", max_temp_year)
