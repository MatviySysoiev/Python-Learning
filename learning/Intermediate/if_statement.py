if 10 > 2:
    print(True)  # True

num_one = 10
num_two = 5.3

if (num_one > 0 and num_two > 0) and (isinstance(num_one, int) and isinstance(num_two, int)):
    print("Both number are ints and positives")
else:
    print("At least one number is not an int or is negative")
    # At least one number is not an int or is negative

my_phone = {
    'price': 200
}

if my_phone.get('brand'):
    print("Phone's brand is ", my_phone['brand'])
else:
    print("Phone's brand is not specified")  # Phone's brand is not specified


#


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "One of the arguments is not int"

    if a >= b:
        return f"{a} is greater than or equal to {b}"

    return f"{a} is less than {b}"


def nums_info(a, b):  # The same
    if (type(a) is not int) or (type(b) is not int):
        return "One of the arguments is not int"
    elif a >= b:
        return f"{a} is greater than or equal to {b}"
    else:
        return f"{a} is less than {b}"


print(nums_info(True, 10))
# One of the arguments is not int
print(nums_info(10, 5))  # 10 is greater than or equal to 5
print(nums_info(5, 10))  # 5 is less than 10
