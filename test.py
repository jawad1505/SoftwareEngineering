def test(x):
    # print(x)
    if  x == 0:
        return -1
    else:
        # x -= 1
        print("check ", x)
        counter = x + test(x-2)
        print("counter = ",counter)
        return counter

def fact(n):

    print("n = ",n)
    if n == 0:
        return 1
    

    else:
        return n * fact(n-1)
        
print(test(10))
    
