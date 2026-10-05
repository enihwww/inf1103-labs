def calculate(a, b):
    return a + b, a * b

sum_value, product_value = calculate(4, 5)
print(sum_value)
print(product_value)

value = calculate(10, 20)
print(value) #outputs (30, 200)

#want to calculate the unknown prices
def calculate_total(*prices):
    return sum(prices)

print(calculate_total(20, 15, 30))
print(calculate_total(10, 15, 30, 40, 50))

discount = 0
def calculate_discount(price):
    global discount
    discount = price * 0.10
    return discount

print(calculate_discount(100))
print(discount)   # NameError: name 'discount' is not defined

def calculate(a, b):
    total = a + b

result = calculate(3, 4)
print(result)