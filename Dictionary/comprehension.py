scores = {
    'english':90,
    'math': 70,
    'stats': 50
}

new_scores = { key +" ! ": val + 10 for (key,val) in scores.items()}
print(new_scores)