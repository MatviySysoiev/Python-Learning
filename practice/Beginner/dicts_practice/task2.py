# Create a dictionary named `player` with the following key-value pairs:
# "name": "Alex"
# "level": 5
# "health": 100
# "items": ["sword", "shield"]

# Instructions:
# 1. Access and print the player's health.
# 2. Add a new key-value pair: "gold" with a value of 50.
# 3. Increase the "level" by 1 (modify the existing value).
# 4. Add "potion" to the list of "items" using the .append() method directly from the dictionary.

player = {
    "name": "Alex",
    "level": 5,
    "health": 100,
    "items": ["sword", "shield"],
}

print(player["health"])

player["gold"] = 50
player["level"] += 1
player["items"].append("potion")

print(player)
