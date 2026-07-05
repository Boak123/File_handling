
# Write a function that returns the number of lines in a text file.
def count_lines(filename):
    with open(filename, "r") as f:
        count = 0
        for line in f:
            count += 1
    return count

count = count_lines("notes.txt")
print(f"The number of lines in notes.txt is: {count}")
# Write a function that returns the number of lines in a text file.
def count_lines(filename):
    with open(filename, "r") as f:
        count = 0
        for line in f:
            count += 1
    return count

count = count_lines("notes.txt")

print(f"The number of lines in notes.txt is: {count}")