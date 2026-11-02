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

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self._weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight} kg")

    def get_fulfilment_info(self):
        print("This product requires physical shipping.")

    def calculate_shipping_cost(self):
        base_cost = 5.00
        cost_per_kg = 7.00
        return base_cost + (cost_per_kg * self._weight)

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size} MB")

    def get_fulfilment_info(self):
        print("This product is delivered digitally via download link.")

physical = PhysicalProduct("P001", "Laptop", 999.99, 10, 2.5)
digital = DigitalProduct("D001", "Antivirus Software", 49.99, 100, 350)
physical.display_information()
physical.get_fulfilment_info()
digital.display_information()
digital.get_fulfilment_info()

laptop = PhysicalProduct("P001", "Laptop", 999.99, 10, 2.5)
monitor = PhysicalProduct("P002", "Monitor", 299.99, 5, 6.0)
mouse = PhysicalProduct("P003", "Mouse", 25.50, 40, 0.2)

print(f"Laptop shipping: ${laptop.calculate_shipping_cost():.2f}")
print(f"Monitor shipping: ${monitor.calculate_shipping_cost():.2f}")
print(f"Mouse shipping: ${mouse.calculate_shipping_cost():.2f}")