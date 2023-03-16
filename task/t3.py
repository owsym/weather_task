from utils.read_files import read_files_for_events


unique_events = read_files_for_events()

print("Unique Events For T3")
for event in unique_events:
    print(event)