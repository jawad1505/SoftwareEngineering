def normalize_str(input_str):
    input_str = input_str.replace(" ", "")
    return input_str.lower()

def is_unique(s):
    ht = dict()
    s = normalize_str(s)
    for i in s:
        if i in ht:
            return False
        else:
            ht[i] = 1
    return True

def is_unique_2(s):
    """ Solution 2: convert string to a set, as set has no duplicates

    if length of set of s and len of set matches, its True

    else False
    """

    s = normalize_str(s)
    return len(set(s)) == len(s)

def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True

s1 = "abcXYz"
s2 = "abcDeFgf"
s3 = "aA"
print(is_unique(s1))
print(is_unique_2(s2))
print(is_unique_3(s3))