inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# 1. Products with stock less than 10
print("Products with stock less than 10:")
for product, stock in inventory.items():
    if stock < 10:
        print(product, stock)

print("\n")

# 2. Count products having stock more than 50
count_high = 0
for stock in inventory.values():
    if stock > 50:
        count_high += 1

print("Products with stock more than 50:", count_high)
print("\n")

# 3. Product with minimum stock
min_product = min(inventory, key=inventory.get)
print("Product with minimum stock:", min_product, inventory[min_product])
print("\n")

# 4. Products