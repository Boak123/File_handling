# Write a function called count_words(filename) that returns the total number of words in a text file. A word is defined as a sequence of characters separated by whitespace.

def count_words(filename):
    with open(filename, "r") as f:
        test = f.read()
        words = test.split()
        return len(words)
    
count = count_words("notes.txt")
print(f"The total number of words in notes.txt is: {count}")