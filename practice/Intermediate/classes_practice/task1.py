class Image:
    def __init__(self, title, resolution, extension):
        self.title = title
        self.resolution = resolution
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def rename(self, new_title):
        self.title = new_title

    def change_extension(self, new_extension):
        self.extension = new_extension

    def __str__(self):
        return f"{self.title}.{self.extension}"


new_image = Image("Beautiful picture", "1920x180", "jpg")
print(new_image.title)
print(new_image.extension)
print(new_image.resolution)
print(new_image)

new_image.resize("3440x1440")
new_image.extension = "png"
new_image.title = "Cute picture"

print(new_image.title)
print(new_image.extension)
print(new_image.resolution)
