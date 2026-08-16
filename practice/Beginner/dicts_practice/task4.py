# 1. Access the "fps_limit" using double key indexing and print it.
# 2. Update the "audio" sub-dictionary with new settings using the .update() method:
#    Change "volume" to 100 and "muted" to True.
# 3. Swap the values of "graphics" and "audio" keys inside `game_config`.

game_config = {
    "graphics": {
        "resolution": "1920x1080",
        "fps_limit": 60
    },
    "audio": {
        "volume": 80,
        "muted": False
    }
}

print(game_config["graphics"]["fps_limit"])
game_config["audio"].update({"volume": 100, "muted": True})

game_config["graphics"], game_config["audio"] = game_config["audio"], game_config["graphics"]

print(game_config)
