"""
Write a function:


It should:

Read the file.
Check whether the given word exists.
Return True if found, otherwise False.
"""

def find_word(filename, word):
    with open(filename, "r") as f:
        content = f.read().lower()
        word = word.lower()
        if word in content:
            return True
        else:
            return False
        
count = find_word("notes.txt", "Python")
print(f"The word 'Python' exists in notes.txt: {count}")