# #Using only the topics that you have been taught as listed below.
# #input() statement
# #print() statement
# #f-strings
# #Concatenation
# #Escape sequence
# #Variables
# #Data types
# #Type casting

# # 1. Collecting User Details
# # Ask the user for their first name and age, then print a welcome message using an f-string.
# # likely output
# # Welcome Ade, you are 25 years old

# # name = input("Enter your first name: ")
# # age = int(input("Enter your age: "))
# # print(f"Welcome {name},  you are {age} years old")

# # 2. Price Display with Type Casting
# # Ask the user for the price of garri per paint in naira (as a string) and convert it to float. Display it with a message showing the amount in naira and kobo using print().

# price = str(input("What is the price of gaari per paint in Naira: "))
# float_price = float(price)
# print(f"The price is ₦{float_price}k")

# #3. School Registration Form
# #- Ask for student’s name, class, and state of origin. Use string concatenation to print them in one sentence.
# #likely output
# #Student Ade is in SS2 and is from Ogun State.

# Student_name = input("Hi, what is your name: ")
# Class = input("Which class are you?: ")
# State = input("Which state are you from: ")
# print("Student " + " " + Student_name + " " + "is in " +  " "  + Class + " "  "and is from" " " + State)

# # 4. Escape Sequence 
# # - Ask for the name of a Nigerian dish and the state it is popular in. Print the result in two lines using `\n` and add a tab space before the state name using `\t`.
# Delicacy = input("What is the name of a popular Nigerian_dish?")
# origin = input("Which state {Delicacy} is popular in")
# print(f" The Nigerian dish is {Delicacy}\n It is popular in \t{origin} state")

# 5. Daily Market Report
# Ask the user to input:
#  - Market name
#  - Number of traders
#  - Daily revenue in naira
# - Display the result using f-string formatting with commas for thousands separator

# Market_name = input("Market name: ")
# Number_of_traders =  input("Number of traders: ")
# Daily_revenue_in_naira =  input("Daily revenue in naira: ")
# print(f"Daily_market_report:/nMarket name: {Market_name},\nNumber of traders: {Number_of_traders},\nDaily revenue in naira: ₦{Daily_revenue_in_naira}")

# 6. Electricity Bill Formatter
#  - Ask for:
#    - Customer’s full name
#    - Units consumed (kWh) – integer
#    - Cost per unit – float
# - Calculate the total bill and print it in a neatly formatted receipt using escape sequences for line breaks.

# full_name = input("Customer's fullname: ")
# units_consumed = int(input("Units consumed (kwh): " ))
# unit_cost = float(input("Cost per unit: "))
# total_bill = units_consumed * unit_cost 
# print(f"Electricity Bill Formatter\nTotal Bill is ₦{total_bill}k ")

# 7. Mixing Data Types
#  - Ask the user for:
#     - Your age (integer)
#     - Your height in meters (float)
#     - Your name (string)
# - Print a sentence using f-string showing all details in one line, making sure you type-cast where necessary.

# age = int(input("Your age: "))
# height = float(input("Your height in meters: "))
# name = str(input("Your name: "))
# print(f"My {name} is and I am {age} years old and my height is {height}m.")

# 8. Transport Fare Calculator
#  - Ask for:
#     - Distance in km (float)
#     - Fare per km (float)
# - Calculate and display the total fare with two decimal places using `f"{value:.2f}"`.

# distance = float(input("Distance in km: "))
# fare = float(input("Fare per km: "))
# total_fare = distance * fare
# print(f"The total fare is ₦{total_fare: .2f}k.")

# 9. Nigerian Festival Info
#  - Ask for:
#      - Festival name (string)
#      - Location (string)
#      - Month held (string)
# - Display the info with quotation marks around the festival name using escape sequences `(\")`.

# name = str(input("Festival name: "))
# location = str(input("location: "))
# month = str(input("Month held: "))
# print(f"The {name} is an annual festival that takes place in {location} and usually in the month of {month}." )

# name = str(input("School name: "))
# fee = float(input("Tuition fee: "))
# hostel= float(input("Hostel fee: "))
# feeding =float(input("Feeding fee: "))
# total =fee + hostel + feeding
# print(f"School Fees Breakdown\nReceipt\nSchool name: {name}\nTuition Fee: ₦{fee: .2f}k/nHostel Fee: ₦{hostel: .2f}k\nFeeding Fee: ₦{feeding: .2f}k\nTotal payment: ₦{total: .2f}k")

# 11. Nigerian Currency Converter (Very Advanced)
#   - Ask for:
#     - Amount in Naira (float)
#     - Exchange rate to US Dollars (float)
#     - Exchange rate to British Pounds (float)

# - Convert and print results with thousands separators and currency symbols, neatly aligned in a table-like format using escape sequences.
# amount = float(input("Amount in Naira: "))
# US_dollars = float(input("Exchange rate to US Dollars: ")) 
# British_pounds = float(input("Exchange rate to British pounds: "))
# print(f"Amount in Naira: \t\t₦{amount}, \nExchange rate to US Dollars: \t${US_dollars}, \nExchange rate to British Pounds:£{British_pounds}")

# 12. Simulated USSD Menu Interaction
#  - You are to design a mock USSD interface for a mobile service.
#  - Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction

# print("Welcome to GTB")
# ussd_code = "*737#"
# password = "1234"
# ussd_code = int(input(" dial ussd code: "))
# Data_plans = str(input("1.Data plans\n2.Business plans\n3.Roaming/Int'l\n4.Borrow Credit/Recharge"))
# DataPlans = "1"
# BusinessPlans = "2"
# Roaming = "3"
# BorrowCredit= "4"
# option = int(input("Enter your preferred option:"))
# str(input("1. daily \n2. 2-3 Days\n3.Weekly\n4.Monthly"))
# print(f"data plans: {Data_plans}\noption: {option}")
# amount = int(input("amount: "))
# print("Thank you for suscribing")


print("Welcome to GTB")
code = "*737#"
passcode = "1234"
ussd_code = (input(" dial ussd code: "))
if ussd_code ==code:
    print("1.Data plans\n2.Business plans\n3.Roaming/Int'l\n4.Borrow Credit/Recharge")
    choice = input("Enter your prefered option?: ")
    if choice == "1":
        print("1. daily \n2. 2-3 Days\n3.Weekly\n4.Monthly")
        dataplan_choice = input("What is your preferred option: ")
        if dataplan_choice == "1":
            amount = input("Enter the amount: ")
            password = input("Enter your password: ")
            if password == passcode:
                print("You have successfuly bought a daily data bundle.")
            else:
                print("invalid password.")
        else:
            print("Invalid input. Please enter the correct option")        
else:
    print("Dial *737# to access GTB ussd platform")
print("Thank you for suscribing")