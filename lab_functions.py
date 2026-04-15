def initialize_inventory(products):
    products = ["manzanas", "sandía", "banana", "fresas", "melón"]
    inventory = {}
    for product in products:
        quantity = int(input(f"Enter the quantity of {product}: "))
        inventory[product] = quantity
    return inventory

def get_customer_orders():
    customer_orders = set()
    add_more = "yes"
    while add_more == "yes":
        product = input("Enter a product name: ")
        customer_orders.add(product)
        add_more = input("Do you want to add another product? (yes/no): ")
    return customer_orders

def update_inventory(customer_orders, inventory):
    for product in customer_orders:
        if product in inventory:
            inventory[product] -= 1
    return inventory

def calculate_order_statistics(customer_orders, products):
    total_ordered = len(customer_orders)
    percentage = (total_ordered / len(products)) * 100
    return total_ordered, percentage

def print_order_statistics(order_statistics):
    total, percentage = order_statistics
    print("\nOrder Statistics:")
    print(f"Total Products Ordered: {total}")
    print(f"Percentage of Products Ordered: {percentage:.2f}%")

def print_updated_inventory(inventory):
    print("\nUpdated Inventory:")
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")

# --- Programa principal ---
products = ["manzanas", "sandía", "banana", "fresas", "melón"]

inventory = initialize_inventory(products)
customer_orders = get_customer_orders()
inventory = update_inventory(customer_orders, inventory)
order_statistics = calculate_order_statistics(customer_orders, products)
print_order_statistics(order_statistics)
print_updated_inventory(inventory)