import os

#All files content reading function
def get_contents_of_one_file(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))
    return file_values

#Content reading function for t1
def read_files_t1():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_names = os.listdir(os.path.join(dir_path, '..', 'weatherfiles'))
    file_values = []

    for file_name in file_names:
        with open(os.path.join(dir_path, '..', 'weatherfiles', file_name), "r") as file_reader:
            file_content = file_reader.read()
            file_values += get_contents_of_one_file(file_content)
    return file_values

#Content reading function for t2
def read_files_t2():
    dir_path = os.path.dirname( os.path.realpath( __file__ ) )
    file_names = os.listdir( os.path.join( dir_path, '..', 'weatherfiles' ) )
    file_values = []

    for file_name in file_names:
        with open( os.path.join( dir_path, '..', 'weatherfiles', file_name ), "r" ) as file_reader:
            file_content = file_reader.read()
            file_values += get_contents_of_one_file(file_content)
    return file_values