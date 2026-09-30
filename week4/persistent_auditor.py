def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            total_inventory = int(lines[0].strip())
            return total_inventory

    except FileNotFoundError:
        return 0

total_inventory = load_inventory()
print("Current total inventory:", total_inventory)

