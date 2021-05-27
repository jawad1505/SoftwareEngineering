scores = {}

scores = {
    'english':90,
    'math': 70,
    'stats': 50
}

print(scores)

del (scores['math'])
print(scores)

# pop = remove, popitem = restore

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

# Removes and returns the last inserted pair, as a tuple
lastAdded = phone_book.popitem()
print(lastAdded)