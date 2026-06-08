units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# 1. Houses consuming more than 300 units
print("Houses consuming more than 300 units:")
for house, unit in units.items():
    if unit > 300:
        print(house, unit)

print("\n")

# 2. Count houses consuming less than 200 units
count_low = 0
for unit in units.values():
    if unit < 200:
        count_low += 1

print("Houses consuming less than 200 units:", count_low)
print("\n")

# 3. House with highest consumption
max_house = max(units, key=units.get)
print("Highest consumption:", max_house, units[max_house])
print("\n")

# 4. Energy-saving awareness campaign (> 400 units)
campaign = []
for house, unit in units.items():
    if unit > 400:
        campaign.append(house)

print("Campaign houses (>400 units):", campaign)
print("\n")

# 5. Categorization
print("House Categories:")
for house, unit in units.items():
    if unit < 200:
        category = "Low"
    elif 200 <= unit <= 350:
        category = "Medium"
    else:
        category = "High"
    
    print(house, ":", unit, "->", category)