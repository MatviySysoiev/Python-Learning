# Instructions:
# 1. Combine both lists into a single list named `full_list`.
# 2. Create a new list named `reversed_list` that contains all elements of `full_list` in reverse order using step slicing.
# 3. Extract only the elements at odd indices from `reversed_list` using a step slice of 2.

part1 = [10, 20, 30]
part2 = [40, 50, 60]

full_list = part1 + part2

print(full_list)

reversed_list = full_list[::-1]

odd_list = reversed_list[1::2]
print(odd_list)
