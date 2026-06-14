first = input("Enter first name: ")
last = input("Enter last name: ")
year = input("Enter birth year: ")

first = first.lower()
last = last.lower()

u1 = first + last + year
u2 = first[0] + "." + last + year[-2:]
u3 = last + "_" + first
u4 = first + "_" + year
u5 = first[:3] + last[:3] + year[-2:]

print("\nUsername Suggestions:")
print(u1)
print(u2)
print(u3)
print(u4)
print(u5)
