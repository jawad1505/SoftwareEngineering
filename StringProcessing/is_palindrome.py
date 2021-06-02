'''
A palindrome is a word, number, phrase, 
or any other sequence of characters that
reads the same forward as it does backward.
ex: Was it a cat i saw
    radar
    live on time, emit no evil
    nevel odd or even 
'''
def is_palindrome(s):
    i = 0 
    j = len(s) - 1

    while i < j:
        # handle spaces
        while not s[i].isalnum() and i < j:
            i += 1
        
        while not s[j].isalnum() and i < j:
            j -= 1
        
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

s = "Was it a cat i saw"

print("Is Palindrome :",is_palindrome(s))

# Only get alphanumeric, remove the spaces
# s = ''.join([i for i in s if i.isalnum()]).replace(" ","").lower()
# print(s == s[::-1])

