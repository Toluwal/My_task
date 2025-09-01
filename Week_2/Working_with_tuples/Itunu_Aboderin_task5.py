# **Task1:  Create and Display**

# - Ask the user to enter three favorite Nigerian dishes (one at a time).

#  - Store them in a tuple called dishes.

# - Print the tuple in a single line, separating items with commas.

# - Use the \n escape sequence to print each dish on a new line.

# dish1 = str(input("What is your most prefered favorite Nigerian dishes: "))
# dish2 = str(input("What is your second most prefered favorite Nigerian dishes: "))
# dish3 = str(input("What is your third most prefered favorite Nigerian dishes: "))
# dishes = (dish1, dish2, dish3)
# print(dishes)
# print(f"My most favourite nigerian dish is: {dish1},\n followed by: {dish2},\n and lastly: {dish3}.")


# **Task2: Tuple and Input**

# - Ask the user for 5 best friends’ names.

# - Store them in a tuple friends.

# - Print the tuple in reverse order.

# friend1 = str(input("What is the name of your friend: "))
# friend2 = str(input("What is the name of your friend: "))
# friend3 = str(input("What is the name of your friend: "))
# friend4 = str(input("What is the name of your friend: "))
# friend5 = str(input("What is the name of your friend: "))
# friend = (friend1, friend2, friend3, friend4, friend5)
# print(friend)
# print(friend[::-1])

# **Task3: Tuple Operations**
# - Create a tuple of 5 Nigerian states entered by the user.

#   - Print the first state and last state.

#   - Check if "Lagos" is in the tuple and print "Yes" or "No".

#   - Print the number of states entered.
#     - (Hint: use the tuple membership)

# state1 = str(input("What is the name of your state: "))
# state2 = str(input("What is the name of your state: "))
# state3 = str(input("What is the name of your state: "))
# state4 = str(input("What is the name of your state: "))
# state5 = str(input("What is the name of your state: "))
# state_tuple = (state1, state2, state3, state4, state5)
# print(state_tuple[0])
# print(state_tuple[-1])
# print("lagos" in state_tuple)
# print(len(state_tuple))


# **Task4: Tuple Unpacking**
#  - Ask a user for their;

#   - First name

#   - Age

#   - Favorite color

#   - Home town

#   - Store them in a tuple profile and unpack into variables.

#   - Print and use  escape sequence to align each piece of information nicely.

# first_name = str(input("What is your name?: "))
# age = int(input("What is your age?: "))
# color = str(input("What is your favourite colour?: "))
# home_town = str(input("Where is your home town?: "))
# profile = (first_name, age, color, home_town)
# print(f"First name: \t{first_name}\nage: \t\t{age}\nColour:  \t{color}\nHometown: \t{home_town}")

# **Task5: Modify Tuple Indirectly**
# Ask a user to enter three items for their shopping list.

#   - Store in a tuple shopping_list.

#   - Convert it to a list, then ask for two more items to add.

#   - Convert back to a tuple and print the updated list using join() to display items separated by " | ".

# list1 = str(input("Enter your item: "))
# list2 = str(input("Enter your item: "))
# list3 = str(input("Enter your item: "))
# shopping_list =(list1, list2, list3)
# print(shopping_list)
# shopping_list = list(shopping_list)
# print(shopping_list)
# other_list1 = str(input("Enter other list1: "))
# other_list2 = str(input("Enter other list2: "))
# shopping_list.append(other_list1)
# shopping_list.append(other_list2)
# tuple = tuple(shopping_list)
# print(tuple)

# **Task6: Attendance Tracker**
# - Write a Python program that;

#  - Stores the days of the week in a tuple.

#  - Stores the months of the year in another tuple.

#  - Asks the user to enter:

#    - Student’s name

#    - Gender

#    - Course Track
   
#    - Current month number (1-12)

#    - Current day number (1-7)


weeks = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
student = str(input("What is your name?: "))
gender= str(input("What is your gender?: "))
course_track = str(input("Which course track did you enroll for?: "))
current_month_number = int(input("What is the current month number (1-12): "))
current_day_number = int(input("What is the current day number (1-7) ?: "))
print(weeks)
print(months)
print(f"Attendance tracker:\nweeks: \t\t\t{weeks}\nmonths: \t\t{months}\nstudent: \t\t{student}\ngender: \t\t{gender}\ncourse track: \t\t{course_track}\ncurrent month number: \t{months[current_month_number-1]}\ncurrent day number: \t{weeks[current_day_number-1]} ")