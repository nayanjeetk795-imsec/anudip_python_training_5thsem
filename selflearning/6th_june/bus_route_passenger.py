passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# 1. Stops having more than 20 passengers
print("Stops with more than 20 passengers:")
for stop, count in passengers.items():
    if count > 20:
        print(stop, count)

print("\n")

# 2. Count stops with fewer than 10 passengers
low_count = 0
for count in passengers.values():
    if count < 10:
        low_count += 1

print("Stops with fewer than 10 passengers:", low_count)
print("\n")

# 3. Busiest stop
busiest_stop = max(passengers, key=passengers.get)
print("Busiest stop:", busiest_stop, passengers[busiest_stop])
print("\n")

# 4. Stops requiring extra bus (> 25 passengers)
extra_bus = []
for stop, count in passengers.items():
    if count > 25:
        extra_bus.append(stop)

print("Stops requiring extra bus:", extra_bus)
print("\n")

# 5. Average passengers
total = sum(passengers.values())
average = total / len(passengers)

print("Average passengers:", average)