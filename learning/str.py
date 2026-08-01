long_str = """This is
a very
long string"""
# print(long_str)
# print(type(long_str))
# print(id(long_str))

my_comment = "This is a short comment"

print(len(my_comment))
new_comment = my_comment.replace("short", "long")
print(new_comment)
print(my_comment.count(" "))  # 4 пробела
print(my_comment[-1])  # последний символ
print(my_comment[-5])  # 5 символ с конца
print(my_comment[:5])
