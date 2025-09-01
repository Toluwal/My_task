# **Task1: Fruit collector**
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.
# fruit = str(input("Enter your 5 favourite fruits: " ))
# fruits = set([fruit])
# print(fruits)

# **Task2: Unique Name Collector**
#  - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

name = str(input("What is your name?: "))
list_of_names = name.split()
list_of_name = set(list_of_names)
seminar_attendee = list(list_of_name)
seminar_attendee.sort()
print(seminar_attendee)

# **Task3: Simulate a football match ticket system**
# - Store all seat numbers (1 to 50) in a set.

# - Ask users to "book" a seat by entering the number.

# - Remove booked seats from the set.

# - Show remaining seats after each booking.

# seat_no = [x for x in range (1, 51) ]
# seat_no = set(seat_no)
# booking = int(input("Enter your seat no: "))
# seat_no.remove(booking)
# print(seat_no)


# **Task4: Create a Unique Voters Registration System**

# - Ask for voter names and store in a set.

# - If a voter tries to register twice, display a warning.

# - After registration, display the total number of unique voters.


voter_name = str(input("Enter voter names separated by commas: "))
voters = {name.strip() for name in voter_name.split(',')}
print(voters)
print("\nThe total number of unique voters: ", len(voters))
print("voters list:" , ",".join(voters))