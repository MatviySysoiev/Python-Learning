# my_range = range(5)

# print(my_range)
# print(type(my_range))
# print(my_range[0])
# print(my_range[1])

# for i in my_range:
#     print(i + 1)  # From 1 to 5

# print("\nNEXT\n")

# for i in range(5):
#     print(i)  # From 0 to 4

# print("\nNEXT\n")

# for n in range(5, 26, 5):  # start stop step
#     print(n)

new_range = range(10)

print(new_range.start)  # 0
print(new_range.stop)  # 10
print(new_range.step)  # 1

old_range = range(5, 15, 2)
print(old_range.index(9))  # 2

# if there is a number, returns 1, otherwise returns 0
print(old_range.count(11))
