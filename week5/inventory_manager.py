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




