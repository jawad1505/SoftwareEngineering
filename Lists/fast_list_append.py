def method1():
    l = []
    for n in range(10):
        l = l + [n]
        print(l)
    return(l)

def method2():
    l = []
    for n in range(10):
        l.append(n)
        print(l)
    return(l)
    
def method3():
    l = [n for n in range(10)]

def method4():
    l = range(10) # Python 3: list(range(10000))

print("Lists: ",method1())

print("Lists: ",method2())