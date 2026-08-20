my_img = ('1920', '1080')

another_img = ('3440', '1440', 'true')

print(f"{my_img[0]}x{my_img[1]}") if len(
    my_img) == 2 else print("Incorrect image format")

print(f"{another_img[0]}x{another_img[1]}") if len(
    another_img) == 2 else print("Incorrect image format")


if len(another_img) == 2:
    print(f"{another_img[0]}x{another_img[1]}")
else:
    print("Incorrect image format")
