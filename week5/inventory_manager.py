import json

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45, "stock": 25}
]

def display_all():
    print("\nCurrent Inventory")
    print("------------------------------------")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f}"
             f" | Stock: {product['stock']}")
    print("------------------------------------")


def add_product():
    print("\nAdd New Product")
    product = {}
    product["id"] = input("Product ID: ")
    product["name"] = input("Product Name: ")
    product["price"] = float(input("Price: "))
    product["stock"] = int(input("Stock Quantity: "))

    inventory.append(product)

    print("\nProduct added successfully!")

def update_stock():
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")
            product["stock"] = int(input("\nNew Stock Quantity: "))
            print("\nStock updated successfully!")
            return

    print("\nProduct not found.")

def search_product():
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print("------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("------------------------------------")
            return

    print("\nProduct not found.")

def load_inventory():
    global inventory
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("\nInventory loaded successfully.")

    except FileNotFoundError:
        print("\nInventory.json not found. Starting with empty inventory.")

print("============================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("============================================")

load_inventory()

while True:
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------------------")

    choice = input("Enter option: ")

    if choice == "1":
        display_all()

    elif choice == "2":
        add_product()

    elif choice == "3":
        update_stock()

    elif choice == "4":
        search_product()

    else:
        print("\nInvalid option.")


