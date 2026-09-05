from array import array

# Create new array with only ints
my_int_array = array('i', [4, 10, 32, 9, 5, 5, 40, 5])

print(my_int_array)
print(type(array))

# Add an element to the array
my_int_array.append(13)
print(my_int_array)

# TypeError: 'str' object cannot be interpreted as an integer
# my_int_array.append('ab')

# returns the number of occurances of 5 in the array
print(my_int_array.count(5))

# Deletes selected element (-1 by default)
my_int_array.pop()

# Create new file my_array.bin and add elements from my_int_array
with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)


imported_array = array('i')

with open('my_array.bin', 'rb') as my_file:
    # Takes only 3 elements
    imported_array.fromfile(my_file, 3)
    print(imported_array)


imported_array.reverse()
print(imported_array)
