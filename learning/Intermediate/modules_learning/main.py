from learning.Intermediate.modules_learning.pack.other_module import *
import pack.other_module
import pack.other_module
# import new_file as old_file


# print(my_name)  # Matvii
# print_sum(5, 2)  # 7

# print(old_file)
# print(type(old_file))
# print(old_file.his_name)

# print(dir())
print('main.py', __name__)  # __main__
# print(type(__name__))  # <class 'str'>
print('main.py', __name__ == '__main__')

# If we use this code as the main and not as the module, then we get '__main__' and True

if __name__ == '__main__':
    print("main.py This code is executed directly")
else:
    print("main.py This code runs as the module")

pack
