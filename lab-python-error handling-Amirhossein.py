products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
customer_orders = {}
def input_handler_initialize_inventory(item):
    quantity = int()
    try:
         quantity = int(input(f"How many {item}s are there in the inventory?"))
         if quantity < 0:
             raise ValueError("Invalid quantity. The number should not be negative.")
    except ValueError as error:
        print(f"*** error: {error} ***")
        quantity = input_handler_initialize_inventory(item)
    return quantity

def input_handler_calculate_total(item):
    input_price = float()
    try:
         input_price = float(input(f"what's the price of a {item}?"))
         if input_price < 0:
             raise ValueError("Invalid quantity. The price should not be negative.")
    except ValueError as error:
        print(f"*** error: {error} ***")
        input_price = input_handler_calculate_total(item)
    return input_price

def input_handler_customer_order_name(handler_inventory):
    
    try:
         input_order_name = input(f"What's your order? ")
         if input_order_name not in handler_inventory.keys() :
             raise ValueError("We don't have this product for sale.")
    except ValueError as error:
        print(f"*** error: {error} ***")
        input_order_name = input_handler_customer_order_name(handler_inventory)
    return input_order_name

def input_handler_customer_order_num(handler_inventory,item):
    
    try:
         input_order_num = int(input(f"How many of them? "))
         if input_order_num < 0 :
             raise ValueError("Invalid quantity.")
         elif input_order_num > handler_inventory[item]:
            raise ValueError(f"not enugh resources.{handler_inventory[item]} left")
    except ValueError as error:
        print(f"*** error: {error} ***")
        input_order_num = input_handler_customer_order_num(handler_inventory, item)
    return input_order_num   
   
def initialize_inventory(products_list):
  
    inventory = {item:input_handler_initialize_inventory(item) for item in products_list}
    return inventory

def get_customer_orders(inventory):
    order_invetory = inventory.copy()
    done_ordering = False
    while not(done_ordering):
        product = input_handler_customer_order_name(order_invetory)
        num = input_handler_customer_order_num(order_invetory, product)
        if product in customer_orders.keys():
            customer_orders[product] += num
        else:
            customer_orders[product] = num
        order_invetory[product] -= num 
        if input("Was it all? (yes or no) ") == 'yes':
              done_ordering = True

    return customer_orders, order_invetory

def calculate_order_statistics(inventory, customers_orders):
    total_products_ordered = sum(customer_orders.values()) 
    total_products = sum(inventory.values())
    percentage_of_products_ordered = round(total_products_ordered / total_products , 2)
    order_stat = (total_products_ordered, percentage_of_products_ordered)
    return order_stat

def print_order_statistics(order_stat):
    print("Order Statistics:")
    print(f"Total Products Ordered: {order_stat[0]}")
    print(f"Percentage of Products Ordered: {order_stat[1] * 100}%")

def print_updated_inventory(inventory):
    output = '\n'.join(f"{product}:{quantity}" for product,quantity in inventory.items() )
    print("Updated inventory has:",'\n' ,output)

def calculate_total_price(customer_orders):
    prices = [(item, input_handler_calculate_total(item)) for item in customer_orders.keys()]
    total_price = sum( [product[1] * customer_orders[product[0]] for product in prices])
    print(f"Total price is: {total_price}")


inventory = initialize_inventory(products)
customer_orders, updated_inventory = get_customer_orders(inventory)
order_statistic = calculate_order_statistics(inventory, customer_orders)
print_order_statistics(order_statistic)
inventory = updated_inventory
print_updated_inventory(updated_inventory)
calculate_total_price(customer_orders)


