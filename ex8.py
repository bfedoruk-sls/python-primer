# A class is a blueprint. It bundles related DATA (attributes) together with
# the FUNCTIONS that act on that data (methods). 

class BankAccount:
    # __init__ runs automatically the moment you create a BankAccount. Its
    # job is to set up the object's starting data. `self` refers to the 
    # particular object being built - each account gets its own separate self.

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = [] # this account's own (empty) list.

    # A method is just a function that lives inside the class. Its first
    # parameter is always `self`, the object it was called on.
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.history.append(amount)

    def is_empty(self): 
        return self.balance == 0

# Create an object FROM the blueprint. __init__ receives "Sam" as owner and
# uses the default balance of 0. 

account = BankAccount("Sam")

print("Starting balance:", account.balance)
print("Empty?", account.is_empty)

account.deposit(50)
account.deposit(25)

print("New balance:", account.balance)
print("Empty?", account.is_empty())
print("Deposits made:", len(account.history))