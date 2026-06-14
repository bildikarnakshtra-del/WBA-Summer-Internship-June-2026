a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print("Largest Number =", a)
elif b >= a and b >= c:
    print("Largest Number =", b)
else:
    print("Largest Number =", c)
