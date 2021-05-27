count = 0 
def sum(n) -> int:
    global count
    count +=1
    print(count)
    if n <=0:
        return 0
    return n + sum(n-1)
    

print(sum(5))