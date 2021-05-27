
from stack import Stack

def is_matched(b1, b2):
    if b1 == "(" and b2 ==")":
        return True
    else:
        return False

def brackets_balanced(my_str):
    s = Stack()
    is_balanced = True
    index = 0
   
    while index < len(my_str) and is_balanced:
        paren = my_str[index]
        if  paren == "(":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_matched(top, paren):
                    is_balanced =  False
                    break
        index += 1
    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(brackets_balanced("(())))"))
