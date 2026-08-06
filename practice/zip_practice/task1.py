store_items = ['phone', 'laptop', 'tv', 'apple']

store_prices = [1000, 1500, 2500, 0.5]

store_zip = zip(store_items, store_prices)

store_list = list(store_zip)
print(store_list)

# we can't use store_zip because zip is an iterator and can be read only once
store_dict = dict(store_list)
print(store_dict)
