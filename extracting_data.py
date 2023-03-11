import os


def get_contents_of_one_file(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))

    return file_values


def read_files():
    file_names = os.listdir("weatherfiles")

    # file_reader = open("main.py", "r")
    # file_content = file_reader.read()
    # file_reader.close()

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

min_temp_year = min(Temperatures, key=Temperatures.get)
max_temp_year = max(Temperatures, key=Temperatures.get)

print("Minimum Temperature C :", Temperatures[min_temp_year], "in", min_temp_year)
print("Maximum Temperature C :", Temperatures[max_temp_year], "in", max_temp_year)