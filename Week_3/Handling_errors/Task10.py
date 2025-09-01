# ussd = "*312#"
# print("Welcome to Airtel Me2U, Offering the best service is our priority.")

# while True:
#     print("\nWelcome to Airtel ME2U")
#     print("1. Airtel to Airtel")
#     print("2. Gift Data Bundle")
#     print("3. PIN Management")
#     print("4. INFO")
#     print("5. HELP")

#     choice = int(input("Select an option (1-5):  "))
#     if choice == "1":
#         number = int(input("Enter the airtel number you wish to transfer to: "))
#         amount = float(input("Please enter the amount you wish to transfer: "))
#         pin = int(input("please enter PIN (default PIN is 1234"))
#         confirm = (amount >=50) and (pin=1234) and 
#         print(f" Send {amount} to: {number}?")
#     elif choice == "2":
#         amount = int(input("Enter withdrawal amount: "))
#         if amount <= balance:
#             balance -= amount
#             print(f"Withdrawal successful. New balance: {balance}")
#         else:
#             print("Insufficient funds.")
#     elif choice == 3:
#         print("Thank you for using our ATM. Goodbye!")
#         break
#     else:
#         print("Invalid option. Try again.")


#         Data_plans = str(input("1.Data plans\n2.Business plans\n3.Roaming/Int'l\n4.Borrow Credit/Recharge"))
# DataPlans = "1"
# BusinessPlans = "2"
# Roaming = "3"
# BorrowCredit= "4"
# option = int(input("Enter your preferred option:"))
# str(input("1. daily \n2. 2-3 Days\n3.Weekly\n4.Monthly"))
# print(f"data plans: {Data_plans}\noption: {option}")
# amount = int(input("amount: "))
# print("Thank you for suscribing")


seat_no = [x for x in range (1, 51) ]
seat_no = set(seat_no)
booking = int(input("Enter your seat no: "))
seat_no.remove(booking)
for seat in seat_no:
    print(f"Seat no: {seat}")


seat_no = set(range(1, 51))  # Seats 1 to 50

# Ask for multiple seat bookings, separated by commas
bookings = input("Enter your seat number(s), separated by commas: ")

# Convert input into a list of integers
bookings = [int(x.strip()) for x in bookings.split(",")]

# Remove each booked seat
for seat in bookings:
    if seat in seat_no:
        seat_no.remove(seat)
    else:
        print(f"Seat {seat} is already booked or invalid.")

# Show remaining available seats
print("\nAvailable seat list after booking:")
for seat in sorted(seat_no):
    print(f"Seat no: {seat}")

 
names = ("Ademola", "Adetola", "Ololade")
phone_no = ("8132456786", "7057628931", "9020456789")
phone_book = dict(zip(names, phone_no))
phone_name = input("Enter a name to find the phone no: ")
phone_search = phone_book.get(phone_name, "Name not found")
print(phone_search)
for key, value in phone_book.items():
    print(f"{key}: {value}")

first_name = str(input("What is your name?: "))
age = int(input("What is your age?: "))
if age <=12:
    print("Children")
elif 13 >= age <= 19:
    print("Teenager")
else:
    print("Adult")
color = str(input("What is your favourite colour?: "))
home_town = str(input("Where is your home town?: "))
profile = (first_name, age, color, home_town)
print(f"First name: \t{first_name}\nage: \t\t{age}\nColour:  \t{color}\nHometown: \t{home_town}")



store = {"50cl pet coke": 175, "50cl pet fanta": 50, "5ocl pet sprite": 100, "Predator": 70, "85cl pulpy orange": 500, "78cl berry blast": 50}
while True:
    print("\nProduct Available in store: ")
    print("Before purchase: ", store)
    product = input("What do you want to buy from us?: ")
    if product not in store:
        print(" Sorry, that product is not available in the store.")
        continue
    quantity = int(input("What is the quantity of product you want?: "))
        
    if store[product] >= quantity:
            store[product] -= quantity
            print(f"Purchase sucessful. After purchase: {store}.")
            print("Thank you for buying from us.")
            break 
    else:
            
        print(f"Sorry, only {store[product]} units of {product} available.")
