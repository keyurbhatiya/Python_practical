# Write a program in Python to implement readline, readlines, write line and writelines file handling mechanisms.

# Writing 
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.writelines(["This is the second line.\n", "This is the third line.\n", "This is the fourth line.\n"])

# Reading a single line 
with open("example.txt", "r") as file:
    print("Reading one line using readline():")
    print(file.readline())  # Reads the first line

# Reading all lines using
with open("example.txt", "r") as file:
    print("\nReading all lines using readlines():")
    lines = file.readlines()  # Reads all remaining lines into a list
    print(lines)

# Appending a new line using writelines()
with open("example.txt", "a") as file:
    file.writelines(["This is a newly added line.\n"])


with open("example.txt", "r") as file:
    print("\nFinal content of the file:")
    print(file.read())  # Reads the entire file
