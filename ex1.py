# Python's input() shows a prompt and hands back whatever the user typed,
# ALWAYS as a string (text). Keep that in mind as it causes the classic
# beginner bug we'll see in ex2. 

# input() prints the prompt, waits for the user, and returns the typed text.
name = input("What's your name? ")

# An f-string ("formatted string") lets you drop variables straight into
# text by putting them in {curly braces}. The f before the opening quote
# is what makes it work. Without it, you'd literally print "{name}". 
print(f"Hello, {name}.")

food = input("What's your favorite food: ")

# .lower() returns a lowercased COPY of the string. Strings can't be changed
# in place, so we catch the copy in a variable rather than expecting `food`
# to change on its own. 
food = food.lower()
print(f"Nice, {food} is delicious!")

# len(x) is the length of x. For a string, that's the number of characters. 
print(f"Your name has {len(name)} letters in it.")