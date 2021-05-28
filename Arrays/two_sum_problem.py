# Solution 1: Brute Force => O(n^2), SC O(1)
def two_sum(arr, sum):
    for x in arr:
        for y in arr:
            if x + y == sum :
                print(f'{x} + {y} = {sum}')
                print(f'A[{x}] + {y} = {sum}')
                return True
    return False

# Solution 2: Use Hash/Dictionary, TC O(n), SC O(n)
def two_sum_hash(arr, sum):
    ht = dict()
    for x in range(len(arr)):
        if arr[x] in ht:
            print(ht[arr[x]], arr[x])
            return True
        else:
            ht[sum - arr[x]] = arr[x]
    return False

# Solution 3: two pointers, assumes sorted array, TC O(n), SC O(1)

def two_sum_pointers(arr, sum):
    i = 0
    j = len(arr) - 1 
    
    while i < j:
        if arr[i] + arr[j] == sum:
            return True
        elif arr[i] + arr[j] < sum:
            i +=1
        else:
            j -= 1
    return False

# Solution 4: Return indexes. TC O(n), SC: O(n)
def twoSum( nums, target) :
    ht = {}
    
    
    for x in range(len(nums)):
        if target - nums[x] in ht:
            print(ht)
            return [ht[target - nums[x]], x]
        else:
            ht[nums[x]] = x
    print(ht)
    return False        
        
A = [12, 21, 18, 14, 3, 2]
# print(two_sum_hash(A, 8))
print(two_sum_hash(A, 5))