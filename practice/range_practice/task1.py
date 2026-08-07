"""
Task:
1. Create an empty list named `new_list`.
2. Create a range object named `new_range` that generates odd numbers from 1 to 9 (start: 1, stop: 10, step: 2).
3. Loop through `new_range`, appending each number to `new_list` and printing a message formatted as "added number {n}" for each added element.
4. Print the final `new_list`.
"""

new_list = []
new_range = range(1, 10, 2)

for n in new_range:
    new_list.append(n)
    print(f"added number {n}")

print(new_list)
