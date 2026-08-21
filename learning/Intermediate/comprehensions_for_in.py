my_scores = {
    'a': 10,
    'b': 7,
    'm': 15
}

scores = {k: v * 10 for k, v in my_scores.items()}

print(scores)  # {'a': 100, 'b': 70, 'm': 150}

print(my_scores)  # {'a': 10, 'b': 7, 'm': 15}

new_scores = {v * 10 for k, v in my_scores.items()}
print(new_scores)  # {150, 100, 70}
print(type(new_scores))  # <class 'set'>

foreign_scores = [10, 7, 14]

scores = {index: elem for index, elem in enumerate(foreign_scores)}

print(scores)  # {0: 10, 1: 7, 2: 14}
