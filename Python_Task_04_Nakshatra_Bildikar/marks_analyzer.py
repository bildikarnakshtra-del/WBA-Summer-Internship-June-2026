print("Marks Analysis System")

marks = []

for i in range(5):
    m = float(input("Enter marks for subject: "))
    marks.append(m)

total = 0

for i in marks:
    total = total + i

percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("\nTotal Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
