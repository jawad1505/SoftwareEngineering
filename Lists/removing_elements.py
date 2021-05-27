list = [11,22,30,22,300,41,500,1,123,321]
print(list)
list.pop()
print(list)

# del a particular element
list.remove(22) # remove particular element
print(list)


# slicing 
list = [11,22,33,44,55,66,77]
print("")
print(list)
print("[: 2 ] : ",list[:2]) 
print("[0: 4] : ",list[0:4]) 
print("[1: 4] : ",list[1:4]) 
print("[2 :5] : ",list[2:5]) 
print("[: 5 ] : ",list[:5])
print("[: -2] : ",list[:-2])
print("[-3: -2] : ",list[3:-2])