# - Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).

# - Start with an empty cart total (cart_total = 0).

# - Use assignment operators (+=) to add the price of some items into cart_total.

# - Print the list of items and the total price using an f-string like this:
# ```
# Items: ['Book', 'Pen', 'Bag']
# Total Price: ₦600


items = ["shoe", "clothes", "bag", "wrist-watch", "necklace", "wristband"]
price = [ 15000, 20500, 25000, 12000, 15000, 50000]
cart_total = 0
cart_total += price[0] 
cart_total += price[1] 
cart_total+= price[2]
cart_total+=price[3]
cart_total+=price[4]
cart_total+=price[5]

print(f"Items: {items}\nTotal price: ₦{cart_total}")

# Output
# Items: ['shoe', 'clothes', 'bag', 'wrist-watch', 'necklace', 'wristband']
# Total price: ₦137500
