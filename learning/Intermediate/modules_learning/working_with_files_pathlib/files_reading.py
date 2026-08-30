from pathlib import Path

# test_file = open('test.txt', 'w')
# # File was created
# print(test_file)
# print(type(test_file))

# test_file.write("First string\n")
# test_file.write("Second string\n")

# # print(test_file.read())
# # io.UnsupportedOperation: not readable
# # Because we opened this file as write, so we can't read it

# test_file.close()

# test_file = open('test.txt')

# print(test_file.read())


# Better example

# with open('test.txt', 'w') as test_file:
#     test_file.write("First string\n")
#     test_file.write("Second string\n")

# with open('test.txt') as test_file:
#     print(test_file.read())

# with open('test.txt', 'a') as test_file:  # a means append
#     test_file.write("Third string\n")
#     test_file.write("Fourth string\n")

# with open('test.txt') as test_file:
#     print(test_file.read())

# with open('test.txt') as test_file:
#     print(test_file.readlines())  # list of strings


# with open('test.txt') as test_file:
#     for line in test_file:
#         print(line)

# with open('test.txt') as test_file:
#     print(test_file.readline())  # first string
#     print(test_file.readline())  # second string
#     print(test_file.readline())  # third string
#     print(test_file.readline())  # fouth string
#     print(test_file.readline())  # empty string becuase test.txt has ended


# with open('test.txt') as test_file:
#     while True:
#         line = test_file.readline()
#         if not line:
#             break
#         print(line)

my_file = Path('test.txt')

if my_file.exists():
    Path('test.txt').unlink()  # File was deleted
else:
    print("File was not found!")
