employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

total_salary = 0
count_below_40000 = 0

highest_paid = employees[0]

print("Employees earning above ₹50,000:")

for name, salary in employees:
    total_salary += salary

    if salary > 50000:
        print(name, "-", salary)

    if salary < 40000:
        count_below_40000 += 1

    if salary > highest_paid[1]:
        highest_paid = (name, salary)

print("\nHighest-Paid Employee:", highest_paid[0], "-", highest_paid[1])

print("Total Salary Expenditure: ₹", total_salary)

print("Employees earning below ₹40,000:", count_below_40000)