# So far every value has lived only while the program runs, then vanished. 
# Files let you save data to disk and read it back later. open() gives you a
# file object; the `with` block automatically closes the file whjen you're
# done, even if something goes wrong. 

# Writing to a file
# "w" is write mode: it creates the file, or empties it if it already exists.
with open("notes.txt", "w") as file:
    file.write("apple\n")   #\n is a newline - it puts each word on its own line
    file.write("banana\n")
    file.write("cherry\n")
    file.write("durian\n")

# Reading a file line by line
# "r" is read mode. Looping over a file object hands you one line at a time. 
with open("notes.txt", "r") as file:
    for line in file:
        # Each line still carries its trailing newline. .strip() removes
        # surrounding whitespace, including that \n.
        print("Read:", line.strip())

print("---")

# Reading a whole file into a list
# A very common pattern: turn every line into a clean item in a list. This is
# exactly how the capstone will load its word list. 
words = []
with open("notes.txt", "r") as file: 
    for line in file:
        words.append(line.strip())

print(words)        # ['apple', 'banana', 'cherry', 'durian']
print("Lines read:", len(words))