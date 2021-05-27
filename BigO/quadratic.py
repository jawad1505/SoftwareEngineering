def func_quad(lst):
    '''
    Prints pairs for every item in list.
    '''
    for item_1 in lst:
        for item_2 in lst:
            print (item_1,item_2)
            
lst = [0, 1, 2, 3]

func_quad(lst)

print("====================")
# 3 O(n) => O(n)

def print_3(lst):
    '''
    Prints all items three times
    '''
    for val in lst:
        print (val)
        
    for val in lst:
        print (val)
        
    for val in lst:
        print (val)

print_3(lst)

print("=================")
print(" O ( 1 + n/2 + 10) => O(n)")
def comp(lst):
    '''
    This function prints the first item O(1)
    Then is prints the first 1/2 of the list O(n/2)
    Then prints a string 10 times O(10)
    '''
    print(lst[0])
    
    midpoint = int(len(lst)/2)
    
    for val in lst[:midpoint]:
        print(val)
        
    for x in range(10):
        print('number')

lst = [1,2,3,4,5,6,7,8,9,10]

comp(lst)

print("=========  O(n)")

def matcher(lst,match):
    '''
    Given a list lst, return a boolean indicating if match item is in the list
    '''
    for item in lst:
        if item == match:
            return True
    return False

print(matcher(lst,1))

print(matcher(lst,11))


print("===========")
def printer(n=10):
    '''
    Prints "hello world!" n times
    '''
    for x in range(n):
        print ('Hello World!')

printer()