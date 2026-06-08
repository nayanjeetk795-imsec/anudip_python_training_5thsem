contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# 1. Display all contact names in alphabetical order
print("Contacts in alphabetical order:")
for name in sorted(contacts):
    print(name)

print("\n")

# 2. Count total number of contacts
print("Total contacts:", len(contacts))
print("\n")

# 3. Search for a given contact name
search_name = input("Enter name to search: ")

found = False
for name, number in contacts.items():
    if name == search_name:
        print("Contact found:", name, number)
        found = True
        break   # stop search once found

if not found:
    print("Contact not found")

print("\n")

# 4. Contacts whose names start with a vowel
vowels = ['A', 'E', 'I', 'O', 'U']
vowel_contacts = []

for name in contacts:
    if name[0].upper() in vowels:
        vowel_contacts.append(name)

print("Contacts starting with vowel:", vowel_contacts)