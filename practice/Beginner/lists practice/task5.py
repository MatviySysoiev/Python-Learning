# Instructions:
# 1. Extract the word "coin" using double indexing and print it.
# 2. Add the item "torch" to the third inner list (where "key" is located).
# 3. Swap the first and third inner lists.

inventory = [
    ["sword", "shield"],
    ["potion", "scroll", "coin"],
    ["key"]
]

coin = inventory[1][2]
inventory[2].append('torch')

inventory[0], inventory[2] = inventory[2], inventory[0]

print(inventory)
