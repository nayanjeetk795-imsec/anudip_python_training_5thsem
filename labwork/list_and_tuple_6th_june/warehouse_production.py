products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0

print("Failed Product IDs:")

for pid, status in products:
    if status == "Fail":
        print(pid)
        fail_count += 1
    else:
        pass_count += 1

pass_percentage = (pass_count / len(products)) * 100

print("\nPassed Products:", pass_count)
print("Failed Products:", fail_count)
print("Pass Percentage:", pass_percentage, "%")