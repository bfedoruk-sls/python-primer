# A function is a named, reusable block of logic. You DEFINE it once with
# `def`, then CALL it as many times as you like. `return` hands a value back
# to whoever called the function. 

def add_up(numbers):
    """Return the sum of a list of numbers."""
    running = 0
    for n in numbers: 
        running = running + n
    return running

# Calling the function. The value it RETURNS is caught in `result`.
result = add_up([2,4,6])
print("Sum:", result)
print("Sum:", add_up([10,20,30,40]))

# A parameter can have a DEFAULT value, used when the caller leaves it out.
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Sam"))             # uses the default greeting "Hello"
print(greet("Sam", "Aloha"))    # overrides the default