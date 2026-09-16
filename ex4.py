# A string is a SEQUENCE of characters laid out in order. That means you can
# reach into it by position, take slices out of it, and walk through it - the
# same moves you'll use on the guesses in the capstone.

word = "PYTHON"

# Indexing: reach one character by its position.
# Positions start at 0, not 1. So word[0] is the FIRST character.
print(word[0])      # P
print(word[1])      # Y
print(len(word))    # 6 - the number of characters

# A negative index counts from the end: -1 is the last character. 
print(word[-1])     # N

print("---")

# Slicing: take a whole chunk with [start:stop]
# The stop position is NOT included; word[0:3] gives positions 0, 1, and 2. 
print(word[0:3])    # PYT
print(word[3:])     # HON - from position 3 to the end
print(word[:2])     # PY - from the start up to (not including) position 2

print("---")

# enumerate() hands you both at once: the position i and the character itself.
# It's the Pythonic way to loop when you also need the index - cleaner than
# range(len(word)) - and it's the pattern the capstone uses to line two words
# up letter by letter (enumerate one word, index into the other). 
for i, letter in enumerate(word): 
    print(f"Position {i}: {letter}")

print("---")

# A couple of handy string checks
print("PYTHON".isalpha())   # True - is it all letters? 
print("PY3".isalpha())      # False - there's a digit in it
print("H" in word)          # True - is this character present anywhere? 