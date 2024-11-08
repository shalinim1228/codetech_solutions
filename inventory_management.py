import json
import os

# File paths for storing user data and inventory
USER_DATA_FILE = "user_data.json"
INVENTORY_FILE = "inventory.json"

# Initialize a basic user (can be expanded later)
def initialize_user():
    if not os.path.exists(USER_DATA_FILE):
        user_data = {"username": "admin", "password": "admin"}  # Simple admin user
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(user_data, file)

# Check if the username and password match
def authenticate_user(username, password):
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
            return username == user_data["username"] and password == user_data["password"]
    return False

# Initialize inventory data if it doesn't exist
def initialize_inventory():
    if not os.path.exists(INVENTORY_FILE):
        inventory_data = {}
        with open(INVENTORY_FILE, 'w') as file:
            json.dump(inventory_data, file)

# Load inventory data from the file
def load_inventory():
    with open(INVENTORY_FILE, 'r') as file:
        return json.load(file)

# Save inventory data to the file
def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file)

# Add a new product
def add_product(name, price, quantity, threshold):
    inventory = load_inventory()
    inventory[name] = {"price": price, "quantity": quantity, "threshold": threshold}
    save_inventory(inventory)
    print(f"Product '{name}' added successfully!")

# Edit an existing product
def edit_product(name, price, quantity, threshold):
    inventory = load_inventory()
    if name in inventory:
        inventory[name] = {"price": price, "quantity": quantity, "threshold": threshold}
        save_inventory(inventory)
        print(f"Product '{name}' updated successfully!")
    else:
        print("Product not found.")

# Delete a product
def delete_product(name):
    inventory = load_inventory()
    if name in inventory:
        del inventory[name]
        save_inventory(inventory)
        print(f"Product '{name}' deleted successfully!")
    else:
        print("Product not found.")

# Generate low-stock alerts
def low_stock_alerts():
    inventory = load_inventory()
    alerts = []
    for product, details in inventory.items():
        if details["quantity"] <= details["threshold"]:
            alerts.append(f"Low stock on {product}: {details['quantity']} left")
    return alerts

# Generate sales summary (total sales for each product)
def generate_sales_summary():
    inventory = load_inventory()
    summary = []
    total_sales = 0
    for product, details in inventory.items():
        total_sales += details["price"] * details["quantity"]
        summary.append(f"{product}: Sold {details['quantity']} units, Total Sales: ${details['price'] * details['quantity']}")
    summary.append(f"Total Sales: ${total_sales}")
    return summary

# Main program function
def inventory_management_system():
    # Initialize User and Inventory
    initialize_user()
    initialize_inventory()

    # User authentication
    print("Welcome to the Inventory Management System")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not authenticate_user(username, password):
        print("Invalid username or password. Exiting...")
        return

    print("Login successful!")

    while True:
        print("\nInventory Management Options:")
        print("1. Add Product")
        print("2. Edit Product")
        print("3. Delete Product")
        print("4. View Low Stock Alerts")
        print("5. View Sales Summary")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: $"))
                quantity = int(input("Enter product quantity: "))
                threshold = int(input("Enter low stock threshold: "))
                add_product(name, price, quantity, threshold)
            except ValueError:
                print("Invalid input. Please enter valid price and quantity values.")

        elif choice == "2":
            name = input("Enter product name to edit: ")
            try:
                price = float(input("Enter new product price: $"))
                quantity = int(input("Enter new product quantity: "))
                threshold = int(input("Enter new low stock threshold: "))
                edit_product(name, price, quantity, threshold)
            except ValueError:
                print("Invalid input. Please enter valid price and quantity values.")

        elif choice == "3":
            name = input("Enter product name to delete: ")
            delete_product(name)

        elif choice == "4":
            alerts = low_stock_alerts()
            if alerts:
                print("\nLow Stock Alerts:")
                for alert in alerts:
                    print(alert)
            else:
                print("No products are low on stock.")

        elif choice == "5":
            summary = generate_sales_summary()
            print("\nSales Summary:")
            for item in summary:
                print(item)

        elif choice == "6":
            print("Exiting Inventory Management System...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    inventory_management_system()
