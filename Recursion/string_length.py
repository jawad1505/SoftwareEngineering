def iterative_str_len(input_str):
    input_str_len = 0
    for i in range(len(input_str)):
        input_str_len += 1
    return input_str_len


def string_length_recursive(s):

    # Base Case
    if s == "":
        return 0
    
    return 1 + string_length_recursive (s[1:])

s = "JawadSaleem"

print(iterative_str_len(s))

print(string_length_recursive(s))