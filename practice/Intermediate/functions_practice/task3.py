"""
Task:
1. Create a function `update_car_info` where all keyword arguments are collected into a dictionary named `car`.
2. Add a new key `is_available` with the value `True` to the dictionary.
3. Return the modified dictionary from the function.
4. Call the function using keyword arguments `brand` and `price` (with any values of your choice).
5. Print the return value of the function to the console/terminal.
"""


def update_car_info(**car):
    car['is_available'] = True
    return car


print(update_car_info(brand='audi', price=150_000))
