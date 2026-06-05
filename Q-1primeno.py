# Accept a number from the user
num = int(input("Enter a number: "))

count = 0

# Check how many factors the number has
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

# If a number has exactly 2 factors, it is prime
if count == 2:
    print("The number is Prime")
else:
    print("The number is Not Prime")
    print("Factors are:")

    # Display all factors
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
