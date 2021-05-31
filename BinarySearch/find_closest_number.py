def find_closest_number(data, target):
    '''
    Returns closest number if found
    data   = [10, 20, 30, 40, 50]
    input  = 22
    output = 20
    '''
    low = 0
    high = len(data) - 1
    min_diff = float('inf')
    closest_num = None

    # Edge cases for empty list of list
    # with only one element:
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high) // 2

        # Ensure you do not read beyond the bounds
        # of the list.    
        if mid+1 < len(data):
            min_diff_right = abs(data[mid+1]  - target)
        if mid > 0:
            min_diff_left  = abs(data[mid-1]  - target)

        # Check if the absolute value between left
        # and right elements are smaller than any
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[mid-1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[mid + 1]
       
        # Move the mid-point appropriately as is done
        # via binary search.
        # print("mid = ",data[mid], " target= ",target, "mid =",mid, " high=",high, " low=",low, " closest=",closest_num)
        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
            if high < 0:
                return data[mid]
        else:
            return data[mid]
    return closest_num
        
            




    
    

A = [10, 21, 31, 41, 51, 61, 71, 81, 91]
print(find_closest_number(A,11))