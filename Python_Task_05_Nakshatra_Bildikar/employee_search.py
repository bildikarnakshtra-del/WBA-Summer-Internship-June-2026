employees = ["John", "Alice", "David", "Sophia", "Michael"]

name = input("Enter name to search: ")

found = False

for employee in employees:
    if employee == name:
        found = True

if found:
    print("Record Found")
else:
    print("Record Not Found")
    