fruits = ['apple', 'banana', 'lime']

quantities = [100, 70, 50, 20, 10]  # You can also use dict, etc.

availability = [True, False, False, True]

frit_qty_zip = zip(fruits, quantities, availability)

print(frit_qty_zip)  # zip object at ...

fruit_qtys_list = list(frit_qty_zip)

# There is no 20 and 10 in the terminal because they don't have a pair
print(fruit_qtys_list)


fruits2 = ['apple', 'banana', 'lime']

availability2 = (True, False, False, True)

# You can't use 3 or more objects because you won't be able to convert to dict
fruits_availability_zip = zip(fruits2, availability2)

new_dict = dict(fruits_availability_zip)

print(new_dict)
