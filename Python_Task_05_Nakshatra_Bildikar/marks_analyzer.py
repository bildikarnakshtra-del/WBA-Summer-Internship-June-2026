marks = []

for i in range(5):
    mark = int(input())
    marks.append(mark)

highest = marks[0]
lowest = marks[0]
total = 0

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    total = total + mark

average = total / 5

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
