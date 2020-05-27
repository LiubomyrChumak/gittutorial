lst = [3, 5, 67, -65, 34, 21]

maximum = lst[0]
for i in range(1, len(lst)):
    if lst[i] > maximum:
        maximum = lst[i]
print(maximum)

lst = [3, 5, 67, -65, 34, 21]

minimum = lst[0]
for i in range(1, len(lst)):
    if lst[i] < minimum:
        minimum = lst[i]
print(minimum)


