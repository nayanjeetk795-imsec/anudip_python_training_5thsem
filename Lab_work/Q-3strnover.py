# WAP to check whether a number is a Strong Number or not

num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10

    # Find factorial of the digit
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10

if sum == num:
    print("Strong Number")
else:
    print("Not a Strong Number")