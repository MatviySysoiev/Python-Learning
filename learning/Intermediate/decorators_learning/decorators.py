def decorator_function(fn):
    def wrapper_function(*args, **kwargs):
        # Some actions before execution of the original_fn
        print("Executed before function")
        res = fn(*args, **kwargs)
        print("Function result:", res)

        # Some actions after execution of the original_fn
        print("Executed after function")

        return res

    return wrapper_function


@decorator_function  # call decorator function
def my_function(a, b):
    print("This is my function!")
    return (a, b)


res = my_function(100, 50)
print(res)


# SECOND EXAMPLE

def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Function name: {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        res = fn(*args, **kwargs)
        print(f"Function result: {res}")
        return res

    return wrapper


@log_function_call
def mult(a, b):
    return a * b


@log_function_call
def sum(a, b):
    return a + b


print(mult(5, 20))
print('')
print(mult(a=3, b=20))
print('')
print(sum(20, 5.3))
