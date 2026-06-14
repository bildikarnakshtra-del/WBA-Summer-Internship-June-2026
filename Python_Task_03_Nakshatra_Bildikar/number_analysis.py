n = int(input("Enter a number: "))

sum = 0
even = 0
odd = 0

i = 1

while i <= n:
    sum = sum + i

    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    i = i + 1

print("Sum =", sum)
print("Even Numbers =", even)
print("Odd Numbers =", odd)
