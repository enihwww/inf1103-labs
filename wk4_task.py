# 1. Open file
with open("orders.txt", "r") as file:
    orders = file.readlines()

# 2. Read file
print(orders)

# 3. Get max ID
max_id = 0

for order in orders:
    #order will be ["1001,Wireless Mouse,20"]
    #split the order string by comma to get the order_id
    #[0] is the first element of the split list, which is the order_id
    #int cuz "1001" is a string
    order_id = int(order.split(",")[0])
    if order_id > max_id:
        max_id = order_id

# 4. Generate new ID
new_id = max_id + 1

# 5. Append one order
new_order = f"{new_id},Laptop Bag,30.00\n"
orders.append(new_order)

# 6. Write to file
with open("orders.txt", "w") as file:
    file.writelines(orders)