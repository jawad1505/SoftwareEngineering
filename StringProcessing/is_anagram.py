def is_anagram(s1, s2):
    """An anagram is when two strings can be written using the same letters.

    "rail safety" = "fairy tales"
    "roast beef" = "eat for BSE"
    """
    if len(s1) != len(s2):
        return False
    
    str_ht = dict()
    

    for i in s1:
        if i in str_ht:
            str_ht[i] += 1
        else:
            str_ht[i] = 1

    for i in s2:
        if i in str_ht:
            str_ht[i] -=1
        else:
            str_ht[i] = 1
    
    for i in str_ht: 
        if str_ht[i] != 0:
            return False
    return True


s1 = "fairy tales"
s2 = "rail safety"
s3 = "Berry tales"
s4 = "Car safety"

# Solution 1: big O (n log n) due to sorting 
s1 = s1.replace(" ","").lower()
s2 = s2.replace(" ","").lower()
print(sorted(s1) == sorted(s2))

# Solution 2: big O (n) due to for loop 
print("Is Anagram: ",is_anagram(s1,s2))
print("Is Anagram: ",is_anagram(s3,s4))