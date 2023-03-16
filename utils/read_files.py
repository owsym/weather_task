import os

#this function work for t1 and t2
def get_contents_of_one_file(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))

    return file_values

#this function work for t1
def read_files():
    dir_path = os.path.dirname(os.path.realpath("weathe_task.weatherfiles/"))
    weatherfiles_path = os.path.join(dir_path, '..', 'weatherfiles')
    file_names = os.listdir(weatherfiles_path)
    file_values = []

    for file_name in file_names:
        with open(os.path.join(weatherfiles_path, file_name), "r") as file_reader:
            file_content = file_reader.read()
            file_values += get_contents_of_one_file(file_content)
    return file_values



#this function work for t2

def read_files_for_t2():
    dir_path = os.path.dirname(os.path.realpath("weathe_task.weatherfiles/"))
    weatherfiles_path = os.path.join(dir_path, '..', 'weatherfiles')
    file_names = os.listdir(weatherfiles_path)
    file_values = []

    for file_name in file_names:
        with open(os.path.join(weatherfiles_path, file_name), "r") as file_reader:
            file_content = file_reader.read()
            file_values += get_contents_of_one_file(file_content)
            file_reader.close()
    return file_values



#this function work for t3
def get_contents_for_events(file_content):
    file_values = set()
    for row in file_content.split("\n")[1:-1]:
        values = row.split(",")
        file_values.add(values[-2])
    return file_values

#this function work for t3
def read_files_for_events():
    dir_path = os.path.dirname(os.path.realpath("weathe_task.weatherfiles/"))
    weatherfiles_path = os.path.join(dir_path, '..', 'weatherfiles')

    file_names = os.listdir(weatherfiles_path)

    file_values = set()
    for file_name in file_names:
        with open(os.path.join(weatherfiles_path, file_name), "r") as file_reader:
            file_content = file_reader.read()
            file_values |= get_contents_for_events(file_content)
            file_reader.close()
    return file_values

#this function work for t4
def get_rain_days(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        values = row.split(",")
        event = values[-2]
        date = values[0]
        year, month, day = map(int, date.split("-"))
        if event == "Rain":
            file_values.append((day, month, year))
    return file_values

#this function work for t4
def read_files_for_rain_days():
    dir_path = os.path.dirname(os.path.realpath("weathe_task.weatherfiles/"))
    weatherfiles_path = os.path.join(dir_path, '..', 'weatherfiles')
    file_names = os.listdir(weatherfiles_path)
    file_values = []

    for file_name in file_names:
        with open(os.path.join(weatherfiles_path, file_name), "r") as file_reader:
            file_content = file_reader.read()
            file_values += get_rain_days(file_content)
            file_reader.close()
    return file_values