def get_valid_input():
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip() 
    if user_input.lower() == "quit":
        return "quit"
    if not user_input.isdigit():
        print("Error: Please enter a valid whole number.")
        return None
    return int(user_input)

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax_rate = 0.10  #tax rate of 10%
    return amount * tax_rate

def generate_report(total_units, failed_attempts, deliveries_processed):
    print("\n--- Inventory Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    print(f"Total Deliveries Processed: {deliveries_processed}")

def main():
    total_inventory = 0
    failed_entries = 0
    deliveries_processed = 0
    tax_total = 0
    while True:
        quantity = get_valid_input()
        if quantity == "quit":
            break
        if quantity is None:
            failed_entries += 1
            continue

        #valid input, process the delivery
        total_inventory = process_delivery(total_inventory, quantity)
        deliveries_processed += 1
        tax_total += calculate_tax(quantity)
        print(f"Tax for this delivery: {tax_total:.2f}")
        if total_inventory > 500:
            print(f"ALERT: Overstock! Total inventory ({total_inventory}) exceeds 500 units.")
            break
        elif total_inventory == 500:
            print("Notice: Inventory has reached exactly 500 units.")
        else:
            print(f"Accepted. Current total inventory: {total_inventory}")

    generate_report(total_inventory, failed_entries, deliveries_processed)

if __name__ == "__main__":
    main()