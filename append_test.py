"""
Write a program that:

Asks the user to enter a sentence.
Appends that sentence to the end of notes.txt.
Ensures each new sentence starts on a new line.
"""
sentence = input("Enter a sentence: ")

with open("notes.txt", "a") as f:
    f.write("\n" + sentence)
