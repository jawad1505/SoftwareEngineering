def linear_search(data, target):
    for i in data:
        if i == target:
            return True
    return False

my_list = [2,3,4,51,1,5]
print(linear_search(my_list,1))