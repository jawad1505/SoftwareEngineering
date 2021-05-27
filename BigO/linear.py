# First function (Note the use of xrange since this is in Python 2)
def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n
    '''
    final_sum = 0
    for x in range(n+1): 
        final_sum += x
        print(final_sum)
    
    return final_sum

print("final: ",sum1(10))

print("=============== EXAMPLE 2 ==============")

