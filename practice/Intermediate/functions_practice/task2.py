"""
Task:
1. Rewrite the call to the function `merge_lists_to_dict` from the previous exercise so that keyword arguments are used.
2. Add another call to the function containing one positional argument and one keyword argument.
"""


def merge_lists_to_dict(object_one, object_two):
    new_zip = zip(object_one, object_two)

    zip_dict = dict(new_zip)
    return zip_dict


products = ['Apple', 'Banana', 'Watermelon']
prices = [100, 150, 350]

res = merge_lists_to_dict(object_one=products, object_two=prices)
print(res)

res2 = merge_lists_to_dict(products, object_two=prices)
print(res2)

# Error - SyntaxError: positional argument follows keyword argument
# res2 = merge_lists_to_dict(object_two=prices, products)
# print(res2)
