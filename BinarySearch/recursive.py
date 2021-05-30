def binary_search_recursive(data, target, low, high):
    
    if low > high:
        return False

    else:
        mid = (low + high) //2

        if target == data[mid]:
            return True

        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)

        else:
            return binary_search_recursive(data, target, low+1, high)

my_list = [1,2,3,4,5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
low = 0
high = len(my_list) - 1

num = 2
print(binary_search_recursive(my_list, num, low, high))

num = 200
print(binary_search_recursive(my_list, num, low, high))