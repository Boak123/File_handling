def merge_files(file1, file2, destination):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(destination, 'w') as dest_file:
        content1 = f1.read()
        content2 = f2.read()
        dest_file.write(content1  + content2)