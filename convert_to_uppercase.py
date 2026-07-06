def convert_to_uppercase(source, destination):
    with open(source, 'r') as src_file:
        contents = src_file.read()
    with open(destination, 'w') as dest_file:
        dest_file.write(contents.upper())

convert_to_uppercase('notes.txt', 'destination.txt')