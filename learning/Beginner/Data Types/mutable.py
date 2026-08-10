from copy import deepcopy

info = {
    'name': 'Bodgan',
    'is_instructor': True,
    'reviews': []
}

copy_info = info.copy()  # two different links to objects. Shallow copy (поверхностая)

info['reviews'].append('Great. I was satisfied!')
print(info)
# Also was changed because 'reviews' refers to the same objects. Because list is a mutable object.

print(copy_info)


learners = {
    'name': 'Matvii',
    'is_instructor': False,
    'reviews': []
}

learners_deepcopy = deepcopy(learners)

learners_deepcopy['reviews'].append("Great learner!")

print(learners_deepcopy)
print(learners)  # Wasn't changed because of deepcopy
