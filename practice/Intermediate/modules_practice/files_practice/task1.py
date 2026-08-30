"""
Task:
1. Create a directory named `files` in the current working directory.
2. Add two files, `first.txt` and `second.txt`, into this directory and write 2-3 lines of text into each.
3. Read all lines from the first file.
4. Read the lines from the second file line by line.
5. Delete both files.
6. Delete the `files` directory.
"""

from pathlib import Path

new_directory = Path("New_Folder")

new_directory.mkdir(exist_ok=True)

with open(new_directory/'first.txt', 'w') as new_file:
    new_file.write("First string\n")
    new_file.write("Second string\n")

with open(new_directory/'second.txt', 'w') as other_file:
    lines = [
        "First string",
        "Second string",
        "Third string"
    ]
    for line in lines:
        other_file.write(line + '\n')

with open(new_directory/'first.txt') as first_file:
    print(first_file.read())

with open(new_directory/'second.txt') as second_file:
    while True:
        line = second_file.readline()
        if not line:
            break
        print(line.strip())


first_file_path = new_directory / 'first.txt'

if first_file_path.exists():
    first_file_path.unlink()
    print("First file was deleted!")

second_file_path = new_directory / 'second.txt'

if second_file_path.exists():
    second_file_path.unlink()
    print("Second file was deleted!")

if new_directory.exists():
    # only works if folder is empty. If it's not then use shutil.rmtree(new_directory)
    new_directory.rmdir()
    print("Folder was deleted!")
