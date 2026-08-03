my_nums = (10, 5, 100, 0)
print(type(my_nums))
print(my_nums[-2])
# my_nums[-1] = 0  # Error

# del my_nums[-2]  # Error

users = (
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 135,
        'user_name': 'Bob'
    },
)

print(users[1]['user_id'])
users[1]['user_id'] = 131  # No error
print(users[1]['user_id'])

print(users.index({'user_id': 134, 'user_name': 'Alice'}))

users_list = list(users)  # Converts to list
users_list.append({'user_id': 169, 'user_name': 'Matvii'})

users = tuple(users_list)

print(users)

my_nums2 = (10, 5, 100, 0, 9, 5, 5)

index_one = my_nums2.index(5)
# Start looking from the found index + 1
index_two = my_nums2.index(5, index_one + 1)
index_three = my_nums2.index(5, index_two + 1)
print(index_three)
