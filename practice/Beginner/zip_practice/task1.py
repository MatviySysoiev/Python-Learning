"""
Task:
1. Create two lists: `store_items` with item names and `store_prices` with their corresponding prices.
2. Combine these two lists into pairs using the `zip()` function and store the iterator in `store_zip`.
3. Convert `store_zip` into a list named `store_list` and print it.
4. Convert `store_list` into a dictionary named `store_dict` and print it.
(Note: Use `store_list` instead of `store_zip` to build the dictionary because the zip iterator can only be consumed once).
"""

store_items = ['phone', 'laptop', 'tv', 'apple']

store_prices = [1000, 1500, 2500, 0.5]

store_zip = zip(store_items, store_prices)

store_list = list(store_zip)
print(store_list)

# we can't use store_zip because zip is an iterator and can be read only once
store_dict = dict(store_list)
print(store_dict)
