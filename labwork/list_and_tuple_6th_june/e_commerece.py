orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# 1. Display products costing more than ₹1000
print("Products costing more than ₹1000:")
for product in orders:
    if product[1] > 1000:
        print(product)

# 2. Find the most expensive product
expensive = orders[0]

for product in orders:
    if product[1] > expensive[1]:
        expensive = product

print("\nMost Expensive Product:")
print(expensive)

# 3. Calculate total order value
total = 0

for product in orders:
    total += product[1]

print("\nTotal Order Value:", total)

# 4. Count products costing below ₹1000
count = 0

for product in orders:
    if product[1] < 1000:
        count += 1

print("\nProducts costing below ₹1000:", count)
