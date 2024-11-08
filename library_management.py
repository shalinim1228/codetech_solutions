import json
import os
from datetime import datetime, timedelta

# File path for storing library data
LIBRARY_FILE = "library_data.json"

# Initialize the library if it doesn't exist
def initialize_library():
    if not os.path.exists(LIBRARY_FILE):
        library_data = {
            "books": [],
            "magazines": [],
            "dvds": [],
        }
        with open(LIBRARY_FILE, 'w') as file:
            json.dump(library_data, file)
        print("Library initialized.")

# Load library data from the file
def load_library():
    with open(LIBRARY_FILE, 'r') as file:
        return json.load(file)

# Save library data to the file
def save_library(library_data):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library_data, file)

# Add a new item to the library
def add_item(category, title, author, year, rental_period_days=14):
    library_data = load_library()
    item = {
        "title": title,
        "author": author,
        "year": year,
        "rental_period_days": rental_period_days,
        "checked_out": False,
        "due_date": None,
    }
    library_data[category].append(item)
    save_library(library_data)
    print(f"{category.capitalize()} '{title}' added to the library.")

# Check out an item
def checkout_item(category, title):
    library_data = load_library()
    for item in library_data[category]:
        if item["title"].lower() == title.lower() and not item["checked_out"]:
            item["checked_out"] = True
            item["due_date"] = datetime.now() + timedelta(days=item["rental_period_days"])
            save_library(library_data)
            print(f"Checked out '{title}'. Due date: {item['due_date'].strftime('%Y-%m-%d')}")
            return
    print(f"'{title}' is not available for checkout.")

# Return an item
def return_item(category, title):
    library_data = load_library()
    for item in library_data[category]:
        if item["title"].lower() == title.lower() and item["checked_out"]:
            overdue_fine = 0
            if datetime.now() > item["due_date"]:
                overdue_days = (datetime.now() - item["due_date"]).days
                overdue_fine = overdue_days * 1  # Fine of $1 per day
            item["checked_out"] = False
            item["due_date"] = None
            save_library(library_data)
            print(f"Returned '{title}'. Overdue fine: ${overdue_fine}")
            return
    print(f"'{title}' was not checked out.")

# Search for an item by title, author, or category
def search_items(query, category=None):
    library_data = load_library()
    results = []
    if category:
        items = library_data.get(category, [])
        for item in items:
            if query.lower() in item["title"].lower() or query.lower() in item["author"].lower():
                results.append(item)
    else:
        for category_items in library_data.values():
            for item in category_items:
                if query.lower() in item["title"].lower() or query.lower() in item["author"].lower():
                    results.append(item)
    if results:
        for item in results:
            print(f"Title: {item['title']}, Author: {item['author']}, Year: {item['year']}, Due Date: {item['due_date']}")
    else:
        print("No matching items found.")

# Main program loop
def library_system():
    initialize_library()

    while True:
        print("\nLibrary System:")
        print("1. Add Item")
        print("2. Checkout Item")
        print("3. Return Item")
        print("4. Search Items")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category (books, magazines, dvds): ").lower()
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            add_item(category, title, author, year)

        elif choice == "2":
            category = input("Enter category (books, magazines, dvds): ").lower()
            title = input("Enter title: ")
            checkout_item(category, title)

        elif choice == "3":
            category = input("Enter category (books, magazines, dvds): ").lower()
            title = input("Enter title: ")
            return_item(category, title)

        elif choice == "4":
            query = input("Enter search query (title/author): ")
            category = input("Enter category to search (leave empty to search all): ").lower()
            search_items(query, category)

        elif choice == "5":
            print("Exiting Library System...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    library_system()
