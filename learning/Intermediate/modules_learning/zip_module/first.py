from zipfile import ZipFile
from pathlib import Path

# Path('my-files').mkdir(exist_ok=True)

# with open("my-files/first.txt", 'w') as my_file:
#     my_file.write("This is first file")


# with open("my-files/second.txt", 'w') as my_file:
#     my_file.write("This is second file")

# with ZipFile('my-files.zip', mode='w') as my_zip_file:
#     for file in Path('my-files').iterdir():
#         print(file)
#         my_zip_file.write(file)

with ZipFile('my-files.zip') as my_zip_file:
    # Extract all files to the folder 'my-files-unzipped'
    my_zip_file.extractall('my-files-unzipped')
    print(my_zip_file.infolist())
