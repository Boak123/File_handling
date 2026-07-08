def remove_duplicate_lines(source, destination):
    with open(source, 'r') as src_file:
        seen = set()
        unique_lines = []
        Lines = src_file.readlines()
        for line in Lines:
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)
    with open(destination, 'w') as dest_file:
        dest_file.writelines(unique_lines)

remove_duplicate_lines("notes.txt", "destination.txt")