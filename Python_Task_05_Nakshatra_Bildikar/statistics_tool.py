numbers = []

for i in range(10):
    num = int(input())
    numbers.append(num)

largest = numbers[0]
smallest = numbers[0]
total = 0
even_count = 0
odd_count = 0

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    total = total + num

    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

average = total / 10

print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("Sum:", total)
print("Average:", average)
print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)
