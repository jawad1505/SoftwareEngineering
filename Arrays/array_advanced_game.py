def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        # print("f = ",furthest_reached,  ", i = ", i, ", A[",i,"]","=",A[i] )
        i += 1
        
    return furthest_reached >= last_idx

A = [2, 0, 0, 1, 3, 0, 3]
print(array_advance(A))

# A = [2, 4, 1, 1, 0, 2, 3]
# print(array_advance(A))

# # True: Possible to navigate to last index in A:
# # Moves: 1,3,2
# A = [3, 3, 1, 0, 2, 0, 1]
# print(array_advance(A))

# # False: Not possible to navigate to last index in A:
# A = [3, 2, 0, 0, 2, 0, 1]
# print(array_advance(A))