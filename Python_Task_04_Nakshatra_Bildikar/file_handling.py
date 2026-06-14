print("Student Data File System")

file = open("student_data.txt", "w")

name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
marks = input("Enter Marks: ")

file.write("Student Record\n")
file.write("Name: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.write("Branch: " + branch + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("\nData saved successfully!")

print("\nReading file...\n")

file = open("student_data.txt", "r")
print(file.read())
file.close()
