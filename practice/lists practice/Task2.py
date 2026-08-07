"""
Task:
1. Create two lists: `first_list` containing two integers and `second_list` containing two strings.
2. Concatenate the two lists using the `+` operator and print the result.
3. Perform the same list concatenation using the `__add__()` dunder method and print the result.
"""

first_list = [1, 2]
second_list = ["I", "Python"]

print(first_list + second_list)

print(first_list.__add__(second_list))
