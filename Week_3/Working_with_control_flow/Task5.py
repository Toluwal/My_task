

store = {"50cl pet coke": 175, "50cl pet fanta": 50, "5ocl pet sprite": 100, "Predator": 70, "85cl pulpy orange": 500, "78cl berry blast": 50}
while True:
    print("\nProduct Available in store: ")
    print("Before purchase: ", store)
    product = input("What do you want to buy from us?: ")
    if product not in store:
        print(" Sorry, that product is not available in the store.")
    
    quantity = int(input("What is the quantity of product you want?: "))
        
    if store[product] >= quantity:
            store[product] -= quantity
            print(f"Purchase sucessful. After purchase: {store}.")
            print("Thank you for buying from us.")
            break 
    else:
            
        print(f"Sorry, only {store[product]} units of {product} available.")
