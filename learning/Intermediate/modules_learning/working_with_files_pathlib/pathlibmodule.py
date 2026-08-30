from pathlib import Path

cwd = Path('.')

print(isinstance(cwd, Path))  # True
print(type(cwd))  # <class 'pathlib.WindowsPath'>
# [<class 'pathlib.PosixPath'>, <class 'pathlib.WindowsPath'>]
print(Path.__subclasses__())

all_methods = [method for method in dir(cwd) if not method.startswith('_')]
# print(all_methods)
print(cwd.absolute())  # c:\Users\��������\Desktop\Learning Python
cwd = Path('C:/').joinpath('Users').joinpath(
    'Владелец').joinpath('Desktop').joinpath('Learning Python')  # The same
print(cwd)


cwd = Path('C:/') / 'Users' / 'Владелец' / 'Desktop' / 'Learning Python'

new_cwd = Path('.') / 'New Folder'
print(cwd.is_dir())  # True

if not new_cwd.exists():
    print("Folder was created!")
    new_cwd.mkdir()
else:
    print("Folder was deleted!")
    new_cwd.rmdir()

print(type(Path('.')))  # <class 'pathlib.WindowsPath'>
