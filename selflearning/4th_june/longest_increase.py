n = int(input("Enter the number of elements: "))

max_len = 1
current_len = 1

prev = int(input("Enter number 1: "))

for i in range(1, n):
    num = int(input(f"Enter number {i + 1}: "))

    if num > prev:
        current_len += 1
    else:
        current_len = 1

    if current_len > max_len:
        max_len = current_len

    prev = num

print("Longest increasing sequence length =", max_len)