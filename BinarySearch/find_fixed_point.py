# Time Complexity O(n)
# Space Complexity O(1)

# A fixed point in an array A is an index i such that A[i] is equal to i.
def fixed_point_naive(data):
    for i in range(len(data)):
        # print(" i=",i," data=",data[i])
        if data[i] == i:
            return data[i]
    return None

def find_fixed_point_binary_search(data):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if data[mid] < mid:
            low = mid + 1
        elif data[mid] > mid:
            high = mid -1
        else:
            return data[mid]
    return None

# A = [-10, -5, 0, 3, 7]
# print(fixed_point_naive(A)) # 3
# print(find_fixed_point_binary_search(A)) # 1

# A = [0, 2, 5, 8, 17]
# print(find_fixed_point_binary_search(A)) # 1
# print(fixed_point_naive(A)) # 3

A = [-10, -5, 3, 4, 7, 9]
print(fixed_point_naive(A)) # 1
print(find_fixed_point_binary_search(A)) # 1
