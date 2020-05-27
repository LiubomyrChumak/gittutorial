from random import random
n= 13
lst = []
for i in range(n):
    lst.append(int(random()*100))
lst.sort()
print(lst)

number = int(input())

low = 0
high = n-1
while low <= high:
    mid = (low + high) // 2
    if number < lst[mid]:
        high = mid - 1
    elif number > lst[mid]:
        low = mid + 1
    else:
        print(mid)
        break
else:
    print("No the number")
