"""
Task:
Write a program that creates an empty dictionary and prompts the user to enter 
three keys followed by three corresponding values. Add the key-value pairs 
to the dictionary and print the final dictionary.
"""

new_dict = {}

first_key = input("Enter first key: ")
second_key = input("Enter second key: ")
third_key = input("Enter third key: ")

first_key_value = (input("Enter first key value: "))
second_key_value = (input("Enter second key value: "))
third_key_value = (input("Enter third key value: "))

new_dict[first_key] = first_key_value
new_dict[second_key] = second_key_value
new_dict[third_key] = third_key_value

print(new_dict)
