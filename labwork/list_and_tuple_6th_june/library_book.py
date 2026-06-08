books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

available_count = 0

print("Unavailable Books:")
for title, copies in books:
    if copies == 0:
        print(title)

print("\nBooks with more than 2 copies:")
for title, copies in books:
    if copies > 2:
        print(title, "-", copies, "copies")

for title, copies in books:
    if copies > 0:
        available_count += 1

print("\nAvailable Books Count:", available_count)

# Search for a requested book
requested_book = input("\nEnter the book name to search: ")

for title, copies in books:
    if title.lower() == requested_book.lower():
        print("Book found:", title)
        break
else:
    print("Book not found")