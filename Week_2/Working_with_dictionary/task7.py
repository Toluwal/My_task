# **Task1: Student Bio Data Storage**

# - Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.

#   - Courses should be stored as a list.

#   - Display the bio-data neatly using escape sequences.

# - Requirements:

#   - Use `input()` to collect details.

#   - Use dictionary operations `(dict[key] = value)` to store data.

#   - Use `print()` formatting with `\n` and `\t` for better output.

# student_info = {}
# s_name = str(input("name of student: "))
# s_age = int(input("age of student: "))
# s_gender = str(input("gender of student: "))
# s_courses = str(input("student course: "))

# student_info = dict(name=s_name, age=s_age, gender=s_gender, )
# courses = list(s_gender)

# print(f"Student biodata information: \nName: \t\t{s_name}\nAge: \t\t{s_age} years old\nGender: \t{s_gender}\nCourses: \t{s_courses}") 

# - Create a program that stores items and their prices in a dictionary.

#   - Items should come from a list.

#   - Prices are entered by the user.

#   - Display all items and prices, then allow the user to update the price of an item.

# - Requirements:

#   - Use dictionary update method `.update()` or assignment.

#   - Use `.keys()` to display available items.

#   - Use input validation (no advanced functions).

# items_list = ["Book", "Pen", "Pencil", "Eraser", "Ruler"]
# prices = {}
# print("input the price of the items")
# for item in items_list:
#     price = int(input(f"Enter the price for {item}?: "))
#     prices[item] = price
# print("\nItems and their prices: ")
# for item, price in prices.items():
#     print(f"{item}: {price}")
# print("\nAvailable items to update:", list(prices.keys()))
# update_item = input("Enter the item you want to update the price for: ")
# new_price = int(input(f"Enter the new price for {update_item}: "))
# prices.update({update_item: new_price})

# print("\nUpdated items and their prices:")
# for item, price in prices.items():
#     print(f"{item}: {price}")


# week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday")
# activity = str(input("input activity for three days: "))
# selected_days = ("Tuesday", "Thursday", "Saturday")
# activities = []
# for day in selected_days:
#     activity = input(f"What activity do you want to do on {day}? ")
#     activities.append(activity)
# print(activities)
# activity_dict = {day: activity for day, activity in zip(selected_days, activities)}
# print("\nPlanned activities:")
# print(activity_dict)

# **Task3: Days and Activities Pairing**
# - Store days of the week in a tuple and ask the user to input an activity for three specific days.

#   - Use dictionary comprehension to pair days and activities.

#   - Print the dictionary.

# - Requirements:

#   - Use a tuple for days.

#   - Use {day: activity for day, activity in `zip(..., ...)`}.
#   Tip: Research on how to use `zip()`

# week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
# selected_days = ("Monday", "Thursday",  "Saturday")
# activities = []
# for day in selected_days:
#     activity = input(f"Enter an activity for {day}: ")
#     activities.append(activity)
# day_activity = {day: activity for day, activity in zip(selected_days, activities)}
# print("\nActivities for the selected  for the selected days: ")
# print(day_activity)

# **Task4: Unique Members Registration**
# - Ask the user to enter three names separated by commas.

#    - Convert them to a set to ensure uniqueness.

#    - Create a dictionary where each name is a key and its length is the value.

# - Requirements:

#    - Use `.split(",")` and `set()` to remove duplicates.

#    - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.
# names = input("Enter three names: ")
# list_of_names = set(names.split(","))
# dict = {name.strip: len(name.strip()) for name in list_of_names}
# print("dict:", list_of_names)


# **Task5: Contact Quick Lookup**
# - Store three names and their phone numbers in two separate tuples.

#   - Create a dictionary from them using `dict(zip(...))`.

#   - Ask the user for a name and display the corresponding number (or an error message).

# - Requirements:

#   - Use `zip()` and d`ict()` to combine tuples.

#   - Use `.get()` for safe retrieval.

#   - No loops.

names = ("Ademola", "Adetola", "Ololade")
phone_no = ("8132456786", "7057628931", "9020456789")
phone_book = dict(zip(names, phone_no))
phone_name = input("Enter a name to find the phone no: ")
phone_search = phone_book.get(phone_name, "Name not found")
print(phone_search)