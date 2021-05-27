star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

print()
list_1 = set(star_wars_set)
print(list_1)

list_1 = set(star_wars_tup)
print(list_1)

list_1 = set(star_wars_dict)
print(list_1)


list_1 = set(star_wars_dict.items())
print(list_1)

list_1 = set(star_wars_dict.values())
print(list_1)