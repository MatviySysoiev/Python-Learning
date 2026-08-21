list = [1, 'abc', True]

for el in list:
    print(type(el))
    print(el)

print(el)  # True (the last element)

my_dict = {
    'a': 123,
    'id': 931
}

for key in my_dict:
    print(key, my_dict[key])

# a 123
# id 931
print(type(my_dict.items()))

for item in my_dict.items():
    print(item)
    print(type(item))
    k, v = item  # item is a tuple
    print(k, v)


for k, v in my_dict.items():
    print(k, v)


video_ids = {124, 310, 4344, 9393}

for id in video_ids:
    print(id)

# 4344
# 9393
# 124
# 310

my_name = 'Matvii'

vowels = 'aeiouAEIOU'
total_vowels = 0

for char in my_name:
    if char in vowels:
        total_vowels += 1

print(total_vowels)  # 3


for num in range(5):
    print(num)  # 0, 1, 2, 3, 4
