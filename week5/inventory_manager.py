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



