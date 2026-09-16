# The number-one Python beginner bug: input() ALWAYS returns a string, even
# when the user types digits. Watch what has to happen before we can do 
# arithmetic with it. 

reply = input("Enter your score out of 50: ")

# `reply` is a string like "42", NOT the number 42.
# "42" + 1 would crash (you cannot add a number to text)
# int() converts a string of digits into an actual integer.
score = int(reply)

# In Python 3, / always gives a decimal (float) result, so this works
# cleanly even though 50 is a whole number. 
percentage = (score / 50) * 100
print(f"That's a {percentage}%.")

# if / elif / else runs the FIRST branch whose test is True, then stops.
# Order matters: put the more specific test first. 
if percentage >= 90:
    print("Grade A")
elif percentage >= 50:
    print("Grade: Pass")
else:
    print("Grade: Fail")