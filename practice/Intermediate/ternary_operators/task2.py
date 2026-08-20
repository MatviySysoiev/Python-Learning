new_text = "random string"
another_text = "This string is defenitely contains more than 79 symbolssssssssssssssssssssssssssss"

print(f"{new_text}. This text has less then 79 symbols") if len(
    new_text) < 79 else print("This text has more than 79 symbols")
print(f"{another_text}. This text has less then 79 symbols") if len(
    another_text) < 79 else print("This text has more than 79 symbols")
