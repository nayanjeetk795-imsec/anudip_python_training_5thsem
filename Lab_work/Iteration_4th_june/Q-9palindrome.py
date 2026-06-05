# Palindrome and Reverse Number Checker

num = int(input("Enter a number: "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reverse Number =", reverse)

if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")