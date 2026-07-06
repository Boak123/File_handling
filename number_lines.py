def number_lines(source, destination):
    with open(source, 'r') as src_file:
        lines = src_file.readlines()
    with open(destination, 'w') as dest_file:
        for i, line in enumerate(lines, start=1):
            dest_file.write(f"{i}: {line}")