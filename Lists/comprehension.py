# List comprehension is a technique that uses a for loop 
# and a condition to create a new list from an existing one.

a = [1,2,3,4,5]
b = []

for n in a:
    b.append(n * 2)

print("non comprehension: ",b)

# List comprehension

c = [n * 2 for n in a]
print("Comprehension: ",c)

d = [n * 2 for n in a if n >2]
print("comprehension using a condition: ", d)

list_1 = [10,90,50]
list_2 = [10,31,55]
sum = [ n1 + n2 for n1 in list_1 for n2 in list_2 if n1+n2 > 100]
print(sum)

new_tuple = [ (n1,n2) for n1 in list_1 for n2 in list_2 if n1+n2 > 100]
print(new_tuple)