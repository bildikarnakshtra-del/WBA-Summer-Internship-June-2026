logins = ["Success", "Failed", "Failed", "Success", "Failed", "Success"]

total_attempts = len(logins)
successful_logins = 0
failed_logins = 0

for login in logins:
    if login == "Success":
        successful_logins = successful_logins + 1
    else:
        failed_logins = failed_logins + 1

print("Total Attempts:", total_attempts)
print("Successful Logins:", successful_logins)
print("Failed Logins:", failed_logins)
