my_num = 10

print(- my_num)  # -10
print(+ my_num)  # 10
print(not my_num)  # False

another_num = 0
print(not another_num)  # True


# my_bool = True
# print(+ my_bool)  # 1
# print(- my_bool)  # -1
# another_bool = False
# print(+ another_bool)  # 0


print(bool(0))  # False
print(bool(0.0))  # False
print(bool(0j))  # False

print(bool({}))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool(set()))  # False
print(bool(range(0)))  # False
print(bool(""))  # False
print(not not {'a': 10})  # True

my_list = []
print(len(my_list) > 0)  # False

new_list = [1, 2]
print(len(new_list) >= 0)  # True
