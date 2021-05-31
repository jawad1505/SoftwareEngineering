# An array that starts off with increasing terms and then concludes with decreasing terms
# 1, 2, 3, 4, 5, 4, 3, 2, 1

def bitonic_peak_naive(data):

    peak = max(data)

    peak_index = data.index(peak)
    peak_left = peak_index - 1
    peak_right = peak_index + 1

    if peak_left < 0 or peak_right > len(data)-1:
        return "not bionic - out of range"
    elif data[peak_left] < data[peak_index] > data[peak_right]:
        return "bionic"
    else:
        return "not bionic"

def find_heighest_number(data):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        
        mid_left  = data[mid - 1] if mid - 1 > 0         else float("-inf")
        mid_right = data[mid + 1] if mid - 1 < len(data) else float(" inf")
        print(low, high, mid)

        if mid_left < data[mid]   and mid_right > data[mid]:
            low  = mid + 1 
        elif mid_left > data[mid] and mid_right < data[mid]:
            high = mid - 1
        elif mid_left < data[mid] and mid_right < data[mid]:
            return data[mid]

    return None

# A = [1,2,3,4,5,5,4,2,6]
# print(bitonic_peak_naive(A))

A = [1,2,3,4,5,6,7,8,16,15,14,12,11]
print("len = ", len(A))
print(find_heighest_number(A))