# List inside another list
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners)
print(len(world_cup_winners))

print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0])  # Accessing 'S'


# multiple  lists
lista = [1, 2, 3, 4, 5]
listb = [6, 7, 8, 9, 10]
c = [a*b for a,b in zip(lista,listb)]
print(c)

import numpy as np
a = [1, 2, 3, 4, 5]
b = [600, 7, 8, 9, 10]
c = np.multiply(a,b)
print(c)
print(c[0])
print(len(c))