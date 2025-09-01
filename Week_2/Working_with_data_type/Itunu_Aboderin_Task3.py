# Task 1
# 1. Write a program to take a string input from the user and display it in uppercase.
# Occupation = str(input("What do you do for a living?: "))
# print(f"My occupation is {Occupation.upper()}.")
# 2. Given the string "python", print its first and last characters.

# string = "python"
# print(string[0])
# print(string[-1])
# 3. Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.

# name =input("<name>: ")
# print(f"Hello, {name}")

# 4. Write a program to count the number of characters in a string without using len().

# 5. Given "Hello World", replace "World" with "Python".

message = "Hello World"
print(message.replace("World", "Python"))

# **Task2**

# 6. Check if a given string contains the substring "python" (case-insensitive).

message = "python is a programming language"
print("python" in message)
# 7. Write a program to reverse a string without using slicing ([::-1]).

word = "robot"
print(word.find(word[-1]) + 1)
# 8. Given a string with extra spaces, remove the leading and trailing spaces.

school ="    Ladoke Akintola University of Technology      "
print(school.strip())
# 9. Ask the user to enter a sentence and print the number of vowels in it.
vowels = "aeiouAEIOU"
country = str(input("Enter your country: "))
count = 0
for c in country:
    if c in vowels:
        count +=1
print(count)

# 10. Convert a string "1234" to an integer and multiply it by 2.
word = "1234"
print(int(word)*2)

# **Task3: Pattern Matching & Splitting**
# 11. Given "apple,banana,orange", split the string into a list of fruits.
fruits = "apple banana orange"
print(fruits.split())

# 12. Ask the user for a sentence and print each word on a new line.

sentence = input("Enter a new sentence: ")
print(sentence.split())

# 13. Replace all spaces in a string with underscores (_).
movie = "The hunter's watch party"
print(movie.replace(" ", "_"))

# 14. Count how many times the letter "a" appears in "Banana".

letter = "Banana"
count = letter.count("a")
print(count)

# 15. Check if a given string starts with "https://".

website = "https://mail.google.com/mail"
print(website.startswith("https://"))