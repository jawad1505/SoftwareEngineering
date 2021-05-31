def integer_square_root(num):
    low  = 0
    high = num

    while low <= high:
        mid = (low + high) // 2
        mid_square = mid * mid

        # print(low, high, mid, mid_square)
        if mid_square <= num:
            low  = mid + 1
        else:
            high = mid - 1
    return low - 1
        

print(integer_square_root(300))


#  target = 300
#  output = 17
# print(300 ** 0.5)
# print(17 ** 2)
# print(18 ** 2)
# print(19 ** 2)
