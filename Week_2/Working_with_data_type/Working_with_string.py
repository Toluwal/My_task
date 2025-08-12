# **Python data structure**

# 1. String — immutable sequence of characters (often treated like a sequence)

# 2. Tuple — ordered, immutable sequence

# 3. Set — unordered collection of unique items

# 4. Dict (dictionary / map) — key → value mapping

# 5.  List— ordered, mutable sequence

# 6. Also: range, bytes/bytearray, and useful types from collections (namedtuple, defaultdict, Counter, deque)

# **1. Strings in Python**
#  - A string in Python is a sequence of characters enclosed in either single quotes `('...')`, double quotes `("...")`, or triple quotes `('''...''' or """...""")`.
# - Strings are used to store text data like names, sentences, or any combination of letters, numbers, and symbols.


# # Single Quotes
# name = "Ada"
# print(name)

# # Double quotes
# greetings = "Hello"
# print(greetings)

# # Triple quotes (for multi-line strings)
# story = '''Once upon a time, 
# there was acoder named Ada.'''
# print(story)

# # String with numbers and symbols
# password = "p@ssw0rd123"
# print(password)

# # **Explanation**
# # - Single quotes `'` and double quotes `"` work the same way.

# # - Triple quotes allow your string to span across multiple lines without using `\n`.

# # - Strings can contain letters, numbers, spaces, and special characters.

# #    - Tip: In Python, there’s no “character” type— even a single letter is considered a string.

# # string Operations

# # indexing
# word = "She is an intelligent student./n She is JSS 3./nShe is from Ogun State."
# print(word[0]) # S
# print(word[-1]) # .

# #Slicing
word = "She is the most curious I know. "
# print(word[0:4]) #She
# print(word[2:])  # e is the most curious I know.
# print(word[:3])  # She
# print(word[::2]) # Sei h otcrosIko.
print(word[::-1]) # .wonk I suoiruc tsom eht si ehS

# String Concatenation and Repetition

#Concatenation

a = "Hello"
b = "World"
print ( a + " " + b)  # Hello  World

# Repetition

word = "Hi!"
print(word * 3) # Hi!Hi!Hi!

# String Searching & Checking

# Membership
text = "Python programming"
print("Python" in text) #True
print("Java" not in text) #True

# find() /rfind()

text = "Hello World"
print(text.find("o")) #4
print(text.rfind("o")) #7

# Index() / rindex()
# -(Like find() but raises an error if not found)

text = "Hello World"
print(text.index("World")) # 6

#startswith() / endswitch()

filename = "data.csv"
print(filename.startswith("data"))  # True
print(filename.endswith(".csv"))  # True

# String Methods
# - Creating and manipulating strings.

#   - upper()
#   - lower()
#   - title()
#   - strip()
#   - replace()

# Creating and manipulating strings.

#   - upper()
#   - lower()
#   - title()
#   - strip()
#   - replace()
#   - capitalize()
#   - swapcase()
#   - strip()
#   - lstrip()
#   - rstrip()
#   - split()
#   - rsplit()
#   - splitlines()
#   - join()
#   - replace()
#   - center()
#   - ljust()
#   - rjust()
#   - zfill()
#   - isalpha()
#   - isdigit()
#   - isalnum()
#   - isspace()
#   - islower()
#   - isupper()
#   - istitle()

# Upper()
# -Converts all characters in the string to uppercase

name = "Ada Balogun"
print(name.upper())   # ADA BALOGUN

#lower()
#-Converts all characters in the string to lower case.

sentence = "python is amazing"
print(sentence.lower())  # python is amazing

#title()
# Converts the first character in the string to upper case
sentence = "python is amazing"
print(sentence.title())  # python is amazing



#strip()
#-Removes whitespace(or specified characters) from both ends of string.

text = "   Abuja   "
print(text.strip())     # Abuja

# replace()
#- Replaces occurrences of a substring with another substring.

message = "I love Java"
print(message.replace("Java", "Python"))  # I love Python

# swapcase()
# Switches lowercase to uppercase and vice versa

text = "Hello ABEOKUTA"
print(text.swapcase())    #hELLO abeokuta

#lstrip()
#- Removes whitespace (or specified characters) from the leftside only.

text = "   Nigeria"
print(text.lstrip())    #Nigeria

#rstrip()
#-Removes white space (or specified characters) from the right side only.

text = "Nigeria  "
print(text.rstrip())     #Nigeria

# split()
# Splits a string into a list using a separator (default is space).

fruits = "mango orange banana"
print(fruits.split())   #['mango', 'orange', 'banana']

#rsplit()
#-Splits a string into a list from the right side
text = "one, two, three, four"
print(text.rsplit(",", 2))   # ['one, two', ' three', ' four']

text = "one, two, three, four"
print(text.rsplit())    # ['one,', 'two,', 'three,', 'four']

#splitline()
#- Splits a string into a list at each new line(\n)

lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())  #['Line 1', 'Line 2', 'Line 3']

#Join()
#- Joins a list of strings into one string with a specified separator.

words = ["I", "love", "Python"]
print(" ".join(words))   #I love Python

# Center()
#- Centers the string within a specified width, padding with spaces or caharacters

text = "Python"
print(text.center(20, "-"))    # -------Python-------


#ljust()
#- Left-aligns the string within a specified width, padding with spaces or characters.

text = "Python"
print(text.ljust(10, "*"))    #Python****

#rjust()
#- Right-aligns the string within a specified width, padding with spaces or characters.

text = "Python"
print(text.rjust(10, "*"))      #****Python

# zfill()
# -Pads a numeric string on the leftnwith zeros until it reaches a given length.

num ="42"
print(num.zfill(5))  #00042

# isalpha()
#- Checks if  the string contains only letters.

print("Lagos".isalpha())    # True
print("Lagos123".isalpha()) # False

#isdigit()
#- checks if the string contains only digits.

print("12345".isdigit())   #True
print("123a".isdigit())    #False

#isalnum()
# Checks if the string contains only letters and digits.

print("Python3".isalnum())    #True
print("Python 3".isalnum())   #False

# Reverse a string
country = "Nigeria"
print(country[::-1])