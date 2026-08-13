def mult_by_factor(value, mult=1):
    """Multiplies number by multiplicator"""  # Will be shown as a description of the functions
    return value * mult


mult_by_factor(5)  # 5


def print_number_info(num):  # Callback function
    """
    Prints num information

    Args:
        num (int): Integer number

    Returns:
        int: Same Number
    """
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number in odd")

    return num


print_number_info(123)
