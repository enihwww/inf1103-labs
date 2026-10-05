"""
Shopee Product Administrator
------------------------------
You are a Shopee product administrator managing product information:
1. Display all product names from the product list.
2. Add a new product to the existing product list.
3. Update the stock quantity of an existing product after a sale.
4. Identify products priced above $30 and display their names.
"""

import json

# Starting product list — each product is a dictionary
products = [
    {"name": "Wireless Mouse", "price": 15.90, "stock": 50},
    {"name": "Mechanical Keyboard", "price": 89.00, "stock": 20},
    {"name": "USB Cable", "price": 5.50, "stock": 100},
    {"name": "Monitor", "price": 199.00, "stock": 10},
    {"name": "Laptop Stand", "price": 35.00, "stock": 25},
]


# 1. Display all product names
def display_all_names(product_list):
    print("\n--- All Product Names ---")
    for product in product_list:
        print(product["name"])


# 2. Add a new product to the existing product list
def add_product(product_list, name, price, stock):
    new_product = {"name": name, "price": price, "stock": stock}
    product_list.append(new_product)
    print(f"\nAdded new product: {name}")


# 3. Update the stock quantity of an existing product after a sale
def update_stock(product_list, name, quantity_sold):
    for product in product_list:
        if product["name"] == name:
            product["stock"] -= quantity_sold
            print(f"\nUpdated stock for {name}: {product['stock']} left")
            return
    print(f"\nProduct '{name}' not found.")


# 4. Identify products priced above $30 and display their names
def products_above_price(product_list, threshold=30):
    print(f"\n--- Products priced above ${threshold} ---")
    for product in product_list:
        if product["price"] > threshold:
            print(product["name"])


# Save the product list to a JSON file (persistent storage)
def save_to_json(product_list, filename="products.json"):
    with open(filename, "w") as f:
        json.dump(product_list, f, indent=4)
    print(f"\nProduct data saved to {filename}")


# ---- Run the tasks ----
display_all_names(products)

add_product(products, "Webcam", 45.00, 15)

update_stock(products, "Wireless Mouse", quantity_sold=5)

products_above_price(products, threshold=30)

save_to_json(products)

print("\n--- Final Product List ---")
for p in products:
    print(p)