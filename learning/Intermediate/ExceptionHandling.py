# try:
#     print(10 / '2')
# except ZeroDivisionError as e:
#     print(type(e))  # <class 'ZeroDivisionError'>
#     print(f"Error - {e}")  # Error - division by zero
#     b = e.__str__()
#     print(f"Error - {b}")  # Error - division by zero
# except TypeError as e:
#     print(f"Error - {e}")  # unsupported operand type(s) for /: 'str' and 'int'
# except Exception as e:
#     print(f"Error - {e}")
# else:
#     print("There was no errors")
# finally:  # This block of code runs in any case
#     print('Continue...')  # Continue...


try:
    print(10 / 0)
except ZeroDivisionError as e:
    # True (e is a type of class ZeroDivisionError)
    print(isinstance(e, ZeroDivisionError))
    print(isinstance(e, Exception))  # True (e is a type of class Exception)
    print(isinstance(e, object))  # True (e is a type of class object)
    print(e)

try:
    print('10'/0)
except Exception as e:  # Any error
    print(e)

try:
    print(10/0)
except:  # NOT RECOMMENDED
    print("Some error has occurred")


def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")  # Good decision
    return a/b


try:
    divide_nums(10, 0)
except TypeError as e:
    print(e)  # Skipped
except Exception as e:
    print(e)  # Second argument can't be 0
