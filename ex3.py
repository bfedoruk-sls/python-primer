# Two loops cover almost everything: `for` when you know what you're looping
# over, and `while` when you loop until some condition changes.

fruits = ["apple", "banana", "cherry", "durian"]

# A `for` loop over a list visits each item in turn. This is the Python
# mental-model shift: you loop over the ITEMS themselves, not over a counter
# that you use to index in. Read it as "for each fruit in fruits". 
for fruit in fruits: 
    print(f"I have a {fruit}.")

print("---")

# When you genuinely need counting, range(n) produces 0, 1, ..., n-1. 
for n in range(5):
    # range starts at 0, so add 1 for a human-friendly count. 
    print(f"Count: {n+1}")

print("---")

# A `while` loop runs as long as its condition stays True. Here we use it to
# add up the numbers 1 to 5. `total` is an accumulator: a variable that
# builds up a result across the loop. 
total = 0
number = 1
while number <= 5:
    total = total + number
    number = number + 1 # without this line the loop would never end! 
print(f"The numbers 1 to 5 add up to {total}.")

print("---")

# `break` stops the loop immediately. `continue` skips the rest of THIS pass
# and jumps straight to the next one. Both turn up in the capstone. 
for n in range(1,10):
    if n == 5:
        break               # stop the moment we reach 5
    print("Counting:", n)   # prints 1,2,3,4    

print("- - -")

for n in range(1,6):
    if n == 3:
        continue            # skip 3, but keep looping
    print("Keeping:", n)    # prints 1,2,4,5