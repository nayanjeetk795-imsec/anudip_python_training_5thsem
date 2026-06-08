# Employee Performance Dashboard

performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp, end=" ")
print()

# 2. Count employees needing improvement (score < 60)
count = 0
for score in performance.values():
    if score < 60:
        count += 1
print("Employees Needing Improvement:", count)

# 3. Find the top performer
top_emp = max(performance, key=performance.get)
print("Top Performer:", top_emp, f"({performance[top_emp]})")

# 4. Calculate average performance score
average = sum(performance.values()) / len(performance)
print("Average Score:", round(average, 1))

# 5. Create separate lists
excellent = []
good = []
average_list = []
poor = []

for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif 75 <= score <= 89:
        good.append(emp)
    elif 60 <= score <= 74:
        average_list.append(emp)
    else:
        poor.append(emp)

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average_list)
print("Poor:", poor)