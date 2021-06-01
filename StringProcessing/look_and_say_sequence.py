''' 
Understanding Loack and Say Sequqnce
'''
# 1        => one 1                               => 11
# 11       => two 1                               => 21
# 21       => one 2 one 1                         => 1211
# 1211     => one 1, one 2, two 1                 => 111221
# 111221   => three 1, two 2, one 1               => 312211
# 312211   => one 3, one 1, two 2, two 1          => 13112221
# 13112221 => one 1, one 3, two 1. three 2, one 1 => 1113213211

def look_say_sequence(s):
    results = []
    i = 0

    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        results.append(str(count) + s[i])
        i += 1

    return ''.join(results)


# s = "111221"
s = "21"
result = look_say_sequence(s)
print(result)