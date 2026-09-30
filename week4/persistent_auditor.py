def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            total_inventory = int(lines[0].strip())
            return total_inventory

    except FileNotFoundError:
        return 0

total_inventory = load_inventory()
transaction_history = []
print("Current total inventory:", total_inventory)

while True:
    user_input = input("Enter transaction amount (or 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        break

    try:
        transaction_amount = int(user_input)
        total_inventory += transaction_amount
        transaction_history.append(transaction_amount)
        print("Transaction added:", transaction_amount)
        print("Updated total inventory:", total_inventory)

    except ValueError:
        print("Error: Please enter a valid whole number.")





