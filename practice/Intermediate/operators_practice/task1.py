"""
Task:
1. Create two variables and assign them identical set objects without assigning or copying one variable from another.
2. Print the result of comparing the two set objects (using ==) to the terminal and explain the output.
3. Compare the two objects using the `is` operator and explain the output.
4. Check whether specific elements exist in the set using the `in` operator.
"""

my_set = {1, '2', 5.4, "Hello"}
another_set = {1, '2', 5.4, "Hello"}

print(another_set == my_set)  # True
print(another_set.__eq__(my_set))  # (The same) True

print(my_set is another_set)
# False because operator 'is' checks objects and not variables

print(5 in my_set)  # False
print(5 not in my_set)  # True
print("Hello" in another_set)  # True
print("Hello" not in another_set)  # False

# # TypeError: cannot use 'list' as a set element (unhashable type: 'list')
# print([] in my_set)
