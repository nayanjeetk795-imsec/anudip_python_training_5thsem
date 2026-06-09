# Vehicle Number Plate Verification

vehicle_no = "MH12AB4589"

# 1. Extract state code
state_code = vehicle_no[0:2]

# 2. Extract district code
district_code = vehicle_no[2:4]

# 3. Extract vehicle series
series = vehicle_no[4:6]

# 4. Extract vehicle number
vehicle_number = vehicle_no[6:10]

# 5. Count letters and digits separately
letters = 0
digits = 0

for ch in vehicle_no:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

# 6. Verify number plate format
is_valid = (
    len(vehicle_no) == 10 and
    vehicle_no[0:2].isalpha() and
    vehicle_no[2:4].isdigit() and
    vehicle_no[4:6].isalpha() and
    vehicle_no[6:10].isdigit()
)

# 7. Display result
print("Vehicle Number:", vehicle_no)
print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)
print("Total Letters:", letters)
print("Total Digits:", digits)

if is_valid:
    print("Vehicle Number Status: Valid")
else:
    print("Vehicle Number Status: Invalid")