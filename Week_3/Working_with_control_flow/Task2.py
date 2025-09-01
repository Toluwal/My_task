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
