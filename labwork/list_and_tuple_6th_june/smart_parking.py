slots = [1, 0, 1, 1, 0, 0, 1, 0]

occupied = 0
available = 0
available_slots = []

for i in range(len(slots)):
    if slots[i] == 1:
        occupied += 1
    else:
        available += 1
        available_slots.append(i + 1)  # Slot numbers start from 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# Find first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("First Available Slot:", i + 1)
        break

print("Available Slot Numbers:", available_slots)

# Check occupancy percentage
occupancy_percentage = (occupied / len(slots)) * 100

print("Occupancy Percentage:", occupancy_percentage, "%")

if occupancy_percentage > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")