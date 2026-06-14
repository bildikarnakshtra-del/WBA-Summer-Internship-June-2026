print("Password Vault System")

file = open("vault.txt", "a")

website = input("Enter Website: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

file.write("Website: " + website + "\n")
file.write("Username: " + username + "\n")
file.write("Password: " + password + "\n")
file.write("------------------------\n")

file.close()

print("\nData saved successfully!")

print("\nStored Records:\n")

file = open("vault.txt", "r")
print(file.read())
file.close()
