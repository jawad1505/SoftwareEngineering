# [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
# target = 108



def find_duplicate(data):
    for x in range(len(data)-1):
        if data[x] == data[x+1]:
            return data[x]
    return None



def find(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        # print(data[mid], " mid=",mid, " low=",low, " high=", high)
        
        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if data[mid - 1]  != target:
                
                return mid
            high = mid -1
    return "Not found"

A = [-14, -10, 2, 108, 240, 243, 285, 285, 285, 401]
print(A)
print("Length =", len(A))
# print(find_duplicate(A))
print(find(A, 108))
