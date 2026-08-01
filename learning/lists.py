# list2 = ["hello", 2]

# Last_Word = list2[-1]

# print(Last_Word)
# list2[-1] = "Not 2"
# Last_Word = list2[-1]

# print(Last_Word)

# del list2[-1]  # delete last element
# Last_Word = list2[-1]
# print(Last_Word)


# first_list = [5, 7, 3, 6]
# first_list.sort(reverse=False)

# print(first_list)

# greetings = "Hello from Python"
# greetings_list = list(greetings)

# print(greetings_list)

# my_dict = {"a": 10, "b": "Hi"}
# my_dict_keys = list(my_dict)

# print(my_dict_keys)

# ratings = [2.5, 5, 7, 1]
# print(min(ratings))
# print(type(min(ratings)))
# print(max(ratings))
# print(type(max(ratings)))
# print(sum(ratings))
# print(type(sum(ratings)))

# print(sum(ratings)/len(ratings))

# other_ratings = [3.5, 1, 6]

# all_ratings = ratings + other_ratings
# print(all_ratings)

# first_two_ratings = ratings[:2]  # 0:2
# print(f"first:  {first_two_ratings}")

# middle_ratings = ratings[1:-1]  # start from 1 and finish before the last one
# print(middle_ratings)

# last_two_ratings = ratings[-2:]
# print(last_two_ratings)

# numbers_list = [1, 2]
# copied_list = numbers_list

# copied_list.append(3)

# print(copied_list)
# print(numbers_list)
# print(id(numbers_list) == id(copied_list))  # The same

# another_copied_list = numbers_list[:]  # copying using "slice"
# # will be completely another list
# another_copied_list.append(4)
# print(another_copied_list)
# print(numbers_list)

# completely_another_copied_list = numbers_list.copy()

# completely_another_copied_list.append(5)
# print(completely_another_copied_list)
# print(numbers_list)

# for_real_completely_another_copied_list = list(numbers_list)

# for_real_completely_another_copied_list.append(6)
# print(for_real_completely_another_copied_list)
# print(numbers_list)


my_nums = [10, 50, 0, 5, 5, 100]
print(my_nums.count(5))  # returns the value of how many 5 in the list
my_nums.append(25)
print(my_nums)  # added 25 to the end

my_nums.insert(1, 20)
print(my_nums)
my_nums.clear()
print(my_nums)

my_nums.extend('abc')
print(my_nums)
