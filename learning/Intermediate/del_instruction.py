# del is an instrunction, not an operator

my_dict = {'a': True, 'b': 10}

del my_dict['a']
my_dict.__delitem__('b')  # the same as del

print(my_dict)
