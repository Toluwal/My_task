# **Task1: Your Favorite Life Quote**
# - Ask the user to input their favorite quote.

# - Convert it to title case.

# - Print it with quotation marks using escape sequences.


# quote = str(input("What is your favourite quote? "))
# print(f"My favorite quote is: \t!!!!!\t{quote.upper()}\t!!!!!")

# **Task 2: Shopping List Manager**
# - Create an empty list.

# - Ask the user to enter 3 shopping items (one by one).

# - Add them to the list.

# - Display the list as a single string, separated by commas.

# items = []
# list1 = str(input("Enter the first shopping item: "))
# list2 = str(input("Enter the second shopping item: "))
# list3 = str(input("Enter the third shopping item : "))
# Shopping_list = [list1, list2, list3]
# Shopping_lists = items.append(Shopping_list)
# print(Shopping_list)

# **Task 3: Word Counter**
# - Ask the user for a sentence.

# - Split the sentence into a list of words.

# - Print how many words are in the sentence.

# sentence =str(input("Where did you get the solar produut"))
# sentence = sentence.split()
# print(len(sentence)) 


# **Task 4: Name Organizer**
# - Ask the user to enter 5 names (separated by spaces).

# - Convert all names to lowercase.

# - Sort the list alphabetically.

# - Display them one name per line.
#   -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` 

# name = (input("Give five names in JSS3: "))
# names = name.split(" ")
# for i in range(len(names)):
#     names[i] = names[i].lower()
# names.sort()
# print("\nSorted Names: ")
# for i in range(len(names)):
#     print(names[i])

# **Task 5: Student Score Tracker**

# - Ask the user for 3 student names.

# - For each student, ask for their score.

# - Store the results in two lists (one for names, one for scores).

# - Print a formatted output showing Name — Score, aligned neatly.
#   - Tips: You are to start by creating two empty lists.

# names = []
# scores = []
# for i in range(3):
#     name = input(f"Enter name of student {i+1}: ")
#     score = int(input(f"Enter score for {name}: "))

#     names.append(name)
#     scores.append(score)
# print("\nStudent Results: ")
# print("{:<15} {:<5}".format("Name", "Score"))  
# print("-" * 20)

# for i in range(3):
#     print("{:<15} {:<5}".format(names[i], scores[i]))


# **Task 6: Word Analyzer**
# - Ask the user to input a word.

# - Print the length of the word.

# - Check if it is all uppercase, all lowercase, or title case.

# - Reverse the word using slicing


# word =str(input("Enter your favourite city: "))
# print("Length of word: ", len(word))

# if word.isupper():
#     print("The word is in UPPERCASE.")
# elif word.islower():
#     print("The word is in lowercase.")
# elif word.istitle():
#     print("The word is in Title Case.")
# else:
#     print("The word has mixed case.")

# print("Reversed word:", word[::-1])

# **Task 7: List Manipulation**
# - Create a list of five cities.

# - Replace the third city with a new one (entered by the user).

# - Remove the last city.

# - Add a new city to the beginning of the list.

# - Print the updated list.
cities = ["Ikeja", "osogbo", "Ibadan", "Akure", "Abeokuta"]
new_city = str(input("Enter a new city: "))
cities[2] = new_city
city = cities.pop()
print(city)
print(cities)
cities.insert(0, "Ilorin")
print(cities)  
