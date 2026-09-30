def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            total_inventory = int(lines[0].strip())
            transaction_history = []
            for line in lines[1:]:
                transaction_history.append(int(line.strip()))

            return total_inventory, transaction_history

    except FileNotFoundError:
        return 0, []

def save_inventory(total_inventory, transaction_history):
    with open("inventory.txt", "w") as file:
        file.write(str(total_inventory) + "\n")
        for transaction in transaction_history:
            file.write(str(transaction) + "\n")

total_inventory, transaction_history = load_inventory()
print("Current total inventory:", total_inventory)

while True:
    user_input = input("Enter transaction amount (or 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        save_inventory(total_inventory, transaction_history)
        print("Inventory saved.")
        break

    try:
        transaction_amount = int(user_input)
        total_inventory += transaction_amount
        transaction_history.append(transaction_amount)
        print("Transaction added:", transaction_amount)
        print("Updated total inventory:", total_inventory)

    except ValueError:
        print("Error: Please enter a valid whole number.")





