# Write a function named count_characters(filename) that returns the total number of characters in a file, including spaces and newline (\n) characters.

def count_characters(filename):
    with open(filename, "r") as f:
        content = f.read()
        return len(content)
    
count = count_characters("notes.txt")
print(f"The total number of characters in notes.txt is: {count}")