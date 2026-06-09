# Employee ID Analyzer

emp_id = "EMP2026ANUJ458"

# 1. Count uppercase letters
uppercase_count = 0
for ch in emp_id:
    if ch.isupper():
        uppercase_count += 1

# 2. Count digits
digit_count = 0
digit_list = []

for ch in emp_id:
    if ch.isdigit():
        digit_count += 1
        digit_list.append(int(ch))

# 3. Extract joining year
joining_year = emp_id[3:7]

# 4. Extract employee name
employee_name = emp_id[7:-3]

# 5. Check validity
is_valid = (
    emp_id.startswith("EMP") and
    joining_year.isdigit() and len(joining_year) == 4 and
    emp_id[-3:].isdigit() and len(emp_id[-3:]) == 3
)

# 6. List of all digits is already stored in digit_list

# 7. Sum of all digits
sum_digits = sum(digit_list)

# 8. Display results
print("Employee ID:", emp_id)
print("Uppercase Letters:", uppercase_count)
print("Digits:", digit_count)
print("Joining Year:", joining_year)
print("Employee Name:", employee_name)
print("Digit List:", digit_list)
print("Sum of Digits:", sum_digits)

if is_valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")