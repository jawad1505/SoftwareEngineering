def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f'low={low}  high={high}')        

        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
my_list = [1,2,3,4,5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(binary_search_iterative(my_list, 2))