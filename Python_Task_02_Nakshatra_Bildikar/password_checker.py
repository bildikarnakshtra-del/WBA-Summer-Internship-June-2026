password = input("Enter Password: ")

if len(password) >= 8:
    if "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
        print("Strong Password")
    else:
        print("Moderate Password")
else:
    print("Weak Password")
