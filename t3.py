import os

def get_contents_of_one_file(file_content):
    events = set()
    for row in file_content.split("\n")[1:-1]:
        values = row.split(",")
        events.add(values[-2])
    return events

def read_files():
    file_names = os.listdir("weatherfiles")
    unique_events = set()
    for file_name in file_names:
        with open(f"weatherfiles/{file_name}", "r") as file_reader:
            file_content = file_reader.read()
            unique_events |= get_contents_of_one_file(file_content)
    return unique_events

unique_events = read_files()

print("Unique Events:")
for event in unique_events:
    print(event)
