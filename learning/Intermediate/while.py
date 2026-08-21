# import random

# random_num = random.randint(1, 5)
# while True:
#     num = int(input("Guess the number from 1 to 5:\n"))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congrats!", random_num)
#     break

i = 10
while i < 100:
    print(i)
    if i == 30:
        print("i is 30")
        i += 20
        continue  # start the while cycle again, complete this iteration
    i += 10
