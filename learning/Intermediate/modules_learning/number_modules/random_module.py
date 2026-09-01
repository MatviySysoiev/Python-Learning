import random

print(random.random())  # Generates random number from 0 to 1 (1 not included)

# generates random number between 1 and 10 (both included)
print(random.randint(1, 10))
# takes random element from a sequence
print(random.choice(["hello", 10, True, 20]))

# takes random k (3) elements from a sequence
print(random.choices(["hello", 10, True, 20, 15, False], k=3))

new_list = ["hello", 10, True, 20, 15, False]
print(random.shuffle(new_list))  # Change the order of the elements

print(new_list)

print(''.join(random.choices('0123456789', k=8)))
