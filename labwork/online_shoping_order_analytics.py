# Online Shopping Order Analytics

sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product, qty in sales.items():
    if qty > 20:
        print(product, end=" ")
print()

# 2. Find the best-selling product
best_product = max(sales, key=sales.get)
print("Best Selling Product:", best_product, f"({sales[best_product]})")

# 3. Find the least-selling product
least_product = min(sales, key=sales.get)
print("Least Selling Product:", least_product, f"({sales[least_product]})")

# 4. Calculate total products sold
total_sold = sum(sales.values())
print("Total Units Sold:", total_sold)

# 5. Create a list of products requiring promotion (sales < 15)
promotion = [product for product, qty in sales.items() if qty < 15]
print("Products Requiring Promotion:", promotion)

# 6. Count products having sales between 10 and 30
count = 0
for qty in sales.values():
    if 10 <= qty <= 30:
        count += 1

print("Products Having Sales Between 10 and 30:", count)