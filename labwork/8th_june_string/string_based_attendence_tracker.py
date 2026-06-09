# String-Based Attendance Tracker

attendance = "PPAPPPAAPPPPAPP"

# 1. Count Present and Absent days
present_days = attendance.count('P')
absent_days = attendance.count('A')

# 2. Calculate attendance percentage
total_days = len(attendance)
attendance_percentage = (present_days / total_days) * 100

# 3. Find longest consecutive streak of Presence
current_present = 0
longest_present = 0

for ch in attendance:
    if ch == 'P':
        current_present += 1
        if current_present > longest_present:
            longest_present = current_present
    else:
        current_present = 0

# 4. Find longest consecutive streak of Absence
current_absent = 0
longest_absent = 0

for ch in attendance:
    if ch == 'A':
        current_absent += 1
        if current_absent > longest_absent:
            longest_absent = current_absent
    else:
        current_absent = 0

# 5. Determine attendance status
if attendance_percentage < 75:
    status = "Below 75%"
else:
    status = "75% or Above"

# Display results
print("Attendance Record:", attendance)
print("Present Days:", present_days)
print("Absent Days:", absent_days)
print("Attendance Percentage:", round(attendance_percentage, 2), "%")
print("Longest Present Streak:", longest_present)
print("Longest Absent Streak:", longest_absent)
print("Attendance Status:", status)