def printer(n=3):
    '''
    Prints "hello world!" n times
    '''
    for x in range(n):
        print ('Hello World!')

print("space complexity: O(1), Time complexity: O(n): ")
printer()

print("============")
print("space complexity: O(n), Time complexity: O(n): ")
def create_list(n):
    new_list = []
    
    for num in range(n):
        new_list.append('new')
    
    return new_list