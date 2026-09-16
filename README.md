# Python Primer

A short, hands-on introduction to Python for students with no programming
background. Six small example files, each teaching one idea, that build
toward a capstone project: a working command-line **Wordle**.

## Who this is for

Anyone starting a course that uses Python — or anyone who wants a fast,
practical refresher in the first weeks of term. It assumes you have never
written a line of code. If you *have* programmed in another language, you
can move quickly; the examples are deliberately short.

## Setting up

Python usually comes pre-installed on macOS and Linux. On Windows you can
install it from [python.org](https://www.python.org/downloads/) or the
Microsoft Store. To check that it's there, open a terminal and run:

```
python3 --version
```

If that prints a version number (`3.something`), you're ready. If `python3`
isn't found, try `python` instead — on some systems that's the name.

You don't need anything else: no compiler, no project to configure. A plain
text editor and a terminal are enough, though an editor like VS Code makes
life nicer.

## The files

| File | Topic | What you'll be able to do |
|---|---|---|
| `ex1.py` | Input and output | Read from the user and print formatted results |
| `ex2.py` | Types, conversion, decisions | Turn text into numbers; branch with `if` |
| `ex3.py` | Loops | Repeat work with `for` and `while` |
| `ex4.py` | Functions | Package logic and return a result |
| `ex5.py` | Lists and dictionaries | Store collections and look things up by key |
| `ex6.py` | Reading and writing files | Save data to disk and read it back into a list |
| `ex7.py` | Classes and objects | Bundle data and behaviour together |
| `proj.py` | Capstone project | Build a playable Wordle |
| `words.txt` | Word list (data) | The five-letter words the capstone draws from |

Work through them in order. Each example assumes the ones before it.

## How to run an example

From a terminal, in the folder containing the files:

```
python3 ex1.py
```

Unlike some languages, Python has no separate compile step — you run the
source file directly, and your latest edit takes effect the moment you save
and re-run. (If `python3` isn't recognised, try `python ex1.py`.)

## How to use this primer

Reading code is not the same as understanding it. For each example:

1. Read the file and **predict what it will print**, before running it.
2. Run it. Compare the output to your prediction.
3. Where you were wrong, that gap is the thing worth studying.
4. Change something — a value, a condition, a word — and predict again.

Breaking the examples on purpose is encouraged. Error messages are
information, and getting comfortable reading them early will save you more
time than anything else here. Python's errors are shorter than most
languages': the **last line** names the problem, and the lines above it
point at where it happened.

## The capstone project

`proj.py` is a guided scaffold for building **Wordle**: the program picks a
secret five-letter word, the player gets six guesses, and after each guess
the program marks which letters are correct and in place (`#`), which are in
the word but misplaced (`?`), and which aren't in the word at all (`.`).

Each concept from the examples powers a piece of it:

- Input and f-strings (`ex1`) → prompt for each guess and print the feedback
- Conversion and `if`/`elif`/`else` (`ex2`) → check a guess is a legal word
- Loops (`ex3`) → run the round for up to six guesses
- Functions that return a value (`ex4`) → the scoring function
- Lists, dicts, and the `.get()` counting pattern (`ex5`) → counting the secret's letters
- Reading a file into a list (`ex6`) → loading the word list from `words.txt`
- Classes (`ex7`) → the `Game` object that tracks the round

The word list lives in `words.txt` — one word per line, currently a few
hundred five-letter words — and `proj.py` reads it in at startup, so growing
or swapping the vocabulary is just editing a text file. The scaffold hands you the game loop and the `Game` class already written, so
you can concentrate on the interesting part: the scoring function. The tricky
bit — handling repeated letters so you never light up more copies of a letter
than the secret actually contains — is spelled out as a two-pass hint in the
file. Build one piece at a time, running after each.

## Errors you may hit

**`IndentationError`** — Python groups code by indentation. Every line inside
an `if`, loop, function, or class must be indented by the same amount. Mixing
tabs and spaces triggers this too; pick one (spaces) and stick with it.

**`TypeError: can only concatenate str (not "int") to str`** — you're mixing
text and numbers, almost always because `input()` handed you a string.
Convert it with `int(...)`, or build the message with an f-string. (This is
the `ex2` lesson.)

**`NameError: name 'x' is not defined`** — a typo in a variable name, or you
used it before creating it. Python is case-sensitive, so `Guess` and `guess`
are two different names.

**`IndexError: string index out of range`** — you asked for a position that
doesn't exist, e.g. `word[5]` on a five-letter word (its positions are 0–4).

## Getting help

Bring your code — working or broken — to a Coding and Programming (C&P)
appointment or drop-in. Book at [booking link] or email [contact email].
Drop-in times for [term] are posted at [link].

## About

This primer is part of the Coding and Programming (C&P) Primers series from
the Teaching and Learning Centre at Ontario Tech University. Written by
Benjamin D. Fedoruk, Subject Specialist in Mathematics and Coding &
Programming.