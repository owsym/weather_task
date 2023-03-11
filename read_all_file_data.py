import os


dir_path = '/home/owsym/Project/Python/WeatherMan/weatherfiles/'

# Loop through each file in the directory
for filename in os.listdir(dir_path):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        # Open the file in read mode
        with open(os.path.join(dir_path, filename), 'r') as file:
            # Read the contents of the file
            contents = file.read()
            # Print the contents of the file
            print(f"Contents of {filename}:")
            print(contents)