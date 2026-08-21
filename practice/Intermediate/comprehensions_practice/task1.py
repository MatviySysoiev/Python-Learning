"""
Task:
1. Create a dictionary with several keys, where all values are of type `str`.
2. Create a new dictionary based on the existing one, in which the values of all keys are converted to uppercase.
3. Print the resulting dictionary to the terminal.
"""

dictionary = {
    'Hello': "bye",
    "I am here": "I am far away",
    "I am lost": "I know where I am"
}

new_dictionary = {k: v.upper() for k, v in dictionary.items()}

print(new_dictionary)
