username = input("Enter Username: ")
password = input("Enter Password: ")

stored_username = "admin"
stored_password = "password123"

if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Credentials")
