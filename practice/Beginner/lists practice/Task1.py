"""
Task:
1. Create a list named `new_list` containing 5 random elements of different data types (including a nested list).
2. Remove the element at index 2 from `new_list`.
3. Print the length of `new_list`.
4. Reverse the order of elements in `new_list`.
5. Create a second list named `another_new_list` with two string elements.
6. Extend `new_list` by appending all elements from `another_new_list`.
7. Print the updated `new_list`.
"""

new_list = ["python", True, 2, ["hello", 5], None]
new_list.pop(2)
print(len(new_list))
new_list.reverse()

another_new_list = ["hello", "bye"]
new_list.extend(another_new_list)
print(new_list)
