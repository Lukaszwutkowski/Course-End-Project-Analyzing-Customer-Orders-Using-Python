# Task 1: Store Customers Orders

#  List of customers (name)
customers = ["Erik", "Emma", "Lars", "Sophie", "Ingrid", "Oliver", "Astrid"]

#  List of order details as tuples (customer_name, product, price, category)
orders = [
    ("Erik", "Laptop", 899.99, "Electronics"),
    ("Erik", "T-shirt", 29.99, "Clothing"),
    ("Emma", "Headphones", 79.99, "Electronics"),
    ("Emma", "Jeans", 59.99, "Clothing"),
    ("Emma", "Pillow", 24.99, "Home Essentials"),
    ("Lars", "Smartphone", 699.99, "Electronics"),
    ("Lars", "Dress", 89.99, "Clothing"),
    ("Sophie", "Lamp", 45.00, "Home Essentials"),
    ("Sophie", "Towel Set", 35.00, "Home Essentials"),
    ("Ingrid", "Tablet", 349.99, "Electronics"),
    ("Ingrid", "Sneakers", 120.00, "Clothing"),
    ("Ingrid", "Blender", 89.99, "Home Essentials"),
    ("Oliver", "USB Cable", 12.99, "Electronics"),
    ("Oliver", "Socks", 9.99, "Clothing"),
    ("Astrid", "Smart Watch", 199.99, "Electronics"),
    ("Astrid", "Jacket", 149.99, "Clothing"),
    ("Astrid", "Curtains", 79.99, "Home Essentials"),
]

#  Dictionary: key = customer_name, value = list of ordered products
customer_products = {}

for order in orders:
    customer_name = order[0]
    product_name = order[1]

    if customer_name in customer_products:
        customer_products[customer_name].append(product_name)
    else:
        customer_products[customer_name] = [product_name]

# --------- OUTPUT ---------

print("=" * 20)
print("TASK 1: Store Customer Orders")
print("=" * 20)

print("\n1. Customer list:")
print(customers)

print("\n2. Orders:")
for order in orders:
    print(f"{order}")

print("\n3. Products per customer:")
for customer, products in customer_products.items():
    print(f"{customer}: {products}")

#  Task 2: Classify Products by Category

#  Mapping product -> category
product_category = {}

for order in orders:
    product = order[1]
    category = order[3]

    product_category[product] = category

#  Set of unique product categories
categories = set()

for order in orders:
    categories.add(order[3])

# ---------- OUTPUT -----------
print("\n")
print("=" * 20)
print("TASK 2: Store Customer Orders")
print("=" * 20)

print("\n1. Product -> Category:")
for product, category in product_category.items():
    print(f"{product}: {category}")

print("\n2. unique categories:")
print(f"{categories}")

print("\n3. Product categories:")
for category in categories:
    print(f"{category}")


#  Task 3: Analyze Customer Orders

#  Total spending $ per customer
customer_spending = {}

for order in orders:
    customer = order[0]
    price = order[2]

    if customer in customer_spending:
        customer_spending[customer] += price
    else:
        customer_spending[customer] = price

#  Classification of customers based on total $ spending
customer_classification = {}

for customer, total in customer_spending.items():
    if total > 100:
        customer_classification[customer] = "high-value"
    elif total > 50:
        customer_classification[customer] = "moderate"
    else:
        customer_classification[customer] = "low-value"

# ------------- OUTPUT ---------------
print("\n")
print("=" * 20)
print("TASK 3: Analyze Customer Orders")
print("=" * 20)

print("\n1. Total $ per customer:")
for customer, total in customer_spending.items():
    print(f"{customer}: {total}")

print("\n2. Customer classification:")
for customer, classification in customer_classification.items():
    total = customer_spending[customer]
    print(f"{customer}: {classification} (${total})")