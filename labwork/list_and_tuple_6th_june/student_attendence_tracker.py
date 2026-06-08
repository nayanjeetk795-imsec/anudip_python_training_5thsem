ttendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

present = 0
absent = 0
absent_positions = []

for i in range(len(attendance)):
    if attendance[i] == 'P':
        present += 1
    else:
        absent += 1
        absent_positions.append(i + 1)  # Day numbers start from 1

attendance_percentage = (present / len(attendance)) * 100

print("Present Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", attendance_percentage, "%")

if attendance_percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

print("Absent on Days:", absent_positions)