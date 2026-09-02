import re

my_string = "My name is Matvii."

# Returns a match object if found, else None
# . means any symbol.
# $ means the end of str.
# ^ means the start of str.
# * means anything.
# \\. means that we want to find a dot
res = re.search("^M.*name", my_string)
print(res)
print(res.span())  # the index of found element

res = re.search("M....i\\.$", my_string)
print(res)
print(res.span())  # the index of found element

print("Hello\nBye")  # \n starts a new row
print(r"Hello\nBye")  # \n does nothing

my_pattern = re.compile(r"^M.*name")  # Create new pattern

print(my_pattern.search(my_string))  # find the pattern in the string
print(my_pattern.match(my_string))  # if the pattern maches the string
# find all strings that maches this pattern
print(my_pattern.findall(my_string))
