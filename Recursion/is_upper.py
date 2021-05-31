def find_uppercase_iterative(s):
    my_str = str()
    for i in range(len(s)):
        if s[i].isupper():
                my_str += s[i]+"-"

    a =  my_str if len(my_str) > 0 else "no upper found"
    return a

def find_upper_recursive(s, idx=0):
    # Base Case
    if s[idx].isupper():
        return s[idx]

    if idx == len(s) - 1:
        return "no upper"
    
    # Recursion
    return find_upper_recursive(s, idx+1)
    
s = "JawadSaleem"
print(find_uppercase_iterative(s))
print(find_upper_recursive(s))