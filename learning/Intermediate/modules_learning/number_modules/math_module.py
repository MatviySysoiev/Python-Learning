import math

print(math.pi)  # constant pi
print(math.e)  # constant e

print(math.sqrt(25))  # square root of the given number (25)

print(math.log(100, 10))  # logarifm

print(math.factorial(5))  # factorial


def calc_factorial(num):
    if type(num) is not int:
        raise TypeError("Number must be int")
    if num <= 0:
        raise ValueError("Number must be positive")
    if num == 1:
        return 1
    return calc_factorial(num - 1) * num


print(calc_factorial(5))
