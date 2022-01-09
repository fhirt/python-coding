import pathlib

path = pathlib.Path("C:/Users/fabio")
print(path)

print(pathlib.Path.home())
print(pathlib.Path.cwd())

print(path / "Desktop" / "hello.txt")

print(list(path.parents))

for directory in path.parents:
    print(directory)


file_path = pathlib.Path.home() / "my_folder" / "my_file.txt"
print(file_path)

print(file_path.exists())
print(file_path.name)
print(file_path.parent.name)
