"""
Task: Error Handling
1. Create a function `image_info` with a single parameter of type `dict`.
2. The function expects a dictionary that must contain at least two keys:
   - `image_id`
   - `image_title`
3. The function should return a string formatted like this:
   "Image 'my cat' has id 5136"
4. If at least one of these keys is missing in the dictionary, the function must raise a `TypeError`.
5. Call the function and handle the error properly if it occurs.
"""


def image_info(cat_info):
    if 'image_title' not in cat_info:
        raise TypeError("image_title was not found")
    if 'image_id' not in cat_info:
        raise TypeError("image_id was not found")

    return f"Image '{cat_info['image_title']}' has id {cat_info['image_id']}"


new_dict = {'image_title': 'rush', 'image_id': 12345}
try:
    res = image_info(new_dict)
    print(res)
except TypeError as e:
    print(e)

another_dict = {'image_title': 'rudick'}
try:
    res = image_info(another_dict)
    print(res)
except TypeError as e:
    print(e)
