# Solution 1: 
def interection_array_python(A, B):
    return set(A).intersection(B)

# Solution 2: 
def interction_array(A, B):
    inter = list()
    for x in A:
        for y in B:
            if x == y:
                inter.append(x)
    return inter

# Solution 3: 2 pointers
def intersection_array_pointers(A, B):
    i, j = 0,0
    # inter = set()
    inter = list()
    
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i +=1
        elif B[j] < A[i]:
            j +=1
        elif A[i] == B[j]:
            if  A[i] != A[i-1]:
                # inter.add(A[i])
                inter.append(A[i])
            i +=1
            j +=1
        
    return inter

A = [1, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

# print(interction_array(A, B)) # 4, 5
# print(interection_array_python(A, B))
print(intersection_array_pointers(A, B))