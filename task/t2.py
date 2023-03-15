from utils.read_files import read_files_t2

file_values = read_files_t2()

temperatures = {}
for file_value in file_values:
    if file_value and len(file_value) >= 4 and file_value[1] and file_value[3]:
        min_temp = float(file_value[3])
        max_temp = float(file_value[1])
        avg_temp = (min_temp + max_temp) / 2
        temperatures[file_value[0]] = avg_temp

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