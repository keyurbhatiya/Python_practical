file = open("example.txt", "r")

print("Current Position:", file.tell())  # 0 (beginning of file) 

file.seek(5)  # Move to 5th byte
print("Position after seek:", file.tell())  # 5

file.close()
