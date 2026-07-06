"""Write a function:
It should:

Read the contents of the source file.
Create (or overwrite) the destination file.
Write the exact same contents into the destination file.
"""

def copy_file(source, destination):
    with open(source, 'r') as src_file:
        contents = src_file.read()
    with open(destination, 'w') as dest_file:
        dest_file.write(contents)

copy_file('notes.txt', 'destination.txt')