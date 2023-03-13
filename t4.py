import os

def get_rain_days(file_content):
    rain_days = []
    for row in file_content.split("\n")[1:-1]:
        values = row.split(",")
        event = values[-2]
        date = values[0]
        year, month, day = map(int, date.split("-"))
        if event == "Rain":
            rain_days.append((day, month, year))
    return rain_days

def read_files():
    file_names = os.listdir("weatherfiles")
    rain_days = []
    for file_name in file_names:
        with open(f"weatherfiles/{file_name}", "r") as file_reader:
            file_content = file_reader.read()
            rain_days += get_rain_days(file_content)
    return rain_days

rain_days = read_files()

if rain_days:
    print("Rain Days:")
    for day, month, year in rain_days:
        print(f"{day}/{month}/{year}")
else:
    print("No data available for 'Rain' event.")