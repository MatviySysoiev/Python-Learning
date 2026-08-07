"""
Task:
1. Create a set named `new_set` containing the integers 1 through 5.
2. Add the integer 6 to `new_set`.
3. Create a second set named `other_set` containing a few integer elements.
4. Find the intersection of `new_set` and `other_set` and store the result in `full_set`.
5. Convert `full_set` into a list named `full_list` and print it.
"""

new_set = {1, 2, 3, 4, 5}
new_set.add(6)

other_set = {2, 5, 6, 9, 10, 12}

full_set = new_set.intersection(other_set)

full_list = list(full_set)
print(full_list)
