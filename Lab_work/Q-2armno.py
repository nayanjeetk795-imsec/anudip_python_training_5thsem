# WAP to accept a number from the user and check whether it is an Armstrong number

num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum = armstrong_sum + digit ** digits
    temp = temp // 10

if armstrong_sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")