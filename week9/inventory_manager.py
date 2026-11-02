import json
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def update_stock(self, quantity):
        if self._stock + quantity < 0:
            print("Not enough stock.")
        else:
            self._stock += quantity

    def display_information(self):
        print(f"Product ID: {self._product_id}")
        print(f"Name: {self._name}")
        print(f"Price: ${self._price:.2f}")
        print(f"Stock: {self._stock}")

    #getter
    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self._weight = weight

    @property
    def weight(self):
        return self._weight
    
    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        base_cost = 5.00
        cost_per_kg = 7.00
        return base_cost + (cost_per_kg * self._weight)

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size = download_size

    @property
    def download_size(self):
        return self._download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally via download link."

class Inventory:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def search_product(self, product_id):
        for product in self._products:         #check all the products in the list
            if product.product_id == product_id:  
                return product
        return None
    
    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------")
        for product in self._products:
            product.display_information()
            print("------------------------------------")

    def save(self, filename):
        inventory_data = []
        for product in self._products:
            product_data = {
                "product_id": product.product_id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock
            }
            if isinstance(product, PhysicalProduct):
                product_data["type"] = "Physical"
                product_data["weight"] = product.weight
            elif isinstance(product, DigitalProduct):
                product_data["type"] = "Digital"
                product_data["download_size"] = product.download_size
            inventory_data.append(product_data)

        with open(filename, 'w') as file:
            json.dump(inventory_data, file, indent=4)

        print("Inventory saved successfully.")

    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                inventory_data = json.load(file)

            for product_data in inventory_data:
                if product_data["type"] == "Physical":
                    product = PhysicalProduct(
                        product_id=product_data["product_id"],
                        name=product_data["name"],
                        price=product_data["price"],
                        stock=product_data["stock"],
                        weight=product_data["weight"]
                    )
                elif product_data["type"] == "Digital":
                    product = DigitalProduct(
                        product_id=product_data["product_id"],
                        name=product_data["name"],
                        price=product_data["price"],
                        stock=product_data["stock"],
                        download_size=product_data["download_size"]
                    )
                self.add_product(product)
            print("Inventory loaded successfully.")
        except FileNotFoundError:
            print("Inventory file not found. Starting with an empty inventory.")    

def add_product(inventory):
    print("\nAdd New Product")
    print("1. Physical Product")
    print("2. Digital Product")
    product_type = input("Select product type (1 or 2): ")

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
 
    if product_type == "1":
        weight = float(input("Weight(kg): "))
        product = PhysicalProduct(product_id, name, price, stock, weight)
    elif product_type == "2":
        download_size = float(input("Download Size(MB): "))
        product = DigitalProduct(product_id, name, price, stock, download_size)
    else:
        print("Invalid product type.")
        return

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
    print(f"Name: {product.name}")
    print(f"Current Stock: {product.stock}")
    quantity = int(input("\nQuantity to add (use negative to remove): "))
    product.update_stock(quantity)
    print(f"Stock is now: {product.stock}")
def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
 
    if product is None:
        print("\nProduct not found.")
    else:
        print("\nProduct Found:")
        product.display_information()
        print(product.get_fulfilment_info())
        if isinstance(product, CanBeShipped):
            print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")

#main
file_name = "inventory.json"

print("============================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("============================================")
 
inventory = Inventory()
inventory.load(file_name)
 
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
        inventory.save(file_name)
    elif choice == "6":
        print("\nSaving inventory before exit...")
        inventory.save(file_name)
        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("\nInvalid option.")

