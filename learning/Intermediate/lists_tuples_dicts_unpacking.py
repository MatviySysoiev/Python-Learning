my_list = [1, 2, 3]

first, second, third = my_list

# ValueError: not enough values to unpack (expected 4, got 3)
# first, second, third, fourth = my_list

# ValueError: too many values to unpack (expected 2, got 3)
# first, second = my_list

print(first)
print(second)
print(third)

my_tuple = ('apple', 'banana', 'peach', 'orange')
apple, banana, peach, orange = my_tuple

print(apple, banana, peach, orange)  # apple banana peach orange


my_fruits = ['apple', 'lime', 'cucumber']

my_apple, *remaining_fruits = my_fruits
print(my_apple)  # apple
print(remaining_fruits)  # ['lime', 'cucumber']


user_profile = {
    'name': 'Matvii',
    'comments_qty': 23,
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"

    return f"{name} has {comments_qty} comments"


print(user_info(**user_profile))  # Matvii has 23 comments
# Matvii has 23 comments
print(user_info(user_profile['name'], user_profile['comments_qty']))
# Matvii has 23 comments
print(user_info(name=user_profile['name'],
      comments_qty=user_profile['comments_qty']))


name, comments_qty = user_profile
print(name)  # name
print(comments_qty)  # comments_qty
# We don't get our key values


user_data = ['Matvii', 23]
new_data = ['notmatvii', 30, 123]


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"

    return f"{name} has {comments_qty} comments"


print(user_info(*user_data))  # Matvii has 23 comments
print(user_info(user_data[0], user_data[1]))  # Matvii has 23 comments

# TypeError: user_info() takes 2 positional arguments but 3 were given
# print(user_info(*new_data))

my_name, my_comments_qty = user_data
print(user_info(my_name, my_comments_qty))  # Matvii has 23 comments


new_list = [
    {'name': 'Matvii', 'age': 14},
    {'name': 'Yaroslav', 'age': 25},
    {'name': 'Svetlana', 'age': 48},
]

matvii, yaroslav, svetlana = new_list


def unpack_dict(name, age):
    return name, age


print(unpack_dict(**matvii)) # ('Matvii', 14)
print(unpack_dict(**yaroslav)) # ('Yaroslav', 25)
print(unpack_dict(**svetlana)) # ('Yaroslav', 25)
