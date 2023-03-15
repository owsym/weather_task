from utils.read_files import read_files_t2

file_values = read_files_t2()

temperatures = []
for file_value in file_values:
    if file_value and len(file_value) >= 4 and file_value[1] and file_value[3]:
        date = file_value[0]
        min_temp = int(file_value[3])
        max_temp = int(file_value[1])
        temperatures.append({'date': date, 'min_temp': min_temp, 'max_temp': max_temp})

# Filter dates with a difference of exactly 7 between min and max temp
filtered_temperatures = []
for temp in temperatures:
    if abs(temp['max_temp'] - temp['min_temp']) == 7:
        filtered_temperatures.append(temp)

# Print filtered dates in desired format
if filtered_temperatures:
    print("Dates with a difference of exactly 7 between Min and Max TemperatureC:")
    for temp in filtered_temperatures:
        print(f"Date: {temp['date']}, Max TemperatureC: {temp['max_temp']}, Min TemperatureC: {temp['min_temp']}")
else:
    print("No dates found with a difference of exactly 7 between Min and Max TemperatureC.")
