students = []

while True:
    print()
    print("==========================")
    print("Student Security Manager")
    print("==========================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Security Assessment")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        student_id = input("Enter Student ID: ")
        branch = input("Enter Branch: ")
        email = input("Enter Email Address: ")

        student = {
            "name": name,
            "id": student_id,
            "branch": branch,
            "email": email
        }

        students.append(student)

        print("Student Added Successfully")

    elif choice == "2":
        if len(students) == 0:
            print("No Student Records Found")
        else:
            for student in students:
                print()
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Branch:", student["branch"])
                print("Email:", student["email"])

    elif choice == "3":
        print("Search Student")

    elif choice == "4":
        print("Delete Student")

    elif choice == "5":
        print("Security Assessment")

    elif choice == "6":
        print("Generate Report")

    elif choice == "7":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")