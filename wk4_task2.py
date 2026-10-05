FILENAME = "orders.txt"

# Each line in orders.txt is stored as: order_id,product,quantity
# Example: 1001,Wireless Mouse,2


# 1 & 2. Open and read the file
def read_orders(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        # If the file doesn't exist yet, start with an empty order list
        lines = []
    return lines


# 3. Get max id from the existing orders
def get_max_id(lines):
    if not lines:
        return 1000  # starting point if no orders exist yet

    max_id = 0
    for line in lines:
        order_id = int(line.split(",")[0])
        if order_id > max_id:
            max_id = order_id
    return max_id


# 4. Generate a new id
def generate_new_id(max_id):
    return max_id + 1


# 5. Append one new order to the list
def append_order(lines, new_id, product, quantity):
    new_order = f"{new_id},{product},{quantity}\n"
    lines.append(new_order)
    return lines


# 6. Write the updated list back to the file
def write_orders(filename, lines):
    with open(filename, "w") as file:
        file.writelines(lines)


# ---- Run the task ----
orders = read_orders(FILENAME)
print("Existing orders:")
for order in orders:
    print(order.strip())

max_id = get_max_id(orders)
new_id = generate_new_id(max_id)
print(f"\nMax ID found: {max_id}")
print(f"New ID generated: {new_id}")

orders = append_order(orders, new_id, "Laptop Stand", 3)
write_orders(FILENAME, orders)

print(f"\nNew order (ID {new_id}) added and saved to {FILENAME}")
print("\nFinal orders.txt contents:")
for order in orders:
    print(order.strip())