# Lists and dicts are Python's two workhorse containers.

# Lists: an ordered collection you can grow.
scores = [88, 92, 75]

print("First score:", scores[0])       # index 0 is the FIRST item, not 1
print("How many:", len(scores))

scores.append(100)                      # add a new item onto the end
print("After adding:", scores)

# `in` asks whether something is present
print("Is 92 there?", 92 in scores)
print("Is 90 there?", 90 in scores)

print("---")

# Dicts: look things up by a KEY instead of a position
capitals = {"Canada": "Ottawa", "France": "Paris", "Egypt": "Cairo"}

print("Capiutal of Canada:", capitals["Canada"])

capitals["Japan"] = "Tokyo"     # add a new key -> value pair
print(capitals)

print("---")

# The counting pattern: how many times does each item appear? 
# This little idiom shows up constantly: A dict maps each word to its count.
sentence = "the cat sat on the mat"
counts = {}                         # start with an empty dictionary

for word in sentence.split():       # .split() breaks text into a list of words. 
    # counts.get(word, 0) returns the current count, or 0 if we haven't 
    # seen this word yet. Then we add one and store it back.
    counts[word] = counts.get(word, 0) + 1

print(counts)       # {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}