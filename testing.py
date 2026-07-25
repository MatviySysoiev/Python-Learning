def hello(name):  # name - парамет р
    print("Hello there,", name, "!")


# hello('Matthew') #аргумент

def sum_nums(a, b):
    sum = a+b
    return (sum)
    print("This text won't be shown")  # все, что после return не выполняется


first_sum = sum_nums(2, 4)
print(first_sum)
print(sum_nums(154, 3))
print(sum_nums(sum_nums(13, 5), 2))
