from stack import Stack

def reverse_string(str):
    s = Stack()
    r = ""
    for n in str:
        s.push(n)
    
    for n in range(len(str)):
        r +=  s.pop()
    return r

str = "jawad"
print(reverse_string(str))
# print(str[::-1])