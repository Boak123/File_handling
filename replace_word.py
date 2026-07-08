def replace_word(source, destination, old_word, new_word):
    with open(source, 'r') as src_file:
        content = src_file.read()
        updated_content = content.replace(old_word, new_word)
    with open(destination, 'w') as dest_file:
        dest_file.write(updated_content)

replace_word("notes.txt", "destination.txt", "Python", "Java")