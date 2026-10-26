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

