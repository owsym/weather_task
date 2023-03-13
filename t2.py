import os

def get_contents_of_one_file(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))
    return file_values

def read_files():
    file_names = os.listdir("weatherfiles")
    file_values = []
    for file_name in file_names:
        with open(f"weatherfiles/{file_name}", "r") as file_reader:
            file_content = file_reader.read()
            file_values += get_contents_of_one_file(file_content)
    return file_values

file_values = read_files()

Temperatures = {}
for file_value in file_values:
    if file_value and file_value[1]:
        Temperatures[file_value[0]] = float(file_value[1])

dates_with_difference_of_7 = set()
for date1, temp1 in Temperatures.items():
    for date2, temp2 in Temperatures.items():
        if date1 < date2 and abs(temp1 - temp2) == 7:
            dates_with_difference_of_7.add((date1, date2))

if dates_with_difference_of_7:
    print("Dates with a difference of exactly 7 between Min and Max TemperatureC:")
    for date1, date2 in dates_with_difference_of_7:
        print(date1, "and", date2)
else:
    print("No dates found with a difference of exactly 7 between Min and Max TemperatureC.")
