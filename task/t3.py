from utils.read_files import get_content_for_t3_event


unique_events = get_content_for_t3_event()

print("Unique Events For T3")
for event in unique_events:
    print(event)