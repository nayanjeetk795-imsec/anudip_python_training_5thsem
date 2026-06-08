passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed_count = 0
waiting_count = 0

confirmed_list = []
waiting_list = []

print("Waiting-List Passengers:")

for name, status in passengers:
    if status == "Waiting":
        print(name)
        waiting_count += 1
        waiting_list.append(name)
    else:
        confirmed_count += 1
        confirmed_list.append(name)

print("\nConfirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

# Check a specific passenger
search_name = input("\nEnter passenger name to check: ")

found = False

for name, status in passengers:
    if name.lower() == search_name.lower():
        found = True
        if status == "Confirmed":
            print(name, "has a confirmed ticket.")
        else:
            print(name, "is on the waiting list.")
        break

if not found:
    print("Passenger not found.")

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)