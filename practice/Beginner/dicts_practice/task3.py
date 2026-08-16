# Instructions:
# 1. Safely retrieve the value for the key "stamina" using .get(), providing a default value of 0. Print the result.
# 2. Remove the key "mana" using .pop() and save its value to a variable named `removed_mana`.
# 3. Clear all items from `character_stats` using the appropriate dictionary method.

character_stats = {
    "strength": 15,
    "agility": 12,
    "intelligence": 18,
    "mana": 50
}

stamina_value = character_stats.get("stamina", 0)
removed_mana = character_stats.pop("mana")
print(removed_mana)

character_stats.clear()
print(character_stats)
