def is_perm_1(s1,s2):
    """ Approach 1: Sorting

    Time Complexity:  O(n logn)
    Space Complexity: O(1)
    """

    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    
    return True

def is_perm_2(s1,s2):
    """ Approach 2: Sorting

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False
    ht = dict()

    for i in s1:
        if i in ht:
            ht[i] +=1
        else:
            ht[i] = 1
   
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            return False
    
    return True

s1 = "google"
s2 = "ooggle"
print("Permutation: ",is_perm_2(s1, s2))

s1 = "not"
s2 = "top"
print("Permutation: ",is_perm_2(s1, s2))