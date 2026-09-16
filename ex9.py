# Some errors are bugs you fix. Others you can't prevent - like a user typing
# letters when you asked for a number. For those, Python lets you CATCH the
# error and respond, instead of letting the program crash. 

# Left unguarded, this line crashes if the user doesn't type digits:
#    number = int(input("A number? "))      # ValueError if they type "ten"

# `try` runs the risky code. If it raises an error, the matching `except`
# runs instead - and the program carries on.

reply = input("Enter a whole number: ")
try: 
    number = int(reply)
    print(f"Thanks - double your number is {number * 2}.")
except ValueError:
    # This runs ONLY if int() failed.
    print("That wasn't a whole number.")

print("The program keeps running either way.")

print("---")

# A very common pattern: keep asking until the input is valid. This is the
# polished version of the capstone's "Please enter a five-letter word" check.
while True:
    reply = input("Enter a number from 1 to 10: ")
    try:
        n = int(reply)
    except ValueError: 
        print("Not a number - try again.")
        continue        # jump back to the top and re-ask
    if 1 <= n <= 10:
        break
    print("Out of range - try again.")

print(f"Got a valid number: {n}")