names = ("Ademola", "Adetola", "Ololade")
phone_no = ("8132456786", "7057628931", "9020456789")
phone_book = dict(zip(names, phone_no))
phone_name = input("Enter a name to find the phone no: ")
phone_search = phone_book.get(phone_name, "Name not found")
print(phone_search)
for key, value in phone_book.items():
    print(f"{key}: {value}")
