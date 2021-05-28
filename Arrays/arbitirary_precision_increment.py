

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        # case 1: i  < 10
        if A[i] != 10:
            break
        
        # case 2: i >10
        A[i] = 0
        A[i-1] += 1

    # case 3: if first number 10
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

A = [9, 9, 9, 8, 9]
print(plus_one  (A))

A = [1, 9, 9]
print(plus_one  (A))

A = [1, 8, 9]
print(plus_one  (A))