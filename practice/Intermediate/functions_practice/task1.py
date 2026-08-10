# TASK
# 1. Create a function named merge_lists_to_dict
# 2. The function should have two parameters
# 3. The function should merge two lists using the built-in zip function
# 4. Convert the zip object into a dictionary and return it from the function
# 5. Call the function, passing two lists as arguments
# 6. Print the result of the function call to the terminal

def merge_lists_to_dict(object_one, object_two):
    new_zip = zip(object_one, object_two)

    zip_dict = dict(new_zip)
    return zip_dict


products = ['Apple', 'Banana', 'Watermelon']
prices = [100, 150, 350]

res = merge_lists_to_dict(products, prices)
print(res)
