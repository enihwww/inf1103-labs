total_inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip() #remove spaces

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Error: Please enter a valid whole number.")
        failed_entries += 1
        continue #skip the rest of this loop iteration and jump back to the top of the loop for the next input

    quantity = int(user_input)

    if quantity < 0:
        print("Error: Negative stock values are not allowed.")
        failed_entries += 1
        continue

    total_inventory += quantity

    if total_inventory > 500:
        print(f"ALERT: Overstock! Total inventory ({total_inventory}) exceeds 500 units.")
        break
    elif total_inventory == 500:
        print("Notice: Inventory has reached exactly 500 units.")
    else:
        print(f"Accepted. Current total inventory: {total_inventory}")

print("\n--- Inventory Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")