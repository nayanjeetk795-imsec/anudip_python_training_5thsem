salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# 1. Employees earning above ₹60,000
print("Employees earning above ₹60,000:")
for emp, sal in salary.items():
    if sal > 60000:
        print(emp, sal)

print("\n")

# 2. Count employees earning below ₹40,000
count_low = 0
for sal in salary.values():
    if sal < 40000:
        count_low += 1

print("Employees earning below ₹40,000:", count_low)
print("\n")

# 3. Highest-paid employee
top_emp = max(salary, key=salary.get)
print("Highest-paid employee:", top_emp, salary[top_emp])
print("\n")

# 4. Employees eligible for bonus (> ₹50,000)
bonus_list = []
for emp, sal in salary.items():
    if sal > 50000:
        bonus_list.append(emp)

print("Employees eligible for bonus:", bonus_list)
print("\n")

# 5. Average salary
total = sum(salary.values())
avg = total / len(salary)

print("Average salary:", avg)