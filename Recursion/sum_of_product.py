def iterative_multiply(x,y):
    sum = 0
    for i in range(y):
        sum +=x
    return sum

def recursive_multiply(x,y):
    # Base Case
    if x < y:
        recursive_multiply(y, x)

    if y == 0:
        return 0
    
    # Recursion
    return x + recursive_multiply(x, y-1)
    

print(iterative_multiply(5, 3))
# print(recursive_multiply(5, 3))
print(recursive_multiply(200, 300))