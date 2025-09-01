# services/library.py   - This will handle business logic

import data.my_data as my_data

def borrow_book(title):
    for book in data.get_books():
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            return f"You have borrowed '{book['title']}'"
        return "Book not available."
    

# services/library.py - This will update to save after borrow/return

import data as my_data

def borrow_book(title):
    for book in my_data.get_books():
        if book["title"].lower() == title.lower()  and book["available"]:
            book["available"] = False
            my_data.save_books()
            return f"You have borrowed '{book['title']}'"
    return  "Book not available."

def return_book(title):
    for book in my_data.get_books():
        if book["title"].lower() == title.lower() and not book["available"]:
            book["available"] = True
            my_data.save_books()
            return f"You have returned '{book['title']}"
    return "Book not found or not borrowed."