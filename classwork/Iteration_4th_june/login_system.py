print("--------------- Login System ------------------")

correct_password = "admin123"

# User enters the password
while True:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Login successful")
        break
    else:
        print("Incorrect password. Try Again.")