from stack import Stack


def convert_int_to_bin(dec):
    """Converts decimal number to 
    binary number."""
    if dec == 0:
        return 0

    s = Stack()
    binary = ""

    while dec > 0:
        s.push(dec % 2)
        dec = dec // 2
        
    while not s.is_empty():
        binary += str(s.pop())
    
    return binary

print(convert_int_to_bin(31))
print(convert_int_to_bin(64))
print(convert_int_to_bin(70))
print(convert_int_to_bin(242))

# def dec_to_bin(dec):
#     stop = 1
#     bin = []
#     while True:
#         # print("in while")
#         print(dec)
#         bin.append( int(dec) % 2)
#         dec = int(dec) / 2
        
#         if round(dec) ==0:
#             break
#         else:
#             continue

#     return bin
            
# print(dec_to_bin(242))


# print( "{0:b}".format(242))
# print( bin(242).replace("0b",""))
# print(f"{242:b}")
# print(11 // 2)
# print(10 / 2)

# def decimalToBinary(num):
#     """This function converts decimal number
#     to binary and prints it"""
#     # print(num)
#     if num > 1:
#         decimalToBinary(num // 2)
#     # print("")
#     # print("here: ",num)
#     print(num % 2, end='')


# # decimal number
# # number = int(input("Enter any decimal number: "))

# decimalToBinary(60)

