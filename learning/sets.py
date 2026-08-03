posts_ids = {10, 25, 16, 73, 10, 25, 73, 10}
# print(posts_ids[0])  # Error

print(posts_ids)  # no duplicates
print(len(posts_ids))  # 4

# del posts_ids[0] # can't delete

# set = {[10, 10], 5, 15}  # can't add editable objects (list, dict, set)
tuple = ([10, 10], 5, 15, [10, 10], 15, 5, 5)
print(tuple)

new_set = set()
print(type(new_set))

# add
posts_ids.add(150)
print(posts_ids)

# union
first_set = {1, 2}
second_set = {2, 3}
full_set = first_set.union(second_set)  # only unique
print(full_set)

full_set2 = first_set | second_set  # the same
print(full_set2)

# intersection
common_s = first_set.intersection(second_set)  # objects
# that are in both sets
print(common_s)

common_s2 = first_set & second_set
print(common_s2)  # the same

# subset, superset
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
res = set1.issubset(set2)
print(res)  # True because set2 contains all objects from set1

other_res = set2.issuperset(set1)
print(other_res)  # the same

# Practice 2
my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))  # objects that are in both sets
print(other_set.intersection(my_set))  # the same

print(my_set.union(other_set))  # all objects without duplicates

print(other_set.issubset(my_set))  # False because there is no 'a' in my_set
print(my_set.issuperset(other_set))  # The same

# returns elements that are in my_set but there aren't in other_set
print(my_set.difference(other_set))
print(my_set - other_set)  # The same

# Returns none but deletes 'a' in other_set set. But doesn't summon an error
other_set.discard('a')
# other_set.remove('abvdf') #Returns an error because there is no 'abvdf' in the set
print(my_set.issuperset(other_set))  # True

# Returns all str that doesn't match
print(my_set.symmetric_difference(other_set))
print((my_set | other_set) - (my_set & other_set))  # the same
