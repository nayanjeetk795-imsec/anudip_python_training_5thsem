scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# 1. Players scoring 50 or more runs
print("Players scoring 50 or more runs:")
for player, runs in scores.items():
    if runs >= 50:
        print(player, runs)

print("\n")

# 2. Count centuries (100