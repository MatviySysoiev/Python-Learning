brand = 'brand'

my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
}

other_motorbike = {
    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati',
}

print(my_motorbike == other_motorbike)  # True
print(id(my_motorbike) == id(other_motorbike))  # False, 2 dif objects

list1 = [
    my_motorbike,
    other_motorbike
]


# print(list1[0]['brand'])

print(my_motorbike[brand])

index_found = list1.index(my_motorbike)

print(list1[index_found]['brand'])

my_motorbike['price'] = 20000  # change price
print(my_motorbike)

print(dir(my_motorbike))

my_motorbike['total_km'] = 50000  # new element

print(my_motorbike)

del my_motorbike['total_km']  # delete element


new_bike = {
    'brand': 'Ausom',
    'model': 'Ausom DT2 Pro',
    'price_info': {
        'price': 45000,
        'is_available': False
    }
}

print(new_bike['price_info']['is_available'])

new_price_info = {
    'price': 50000,
    'is_available': True
}

new_bike['price_info'] = new_price_info

print(len(new_bike))

print(my_motorbike.get('model'))  # if there isn't, returns none, not error
# returns Not Found if model wasn't found
print(my_motorbike.get('model', 'Not Found'))

print(my_motorbike.items())
print(type(my_motorbike.items()))  # кортежи dict_items

print(my_motorbike.keys())
print(type(my_motorbike.keys()))

print(list(my_motorbike.keys()))  # class list

print(my_motorbike.popitem())  # not recommended

#

new_disk = my_motorbike.copy()

new_disk['type'] = 'ssd'
print(my_motorbike)
print(new_disk)
print(my_motorbike == new_disk)  # false

#

my_list = [['first', 0], ['second', 2]]

my_dict = dict(my_list)

print(my_dict)
