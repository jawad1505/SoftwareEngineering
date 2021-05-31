def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2

        if A[mid] > A[high]:
            low  = mid + 1
        elif A[mid] <= A[high]: 
            high = mid

    return A[low]

A = [4, 5, 6, 7, 1, 2, 3]
print(find(A))

print("")
print((1+0) // 2)