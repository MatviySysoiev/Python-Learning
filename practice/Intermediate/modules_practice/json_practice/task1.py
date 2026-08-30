"""
Task:
1. Create any dictionary using keys with values of different data types.
2. Convert the dictionary into JSON.
3. Print the resulting JSON string to the terminal.
4. Print the data type of the resulting value to the terminal.
"""

import json

new_dict = {
    'brand': 'Audi',
    'model': 'Q7',
    'price': 40000,
    'Available': True
}
json_car = json.dumps(new_dict, indent=1)
print(json_car)
print(type(json_car))
