from sys import getsizeof

squares_gen = (num * num for num in range(10000))

print(getsizeof(squares_gen))
# 208

print(type(squares_gen))
# <class 'generator'>

# TypeError: 'generator' object is not subscriptable
# print(squares_gen[100])

for elem in squares_gen:
    print(elem)
    if elem == 100:
        break

# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100


squares_list = [num * num for num in range(10000)]

print(getsizeof(squares_list))
# 85176

print(type(squares_list))
# <class 'list'>
