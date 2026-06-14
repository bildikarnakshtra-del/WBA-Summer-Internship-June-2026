# Pattern 1
i = 1
while i <= 5:
    print("*" * i)
    i = i + 1

print()

# Pattern 2
i = 5
while i >= 1:
    print("*" * i)
    i = i - 1

print()

# Pattern 3
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1
