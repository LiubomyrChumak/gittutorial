

def insert_sort(A):
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
            print(A)
b = [10,22,43,34,21,56,78,45,32,12,14,18]

print(insert_sort(b))



