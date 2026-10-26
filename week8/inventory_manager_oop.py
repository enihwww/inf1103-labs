import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        if self.__stock + quantity < 0:
            print("Not enough stock.")
        else:
            self.__stock += quantity

    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    #to use in Inventory class to search for a product by its ID
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:         #check all the products in the list
            if product.get_product_id() == product_id:  
                return product
        return None
    
    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------")
        for product in self.__products:
            product.display_information()
            print("------------------------------------")

    def get_products(self):
        return self.__products

def load_inventory(inventory):
    try:
        with open("inventory.json", "r") as file:
            inventory_data = json.load(file)

        for product_data in inventory_data:
            product = Product(
                product_id=product_data["id"],
                name=product_data["name"],
                price=product_data["price"],
                stock=product_data["stock"]
            )
            inventory.add_product(product)

        print("\nInventory loaded successfully.")

    except FileNotFoundError:
        print("\nInventory.json not found. Starting with empty inventory.")

def save_inventory(inventory):
    print("\nSaving Inventory...")
    inventory_data = []
    for product in inventory.get_products():
        product_data = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        }
        inventory_data.append(product_data)
    with open("inventory.json", "w") as file:
        json.dump(inventory_data, file, indent=4)
    print("Inventory saved successfully to inventory.json.")

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
 
    product = Product(product_id, name, price, stock)
    inventory.add_product(product)
    print("\nProduct added successfully!")
 
def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
 
    if product is None:
        print("\nProduct not found.")
        return
 
    print("\nProduct Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    quantity = int(input("\nQuantity to add (use negative to remove): "))
    product.update_stock(quantity)
    print(f"Stock is now: {product.get_stock()}")
 
def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
 
    if product is None:
        print("\nProduct not found.")
    else:
        print("\nProduct Found:")
        product.display_information()
 
print("============================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("============================================")
 
inventory = Inventory()
load_inventory(inventory)
 
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
        inventory.display_all()
    elif choice == "2":
        add_product(inventory)
    elif choice == "3":
        update_stock(inventory)
    elif choice == "4":
        search_product(inventory)
    elif choice == "5":
        save_inventory(inventory)
    elif choice == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("\nInvalid option.")


