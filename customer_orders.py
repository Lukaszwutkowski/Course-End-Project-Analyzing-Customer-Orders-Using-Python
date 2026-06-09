# Task 1: Store Customers Orders
from unittest.util import sorted_list_difference

#  Create a list of customer names --- List of customers (name)
customers = ["Erik", "Emma", "Lars", "Sophie", "Ingrid", "Oliver", "Astrid"]

#  Store each customer's order details (customer name, product, price, category) as
# tuples inside a list --- List of order details as tuples (customer_name, product, price, category)
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

#  Use a dictionary where keys are customer names and values are lists of ordered
# products --- Dictionary: key = customer_name, value = list of ordered products
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

#  Use a dictionary to map each product to its respective category --- Mapping product -> category
product_category = {}

for order in orders:
    product = order[1]
    category = order[3]

    product_category[product] = category

#  Create a set of unique product categories --- Set of unique product categories
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

#  Use a loop to calculate the total amount each customer spends --- Total spending $ per customer
customer_spending = {}

for order in orders:
    customer = order[0]
    price = order[2]

    if customer in customer_spending:
        customer_spending[customer] += price
    else:
        customer_spending[customer] = price

#  If the total purchase value is above $100, classify the customer as a high-value buyer,
#  If it is between $50 and $100, classify the customer as a moderate buyer,
#  If it is below $50, classify them as a low-value buyer
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

# Task 4: Generate business insights

# Calculate the total revenue per product category and store it in a dictionary
category_revenue = {}

for order in orders:
    category = order[3]
    price = order[2]

    if category in category_revenue:
        category_revenue[category] += price
    else:
        category_revenue[category] = price

# Extract unique products from all orders using a set
unique_products = set()

for order in orders:
    unique_products.add(order[1])

# Use a list comprehension to find all customers who purchased electronics
electronics_buyers = [
    order[0] for order in orders if "Electronics" in order[3]
]

#  Identify the top three highest-spending customers using sorting
sorted_customers = sorted(
    customer_spending.items(),
    key=lambda x: x[1],
    reverse=True,
)

top_three_customers = sorted_customers[:3]

# ------- OUTPUT -----------
print("=" * 20)
print("TASK 4: Analyze Customer Orders")
print("=" * 20)

print("\n1. Total revenue per product category:")
for category, revenue in category_revenue.items():
    print(f"{category}: {revenue}")

print("\n2. Unique products from all orders:")
print(unique_products)

print("\n3. Electronics buyers:")
print(electronics_buyers)

print("\n4. Top 3 customers:")
print(top_three_customers)

# Task 5: Organize and display data

# Print a summary of each customer's total spending and their classification
print("\n")
print("=" * 20)
print("TASK 5: Organize and Display Data")
print("=" * 20)

print("\n1. Customer spending summary:")
for customer, total in customer_spending.items():
    classification = customer_classification[customer]
    print(f"{customer}: ${total:.2f} - {classification}")

# Use set operations to find customers who purchased from multiple categories
customer_categories = {}
for order in orders:
    customer = order[0]
    category = order[3]

    if customer in customer_categories:
        customer_categories[customer].append(category)
    else:
        customer_categories[customer] = [category]

multiple_category_customers = {
    customer
    for customer, categories in customer_categories.items()
    if len(categories) > 1
}

print("=" * 20)
print("\n2: Customers who purchased from multiple categories:")
print(multiple_category_customers)

# Identify common customers who bought both electronics and clothing
electronics_customers = set(electronics_buyers)
clothing_customers = {
    order[0]
    for order in orders
    if "Clothing" in order[3]
}

electronics_and_clothing_buyers = electronics_customers & clothing_customers
print("=" * 20)
print("\n3. Customer who bought both Electronics and Clothing:")
print(electronics_and_clothing_buyers)


# Identify common customers who bought both electronics and clothing
