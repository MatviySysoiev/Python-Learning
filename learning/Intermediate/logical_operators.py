print(not not 10)
print(not not 0)

print(not not ['a'])
print(not not [])

print(not not True)
print(not not None)

my_list = []
print(not my_list)  # True
my_list.append('x')
print(not my_list)  # False

other_list = ['a', 'b']
print(my_list or other_list)  # ['x']
print(len(my_list) < 0 or other_list[0])  # a

my_dict = {}
print(my_list and my_dict)  # {}
print(bool(my_list and my_dict))  # False
print(bool(my_list or my_dict))  # True

dict_one = {'a': 'hello', 'b': 'bye'}
dict_two = {'b': 'bye', 'a': 'hello'}

dict_one == dict_two and print("Dictionaries are equal")
