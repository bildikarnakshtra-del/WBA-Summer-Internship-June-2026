password = "admin123"
attempts = 3

while attempts > 0:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access Granted")
        break
    else:
        attempts = attempts - 1
        print("Wrong Password")

if attempts == 0:
    print("Account Locked")
