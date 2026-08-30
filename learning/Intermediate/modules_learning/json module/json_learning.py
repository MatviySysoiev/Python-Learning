import json

# In json only double quetos!
json_str = '{"id":235, "brand": "Nike", "qty":84, "status": {"isForSale":true}}'
json_array = '[{"a":1}, {"b": 3}]'

sneakers = json.loads(json_str)

print(type(sneakers))  # <class 'dict'>
print(sneakers)

print(sneakers['brand'])  # Nike
print(sneakers['qty'])  # 84
print(sneakers['status']['isForSale'])  # True

my_list = json.loads(json_array)

print(my_list)

# indent is used for better look in terminal
json_from_dict = json.dumps(sneakers, indent=1)

print(json_from_dict)

print(type(json_from_dict))  # <class 'str'>
