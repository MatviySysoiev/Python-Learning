# 1. Replace the element "pear" with "lemon".
# 2. Add "pineapple" to the end of the list using the .append() method.
# 3. Insert "plum" into the second position (index 1) using the .insert() method.
# 4. Remove the last element using .pop() and save it into a variable named `last_fruit`.
# 5. Extract a slice containing the 3 middle elements of the resulting list.

fruits = ["apple", "banana", "pear", "orange", "kiwi", "mango", "peach"]

pear_index = fruits.index('pear')
fruits[pear_index] = 'lemon'

fruits.append('pineapple')

fruits.insert(1, 'plum')

last_fruit = fruits.pop(-1)
print(last_fruit)

three_slice_fruits = fruits[3:-2]
print(three_slice_fruits)
