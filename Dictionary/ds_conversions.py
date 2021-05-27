star_wars_list = [[1,"Anakin"], [2,"Darth Vader"], [3, 1000]]
print (star_wars_list)
star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
print (star_wars_tup)
star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}
print (star_wars_set)

print()
star_wars_dict = dict(star_wars_set) # Converting from set
print(star_wars_dict)

list_1 = dict(star_wars_tup)
print(list_1)

list_1 = dict(star_wars_list)
print(list_1)

