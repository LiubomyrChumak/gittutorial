A = [1,3,5,4,6,7,2,8,9,0,81,42,54,67,17,43,72,86,45,87,95]
leng = len(A)
j= 2
i = 1
while i <leng:
    if A[i-1]<=A[i]:
        i = j
        j = j+1
    else:
        A[i-1],A[i] = A[i],A[i-1]
        i = i-1
        if i == 0:
            i = j
            j = j+1
print(A)

