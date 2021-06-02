def int_to_str(input_int):
    
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []

    if input_int == 0:
        output_str.append('0')
    else:   
        while input_int > 0:
            output_str.append(chr(ord('0') + input_int % 10))
            input_int //= 10
        output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str

input_int = 123
print(input_int)
print(type(input_int))

output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))

# print(str(123))
# print(type(str(123)))

# print(ord('A')) # char to unicode
# print(chr(65))  # unicode to char

# print(ord('1')) # char to unicode
# print(chr(ord('1')))  # unicode to char

# print(ord('0')+ 1) # unicode of 0 is 48