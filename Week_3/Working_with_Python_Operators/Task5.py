# **Task5: Store Inventory Update**
# - Create a dictionary called store with items and their available quantities. Example:
# ```
# store = {"Book": 10, "Pen": 20, "Bag": 5}
# ```


# - Ask the user to input the item they want to buy (e.g., "Pen").

# - Ask the user to input the quantity they want to purchase.

# - Use the assignment operator -= to update (reduce) the item quantity in the dictionary.

# - Print the updated dictionary in this format:

# ```
# Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
# After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}
# ```

store = {"50cl pet coke": 175, "50cl pet fanta": 50, "5ocl pet sprite": 100, "Predator": 70, "85cl pulpy orange": 500, "78cl berry blast": 50}
print("Before purchase: ", store)
product = input("What do you want to buy from us?: ")
quantity = int(input("What is the quantity of product you want?: "))
store[product] -= quantity
print("After purchase: ", store)