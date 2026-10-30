import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

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

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self._weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight} kg")

product = PhysicalProduct("P001", "Laptop", 999.99, 10, 2.5)
product.display_information()