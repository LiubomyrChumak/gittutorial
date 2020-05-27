A = [1,3,5,4,6,7,2,8,9,0,81,42,54,67,17,43,72,86,45,87,95]
leng = len(A)
i = 0
while i < leng -1:
    m = i
    j = i+1
    while j < leng:
        if A[j] < A[m]:
            m = j
            j+1
            A[i],A[m] = A[m],A[i]
print(A)
