# proj.py — CAPSTONE: build Wordle
# =================================
#
# Your goal: a playable command-line Wordle. The program picks a secret
# five-letter word; the player has six guesses; after each guess you show
# which letters are in the right spot, which are in the word but misplaced,
# and which aren't in the word at all.
#
# You already have every tool you need. Here's the map from the examples:
#
#   input() and f-strings ............. ex1  -> prompt for and print guesses
#   int()/decisions ................... ex2  -> compare and branch
#   for / while / break / continue .... ex3  -> the six-guess round
#   string indexing & slicing ......... ex4  -> compare letters by position
#   functions that return a value ..... ex5  -> the scoring function
#   lists, dicts, the .get() counter .. ex6  -> counting the secret's letters
#   reading a file into a list ........ ex7  -> loading the word list
#   classes ........................... ex8  -> the Game object (like BankAccount)
#   try/except for bad input .......... ex9  -> a robust guess prompt
#
# Build it PIECE BY PIECE and run after each piece. Do not write the whole
# thing and run it once at the end.
#
# Feedback markers used below:
#   #  = right letter, right spot   (Wordle green)
#   ?  = right letter, wrong spot   (Wordle yellow)
#   .  = letter not in the word     (Wordle grey)
